import os
import shutil
from pathlib import Path

from dotenv import load_dotenv
from fabric import Connection

load_dotenv(".env")
JELLYFRIEND_IP = os.getenv("HOST")
JELLYFRIEND_USERNAME = os.getenv("USER")
JELLYFRIEND_PORT = os.getenv("PORT")


def get_ssh_dir():
    home = Path.home()
    ssh_dir = Path.joinpath(home, ".ssh")
    return ssh_dir


def verify_id(ssh_dir):
    id_rsa = Path.joinpath(ssh_dir, "id_rsa")
    if Path.exists(ssh_dir):
        if id_rsa.exists():
            return
        else:
            shutil.move("id_rsa", str(id_rsa))
            return
    else:
        os.mkdir(ssh_dir)
        shutil.move("id_rsa", str(id_rsa))
        return


def choose_files():
    path_to_files = Path(input("File(s) to upload."))
    return path_to_files


def main():
    c = Connection(
        host=JELLYFRIEND_IP, user=JELLYFRIEND_USERNAME, port=JELLYFRIEND_PORT
    )
    ssh_dir = get_ssh_dir()
    verified_id = verify_id(ssh_dir)
    if verified_id == 0:
        raise Exception("Missing id_rsa")
    elif verified_id == 100:
        files = choose_files()
        result = c.put(files, remote="/uploads")
        print("Uploaded {0.local} to {0.remote}".format(result))
    else:
        print("Something went awfully wrong...")


main()
