import pandas as pd
import pdfplumber
import re

pdf_path = 'MAN_32-40_IMO_TierIII–Marine_.pdf'

df = pd.read_excel("ALARMS.xlsx")

first_subsystem = df['SUBSYSTEM'].iloc[0]
print(f"First SUBSYSTEM value: {first_subsystem}")
