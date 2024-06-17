import tabula
import pandas as pd

# Read PDF into list of DataFrame
dataframe = tabula.read_pdf(
    "MAN_32-40_IMO_TierIII–Marine_.pdf", pages='216')

print(dataframe)
