OculusBlend
===========

Dependencies
---
* Visual C++
* Cython 
* Python 3.4
* Blender 2.72b
* Oculus SDK

Build instructions
----
Copy&paste your libOVR.lib in VS/python_bindings.  
Open command prompt, navigate to VS/python_bindings and launch `python setup.py build_ext` followed by `python setup.py build --inplace`
