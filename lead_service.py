from pathlib import Path
import pandas as pd

# Location of your existing lead CSV file
LEADS_FILE = Path(
    r"C:\Users\Admin\Auto_Mail_System\data\raw\sample_leads.csv"
)


def load_leads():
    # Check whether the file exists
    if not LEADS_FILE.is_file():
        raise FileNotFoundError(
            f"Lead file not found: {LEADS_FILE}"
        )

    # Read CSV data into a DataFrame
    df = pd.read_csv(LEADS_FILE)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    return df