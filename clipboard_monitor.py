import time
from datetime import datetime
from os import path
from uuid import uuid4
from ClipboardWatcher import ClipboardWatcher

IMAGE_FOLDER = 'img'

def save_image(clipboard_content):
    now = datetime.now()
    try:
        filename = str(uuid4()).replace('-','')+'.png'
        clipboard_content.save(path.join(IMAGE_FOLDER, filename), 'PNG')
        print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - Found a new image, saving it locally.')
    except:
        print (f'{now.strftime("%Y/%m/%d %H:%M:%S")} - Found a new image, but couldn\'t save it.')

def main():
    watcher = ClipboardWatcher( save_image,
                                .5)
    watcher.start()
    while True:
        try:
            print("Waiting for changed clipboard...")
            time.sleep(10)
        except KeyboardInterrupt:
            watcher.stop()
            break


if __name__ == "__main__":
    main()