import pandas as pd
import pdfplumber
import re

# Read in the Documents

manual = 'MAN_32-40_IMO_TierIII–Marine_.pdf'
troubleshoot = 'MAN_32-40_Troubleshooting_Guide.pdf'
df = pd.read_excel("ALARMS.xlsx")

# Select the Alarm Subsystem

subsystem = df['SUBSYSTEM'].iloc[0]
print(f"First SUBSYSTEM value: {subsystem}")

# Read the PDF file and extract text
with pdfplumber.open(manual) as pdf:
    full_text = ''
    for page in pdf.pages:
        full_text += page.extract_text() + '\n'

# Perform regex search for the first subsystem in the Manual

    pattern = re.compile(re.escape(subsystem), re.IGNORECASE)
    matches = pattern.findall(full_text)
    if matches:
        print(f"Found {len(matches)} matches for '{subsystem}': {matches}")
    else:
        print(f"No matches found for '{subsystem}'")
