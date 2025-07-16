from fastapi import FastAPI
from api.endpoints import router
from services.simulation import simulate_transaction
from storage.memory import add_transaction
import asyncio
import requests
from api.endpoints import convert_to_unlabeled
from datetime import datetime
import json

app = FastAPI(title="Bank Transaction Simulation API")
app.include_router(router)


async def generate_transactions_periodically(anomaly_rate: float = 0.5):
    while True:
        i=0
        while i<100:
            txn = simulate_transaction(anomaly_rate)
            add_transaction(txn)
            i+=1
        unlabeled_transaction = [convert_to_unlabeled(txn) for txn in get_transactions()]

        # Forward to AWS API Gateway
        try:
            aws_api_url = "https://i6zvrxpu46.execute-api.ap-southeast-2.amazonaws.com/Prod/transcation_simulation" # Corrected resource name
            payload = unlabeled_transaction.model_dump_json()
            # if isinstance(payload["timestamp"], datetime):
            #     payload["timestamp"] = payload["timestamp"].isoformat()

            req = requests.post(
                aws_api_url,
                json=unlabeled_transaction,  # This is the correct way!
                headers={"Content-Type": "application/json"}
            )
            req.raise_for_status()
            if req.status_code == 200:
                print(f"Transaction {unlabeled_transaction} forwarded to AWS successfully.")
        except Exception as e:
            print(f"Failed to forward to AWS: {e}")
            print(unlabeled_transaction)
        await asyncio.sleep(5)

@app.on_event("startup")
async def start_background_generation():
    asyncio.create_task(generate_transactions_periodically())
