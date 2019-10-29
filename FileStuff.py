import os
import shutil
from datetime import datetime

def printDir(path='.', numTabs=0, recursive=False):
    '''
        This guy is chill to print out all files
        in a directory (including subdirs!)
    '''
    directory = os.scandir(path)
    tabs = '|'
    for i in range(0, numTabs+1):
        tabs += '\t' 
    for entry in directory:
        if entry.is_file():
            print(tabs, "File:",entry.name)
        elif entry.is_dir():
            print(tabs, "Directory:", entry.name)
            if recursive:
                printDir(path + "/" + entry.name, numTabs+1)

def printInfo():
    '''
        This guy is chill to print OS information
        regarding a file in the current directory!
        We also get some dealings with time (the devil)
    '''
    toMDY = lambda time : datetime.utcfromtimestamp(time).strftime('%b %d, %Y - %H:%M:%S')
    directory = os.scandir('.')
    spacer = " -"
    for entry in directory:
        print(entry.name)
        info = entry.stat()
        print(spacer, "File type and permissions:",info.st_mode)
        print(spacer, "Inode number:",info.st_ino)
        print(spacer, "Device ID:",info.st_dev)
        print(spacer, "Number of hard links:",info.st_nlink)
        print(spacer, "UID:",info.st_uid)
        print(spacer, "GID:",info.st_gid)
        print(spacer, "Size (bytes):",info.st_size)
        print(spacer, "Last access time (s):",toMDY(info.st_atime))
        print(spacer, "Last modify time (s):",toMDY(info.st_mtime))
        print(spacer, "Last metadata change time (s):",toMDY(info.st_ctime))
        break

def makeDirsAndFiles():
    '''
        This guy makes a bunch of directories and files
    '''
    try:
        os.mkdir('./MyNewDirectory')
    except FileExistsError as e:
        print("Directory exists!")
    os.makedirs('./MyNewDirectory/My/New/Directory', exist_ok=True)
    for i in range(0,4):
        for extension in ['.py', '.txt']:
            fileName = "MyNewDirectory/My/New/Directory/"+str(i)+extension
            with open (fileName, 'w') as f:
                f.write("Oh hi there :)")

def copyAndMove():
    '''
        This guy copies stuff and moves stuff
    '''
    basedir = "./MyNewDirectory/My/New/Directory/"
    try:
        shutil.copytree(basedir, basedir+"backup")
    except FileExistsError as e:
        print("Already exists :)")
    os.rename(basedir+"backup", basedir+"backup2")
    os.rename(basedir+"backup2/0.py", basedir+"backup2/cool.py")
    shutil.move(basedir+"backup2/", basedir+"renamedIt/")
    shutil.move(basedir+"renamedIt/", "./MyNewDirectory/My/New")


def deleteStuff():
    '''
        This guy deletes stuff we just made
    '''
    basedir = "./MyNewDirectory/My/New/renamedIt/"
    directory = os.scandir(basedir)
    for entry in directory:
        os.remove(basedir + entry.name)
    os.rmdir(basedir)
    
    basedir = "./MyNewDirectory/My/New/Directory/"
    directory = os.scandir(basedir)
    for entry in directory:
        os.remove(basedir + entry.name)
    
    basedir = basedir[:basedir.rfind('/')]
    while basedir.rfind('/') != -1:
        os.rmdir(basedir)
        basedir = basedir[:basedir.rfind('/')]


if __name__ == "__main__":
    printDir(recursive=False)
    printInfo()
    makeDirsAndFiles()
    copyAndMove()
    deleteStuff()
