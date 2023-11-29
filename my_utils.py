import os
from dotenv import load_dotenv
from pathlib import Path


def load_kaggle_cred():
    # Load the .env file
    load_dotenv()
    # add api key to kaggle
    creds = f'{{"username":"{os.getenv("username")}","key":"{os.getenv("key")}"}}'

    # add api key
    cred_path = Path("~/.kaggle/kaggle.json").expanduser()
    if not cred_path.exists():
        cred_path.parent.mkdir(exist_ok=True)
        cred_path.write_text(creds)
        cred_path.chmod(0o600)
