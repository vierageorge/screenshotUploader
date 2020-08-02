import time
from clipboard_watcher import clipboard_watcher
from google_docs_uploader import google_docs_uploader

def main():
    print('GoogleDocs file url: ')
    file_url = input()
    watcher = clipboard_watcher(.2)
    gdocs_uploader = google_docs_uploader(file_url, 5.)
    watcher.start()
    gdocs_uploader.start()
    while True:
        try:
            print("Waiting for changed clipboard...")
            time.sleep(10)
        except KeyboardInterrupt:
            watcher.stop()
            gdocs_uploader.stop()
            break

if __name__ == "__main__":
    main()