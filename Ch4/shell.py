import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():

    # Duplicate file step-by-step
    if path.exists("textfile.txt"):
        # Get the path to the file in the current directory
        src = path.realpath("textfile.txt")

        # Create the copy path
        # dst = src + ".bak"

        # Copy content
        # shutil.copy(src, dst)

        # Copy over the permissions, modification times, and other info
        # shutil.copystat(src, dst)

        # Rename file
        # os.rename("textfile.txt", "newfile.txt")

        # Put into zip
        # root_dir, filename = path.split(src)
        # shutil.make_archive("archive", "zip", root_dir)

        # Put into with more resources
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")



if __name__ == "__main__":
    main()