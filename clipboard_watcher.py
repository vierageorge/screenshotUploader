import time
import threading
from datetime import datetime
from os import path
from uuid import uuid4
from PIL import ImageGrab
from global_settings import IMAGE_DIR

class clipboard_watcher(threading.Thread):
    def __init__(self, pause=1.):
        super(clipboard_watcher, self).__init__()

        self._pause = pause
        self._stopping = False

    def run(self):       
        recent_value = None
        while not self._stopping:
            tmp_value = ImageGrab.grabclipboard()
            if tmp_value != None and tmp_value != recent_value:
                recent_value = tmp_value
                self.save_image(recent_value)
            time.sleep(self._pause)

    def stop(self):
        now = datetime.now()
        print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - Stopping Clipboard Watcher.')
        self._stopping = True

    def save_image(self, clipboard_content):
        now = datetime.now()
        try:
            filename = str(uuid4()).replace('-','')+'.png'
            clipboard_content.save(path.join(IMAGE_DIR, filename), 'PNG')
            print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - Found a new image, saving it locally.')
        except:
            print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - Found a new image, but couldn\'t save it.')