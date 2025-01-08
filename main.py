import os
from pathlib import Path

import paramiko
from dotenv import load_dotenv

from src.inputs import get_source_path
from src.install import setup


def prepare_source():
    manifest = []
    source = get_source_path()
    if source.is_dir():
        files = os.listdir(source)
        for file in files:
            filename = Path.joinpath(source, file)
            manifest.append(filename)
        return manifest
    else:
        return source


def upload_files(files, hostname, port, username, keyfile):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=hostname,
        port=port,
        username=username,
        key_filename=keyfile,
        password=None,
    )

    sftp = ssh.open_sftp()
    destination = str(input("Directory name: "))
    sftp.chdir("uploads")
    print(sftp.getcwd())
    print(sftp.mkdir(destination))
    sftp.chdir(destination)
    print(sftp.getcwd())
    for file in files:
        file_path = Path.as_posix(file)
        file_name = os.path.basename(file_path)
        dest_file = f"/uploads/{destination}/{file_name}"
        #        print(dest_file)
        sftp.put(str(file_path), str(dest_file))
        print(f"Uploaded {file_name}.")
    print("All files successfully uploaded!")
    sftp.close()
    ssh.close()


if __name__ == "__main__":
    setup()
    load_dotenv(".env")
    jellyfriend_ip = os.getenv("HOST")
    jellyfriend_username = os.getenv("USER")
    jellyfriend_port = os.getenv("PORT")
    upload = prepare_source()
    ssh_dir = Path.joinpath(Path.home(), ".ssh")
    keyfile = str(Path.joinpath(ssh_dir, "id_rsa"))
    upload_files(
        upload, jellyfriend_ip, jellyfriend_port, jellyfriend_username, keyfile
    )
