echo "Starting daily pipeline..."

source venv/bin/activate

python3 fetch_data/fetch_mlb.py
python3 fetch_data/fetch_nba.py

python3 output/daily_summary.py

echo "Pipeline completed successfully."


