from pathlib import Path
import json

class Storage:
    __clips: list[str] = []
    __path: Path = Path("clips.json")

    @classmethod
    def load(cls) -> list[str]:
        #load all the clips from the db
        if cls.__path.exists():
            cls.__clips = json.loads(cls.__path.read_text())
        return cls.__clips

    @classmethod
    def find_by(cls, query) -> list[str]:
        #find a clip that matches the search queries
        return [clip for clip in cls.__clips if query in clip]

    @classmethod
    def save(cls, clip: str) -> None:
        #save a clip on the json
        cls.load()
        cls.__clips.append(clip)
        cls.__persist()

    @classmethod
    def __purge(cls):
        #deletes batches of clips from the db
        userSelection = input("Are you sure that you want to purge the clips?: (y) yes ... (n) no")
        if userSelection == 'y' or userSelection == "Y":
            cls.__clips = []
            cls.__persist()
        else:
            print("Insert a valid option to purge it.")

    @classmethod
    def __persist(cls):
        cls.__path.write_text(json.dumps(cls.__clips, indent=2))