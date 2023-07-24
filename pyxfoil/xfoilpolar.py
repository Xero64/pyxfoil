from os.path import join
from typing import Optional, Tuple, List

class XfoilPolar():
    name: 'str' = None
    numpnl: 'int' = None
    re: Optional['float'] = None
    mach: Optional['float'] = None
    ncrit: 'float' = None
    xtrftop: 'float' = None
    xtrfbot: 'float' = None
    alpha: List['float'] = None
    cl: List['float'] = None
    cd: List['float'] = None
    cdp: List['float'] = None
    cm: List['float'] = None
    trtop: List['float'] = None
    trbot: List['float'] = None

    def __init__(self, name: 'str', numpnl: 'int') -> None:
        self.name = name
        self.numpnl = numpnl

    def read_polar(self, filepath: str) -> None:
        self.alpha = []
        self.cl = []
        self.cd = []
        self.cdp = []
        self.cm = []
        self.trtop = []
        self.trbot = []
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
                    self.re = float(line[25:38].replace(' ', ''))
                    self.ncrit = float(line[51:58])
                if line[0:8] == '   alpha':
                    read = True
                    continue
                if read:
                    if line[0:8] != '  ------':
                        self.alpha.append(float(line[0:8]))
                        self.cl.append(float(line[8:17]))
                        self.cd.append(float(line[17:27]))
                        self.cdp.append(float(line[27:37]))
                        self.cm.append(float(line[37:46]))
                        self.trtop.append(float(line[46:55]))
                        self.trbot.append(float(line[55:64]))

    @property
    def clocd(self) -> Optional[List['float']]:
        if self.cl is not None and self.cd is not None:
            clocdval = [cli/cdi for cli, cdi in zip(self.cl, self.cd)]
            return clocdval

    def plot_polar(self, xaxis='cd', yaxis='cl', ax=None, *args, **kwargs):
        figsize = kwargs.get('figsize', (12, 8))
        if ax is None:
            from matplotlib.pyplot import figure
            fig = figure(figsize=figsize)
            ax = fig.gca()
            title = r'Polar plot for $M = {:g}$ and $Re = {:.12g}$'
            ax.set_title(title.format(self.mach, self.re))
            grid = kwargs.get('grid', True)
            ax.grid(grid)
            xlabel = self.get_label(xaxis)
            ylabel = self.get_label(yaxis)
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
        label = r''
        if self.re is not None:
            label += r'$Re = {:.12g}$'.format(self.re)
        if self.re is not None and self.mach is not None:
            label += r'; '
        if self.mach is not None:
            label += r'$M = {:g}$'.format(self.mach)
        xvalue = self.get_value(xaxis)
        yvalue = self.get_value(yaxis)
        ax.plot(xvalue, yvalue, *args, label=label)
        return ax

    def get_label(self, var: 'str') -> 'str':
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
            label = r'$Top X Transition$'
        elif var == 'th':
            label = r'$Bottom X Transition$'
        elif var == 'clocd':
            label = r'$\frac{c_l}{c_d}$'
        else:
            raise ValueError(f'{var:s} does not exist in XfoilPolar.')
        return label

    def get_value(self, var: 'str') -> List['float']:
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
        elif var == 'th':
            value = self.trbot
        elif var == 'clocd':
            value = self.clocd
        else:
            raise ValueError(f'{var:s} does not exist in XfoilPolar.')
        return value

    def __repr__(self) -> str:
        return f'<pyxfoil.XfoilPolar {self.name:s}>'

def write_polar_session(name: 'str', datfilepath: 'str', numpnl: 'int',
                        almin: 'float', almax: 'float', alint: 'float',
                        mach: Optional['float']=None,
                        re: Optional['float']=None,
                        ppar: Optional['int']=None) -> Tuple['str', 'str']:

    from pyxfoil import workdir
    
    polname = name.replace(' ', '_') + f'_{numpnl:d}'
    if mach is not None:
        polname += f'_{mach:g}'
    if re is not None:
        polname += f'_{re:.12g}'
    filepath = join(workdir, polname)
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
        if re is not None:
            file.write('visc {:.12g}\n'.format(re))
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
        if re is not None:
            file.write('visc\n')
        file.write('\n')
        file.write('quit\n')
    return sesfilepath, polfilepath
