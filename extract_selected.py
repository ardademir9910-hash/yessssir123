import zipfile
import os

zip_path = 'Desktop.zip'
extract_path = 'workdir'

if not os.path.exists(extract_path):
    os.makedirs(extract_path)

files_to_extract = [
    'htdocs/inc/_global/config.php',
    'htdocs/giris.php',
    'htdocs/login.php',
    'htdocs/dashboard.php',
    'htdocs/kayit.php',
    'htdocs/register.php',
    'htdocs/tcsorgu.php',
    'htdocs/mernis-sorgu.php',
    'htdocs/inc/_global/user.php',
    'htdocs/inc/backend/user.php',
    'htdocs/index.php',
]

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for file in files_to_extract:
        try:
            zip_ref.extract(file, extract_path)
            print(f"Extracted: {file}")
        except KeyError:
            print(f"File not found in zip: {file}")
