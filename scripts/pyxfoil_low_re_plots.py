#%%
# Import Dependencies
from pyxfoil import Xfoil, set_workdir  # , set_xfoilexe
from pyfoil2.tools.naca4 import NACA4

set_workdir('C:/Xfoil_WIP') # Sets the working directory for pyxfoil.
# set_xfoilexe('C:/Xfoil-6.99/xfoil.exe') # Sets the path of the xfoil executable.

#%%
# Creates Xfoil object from reading dat file.
naca4 = NACA4('0002', cnum=120)

xfoil = Xfoil('NACA 0001')
xfoil.set_points(naca4.x[::-1], naca4.y[::-1])
# xfoil.points_from_dat('../files/NACA_0012_180.dat')
xfoil.set_ppar(180)

#%%
# Runs xfoil for the following parameters
al = 0.0
mach = 0.0
re = 5000.0
rescase = xfoil.run_result(al, mach=mach, re=re)

#%%
# Plots xfoil airfoil profile
ax1 = xfoil.plot_profile(ls='-')

#%%
# Shows plots for cases in xfoil cases
ax2 = None
for result in xfoil.results.values():
    ax2 = result.plot_result(yaxis='cp', ax=ax2, ls='-x')
_ = ax2.legend()

#%%
# Shows plots for cases in xfoil cases
ax3 = None
for result in xfoil.results.values():
    ax3 = result.plot_result(yaxis='ds', ax=ax3, ls='-o')
_ = ax3.legend()

#%%
# Shows plots for cases in xfoil cases
ax4 = None
for result in xfoil.results.values():
    ax4 = result.plot_result(yaxis='th', ax=ax4, ls='-o')
_ = ax4.legend()

#%%
# Shows plots for cases in xfoil cases
ax5 = None
for result in xfoil.results.values():
    ax5 = result.plot_result(yaxis='cf', ax=ax5, ls='-o')
_ = ax5.legend()

#%%
# Shows plots for cases in xfoil cases
ax6 = None
for result in xfoil.results.values():
    ax6 = result.plot_result(yaxis='h', ax=ax6, ls='-o')
_ = ax6.legend()

#%%
# Shows plots for cases in xfoil cases
ax7 = None
for result in xfoil.results.values():
    ax7 = result.plot_result(yaxis='ue', ax=ax7, ls='-o')
ax7.set_ylim((0.9, 1.2))
_ = ax7.legend()
