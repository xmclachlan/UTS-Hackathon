import pandas as pd
import fitz  # PyMuPDF
import re

# Read the Excel file
alarms_df = pd.read_excel('ALARMS.xlsx')

# Display the first few rows and the column names of the DataFrame
print(alarms_df.head())
print(alarms_df.columns)

# Function to extract text from a PDF


def extract_text_from_pdf(pdf_path):
    text = ""
    pdf = fitz.open(pdf_path)
    for page_num in range(len(pdf)):
        page = pdf[page_num]
        text += page.get_text()
    return text


# Extract text from the technical manual and troubleshooting guide
tech_manual_text = extract_text_from_pdf('MAN_32-40_IMO_TierIII–Marine_.pdf')
troubleshooting_guide_text = extract_text_from_pdf(
    'MAN_32-40_Troubleshooting_Guide.pdf')

# Function to search for alarm information in the extracted text


def find_alarm_info(alarm_desc, manual_text, troubleshooting_text):
    # Regular expression to find the alarm information
    pattern = re.compile(rf"{re.escape(alarm_desc)}.*", re.IGNORECASE)

    # Search in both documents
    tech_matches = pattern.findall(manual_text)
    troubleshoot_matches = pattern.findall(troubleshooting_text)

    return tech_matches, troubleshoot_matches

# Function to extract relevant information from matches


def extract_relevant_info(matches):
    info = {
        "sensors": [],
        "measuring_points": [],
        "description": [],
        "measuring_range": [],
        "related_system": [],
        "dependent_system": [],
        "related_sensors": [],
        "triggers": [],
        "actions": [],
        "technical_knowledge": [],
        "required_parts": [],
        "drawings_diagrams": []
    }

    # Sample logic to extract the relevant information from the matches
    for match in matches:
        if "sensor" in match.lower():
            info["sensors"].append(match)
        if "measuring point" in match.lower():
            info["measuring_points"].append(match)
        if "description" in match.lower():
            info["description"].append(match)
        if "measuring range" in match.lower():
            info["measuring_range"].append(match)
        if "related system" in match.lower():
            info["related_system"].append(match)
        if "dependent system" in match.lower():
            info["dependent_system"].append(match)
        if "related sensor" in match.lower():
            info["related_sensors"].append(match)
        if "trigger" in match.lower():
            info["triggers"].append(match)
        if "action" in match.lower():
            info["actions"].append(match)
        if "technical knowledge" in match.lower():
            info["technical_knowledge"].append(match)
        if "required part" in match.lower():
            info["required_parts"].append(match)
        if "drawing" in match.lower() or "diagram" in match.lower():
            info["drawings_diagrams"].append(match)

    return info

# Main function to diagnose alarms


def diagnose_alarms(alarms_df, tech_manual_text, troubleshooting_guide_text):
    diagnosis = {}

    for index, alarm in alarms_df.iterrows():
        alarm_id = alarm['ALARM_ID']
        alarm_desc = alarm['DESCRIPTION']  # Adjusted column name

        tech_matches, troubleshoot_matches = find_alarm_info(
            alarm_desc, tech_manual_text, troubleshooting_guide_text)
        tech_info = extract_relevant_info(tech_matches)
        troubleshoot_info = extract_relevant_info(troubleshoot_matches)

        diagnosis[alarm_id] = {
            "description": alarm_desc,
            "technical_info": tech_info,
            "troubleshoot_info": troubleshoot_info
        }

    return diagnosis


# Get the diagnosis for all alarms
all_diagnosis = diagnose_alarms(
    alarms_df, tech_manual_text, troubleshooting_guide_text)

# Output the results for the crew members
for alarm_id, info in all_diagnosis.items():
    print(f"Alarm ID: {alarm_id}")
    print(f"Description: {info['description']}")
    print(f"Technical Info: {info['technical_info']}")
    print(f"Troubleshoot Info: {info['troubleshoot_info']}")
    print("\n")
