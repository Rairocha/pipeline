import pandas as pd

def read_from_gsheets(spreadsheet_link):
    """
    Transform Google Sheets URL into a CSV file
    """
    working_spreadsheet = spreadsheet_link.replace(
        "/edit?usp=sharing", "/export?format=csv"
    )

    return pd.read_csv(working_spreadsheet)