import datetime 
import pathlib
import shutil
import sys

def get_path():
    source_icloud = pathlib.Path(r"D:/iCloudDrive")
    backup_root = pathlib.Path(r"E:/")
    return source_icloud, backup_root

source_icloud, backup_root = get_path()

def get_time():
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    return today, year, month, day

today, year, month, day = get_time()

def set_target():
    target = backup_root / str(year) / str(month)
    return target

target = set_target()

def set_logging_dir():
    logging_dir = backup_root / "Logging data"
    logging_dir.mkdir(parents=True, exist_ok=True)
    return logging_dir

logging_dir = set_logging_dir()

def check_is_dir():
    if not source_icloud.is_dir(): # searching for icloud
        print("Icloud not found")
        sys.exit(1)
    else:
        print("Icloud found")

    if not backup_root.is_dir(): # searching for backup
        print("Backup not found")
        sys.exit(1)
    else:
        print("Backup found")

check_is_dir()

def run_backup(): # backup process 
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

copied_files, updated_files, skipped_files, failed_update_files, failed_copy_files = run_backup()

def create_logging_file():
    backup_log = logging_dir / f"Backup_log_{year}_{month}_{day}.txt"
    backup_log = open(backup_log, "w")
    backup_log.write(f"Backup finished.\nCopied files: {copied_files}.\nUpdated files: {updated_files}.\nSkipped files: {skipped_files}.\nFailed update files: {failed_update_files}.\nFailed copy files: {failed_copy_files}.\nDate: {year}.{month}.{day}")
    backup_log.close
    print("Backup log created")
    return backup_log

backup_log = create_logging_file()

print(f"Backup finished.\nCopied files: {copied_files}.\nUpdated files: {updated_files}.\nSkipped files: {skipped_files}.\nFailed update files: {failed_update_files}.\nFailed copy files: {failed_copy_files}.\nDate: {year}.{month}.{day}")