from pathlib import Path
import json

class Storage:
    __clips: list[str] = []
    __path: Path = Path("clips.json")

    @classmethod
    def __load(cls) -> list[str]
        #load all the clips from the db
        print("Type anything that you want to search on baite... ")
        if cls.__path.exists:
            cls.__clips = json.loads(cls.__path.read_text())
        return cls.__clips

    @classmethod
    def __find_by(cls, query) -> list[str]
        #find a clip that matches the search querys
        print("Search an 'unique' term here..")
        return [clip for clip in cls.__clips if query in clip]

    @classmethod
    def __save(cls, clip: str) -> None
        #save an clip on the json
        print("Saving it, so you can see it later... ")
        cls.__clips.append(clip)
        cls.__persist()

    @classmethod
    def __purge(cls):
        #deletes from batchsOf from the db

        userSelection = input("Are u sure that you want to purge those intervals?: (y) yes ... (n) no")
        if userSelection == 'y' or userSelection == "Y":
            cls.__clips = []
            cls.__persist()
        else:
            print("Insert a valid option to purge it.")

    @classmethod
    def __persist(cls)
