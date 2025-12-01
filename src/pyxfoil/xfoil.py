from collections.abc import Iterable
from os import remove, system, chdir, curdir
from os.path import isfile, join, split
from typing import TYPE_CHECKING, Any

from numpy import asarray

from matplotlib.pyplot import figure

from .xfoilpolar import XfoilPolar, write_polar_session
from .xfoilresult import XfoilResult, write_result_session

if TYPE_CHECKING:
    from matplotlib.axes import Axes
    from numpy.typing import NDArray


class Xfoil:
    name: str = None
    ppar: int = None
    x: 'NDArray' = None
    y: 'NDArray' = None
    results: dict[str, 'XfoilResult'] = None
    polars: dict[str, 'XfoilPolar'] = None
    frmstr: str = None
    _area: float = None

    def __init__(self, name: str, frmstr: str = '11.6f') -> None:
        self.name = name
        self.frmstr = frmstr

    def points_from_dat(self, datfile: str) -> None:
        x = []
        y = []
        with open(datfile, 'rt') as file:
            for i, line in enumerate(file):
                line = line.rstrip('\n')
                if i == 0:
                    self.name = line.strip()
                else:
                    split = line.split()
                    if len(split) == 2:
                        x.append(float(split[0]))
                        y.append(float(split[1]))
        self.x = asarray(x)
        self.y = asarray(y)
        self._area = None

    def set_points(self, x: Iterable[float], y: Iterable[float]) -> None:
        self.x = asarray(x)
        self.y = asarray(y)
        self._area = None

    def set_ppar(self, ppar: int) -> None:
        self.ppar = ppar

    @property
    def area(self) -> float:
        if self._area is None:
            xa, ya = self.x[:-1], self.y[:-1]
            xb, yb = self.x[1:], self.y[1:]
            areax2 = sum(xa*yb - xb*ya)
            xa, ya = self.x[-1], self.y[-1]
            xb, yb = self.x[0], self.y[0]
            areax2 += xa*yb - xb*ya
            self._area = 0.5*areax2
        return self._area

    def write_dat(self) -> str:

        from . import workdir

        datname = self.name.replace(' ', '_')
        filepath = join(workdir, datname)
        datfilepath = f'{filepath:s}.dat'
        num = len(self.x)

        if self.area >= 0:
            order = range(num-1, -1, -1)
        else:
            order = range(num)
        frmstr = '  {:' + self.frmstr + '} {:' + self.frmstr + '}\n'

        with open(datfilepath, 'wt') as file:
            file.write(self.name+'\n')
            for i in order:
                file.write(frmstr.format(self.x[i], self.y[i]))

        return datfilepath

    def run_result(self, alfa: float, *, Re: float = None,
                   mach: float = None, ncrit: float = None,
                   xtrtop: float = 1.0, xtrbot: float = 1.0) -> 'XfoilResult':

        from . import xfoilexe, workdir

        thisdir = curdir

        datfilepath = self.write_dat()
        numpnl = len(self.x) - 1

        chdir(workdir)
        sesfilepath, resfilepath = write_result_session(self.name, datfilepath, numpnl,
                                                        alfa, mach=mach, Re=Re,
                                                        ppar=self.ppar, xtrtop=xtrtop,
                                                        xtrbot=xtrbot, ncrit=ncrit)
        chdir(thisdir)

        if isfile(resfilepath):
            remove(resfilepath)

        if xfoilexe is None:
            err = 'Cannot locate "xfoil.exe" in path. '
            err += 'Import set_xfoilexe and use it to directly point to "xfoil.exe".'
            raise SystemError(err)

        chdir(workdir)
        system('{:s} < {:s}'.format(xfoilexe, sesfilepath))
        chdir(thisdir)

        res: str  = split(resfilepath)[1]
        res = res.replace('.res', '')
        result = XfoilResult(res, numpnl)
        result.set_param(alfa, mach, Re)
        result.read_result(resfilepath)
        if self.results is None:
            self.results = {}
        self.results[res] = result
        return result

    def run_polar(self, almin: float, almax: float, alint: float, *,
                  Re: float | None = None, mach: float | None = None,
                  xtrtop: float = 1.0, xtrbot: float = 1.0,
                  ncrit: float = None) -> 'XfoilPolar':

        from . import xfoilexe, workdir

        thisdir = curdir

        datfilepath = self.write_dat()
        numpnl = len(self.x) - 1

        chdir(workdir)
        sesfilepath, polfilepath = write_polar_session(self.name, datfilepath,
                                                       numpnl, almin, almax, alint,
                                                       mach=mach, Re=Re, ppar=self.ppar,
                                                       xtrtop=xtrtop, xtrbot=xtrbot, ncrit=ncrit)
        chdir(thisdir)

        if isfile(polfilepath):
            remove(polfilepath)

        if xfoilexe is None:
            err = 'Cannot locate "xfoil.exe" in path. '
            err += 'Import set_xfoilexe and use it to directly point to "xfoil.exe".'
            raise SystemError(err)

        chdir(workdir)
        system('{:s} < {:s}'.format(xfoilexe, sesfilepath))
        chdir(thisdir)

        pol: str = split(polfilepath)[1]
        pol = pol.replace('.pol', '')
        polar = XfoilPolar(pol, numpnl)
        polar.read_polar(polfilepath)
        if self.polars is None:
            self.polars = {}
        self.polars[pol] = polar
        return polar

    def plot_profile(self, ax: 'Axes | None' = None, **kwargs: dict[str, Any]) -> 'Axes':
        if ax is None:
            figsize = kwargs.pop('figsize', (12, 8))
            grid = kwargs.pop('grid', True)
            aspect = kwargs.pop('aspect', 'equal')
            fig = figure(figsize=figsize)
            ax = fig.gca()
            ax.grid(grid)
            ax.set_aspect(aspect)
            ax.set_title('Airfoil profile for {:}.'.format(self.name))
        ax.plot(self.x, self.y, **kwargs)
        return ax

    def __repr__(self) -> str:
        return f'Xfoil({self.name:s})'

    def __str__(self) -> str:
        return f'Xfoil({self.name:s})'
