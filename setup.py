from cx_Freeze import setup, Executable

setup(
    name="TRAKTOR",
    version="1.0",
    description="TRAKTOR",
    executables=[Executable("index.py")]
)