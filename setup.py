# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:33:42 2017

@author: DELL
"""
 
 
 
import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["Tkinter","ttk"],"include_files": 
    ["rbd.ico","5.png","a1.png","b8.png","i1.ico","refresh2.ico"]}

 
base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Module_Testing_Tool",
    version = "0.3",
    description = "GUI to debug",
    options = {"build_exe": build_exe_options},
    executables = [Executable("RBD2.py", base = base,icon="rbd.ico")])