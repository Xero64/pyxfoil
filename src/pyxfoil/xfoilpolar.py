from os.path import join
from typing import TYPE_CHECKING, Any

from matplotlib.pyplot import figure
from numpy import asarray, radians

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


class XfoilPolar:
    name: str = None
    numpnl: int = None
    Re: float | None = None
    mach: float | None = None
    ncrit: float | None = None
    xtrftop: float = None
    xtrfbot: float = None
    alpha: 'NDArray' = None
    cl: 'NDArray' = None
    cd: 'NDArray' = None
    cdp: 'NDArray' = None
    cm: 'NDArray' = None
    trtop: 'NDArray' = None
    trbot: 'NDArray' = None
    _alrad: 'NDArray' = None
    _clocd: 'NDArray' = None

    def __init__(self, name: str, numpnl: int) -> None:
        self.name = name
        self.numpnl = numpnl

    def reset(self) -> None:
        for attr in self.__dict__:
            if attr.startswith('_'):
                setattr(self, attr, None)

    def read_polar(self, filepath: str) -> None:
        alpha = []
        cl = []
        cd = []
        cdp = []
        cm = []
        trtop = []
        trbot = []
        read = False
        with open(filepath, 'rt') as file:
            for line in file:
                line = line.rstrip('\n')
                if line.strip() == '':
                    continue
                if line[0:23] == ' Calculated polar for: ':
                    self.name = line[23:].strip()
                if line[0:8] == ' xtrf = ':
                    self.xtrftop = float(line[8:15])
                    self.xtrfbot = float(line[27:34])
                if line[0:8] == ' Mach = ':
                    self.mach = float(line[8:15])
                    self.Re = float(line[25:38].replace(' ', ''))
                    self.ncrit = float(line[51:58])
                if line[0:8] == '   alpha':
                    read = True
                    continue
                if read:
                    if line[0:8] != '  ------':
                        alpha.append(float(line[0:8]))
                        cl.append(float(line[8:17]))
                        cd.append(float(line[17:27]))
                        cdp.append(float(line[27:37]))
                        cm.append(float(line[37:46]))
                        trtop.append(float(line[46:55]))
                        trbot.append(float(line[55:64]))
        self.alpha = asarray(alpha)
        self.cl = asarray(cl)
        self.cd = asarray(cd)
        self.cdp = asarray(cdp)
        self.cm = asarray(cm)
        self.trtop = asarray(trtop)
        self.trbot = asarray(trbot)
        self.reset()

    @property
    def alrad(self) -> 'NDArray':
        if self._alrad is None:
            self._alrad = radians(self.alpha)
        return self._alrad

    @property
    def clocd(self) -> 'NDArray | None':
        if self._clocd is None:
            if self.cl is not None and self.cd is not None:
                clocdval = [cli/cdi for cli, cdi in zip(self.cl, self.cd)]
                self._clocd = asarray(clocdval)
        return self._clocd

    def plot_polar(self, xaxis='cd', yaxis='cl',
                   ax: 'Axes | None'=None, **kwargs: dict[str, Any]) -> 'Axes':
        if ax is None:
            figsize = kwargs.pop('figsize', (12, 8))
            fig = figure(figsize = figsize)
            ax = fig.gca()
            title = fr'Polar plot for $M = {self.mach:g}$ and $Re = {self.Re:.12g}$'
            ax.set_title(title.format(self.mach, self.Re))
            grid = kwargs.pop('grid', True)
            ax.grid(grid)
            xlabel = self.get_label(xaxis)
            ylabel = self.get_label(yaxis)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
        label = r''
        if self.Re is not None:
            label += r'$Re = {:.12g}$'.format(self.Re)
        if self.Re is not None and self.mach is not None:
            label += r'; '
        if self.mach is not None:
            label += r'$M = {:g}$'.format(self.mach)
        if self.Re is not None and self.mach is not None and self.ncrit is not None:
            label += r'; '
        if self.ncrit is not None:
            label += r'; $N_{{crit}} = {:g}$'.format(self.ncrit)
        xvalue = self.get_value(xaxis)
        yvalue = self.get_value(yaxis)
        kwargs.setdefault('label', label)
        ax.plot(xvalue, yvalue, **kwargs)
        return ax

    def get_label(self, var: str) -> str:
        if var == 'alpha':
            label = r'$\alpha$'
        elif var == 'cl':
            label = '$C_l$'
        elif var == 'cd':
            label = '$C_d$'
        elif var == 'cdp':
            label = '$C_{dp}$'
        elif var == 'cm':
            label = '$C_m$'
        elif var == 'toptr':
            label = 'Top X Transition'
        elif var == 'bottr':
            label = 'Bottom X Transition'
        elif var == 'clocd':
            label = r'$\frac{c_l}{c_d}$'
        else:
            raise ValueError(f'{var:s} does not exist in XfoilPolar.')
        return label

    def get_value(self, var: str) -> 'NDArray':
        if var == 'alpha':
            value = self.alpha
        elif var == 'cl':
            value = self.cl
        elif var == 'cd':
            value = self.cd
        elif var == 'cdp':
            value = self.cdp
        elif var == 'cm':
            value = self.cm
        elif var == 'toptr':
            value = self.trtop
        elif var == 'bottr':
            value = self.trbot
        elif var == 'clocd':
            value = self.clocd
        else:
            raise ValueError(f'{var:s} does not exist in XfoilPolar.')
        return value

    def __repr__(self) -> str:
        return f'<pyxfoil.XfoilPolar {self.name:s}>'


def write_polar_session(name: str, datfilepath: str, numpnl: int,
                        almin: float, almax: float, alint: float,
                        mach: float | None = None,
                        Re: float | None = None,
                        ppar: int | None = None,
                        xtrtop: float = 1.0,
                        xtrbot: float = 1.0,
                        ncrit: float = None) -> tuple[str, str]:

    # from . import workdir

    polname = name.replace(' ', '_') + f'_{numpnl:d}'

    if mach is not None:
        polname += f'_{mach:g}'

    if Re is not None:
        polname += f'_{Re:.12g}'

    if ncrit is not None:
        polname += f'_{ncrit:.1f}'

    # filepath = join(workdir, polname)
    filepath = polname
    sesfilepath = f'{filepath:s}.ses'
    polfilepath = f'{filepath:s}.pol'

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

        # Set TRIP Position:
        file.write('vpar\n')

        if ncrit is not None:
            file.write('N {:.1f}\n'.format(ncrit))

        file.write('xtr\n')
        file.write(f'{xtrtop:g}\n')
        file.write(f'{xtrbot:g}\n')
        file.write('\n')

        file.write('pacc\n')
        file.write('{:s}\n'.format(polfilepath))
        file.write('\n')

        file.write('aseq\n')
        file.write('{:g}\n'.format(almin))
        file.write('{:g}\n'.format(almax))
        file.write('{:g}\n'.format(alint))

        file.write('pacc\n')

        if mach is not None:
            file.write('mach 0.0\n')

        if Re is not None:
            file.write('visc\n')

        if ncrit is not None:
            file.write('vpar\n')
            file.write('N 9.0\n')

        file.write('\n')

        file.write('quit\n')

    return sesfilepath, polfilepath
