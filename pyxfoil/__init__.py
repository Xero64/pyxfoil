from os import curdir

def find_xfoil(exe):
    def is_exe(fpath):
        from os.path import isfile
        from os import access, X_OK
        return isfile(fpath) and access(fpath, X_OK)
    from os.path import split, join
    from os import environ, pathsep
    fpath, _ = split(exe)
    if fpath:
        if is_exe(exe):
            return exe
    else:
        for path in environ["PATH"].split(pathsep):
            exe_file = join(path, exe)
            if is_exe(exe_file):
                return exe_file
    return None

xfoilexe = find_xfoil('xfoil.exe')
workdir = None

def set_xfoilexe(xfoil):
    global xfoilexe
    xfoilexe = xfoil

def set_workdir(wdir):
    from os.path import join
    wdir = join(wdir, '')
    if ' ' in wdir:
        print('The workding directory should have no spaces.')
    global workdir
    workdir = wdir

set_workdir(curdir)

from .xfoil import Xfoil
