# Daily Sports Scores Pipeline

A **fully automated data pipeline** fetching, cleaning, and summarizing live MLB and NBA scores daily — built with Python, CLI tools, and structured logging.

---

## Project Overview

This project demonstrates a real-world Data Engineering pipeline from end-to-end:

- Fetches live MLB data from [MLB Stats API](https://statsapi.mlb.com/)
- Fetches live NBA data from [API-NBA via RapidAPI](https://rapidapi.com/api-sports/api/api-nba)
- Cleans and normalizes raw JSON data for easy consumption
- Generates daily summaries with real-time scores and game statuses
- Logs all steps for monitoring and debugging
- Can be scheduled via cron for daily automation
- Includes a Streamlit app (optional) to visualize daily sports summaries interactively

---

## Tech Stack & Tools

- Python 3.13+
- `requests` for API calls
- `logging` for structured logs
- `python-dotenv` for environment variable management
- Bash shell scripting (`run_pipeline.sh`)
- Cron job automation for scheduling
- Streamlit (optional) for UI visualization

---

## Project Structure

```

daily-pipeline/
├── app.py                    # Streamlit app for summary visualization
├── fetch\_data/
│   ├── fetch\_mlb.py          # Fetch MLB scores script
│   └── fetch\_nba.py          # Fetch NBA scores script
├── format\_data/
│   ├── clean\_mlb.py          # Clean MLB raw data script
│   └── clean\_nba.py          # Clean NBA raw data script
├── logs/                     # Log files generated during runs
├── raw\_data/
│   ├── raw\_mlb.json          # Raw MLB JSON data
│   └── raw\_nba.json          # Raw NBA JSON data
├── run\_pipeline.sh           # Bash script to run the whole pipeline
├── utils/
│   └── logger.py             # Centralized logging setup
├── venv/                     # Python virtual environment
├── requirements.txt          # Project dependencies
├── README.md                 # This file
└── load\_env.py               # Loads environment variables

````

---

## Setup & Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/joanovallesr/daily-pipeline.git
   cd daily-pipeline
````

2. Create and activate virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your RapidAPI key:

   ```
   RAPIDAPI_KEY=your_rapidapi_key_here
   ```

---

## Running the Pipeline

* Run manually:

  ```bash
  ./run_pipeline.sh
  ```

* Run individual scripts:

  ```bash
  python3 fetch_data/fetch_mlb.py
  python3 format_data/clean_mlb.py
  python3 fetch_data/fetch_nba.py
  python3 format_data/clean_nba.py
  python3 output/daily_summary.py
  ```

* Run Streamlit app:

  ```bash
  streamlit run app.py
  ```

---

## Scheduling with Cron

Set up a cron job to run the pipeline daily at 8 AM:

```bash
crontab -e
```

Add the line:

```
0 8 * * * cd /path/to/daily-pipeline && ./run_pipeline.sh >> logs/cron.log 2>&1
```

---

## How It Works

1. **Fetching:** Scripts call external APIs to retrieve raw JSON game data.
2. **Cleaning:** Clean scripts parse and extract relevant data, saving clean JSON.
3. **Summary:** Summary script reads clean data and formats a human-readable daily sports report.
4. **Logging:** All steps logged to console and rotating log files for traceability.
5. **Visualization:** Streamlit app displays the latest daily summary interactively.

---

## Contributing

Contributions welcome! Feel free to open issues or pull requests.

---

## License

MIT License © 2025 Joan Ovalles

---

## Author

Joan Ovalles | [GitHub](https://github.com/joanovallesr) | [LinkedIn](https://linkedin.com/in/joanovallesr)
