"""This module is associated to the latex notes template.

It is needed to:
    - clean the tikzit styles file
    - create the temporary folder for the tikz images
    - delete the temporary folder
    - delete the temporary files associated with the tex document
"""
from sys import argv
from re import M, sub
from pathlib import Path

# constants
TEMP_FOLDERS = ["tikztemp"]
TEMP_EXTENSIONS = ["aux", "auxlock", "log", "pdf", "out", "toc"]
PLACEHOLDER_EXT = ".placeholder"
ARROW_STYLE = "{Triangle[scale=0.8]}"


def clean_styles() -> None:
    """Clean the tikzstyles file as it was created by tikzit."""
    # load styles files
    with open("tikzit.tikzstyles", "r") as f:
        data = f.read()

    # remove tikzit attributes
    data = sub(r"tikzit [a-z]+=(([a-zA-Z]+)|(\{.+\}))(, )?", "", data)
    # remove none fields
    data = sub(r"[a-z]+=none(, )?", "", data)
    # replace arrows
    data = sub(r"[<>]", ARROW_STYLE, data)
    # strip comments
    data = sub(r"^%.*\n", "", data, flags=M)
    # remove empty lines
    data = sub(r"^\s*$\n", "", data, flags=M)

    # save files
    with open("tikzstyle.tikzstyles", "w") as f:
        f.write(data)


def make_folder() -> None:
    """Create the temporary folder for the tikz images."""
    for f in TEMP_FOLDERS:
        Path(f).mkdir(parents=True, exist_ok=True)
        Path(f"{f}/{PLACEHOLDER_EXT}").touch()


def delete_folder() -> None:
    """Delete the temporary folder, thus deleting all the rendered tikz images."""
    for folder in TEMP_FOLDERS:
        for file in Path(folder).iterdir():
            file.unlink()
        Path(folder).rmdir()


def delete_temp() -> None:
    """Delete all the temporary files associated with the tex document images."""
    for e in TEMP_EXTENSIONS:
        for file in Path(".").glob(f"*.{e}"):
            file.unlink(missing_ok=True)


def main(argv: list[str]) -> None:
    """Read the arguments and call the appropriate functions."""
    if "deletetemp" in argv:
        delete_temp()
        delete_folder()
    if "cleanstyle" in argv:
        clean_styles()

    make_folder()


if __name__ == "__main__":
    main(argv)
