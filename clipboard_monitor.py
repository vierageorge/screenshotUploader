import time
from clipboard_watcher import clipboard_watcher

def main():
    watcher = clipboard_watcher(.2)
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