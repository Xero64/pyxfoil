#%%
# Import Dependencies
from pyxfoil import Xfoil#, set_workdir, set_xfoilexe

# set_workdir('C:/Xfoil_WIP') # Sets the working directory for pyxfoil.
# set_xfoilexe('C:/Xfoil-6.99/xfoil.exe') # Sets the path of the xfoil executable.

#%%
# Creates Xfoil object from reading dat file.
xfoil = Xfoil('NACA 0012')
xfoil.points_from_dat('../files/NACA_0012_180.dat')
xfoil.set_ppar(180)

#%%
# Runs xfoil for the following parameters
al = 0.0
mach = 0.0
Re = 100000.0
rescase = xfoil.run_result(al, mach=mach, Re=Re)

#%%
# Plots xfoil airfoil profile
ax1 = xfoil.plot_profile(ls='-')

#%%
# Shows plots for cases in xfoil cases
ax2 = None
for result in xfoil.results.values():
    ax2 = result.plot_result(yaxis='cp', ax=ax2)
_ = ax2.legend()

#%%
# Shows plots for cases in xfoil cases
ax3 = None
for result in xfoil.results.values():
    ax3 = result.plot_result(yaxis='ds', ax=ax3)
_ = ax3.legend()

#%%
# Shows plots for cases in xfoil cases
ax4 = None
for result in xfoil.results.values():
    ax4 = result.plot_result(yaxis='th', ax=ax4)
_ = ax4.legend()

#%%
# Shows plots for cases in xfoil cases
ax5 = None
for result in xfoil.results.values():
    ax5 = result.plot_result(yaxis='cf', ax=ax5)
_ = ax5.legend()

#%%
# Shows plots for cases in xfoil cases
ax6 = None
for result in xfoil.results.values():
    ax6 = result.plot_result(yaxis='h', ax=ax6)
_ = ax6.legend()

#%%
# Shows plots for cases in xfoil cases
ax7 = None
for result in xfoil.results.values():
    ax7 = result.plot_result(yaxis='ue', ax=ax7)
_ = ax7.legend()
