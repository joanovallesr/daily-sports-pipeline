import sys
import os
from datetime import datetime

from requests import get

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "utils")))

from logger import get_logger

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "fetch_data")))

from fetch_mlb import fetch_mlb_scores, display_mlb_scores
from fetch_nba import fetch_nba_scores, display_nba_scores

logger = get_logger("fetch_daily_scores")

def main():
    today = datetime.today()
    month = today.month

    logger.info("Starting daily sports data fetch...")

    if 3 <= month <= 11:
        logger.info("MlB season detected - fetching baseball scores...")

        mlb_data = fetch_mlb_scores()
        display_mlb_scores(mlb_data)
    else:
        logger.info("MLB is out of season.")

    if month <= 6 or month >= 10:
        logger.info("NBA season detected - fetching basketball scores...")

        nba_data = fetch_nba_scores()
        display_nba_scores(nba_data)
    else:
        logger.info("NBA is out of season.")

    logger.info("Daily fetch completed.")


if __name__ == "__main__":
    main()