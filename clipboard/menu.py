import sys

import pyperclip

import baite_interaction
from clipboard.storage import Storage
from clipboard.watcher import Watcher


class Menu:
    @classmethod
    def run(cls):
        try:
            while True:
                cls.__clear_screen()
                print("\n-------- baite menu --------")
                print("[1] Find and load a clip")
                print("[2] Quit")

                option = input("\nPick an option: ").strip()

                if option == "1":
                    cls.__find_and_load()
                elif option == "2":
                    print("\n Putting baite to sleep... 😿")
                    break
                else:
                    print("Insert a valid option.")
        except KeyboardInterrupt:
            print("\n Putting baite to sleep... 😿")

    @classmethod
    def __clear_screen(cls):
        sys.stdout.write("\033[2J\033[H")
        print(baite_interaction.art())
        sys.stdout.flush()

    @classmethod
    def __find_and_load(cls):
        while True:
            query = input("\nSearch an 'unique' term here.. [ENTER to exit] ").strip()
            if not query:
                return

            matches = Storage.find_by(query)
            if matches:
                break

            print("No clips matched that term.")

        print()
        for index, clip in enumerate(matches, start=1):
            preview = " ".join(clip.text.split())[:150]
            print(f"[{index}] {preview}")

        selection = input("\nPick a clip to load (number): ").strip()

        try:
            clip = matches[int(selection) - 1]
        except (ValueError, IndexError):
            print("Insert a valid option.")
            return

        pyperclip.copy(clip.text)
        Watcher.mark_as_seen(clip.text)
        print("Clip loaded into the clipboard.")
