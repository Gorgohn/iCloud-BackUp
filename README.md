# iCloud Backup Automation

This project backs up files from an iCloud folder to an external storage device, such as a hard drive connected to a router.

The script creates backup folders, keeps the original folder structure, copies new files, updates changed files, and skips files that are already up to date.

## Why I Built This

I built this project to spend less time sorting and copying files manually. I have many files in iCloud, and checking everything by hand is time-consuming.

This project helps me automate the backup process and gives me a practical way to improve my Python skills with a real-world use case.

## Features

- Preserves the original folder structure
- Copies new files
- Updates changed files based on modification time
- Skips unchanged files
- Shows a summary after the backup is finished
- Checks if the source and backup folders are available before starting

## Example Backup Structure

```text
backup/
  2026/
    6/
    7/
```

Example with files:

```text
backup/
  2026/
    6/
      Documents/
        invoice.pdf
      School/
        worksheet.pdf
```

## How It Works

The script first checks if the source folder exists. It also checks if the backup destination is available.

After that, it creates a monthly backup folder based on the current year and month.

Then it searches through all files in the source folder, including files inside subfolders. For each file, it keeps the relative folder structure and creates the same structure in the backup location.

If a file does not exist in the backup folder yet, it is copied. If the file already exists, the script compares the modification time. When the source file is newer, the backup file is updated. If the backup file is already up to date, the file is skipped.

At the end, the script prints a summary showing how many files were copied, updated, and skipped.

## Current Status

The project is currently tested with a local test folder.

The source and backup paths are currently set directly inside `backup.py`.

## Requirements

- Python 3
- Access to the source folder
- Access to the backup destination

## Usage

Run the script with:

```bash
python backup.py
```

Before running the script, update the source and backup paths in `backup.py`.

## Technologies Used

- Python
- pathlib
- shutil
- datetime
- sys

## Next Improvements

- Move paths into a configuration file
- Add logging
- Add automated scheduling
- Improve error handling
- Add a dry-run mode
- Add tests