#!/usr/bin/python

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

module1 = Extension("rift",
    ["pyRiftBlend.pyx", "RiftBlend.cpp"],
    language="c++",
    libraries=["ws2_32","winmm","opengl32","Dbghelp","libOVR", "kernel32", "user32", "gdi32"],
    include_dirs=[r'C:\Users\altair\Documents\ovr_sdk_win_0.5.0.1\OculusSDK\LibOVR',r'C:\Users\altair\Documents\ovr_sdk_win_0.5.0.1\OculusSDK\LibOVRKernel\Src'])

setup(name = 'rift',
    version = '1.0',
    description = 'Python OpenHMD Wrapper',
    ext_modules=[module1],
    cmdclass = {'build_ext': build_ext})
