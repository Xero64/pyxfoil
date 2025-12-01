#%%
# Import Dependencies
# from pyxfoil import set_workdir, set_xfoilexe

#%%
# Set Working Directory
# set_workdir('C:/Xfoil_WIP')
# Use set_xfoilexe() if xfoil not added to path

#%%
# Print Out Globals
from pyxfoil import workdir, xfoilexe

print(f'workdir = {workdir:s}\n')
print(f'xfoilexe = {xfoilexe:s}\n')
