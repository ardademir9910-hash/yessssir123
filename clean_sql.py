import re
import os
import zipfile

input_file = 'workdir/sxware.sql'
output_file = 'workdir/sxware_clean.sql'

if not os.path.exists('workdir'):
    os.makedirs('workdir')

if not os.path.exists(input_file):
    # If not extracted yet, extract it
    print("Extracting sxware.sql...")
    with zipfile.ZipFile('Desktop.zip', 'r') as z:
        z.extract('sxware.sql', 'workdir')

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.readlines()

clean_content = []
for line in content:
    if line.strip().startswith('INSERT INTO'):
        continue
    clean_content.append(line)

with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines(clean_content)

print(f"Created {output_file}")
