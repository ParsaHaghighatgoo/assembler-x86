from cx_Freeze import setup, Executable

setup(
    name="x86assembler",
    version="1.0",
    description="this is a x86 assembler.",
    executables=[Executable("x86assembler.py")],
)
