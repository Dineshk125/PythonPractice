# Delete empty directory

import os

if os.path.exists("folder 1"):
    os.remove("folder 1")
    print("Directory deleted.")
else:
    print("Directory dose not exists.")


## Deleting a directory and its contents

# import os
# import shutil
# if os.path.exists("fsMethods.py"):
#     shutil.rmtree("fsMethods.py")
#     print("Directory and its content deleted.")
# else:
#     print("cant delete file and content")
