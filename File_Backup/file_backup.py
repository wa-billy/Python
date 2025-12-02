import os
import shutil
import datetime
import schedule
import time

source_dir = "File_Backup/sources"
dest_dir = "File_Backup/backups"

def copy_folder_to_dir(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

copy_folder_to_dir(source_dir, dest_dir)




# Lambda is use for call function inline
schedule.every().day.at("time").do(lambda: copy_folder_to_dir(source_dir, dest_dir))

while True:
    schedule.run_pending()
    time.sleep(60)

