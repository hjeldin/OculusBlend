#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

module1 = Extension("rift",
    ["pyRiftBlend.pyx", "RiftBlend.cpp"],
    language="c++",
    libraries=["ws2_32","winmm","opengl32","Dbghelp","libOVR", "kernel32", "user32", "gdi32"],
    include_dirs=['C:\SDK\ChironeExternals_vs10\LibOVR'])

setup(name = 'rift',
    version = '1.0',
    description = 'Python OpenHMD Wrapper',
    ext_modules=[module1],
    cmdclass = {'build_ext': build_ext})
