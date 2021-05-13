# Python delete file

import os
import shutil

path = "copy.txt"

try:
    # os.remove(path)
    # os.rmdir(path)
    shutil.rmtree(path) #delete folder and content
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete that usign that function")
else:
    print(path + " was deleted")
