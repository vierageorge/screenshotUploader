import time
from datetime import datetime
import threading
from os import listdir
from os.path import isfile, join, splitext
from global_settings import IMAGE_DIR, ALLOWED_EXTENSIONS

class google_docs_uploader(threading.Thread):
    def __init__(self, file_url, pause=5.):
        super(google_docs_uploader, self).__init__()
        self._pause = pause
        self._stopping = False
        self._file_id = file_url.replace('https://docs.google.com/document/d/','').split('/')[0]

    def run(self):       
        while not self._stopping:
            now = datetime.now()
            image_files = self.get_image_dir_allowed_files()
            if len(image_files) > 0:
                print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - Files: {onlyfiles}')
            else:
                print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - No files to upload')
            time.sleep(self._pause)
    
    def stop(self):
        now = datetime.now()
        print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - Stopping Google Docs Uploader')
        self._stopping = True

    def get_image_dir_allowed_files(self):
        onlyfiles = [f for f in listdir(IMAGE_DIR) if isfile(join(IMAGE_DIR, f)) and splitext(f)[1].lower() in ALLOWED_EXTENSIONS]
        return onlyfiles