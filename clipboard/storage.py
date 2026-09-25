import json
from pathlib import Path

import baite_interaction
from domain import Clip


class Storage:
    __clips: list[Clip] = []
    __path: Path = Path("clips.json")

    @classmethod
    def load(cls) -> list[Clip]:
        # load all the clips from the db
        if cls.__path.exists():
            raw_clips = json.loads(cls.__path.read_text())
            cls.__clips = [Clip.to_raw(clip) for clip in raw_clips]
        return cls.__clips

    @classmethod
    def find_by(cls, query) -> list[Clip]:
        # find a clip that matches the search queries
        return [clip for clip in cls.__clips if query in clip.text]

    @classmethod
    def save(cls, text: str) -> None:
        # save a clip on the json
        cls.load()
        cls.__clips.append(Clip(text=text))
        cls.__persist()

    @classmethod
    def __purge(cls):
        # deletes batches of clips from the db
        userSelection = input(
            "Are you sure that you want to purge the clips?: (y) yes ... (n) no"
        )
        if userSelection == "y" or userSelection == "Y":
            cls.__clips = []
            cls.__persist()
        else:
            print("Insert a valid option to purge it.")

    @classmethod
    def __persist(cls):
        cls.__path.write_text(
            json.dumps([clip.to_dict() for clip in cls.__clips], indent=2)
        )
