from os.path import join
from typing import TYPE_CHECKING, Any

from matplotlib.pyplot import figure
from numpy import asarray, radians

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


class XfoilResult:
    name: str = None
    numpnl: int = None
    alpha: float = None
    Re: float | None = None
    mach: float | None = None
    s: 'NDArray' = None
    x: 'NDArray' = None
    y: 'NDArray' = None
    ue: 'NDArray' = None
    ds: 'NDArray' = None
    th: 'NDArray' = None
    cf: 'NDArray' = None
    h: 'NDArray' = None
    resfile: str = None
    _alrad: 'NDArray' = None
    _cp: 'NDArray' = None

    def __init__(self, name: str, numpnl: int) -> None:
        self.name = name
        self.numpnl = numpnl

    def reset(self) -> None:
        for attr in self.__dict__:
            if attr.startswith('_'):
                setattr(self, attr, None)

    def set_param(self, alpha: float, mach: float, Re: float) -> None:
        self.alpha = alpha
        self.mach = mach
        self.Re = Re

    def read_result(self, resfile: str) -> None:
        with open(resfile, 'rt') as f:
            s = []
            x = []
            y = []
            ue = []
            ds = []
            th = []
            cf = []
            h = []
            for line in f:
                line = line.rstrip('\n')
                if line != '':
                    if line[0] != '#':
                        s.append(float(line[1:11]))
                        x.append(float(line[11:20]))
                        y.append(float(line[20:29]))
                        ue.append(float(line[29:38]))
                        ds.append(float(line[38:48]))
                        th.append(float(line[48:58]))
                        cf.append(float(line[58:68]))
                        h.append(float(line[68:78]))
        self.s = asarray(s)
        self.x = asarray(x)
        self.y = asarray(y)
        self.ue = asarray(ue)
        self.ds = asarray(ds)
        self.th = asarray(th)
        self.cf = asarray(cf)
        self.h = asarray(h)
        self.reset()

    @property
    def alrad(self) -> 'NDArray':
        if self._alrad is None:
            self._alrad = radians(self.alpha)
        return self._alrad

    @property
    def cp(self) -> 'NDArray':
        if self._cp is None:
            self._cp = asarray([1-uei**2 for uei in self.ue])
        return self._cp

    def plot_result(self, xaxis='x', yaxis='ue', ax: 'Axes| None' = None,
                    **kwargs: dict[str, Any]) -> 'Axes':
        if ax is None:
            figsize = kwargs.pop('figsize', (12, 8))
            fig = figure(figsize=figsize)
            ax = fig.gca()
            grid = kwargs.pop('grid', True)
            ax.grid(grid)
            xlabel = self.get_label(xaxis)
            ylabel = self.get_label(yaxis)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            title = r'Result plot for $\alpha = {:g}$'.format(self.alpha)
            if self.Re is not None:
                title += r' and $Re = {:.12g}$'.format(self.Re)
            if self.mach is not None:
                title += r' and $M = {:g}$'.format(self.mach)
            ax.set_title(title)
            if yaxis == 'cp':
                ax.invert_yaxis()
        label = r'$\alpha = {:g}$'.format(self.alpha)
        if self.Re is not None:
            label += r'; $Re = {:.12g}$'.format(self.Re)
        if self.mach is not None:
            label += r'; $M = {:g}$'.format(self.mach)
        xvalue = self.get_value(xaxis)
        yvalue = self.get_value(yaxis)
        kwargs.setdefault('label', label)
        ax.plot(xvalue, yvalue, **kwargs)
        return ax

    def result(self, var: str, correct: bool=False) -> 'NDArray':
        res = self.get_value(var)
        if correct:
            if var == 's':
                offset = max(res[:self.numpnl+1])
                val = [offset-resi for resi in res[:self.numpnl+1]]
            else:
                val = [resi for resi in res[:self.numpnl+1]]
            val.reverse()
            val = val + res[self.numpnl+1:]
        else:
            val = res.copy()
        return val

    def get_label(self, var: str) -> str:
        if var == 'x':
            label = '$x$'
        elif var == 'y':
            label = '$y$'
        elif var == 's':
            label = '$s$'
        elif var == 'ue':
            label = '$u_e$'
        elif var == 'cp':
            label = '$c_p$'
        elif var == 'ds':
            label = r'$\delta^*$'
        elif var == 'th':
            label = r'$\theta$'
        elif var == 'h':
            label = '$h$'
        elif var == 'cf':
            label = '$c_f$'
        else:
            raise ValueError(f'{var:s} does not exist in XfoilResult.')
        return label

    def get_value(self, var: str) -> 'NDArray':
        if var == 'x':
            value = self.x
        elif var == 'y':
            value = self.y
        elif var == 's':
            value = self.s
        elif var == 'ue':
            value = self.ue
        elif var == 'cp':
            value = self.cp
        elif var == 'ds':
            value = self.ds
        elif var == 'th':
            value = self.th
        elif var == 'h':
            value = self.h
        elif var == 'cf':
            value = self.cf
        else:
            raise ValueError(f'{var:s} does not exist in XfoilResult.')
        return value

    def __repr__(self) -> str:
        return f'<pyxfoil.XfoilResult {self.name:s}>'


def write_result_session(name: str, datfilepath: str, numpnl: int,
                         alpha: float, mach: float | None = None,
                         Re: float | None = None,
                         ppar: int | None = None) -> tuple[str, str]:

    from pyxfoil import workdir

    resname = name.replace(' ', '_')
    resname += f'_{numpnl:d}_{alpha:g}'
    if mach is not None:
        resname += f'_{mach:g}'
    if Re is not None:
        resname += f'_{Re:.12g}'
    filepath = join(workdir, resname)
    sesfilepath = f'{filepath:s}.ses'
    resfilepath = f'{filepath:s}.res'
    with open(sesfilepath, 'wt') as file:
        file.write('load {:s}\n'.format(datfilepath))
        if ppar is not None:
            file.write('ppar\n')
            file.write('n {:d}\n'.format(ppar))
            file.write('\n')
            file.write('\n')
        file.write('oper\n')
        if mach is not None:
            file.write('mach {:g}\n'.format(mach))
        if Re is not None:
            file.write('visc {:.12g}\n'.format(Re))
        file.write('alfa {:g}\n'.format(alpha))
        file.write('dump {:s}\n'.format(resfilepath))
        if mach is not None:
            file.write('mach 0.0\n')
        if Re is not None:
            file.write('visc\n')
        file.write('\n')
        file.write('quit\n')

    return sesfilepath, resfilepath
