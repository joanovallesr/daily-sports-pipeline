import sys
import os
import json

# Add the 'utils' directory to the import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))
from logger import get_logger

import requests
from datetime import datetime

logger = get_logger("fetch_mlb")

def fetch_mlb_scores(date=None):
    # If no date is provided, use today's date in YYYY-MM-DD format
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={date}"

    logger.info(f"Fetching MLB scores for {date} from {url}")

    try:
        response = requests.get(url)

        if response.status_code == 404:
            logger.warning(f"No MLB data found for {date} (404 Not Found).")
            
        # Raise an error if the response isn't 200 OK
        response.raise_for_status()
        logger.info("MLB data fetch successfull")
        return response.json()
    except requests.exceptions.RequestException as e:
         # If there's any network or API error, log it
        logger.error(f"Error fetching MLB scores: {e}")
        return None
    

def display_mlb_scores(data):
    if not data:
        logger.warning("No MLB data to display.")
        print("No MLB data to display.")
        return
    # Get the list of games from the JSON data
    games = data.get("dates", [])
    if not games:
        logger.info("No MLB games scheduled for today.")
        print("No MLB games scheduled for today.")
        return
    
    # Loop through all the games
    for game in games[0].get("games", []):
        teams = game["teams"]
        home_team = teams["home"]["team"]["name"]
        away_team = teams["away"]["team"]["name"]

        status = game["status"]["detailedState"]
        
        if status in ["Final", "In progress", "Game over"]:
            home_score = teams["home"].get("score", "N/A")
            away_score = teams["away"].get("score", "N/A")
            score_display = f"{away_score}-{home_score}"
        else:
            score_display = "Scheduled"

        logger.info(f"Game: {away_team} @ {home_team} - {score_display} ({status})")
        print(f"{away_team} @ {home_team} - {score_display} ({status})")
    

if __name__ == "__main__":
    data = fetch_mlb_scores()

    if data:
        # ✅ Extract just the "games" list from the nested "dates"
        games = data.get("dates", [{}])[0].get("games", [])

        # ✅ Save only {"games": [...]}
        try:
            with open("raw_data/raw_mlb.json", "w") as f:
                json.dump({"games": games}, f, indent=2)
            logger.info("Saved cleaned MLB data to raw_data/raw_mlb.json")
        except Exception as e:
            logger.error(f"Failed to save MLB data: {e}")
    else:
        logger.warning("No data returned from fetch_mlb_scores()")

