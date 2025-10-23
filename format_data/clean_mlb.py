import json
import sys
import os

# Add the 'utils' directory to the path for logger import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))
from logger import get_logger

logger = get_logger("clean_mlb")

def load_raw_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            logger.info(f"Loaded raw data from {filepath}")
            return data
    except Exception as e:
        logger.error(f"Failed to load raw data from {filepath}: {e}")
        return {}

def clean_mlb_data(raw_data):
    if not raw_data or "games" not in raw_data:
        logger.warning("Missing 'games' key in raw data.")
        return "⚾ MLB Scores:\n No games available."

    lines = []

    for game in raw_data["games"]:
        try:
            teams = game["teams"]
            home = teams["home"]["team"]["name"]
            away = teams["away"]["team"]["name"]

            home_score = teams["home"].get("score", "N/A")
            away_score = teams["away"].get("score", "N/A")

            status = game["status"]["detailedState"]

            summary = f"{away} {away_score}, {home} {home_score} ({status})"
            lines.append(summary)
        except KeyError as e:
            logger.warning(f"Incomplete data in one game: {e}")
            continue

    if not lines:
        return "MLB Scores:\n No results available."

    return "MLB Scores:\n" + "\n".join(lines)

if __name__ == "__main__":
    raw_file = "raw_data/raw_mlb.json"
    raw_data = load_raw_data(raw_file)
    summary = clean_mlb_data(raw_data)
    print(summary)
