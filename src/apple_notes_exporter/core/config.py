import json
from pathlib import Path


CONFIG_FILE = Path(
    "config.json"
)


DEFAULT_CONFIG = {

    "export_path":
        "./export",

    "format":

    {
        "markdown": True,
        "html": True,
        "pdf": False
    }

}


class Config:


    def __init__(self):

        self.data = DEFAULT_CONFIG.copy()

        self.load()



    def load(self):

        if CONFIG_FILE.exists():

            with open(
                CONFIG_FILE,
                "r",
                encoding="utf-8"
            ):

                self.data.update(
                    json.load(
                        open(
                            CONFIG_FILE,
                            encoding="utf-8"
                        )
                    )
                )



    def save(self):

        with open(
            CONFIG_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )


config = Config()
