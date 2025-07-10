import json
import sys
import os

# Add utils to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))
from logger import get_logger

logger = get_logger("clean_nba")

def load_raw_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            logger.info(f"Loaded raw data from {filepath}")
            return data
    except Exception as e:
        logger.error(f"Failed to load raw data from {filepath}: {e}")
        return {}

def clean_nba_data(raw_data):
    if not raw_data or "games" not in raw_data:
        logger.warning("Missing 'games' key in raw data.")
        return "🏀 NBA Scores:\n No games available."

    lines = []

    for game in raw_data["games"]:
        try:
            # Safeguard against missing fields
            if "teams" not in game or "scores" not in game or "status" not in game:
                logger.warning("Skipping incomplete NBA game entry.")
                continue

            home = game["teams"]["home"].get("name", "Home")
            away = game["teams"]["visitors"].get("name", "Away")

            home_score = game["scores"]["home"].get("points", "N/A")
            away_score = game["scores"]["visitors"].get("points", "N/A")

            status = game["status"].get("long", "Unknown")

            summary = f"{away} {away_score}, {home} {home_score} ({status})"
            lines.append(summary)

        except Exception as e:
            logger.warning(f"Incomplete data in one game: {e}")
            continue

    if not lines:
        return "🏀 NBA Scores:\n No results available."

    return "🏀 NBA Scores:\n" + "\n".join(lines)

if __name__ == "__main__":
    raw_file = "raw_data/raw_nba.json"

    raw_data = load_raw_data(raw_file)
    summary = clean_nba_data(raw_data)
    print(summary)