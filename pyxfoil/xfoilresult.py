from os.path import join
from typing import Tuple, Optional, List

class XfoilResult():
    name: 'str' = None
    numpnl: 'int' = None
    alpha: 'float' = None
    re: Optional['float'] = None
    mach: Optional['float'] = None
    s: List['float'] = None
    x: List['float'] = None
    y: List['float'] = None
    ue: List['float'] = None
    ds: List['float'] = None
    th: List['float'] = None
    cf: List['float'] = None
    h: List['float'] = None
    resfile: 'str' = None
    _cp: List['float'] = None

    def __init__(self, name: 'str', numpnl: 'int') -> None:
        self.name = name
        self.numpnl = numpnl

    def set_param(self, alpha: 'float', mach: 'float', re: 'float') -> None:
        self.alpha = alpha
        self.mach = mach
        self.re = re

    def read_result(self, resfile: 'str') -> None:
        with open(resfile, 'rt') as f:
            self.s = []
            self.x = []
            self.y = []
            self.ue = []
            self.ds = []
            self.th = []
            self.cf = []
            self.h = []
            for line in f:
                line = line.rstrip('\n')
                if line != '':
                    if line[0] != '#':
                        self.s.append(float(line[1:11]))
                        self.x.append(float(line[11:20]))
                        self.y.append(float(line[20:29]))
                        self.ue.append(float(line[29:38]))
                        self.ds.append(float(line[38:48]))
                        self.th.append(float(line[48:58]))
                        self.cf.append(float(line[58:68]))
                        self.h.append(float(line[68:78]))
        self._cp = None

    @property
    def cp(self) -> List['float']:
        if self._cp is None:
            self._cp = [1-uei**2 for uei in self.ue]
        return self._cp

    def plot_result(self, xaxis='x', yaxis='ue', ax=None, *args, **kwargs):
        figsize = kwargs.get('figsize', (12, 8))
        if ax is None:
            from matplotlib.pyplot import figure
            fig = figure(figsize=figsize)
            ax = fig.gca()
            grid = kwargs.get('grid', True)
            ax.grid(grid)
            xlabel = self.get_label(xaxis)
            ylabel = self.get_label(yaxis)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            title = r'Result plot for $\alpha = {:g}$'.format(self.alpha)
            if self.re is not None:
                title += r' and $Re = {:.12g}$'.format(self.re)
            if self.mach is not None:
                title += r' and $M = {:g}$'.format(self.mach)
            ax.set_title(title)
            if yaxis == 'cp':
                ax.invert_yaxis()
        label = r'$\alpha = {:g}$'.format(self.alpha)
        if self.re is not None:
            label += r'; $Re = {:.12g}$'.format(self.re)
        if self.mach is not None:
            label += r'; $M = {:g}$'.format(self.mach)
        xvalue = self.get_value(xaxis)
        yvalue = self.get_value(yaxis)
        ax.plot(xvalue, yvalue, *args, label=label)
        return ax

    def result(self, var: 'str', correct: 'bool'=False) -> List['float']:
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

    def get_label(self, var: 'str') -> 'str':
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

    def get_value(self, var: 'str') -> List['float']:
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

def write_result_session(name: 'str', datfilepath: 'str', numpnl: 'int',
                         alpha: 'float', mach: Optional['float']=None,
                         re: Optional['float']=None,
                         ppar: Optional['int']=None) -> Tuple['str', 'str']:

    from pyxfoil import workdir

    resname = name.replace(' ', '_')
    resname += f'_{numpnl:d}_{alpha:g}'
    if mach is not None:
        resname += f'_{mach:g}'
    if re is not None:
        resname += f'_{re:.12g}'
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
        if re is not None:
            file.write('visc {:.12g}\n'.format(re))
        file.write('alfa {:g}\n'.format(alpha))
        file.write('dump {:s}\n'.format(resfilepath))
        if mach is not None:
            file.write('mach 0.0\n')
        if re is not None:
            file.write('visc\n')
        file.write('\n')
        file.write('quit\n')
    return sesfilepath, resfilepath
