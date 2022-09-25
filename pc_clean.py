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
        except Exception:
            try:
                os.remove(file)
            except Exception as Err:
                print(f"Operation not completed {Err}")
                continue


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


def linux_clean():
    uname = getpass.getuser()
    os.chdir(f'/home/{uname}')
    commands = ["sudo apt autoremove",
                "sudo apt autoclean",
                "sudo apt clean",
                "sudo du -sh /var/cache/apt",
                "du -h /var/lib/snapd/snaps",
                "rm -rf ~/.cache/thumbnails/*"
                ]
    for cmd in commands:
        os.system(cmd)


def pc_clean():
    """Call the full pipeline"""
    platform = (sys.platform).lower()
    if 'win' in platform:
        if is_admin():
            junk_clean()
            tree()
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None,
                                                "runas",
                                                sys.executable,
                                                " ".join(sys.argv),
                                                None,
                                                1)

    elif platform == 'linux':
        linux_clean()


if __name__ == "__main__":
    pc_clean()
