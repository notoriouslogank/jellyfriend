# Jellyfriend

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

Jellyfriend is a simple, safe script allowing arbitrary file uploads to a remote Jellyfin server.  Notably, Jellyfriend does **not** require Jellyfin login permissions -- everything happens on an *ad hoc* SFTP connection (which must be configured on the remote prior to use).

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your machine.

### Prerequisites

SSH is required for Jellyfriend to function.  Linux users generally have this installed by default; if not, it can easily be installed (on Debian 12) with:

```bash
sudo apt install openssh-client
```

For Windows installations, please see [this](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui&pivots=windows-server-2025) guide.

### Installing

#### Linux

**NOTE:** It is highly recommended to install Jellyfriend inside a virtualenv; for the sake of simplicity, hoever, this installation tutorial will assume the installation will be on bare metal.

Clone the repo.

```bash
git clone https://github.com/notoriouslogank/jellyfriend.git
```

Install necessary dependencies.

```bash
pip install -r requirements.txt
```

The first time Jellyfriend is launched, it will attempt to create a .env file for remote host configuration (if a .env file does not exist in the current directory).  Simply follow the prompts to create the .env file.

#### Windows

Jellyfriend has a ready-to-use executable version available for download [here](https://github.com/notoriouslogank/jellyfriend/releases).  Simply download the file(s) and double-click the executable file to get up and running.

## Usage <a name = "usage"></a>

Jellyfriend can be run from the command line.

Linux:

```bash
python3 jellyfriend.py
```

Windows:

```bash
python.exe jellyfriend.py
```
