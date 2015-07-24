@echo off

title "%~0"

set python=C:\Python27\python.exe
if NOT exist %python% (
    echo ERROR: '%python%' doesn't exists?!?
    pause
    exit 1
)

set boot_script=boot_drqueue_env.py
if NOT exist %boot_script% (
    echo ERROR: '%boot_script%' doesn't exists?!?
    pause
    exit 1
)

set destination=%APPDATA%\DrQueueIPython
mkdir %destination%
if NOT exist %destination% (
    echo ERROR: '%destination%' doesn't exists?!?
    pause
    exit 1
)

echo on
%python% %boot_script% %destination%
explorer.exe %destination%
@pause