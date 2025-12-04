import zipfile
import os

zip_path = 'Desktop.zip'
extract_path = 'workdir'

if not os.path.exists(extract_path):
    os.makedirs(extract_path)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for member in zip_ref.infolist():
        filename = member.filename
        # Filter files
        if filename.startswith('htdocs/') and filename.endswith('.php'):
            # Exclude assets and vendor
            if 'htdocs/assets/' in filename:
                continue
            if 'vendor/' in filename:
                continue

            # Extract
            zip_ref.extract(member, extract_path)
            print(f"Extracted: {filename}")
        elif filename == 'sxware.sql':
             zip_ref.extract(member, extract_path)
             print(f"Extracted: {filename}")
