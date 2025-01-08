import os
import shutil
import sys
from pathlib import Path

from rich import print as print


def verify_env():
    env_path = Path(".env")
    if Path.exists(env_path):
        return True
    else:
        return False


def write_env():
    jellyfriend_ip = input("Jellyfin Remote IP: ")
    jellyfriend_port = input("Jellyfin Port: ")
    jellyfriend_username = input("Jellyfriend Username: ")
    data = f'HOST="{jellyfriend_ip}"\nPORT={int(jellyfriend_port)}\nUSER="{jellyfriend_username}"'
    with open(".env", "w") as env_file:
        env_file.write(data)


def query_env():
    print("\nNo .env file found.  Would you like to create one now? [Y/n] ")
    answer = input("").lower()
    if answer in ["", "y"]:
        return True
    else:
        return False


def create_ssh_dir(ssh_dir):
    os.mkdir(ssh_dir)


def move_rsa_key(ssh_dir, rsa_key):
    id_rsa = Path.joinpath(ssh_dir, "id_rsa")
    shutil.copy(rsa_key, str(id_rsa))


def setup():
    if getattr(sys, "frozen", False):
        rsa_key = os.path.join(sys._MEIPASS, "id_rsa")
    else:
        rsa_key = "id_rsa"
    ssh_dir = Path.joinpath(Path.home(), ".ssh")
    id_rsa = Path.joinpath(ssh_dir, "id_rsa")
    env = Path(".env")
    if not ssh_dir.exists():
        create_ssh_dir(ssh_dir)
        move_rsa_key(ssh_dir, rsa_key)
        print(f"Created {ssh_dir}.\nMoved {rsa_key}.\n")
    elif not id_rsa.exists():
        move_rsa_key(ssh_dir, rsa_key)
        print(f"Moved {rsa_key}\n")

    if not env.exists():
        if query_env() == True:
            write_env()
            print("Wrote .env.\n")
        else:
            print("Not writing .env file. Program will now close.\n")
            raise FileNotFoundError()


if __name__ == "__main__":
    setup()
