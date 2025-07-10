import os
import sys
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))
from logger import get_logger

load_dotenv()
logger = get_logger("fetch_nba")

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def fetch_nba_scores(date=None):
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    url = f"https://api-nba-v1.p.rapidapi.com/games"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
    }
    params = {"date": date}

    logger.info(f"Fetching NBA scores for {date} from RapidAPI")

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logger.error(f"Error fetching NBA scores: {e}")
        return None

def save_games(data):
    try:
        games = data.get("response", [])
        with open("raw_data/raw_nba.json", "w") as f:
            json.dump({"games": games}, f, indent=2)
        logger.info("Saved cleaned NBA data to raw_data/raw_nba.json")
    except Exception as e:
        logger.error(f"Failed to save NBA data: {e}")

if __name__ == "__main__":
    data = fetch_nba_scores()
    if data:
        save_games(data)
