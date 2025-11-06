# WEBFISHING Backup Creator by Gvwyn - 2025
import os, shutil
from datetime import datetime as thetime
from pathlib import Path

CFGPATH = Path("config.cfg")
DEFAULTFOLDER = f"C:\\Users\\{os.getlogin()}\\OneDrive\\WEBFISHING Backups"

# if config file doesn't exist, create it
if not CFGPATH.exists():
    CFGPATH.write_text(DEFAULTFOLDER)

timestamp = thetime.now().strftime("%Y%m%d-%H%M%S")
backup_folder = Path(CFGPATH.read_text().strip()) / timestamp
backup_folder.mkdir(parents=True, exist_ok=True)

source = Path(os.getenv("APPDATA")) / "Godot/app_userdata/webfishing_2_newver"

if not source.exists():
    print(" _____  _\tyou don't seem to have any savefiles... yet")
else:
    print(" _____  _\tcreating the backup...")
    shutil.copytree(source, backup_folder, dirs_exist_ok=True)

input(f"/_ o  \\/ |\tbackup successful to {backup_folder} :)\n\\_____/\\_|\tpress enter to leave the terminal")
os.startfile(backup_folder)