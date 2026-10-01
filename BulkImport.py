import os
from dotenv import load_dotenv

load_dotenv()

MEALIE_URL = os.getenv("MEALIE_URL")
MEALIE_TOKEN = os.getenv("MEALIE_TOKEN")


def main():
    print("Starting Mealie importer...")
    print(MEALIE_URL)


if __name__ == "__main__":
    main()