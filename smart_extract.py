import zipfile
import os

zip_path = 'Desktop.zip'
extract_path = 'workdir'

if not os.path.exists(extract_path):
    os.makedirs(extract_path)

# Whitelist of paths to extract
whitelist_prefixes = [
    'htdocs/inc/_global/',
    'htdocs/inc/backend/',
    'htdocs/apiservices/',
    'htdocs/apisystem/',
]

# Extract root files specifically
whitelist_root_files = True

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for member in zip_ref.infolist():
        filename = member.filename

        if not filename.endswith('.php') and not filename.endswith('.sql'):
            continue

        should_extract = False

        # Check prefixes
        if any(filename.startswith(p) for p in whitelist_prefixes):
            should_extract = True

        # Check if it is a root php file in htdocs
        if filename.startswith('htdocs/') and filename.count('/') == 1:
            should_extract = True

        if filename == 'sxware.sql':
            should_extract = True

        if should_extract:
             # Extract
            zip_ref.extract(member, extract_path)
