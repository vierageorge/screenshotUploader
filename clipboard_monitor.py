import time
from ClipboardWatcher import ClipboardWatcher

def print_to_stdout(clipboard_content):
    print ("Found a new image. Saving it locally.")

def main():
    watcher = ClipboardWatcher( print_to_stdout,
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