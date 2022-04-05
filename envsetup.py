from re import sub, M

ARROW_STYLE = "{Triangle[scale=0.8]}"


def clean_styles() -> None:
    """cleans the tikzstyles file as it was created by tikzit"""
    # load styles files
    with open(f"tikzit.tikzstyles", "r") as f:
        data = f.read()

    # remove tikzit attributes
    data = sub("tikzit [a-z]*=(([a-z]+)|(\{.+\}))((, )|(?=\]))", "", data)
    # remove orphan commas
    data = sub("(?<=(\}|[a-z]|[<>])), (?=\])", "", data)
    # replace arrows
    data = sub("[<>]", ARROW_STYLE, data)
    # strip comments and empty lines
    data = sub("(^%.*\n)|(^\n*)", "", data, flags=M)

    # save files
    with open("tikzstyle.tikzstyles", "w") as f:
        f.write(data)


if __name__ == "__main__":
    clean_styles()
