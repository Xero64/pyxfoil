from os import system, remove
from os.path import isfile, join, split
from typing import List, Dict
from .xfoilresult import XfoilResult, write_result_session
from .xfoilpolar import XfoilPolar, write_polar_session
from matplotlib.pyplot import figure

class Xfoil():
    name: 'str' = None
    ppar: 'int' = None
    x: List['float'] = None
    y: List['float'] = None
    results: Dict['str', 'XfoilResult'] = None
    polars: Dict['str', 'XfoilPolar'] = None
    _area: 'float' = None

    def __init__(self, name: 'str') -> None:
        self.name = name

    def points_from_dat(self, datfile: 'str') -> None:
        self.x = []
        self.y = []
        with open(datfile, 'rt') as file:
            for i, line in enumerate(file):
                line = line.rstrip('\n')
                if i == 0:
                    self.name = line.strip()
                else:
                    split = line.split()
                    if len(split) == 2:
                        x = float(split[0])
                        y = float(split[1])
                        self.x.append(x)
                        self.y.append(y)
        self._area = None

    def set_points(self, x: List['float'], y: List['float']) -> None:
        self.x = x
        self.y = y
        self._area = None

    def set_ppar(self, ppar: 'int') -> None:
        self.ppar = ppar

    @property
    def area(self) -> 'float':
        if self._area is None:
            self._area = 0.0
            for i in range(1, len(self.x)):
                self._area += self.x[i]*self.y[i-1]-self.y[i]*self.x[i-1]
            if self.x[0] != self.x[-1] or self.y[0] != self.y[-1]:
                self._area += self.x[0]*self.y[-1]-self.y[0]*self.x[-1]
        return self._area

    def write_dat(self) -> 'str':

        from pyxfoil import workdir

        datname = self.name.replace(' ', '_')
        filepath = join(workdir, datname)
        datfilepath = f'{filepath:s}.dat'
        num = len(self.x)
        if self.area >= 0:
            order = range(num-1, -1, -1)
        else:
            order = range(num)
        frmstr = '  {:11.6f} {:11.6f}\n'
        with open(datfilepath, 'wt') as file:
            file.write(self.name+'\n')
            for i in order:
                file.write(frmstr.format(self.x[i], self.y[i]))
        return datfilepath

    def run_result(self, alfa: 'float', re: 'float'=None,
                   mach: 'float'=None) -> 'XfoilResult':

        from pyxfoil import xfoilexe

        datfilepath = self.write_dat()
        numpnl = len(self.x) - 1
        sesfilepath, resfilepath = write_result_session(self.name, datfilepath, numpnl,
                                                        alfa, mach=mach, re=re,
                                                        ppar=self.ppar)

        if isfile(resfilepath):
            remove(resfilepath)

        if xfoilexe is None:
            err = 'Cannot locate "xfoil.exe" in path. '
            err += 'Import set_xfoilexe and use it to directly point to "xfoil.exe".'
            raise SystemError(err)

        system('{:s} < {:s}'.format(xfoilexe, sesfilepath))

        res = split(resfilepath)[1]
        res = res.replace('.res', '')
        result = XfoilResult(res, numpnl)
        result.set_param(alfa, mach, re)
        result.read_result(resfilepath)
        if self.results is None:
            self.results = {}
        self.results[res] = result
        return result

    def run_polar(self, almin: 'float', almax: 'float', alint: 'float',
                  re: 'float'=None, mach: 'float'=None) -> 'XfoilPolar':

        from pyxfoil import xfoilexe

        datfilepath = self.write_dat()
        numpnl = len(self.x) - 1
        sesfilepath, polfilepath = write_polar_session(self.name, datfilepath,
                                                       numpnl, almin, almax, alint,
                                                       mach=mach, re=re,
                                                       ppar=self.ppar)

        if isfile(polfilepath):
            remove(polfilepath)

        if xfoilexe is None:
            err = 'Cannot locate "xfoil.exe" in path. '
            err += 'Import set_xfoilexe and use it to directly point to "xfoil.exe".'
            raise SystemError(err)

        system('{:s} < {:s}'.format(xfoilexe, sesfilepath))

        pol: 'str' = split(polfilepath)[1]
        pol = pol.replace('.pol', '')
        polar = XfoilPolar(pol, numpnl)
        polar.read_polar(polfilepath)
        if self.polars is None:
            self.polars = {}
        self.polars[pol] = polar
        return polar

    def plot_profile(self, *args, **kwargs):
        grid = kwargs.get('grid', True)
        aspect = kwargs.get('aspect', 'equal')
        figsize = kwargs.get('figsize', (12, 8))
        fig = figure(figsize=figsize)
        ax = fig.gca()
        ax.plot(self.x, self.y, *args, **kwargs)
        ax.grid(grid)
        ax.set_aspect(aspect)
        ax.set_title('Airfoil profile for {:}.'.format(self.name))
        return ax
