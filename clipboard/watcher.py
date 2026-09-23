import time
import pyperclip

class Watcher:
    @classmethod
    def watch(cls):
        previous_clipboard_context = "";
        try:
            while(True):
                current_clipboard_context = pyperclip.paste()

                if current_clipboard_context != previous_clipboard_context:
                    print(current_clipboard_context);

                    previous_clipboard_context = current_clipboard_context

                    time.sleep(0.5)
        except KeyboardInterrupt:
            print ("\n Putting baite to sleep... 😿")
