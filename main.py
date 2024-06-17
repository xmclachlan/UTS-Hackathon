import pandas as pd
import pdfplumber
import re

def extract_subsystem_data_from_excel(excel_path):
    df = pd.read_excel(excel_path)
    return df['SUBSYSTEM'].tolist()

def read_pdf_text(pdf_path):
    full_text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + '\n'
    return full_text

def find_matches_in_text(pattern, text):
    compiled_pattern = re.compile(re.escape(pattern), re.IGNORECASE)
    matches = compiled_pattern.findall(text)
    return matches

def main():
    excel_file_path = "ALARMS.xlsx"
    manual_pdf_path = 'MAN_32-40_IMO_TierIII–Marine_.pdf'
    troubleshoot_pdf_path = 'MAN_32-40_Troubleshooting_Guide.pdf'

    # Extract subsystem data from Excel
    subsystems = extract_subsystem_data_from_excel(excel_file_path)
    
    if not subsystems:
        print("No subsystems found in the Excel file.")
        return

    print(f"Subsystems to search: {subsystems}")

    # Read the PDF files and extract text
    manual_text = read_pdf_text(manual_pdf_path)
    troubleshoot_text = read_pdf_text(troubleshoot_pdf_path)

    for subsystem in subsystems:
        print(f"\nSearching for '{subsystem}' in the manual PDF...")
        manual_matches = find_matches_in_text(subsystem, manual_text)
        if manual_matches:
            print(f"Found {len(manual_matches)} matches for '{subsystem}' in the manual PDF.")
        else:
            print(f"No matches found for '{subsystem}' in the manual PDF.")
        
        print(f"\nSearching for '{subsystem}' in the troubleshooting PDF...")
        troubleshoot_matches = find_matches_in_text(subsystem, troubleshoot_text)
        if troubleshoot_matches:
            print(f"Found {len(troubleshoot_matches)} matches for '{subsystem}' in the troubleshooting PDF.")
        else:
            print(f"No matches found for '{subsystem}' in the troubleshooting PDF.")

if __name__ == "__main__":
    main()
