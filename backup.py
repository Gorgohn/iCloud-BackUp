import datetime 
import pathlib
import shutil
import sys

source_icloud = pathlib.Path(r"D:/iCloudDrive")
backup_root = pathlib.Path(r"E:/")

today = datetime.date.today()
year = today.year
month = today.month

target = backup_root / str(year) / str(month)

if not source_icloud.is_dir(): # searching for icloud
    print("Icloud not found")
    sys.exit(1)

if not backup_root.is_dir(): # searching for backup
    print("Backup not found")
    sys.exit(1)

print("Icloud found")
print("Backup found")

def run_backup(): # creating function
    copied_files = 0
    skipped_files = 0
    updated_files = 0
    failed_update_files = 0
    failed_copy_files = 0

    for new_file in source_icloud.rglob("*"): # getting all files
        if new_file.is_file(): # get path of icloud file and create path in backup
            relative_path = new_file.relative_to(source_icloud)
            destination_file = target / relative_path
            destination_file.parent.mkdir(parents=True, exist_ok=True)
            if destination_file.exists(): # setting timestamp for existing files in the backup
                icloud_file_time = new_file.stat().st_mtime
                backup_file_time = destination_file.stat().st_mtime
                try:
                    if icloud_file_time > backup_file_time: # if icloud file is newer than backup file, update the file
                        shutil.copy2(new_file, destination_file)
                        updated_files += 1
                    else: # if backup file is newest, count + 1 skipped file 
                        skipped_files += 1
                except OSError:
                    failed_update_files += 1
                    print(f"Error while updating file: {new_file}")
            else:
                try: # if file is not in backup, copy to backup
                    shutil.copy2(new_file, destination_file)
                    copied_files += 1
                except OSError:
                    failed_copy_files += 1
                    print(f"Error while copying file: {new_file}")
    return copied_files, updated_files, skipped_files, failed_update_files, failed_copy_files # returning values to global

copied_files, updated_files, skipped_files, failed_update_files, failed_copy_files = run_backup() # getting values and running function

print(f"Backup finished. Copied files: {copied_files}. Updated files: {updated_files}. Skipped files: {skipped_files}. Failed update files: {failed_update_files}. Failed copy files: {failed_copy_files}.")
