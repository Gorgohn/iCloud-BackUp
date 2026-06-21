import datetime 

source_icloud = "C:\Users\amd\iCloudDrive"

backup_root = "E:\ "

year = datetime.date.today().year
month = datetime.date.today().month

target = backup_root / year / month

