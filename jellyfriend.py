import os
import shutil
import sys
from pathlib import Path

from dotenv import load_dotenv
from fabric import Connection
from rich import print as print

if getattr(sys, "frozen", False):
    raw_id_rsa = os.path.join(sys._MEIPASS, "id_rsa")
else:
    raw_id_rsa = "id_rsa"


def create_env():
    jellyfriend_ip = input("Jellyfin Remote IP: ")
    jellyfriend_port = input("Jellyfin port: ")
    jellyfriend_username = input("Jellyfriend username: ")
    data = f'HOST="{jellyfriend_ip}"\nPORT={int(jellyfriend_port)}\nUSER="{jellyfriend_username}"'
    with open(".env", "w") as env_file:
        env_file.write(data)


def check_env():
    env_path = Path(".env")
    if Path.exists(env_path):
        return 100
    else:
        print("Missing .env file!  Would you like to create one now? [Y/n]")
        write_env = input("").lower()
        if write_env == "":
            return 50
        elif write_env == "y":
            return 50
        elif write_env == "n":
            print("no")
            return 0
        else:
            print("Invalid response! Exiting without creating .env file!")
            raise Exception("Invalid response.")


def get_ssh_dir():
    home = Path.home()
    ssh_dir = Path.joinpath(home, ".ssh")
    return ssh_dir


def verify_id(ssh_dir):
    id_rsa = Path.joinpath(ssh_dir, "id_rsa")
    if Path.exists(ssh_dir):
        if id_rsa.exists():
            return 100
        else:
            shutil.move(raw_id_rsa, str(id_rsa))
            return 100
    else:
        os.mkdir(ssh_dir)
        shutil.move(raw_id_rsa, str(id_rsa))
        return 0


def get_upload_path():
    path_to_files = Path(input("File(s) to upload."))
    uploads = []
    if Path.is_dir(path_to_files):
        files = os.listdir(path_to_files)
        for file in files:
            filename = Path.joinpath(path_to_files, file)
            uploads.append(filename)
        return uploads
    else:
        return path_to_files


# def iterate_through_dir(files):


def main():
    env_exists = check_env()
    print(env_exists)
    if env_exists == 100:
        pass
    elif env_exists == 50:
        create_env()
    elif env_exists == 0:
        raise Exception(
            "Missing .env file.  Please create one before running application."
        )
    load_dotenv()
    JELLYFRIEND_IP = os.getenv("HOST")
    JELLYFRIEND_USERNAME = os.getenv("USER")
    JELLYFRIEND_PORT = os.getenv("PORT")
    c = Connection(
        host=JELLYFRIEND_IP, user=JELLYFRIEND_USERNAME, port=JELLYFRIEND_PORT
    )
    ssh_dir = get_ssh_dir()
    verified_id = verify_id(ssh_dir)
    if verified_id == 0:
        raise Exception("Missing id_rsa")
    elif verified_id == 100:
        files = get_upload_path()
        for file in files:
            result = c.put(file, remote="/uploads")
            # result = c.put(files, remote="/uploads")
            print("Uploaded {0.local} to {0.remote}".format(result))
    else:
        print("Something went awfully wrong...")


# get_upload_path()
main()
