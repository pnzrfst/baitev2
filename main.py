import threading

import baite_interaction
from clipboard.menu import Menu
from clipboard.storage import Storage
from clipboard.watcher import Watcher


def main():
    baite_interaction.play()
    Storage.load()

    threading.Thread(target=Watcher.watch, daemon=True).start()

    Menu.run()


if __name__ == "__main__":
    main()
