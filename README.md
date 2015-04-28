OculusBlend
===========

Build dependencies
---
* Visual C++
* Cython 0.22
* Python 3.4
* Blender 2.72b
* Oculus SDK

Build instructions
----
Copy and paste the **libOVR.lib** that match your system configuration from Oculus SDK to VS/python_bindings then edit setup.py adjusting the include_dirs option with your LibOVR folder path and the other required depending on your Oculus SDK version. Finally open command prompt, navigate to VS/python_bindings:

`python setup.py build_ext`

followed by

`python setup.py build --inplace`

The compiled .pyd can be found in build/lib.win32-3.4/rift.pyd, now move this file to your Blender/2.72/scripts/addons folder for have the Oculus in the embedded player. For using the standalone player copy the .pyd to your Blender/2.72/python/lib folder.

Remarks
----
* If during the building you get an error like this **Unicode Error "unicodeescape" codec can't decode bytes...**, probably you have an escape sequence in your include_dirs path. To fix it place an 'r' before the string to produce a raw one.
* For building Cython is better have Visual Studio 2010 installed on your machine.
