import datetime 
import pathlib
import shutil

source_icloud = pathlib.Path(r"D:/test_dir")
backup_root = pathlib.Path(r"E:/")

today = datetime.date.today()
year = today.year
month = today.month

target = backup_root / str(year) / str(month)

if source_icloud.is_dir():
    print("Source found")
    copied_files = 0
    skipped_files = 0
    updated_files = 0

    for icloud_document in source_icloud.rglob("*"):

        if icloud_document.is_file():
            relative_path = icloud_document.relative_to(source_icloud)
            destination_file = target / relative_path

            destination_file.parent.mkdir(parents=True, exist_ok=True)

            if destination_file.exists():
                icloud_file_time = icloud_document.stat().st_mtime
                backup_file_time = destination_file.stat().st_mtime

                if icloud_file_time > backup_file_time:
                    shutil.copy2(icloud_document, destination_file)
                    updated_files += 1

                else:
                    skipped_files += 1

            else:
                shutil.copy2(icloud_document, destination_file)
                copied_files += 1  

    print(f"Backup finished. Copied files: {copied_files}. Updated files: {updated_files}. Skipped files: {skipped_files}.")
    
else:
    print("Source not found")