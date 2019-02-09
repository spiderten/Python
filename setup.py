from cx_Freeze import setup, Executable
 
setup(
    name="calculadora1 EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("calculadora1.py")])
