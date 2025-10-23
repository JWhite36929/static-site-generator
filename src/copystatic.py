import os
import shutil

def copy_files_from_to(src, dst="public"):
    """
    Copy all files from the 'static' directory to the newly created 'public' directory.
    """

    if os.path.exists(dst):
        shutil.rmtree(dst)

    shutil.copytree(src, dst)

    print(f"Copied all files from {src} to {dst}")