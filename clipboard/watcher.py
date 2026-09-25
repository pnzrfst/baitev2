import time
import pyperclip

from clipboard.storage import Storage


class Watcher:
    __last_seen: str = ""

    @classmethod
    def mark_as_seen(cls, text: str) -> None:
        cls.__last_seen = text

    @classmethod
    def watch(cls):
        try:
            while(True):
                current_clipboard_context = pyperclip.paste()

                if current_clipboard_context != cls.__last_seen:
                    Storage.save(current_clipboard_context)

                    cls.__last_seen = current_clipboard_context

                    time.sleep(0.5)
        except KeyboardInterrupt:
            print ("\n Putting baite to sleep... 😿")