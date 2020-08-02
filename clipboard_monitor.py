import time
from ClipboardWatcher import ClipboardWatcher

def main():
    watcher = ClipboardWatcher(.5)
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