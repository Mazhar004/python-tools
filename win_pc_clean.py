import os
import glob
import getpass
import shutil
import ctypes
import sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def remove(path):
    """Remove Files"""
    files = glob.glob(path)
    for file in files:
        try:
            shutil.rmtree(file)
        except:
            try:
                os.remove(file)
            except:
                pass


def junk_clean():
    """Get Junk Paths"""
    uname = getpass.getuser()
    temp = "C:/Windows/Temp/*"
    percent_temp = f"C:/Users/{uname}/AppData/Local/Temp/*"
    recent = f"C:/Users/{uname}/Recent/*"
    prefetch = "C:/Windows/Prefetch/*"

    paths = [temp, percent_temp, recent, prefetch]
    for path in paths:
        remove(path)


def tree():
    """Run tree"""
    current_path = os.getcwd()
    os.chdir("C:/")
    os.system("tree")
    os.chdir(current_path)


def full_pc_clean():
    """Call the full pipeline"""
    junk_clean()
    tree()


if __name__ == "__main__":
    if is_admin():
        full_pc_clean()
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
