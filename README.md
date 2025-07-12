# Bank Transaction Simulation API

This project simulates bank transactions (including anomalies) for an anomaly detection challenge using FastAPI.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```

## Endpoints

- `/transaction` : Get a single simulated transaction (may include anomalies).
- `/transactions?count=N` : Get a list of N simulated transactions.

## Customization
- You can adjust the anomaly rate and simulation logic in `main.py`. 