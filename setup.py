import os, numpy
from distutils.sysconfig import get_python_lib
from setuptools import setup, Extension




# Necessary to create the version.py file for mdentropy to be able to use the original repo directly as a submodule
#from .Packages.mdentropy.basesetup import write_version_py
VERSION = "0.4.0dev0"
ISRELEASED = False
#write_version_py(VERSION, ISRELEASED, 'Packages/mdentropy/mdentropy/version.py')





libinteract = \
      Extension("libinteract.innerloops",
                ["Packages/pyinteraph2/libinteract/innerloops.pyx",
                 "Packages/pyinteraph2/libinteract/clibinteract.c"], \
                include_dirs = [numpy.get_include()])






mdtrajdir = get_python_lib() + "/mdtraj/core/lib"
mdtraj_capi = {'include_dir': mdtrajdir, 'lib_dir': mdtrajdir}

libdistance = \
    Extension('msmbuilder.libdistance',
              language='c++',
              sources=['Packages/msmbuilder/msmbuilder/libdistance/libdistance.pyx'],
              # msvc needs to be told "libtheobald", gcc wants just "theobald"
              libraries=['theobald'],#'%stheobald' % ('lib' if compiler.msvc else '')],
              include_dirs=["Packages/msmbuilder/msmbuilder/libdistance/src",
                            mdtraj_capi['include_dir'], numpy.get_include()],
              library_dirs=[mdtraj_capi['lib_dir']],
              )




on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
	ext_modules = []
else:
	ext_modules = [libinteract, libdistance]





# Where the magic happens:
setup(
    ext_modules = ext_modules
    )
