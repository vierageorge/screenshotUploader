import time
import threading
from PIL import ImageGrab

class ClipboardWatcher(threading.Thread):
    def __init__(self, callback, pause=1.):
        super(ClipboardWatcher, self).__init__()

        self._callback = callback
        self._pause = pause
        self._stopping = False

    def run(self):       
        recent_value = None
        while not self._stopping:
            tmp_value = ImageGrab.grabclipboard()
            if tmp_value != None and tmp_value != recent_value:
                recent_value = tmp_value
                self._callback(recent_value)
            time.sleep(self._pause)

    def stop(self):
        self._stopping = True