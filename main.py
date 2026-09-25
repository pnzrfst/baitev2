from pathlib import Path
import threading

import pyperclip

from clipboard.storage import Storage
from clipboard.watcher import Watcher

def main():
    print(Path("baite_art.txt").read_text())
    Storage.load()

    threading.Thread(target=Watcher.watch, daemon=True).start()

    menu()


def menu():
    while True:
        print("\n-------- baite menu --------")
        print("[1] Find and load a clip")
        print("[2] Quit")

        option = input("\nPick an option: ").strip()

        if option == "1":
            find_and_load()
        elif option == "2":
            print("\n Putting baite to sleep... 😿")
            break
        else:
            print("Insert a valid option.")


def find_and_load():
    query = input("\nSearch an 'unique' term here.. ").strip()
    matches = Storage.find_by(query)

    if not matches:
        print("No clips matched that term.")
        return

    print()
    for index, clip in enumerate(matches, start=1):
        preview = " ".join(clip.split())[:60]
        print(f"[{index}] {preview}")

    selection = input("\nPick a clip to load (number): ").strip()

    try:
        clip = matches[int(selection) - 1]
    except (ValueError, IndexError):
        print("Insert a valid option.")
        return

    pyperclip.copy(clip)
    Watcher.mark_as_seen(clip)
    print("Clip loaded into the clipboard.")



if __name__ == "__main__":
    main()