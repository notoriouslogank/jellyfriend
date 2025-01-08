from pathlib import Path


def get_source_path():
    source = Path(input("File or directory to upload:\n"))
    return source


def get_destination_path():
    dirname = input("Name for this directory:\n")
    root = Path("uploads")
    destination_path = Path.joinpath(root, dirname)
    return destination_path
