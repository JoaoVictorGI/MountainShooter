from cx_Freeze import Executable, setup

executables = [Executable("./src/main.py")]

setup(
    name="MountainShooter",
    version="1.0",
    description="Mountain Shooter Game",
    # options={"build_exe": files},
    executables=executables,
)
