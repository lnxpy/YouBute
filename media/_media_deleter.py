import os, shutil
from time import sleep as slp

folder = './videos'

while True:
    slp(30*60) # equals 30 minutes
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
            print('> %s Removed successfully.'%file_path)
        except Exception as e:
            print('> Failed to delete %s. Reason: %s' % (file_path, e))
