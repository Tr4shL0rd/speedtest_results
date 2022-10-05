import os
import os.path
import pathlib

def get_files():
    path = pathlib.Path().resolve()#path = r"/home/tr4shl0rd/programmingLanguages/python/speedtest_results"
    list_of_files= []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith("py") and "tools" not in os.path.join(root,file):
                list_of_files.append(os.path.join(root,file))

    return [name for name in list_of_files]
print(get_files())
    
