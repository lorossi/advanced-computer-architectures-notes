from pathlib import Path
from re import M, sub
from sys import argv

TEMP_FOLDER = "tikztemp"
TEMP_EXTENSIONS = ["aux", "auxlock", "log", "pdf", "out", "toc"]
TEMP_FILE_NAME = ".placeholder"
ARROW_STYLE = "{Triangle[scale=0.8]}"


def clean_styles() -> None:
    """cleans the tikzstyles file as it was created by tikzit"""
    # load styles files
    with open("tikzit.tikzstyles", "r") as f:
        data = f.read()

    # remove tikzit attributes
    data = sub("tikzit [a-z]+=(([a-zA-Z]+)|(\{.+\}))(, ){0,1}", "", data)
    # remove none fields
    data = sub("[a-z]*=none(, ){0,1}", "", data)
    # replace arrows
    data = sub("[<>]", ARROW_STYLE, data)
    # strip comments
    data = sub("^%.*\n", "", data, flags=M)
    # remove empty lines
    data = sub("^\s*$\n", "", data, flags=M)

    # save files
    with open("tikzstyle.tikzstyles", "w") as f:
        f.write(data)


def make_folder() -> None:
    Path(TEMP_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(f"{TEMP_FOLDER}/{TEMP_FILE_NAME}").touch()


def delete_folder() -> None:
    for file in Path(TEMP_FOLDER).iterdir():
        file.unlink()
    Path(TEMP_FOLDER).rmdir()


def delete_temp() -> None:
    for e in TEMP_EXTENSIONS:
        for file in Path(".").glob(f"*.{e}"):
            file.unlink(missing_ok=True)


def main(argv: list[str]) -> None:
    if "delete" in argv:
        delete_temp()
        delete_folder()
    if "clean" in argv:
        clean_styles()

    make_folder()


if __name__ == "__main__":
    main(argv)
