from fastapi import FastAPI
from api.endpoints import router
from services.simulation import simulate_transaction
from storage.memory import add_transaction, get_transactions
import asyncio
import requests
from api.endpoints import convert_to_unlabeled
import json
from typing import List

app = FastAPI(title="Bank Transaction Simulation API")
app.include_router(router)


async def generate_transactions_periodically(anomaly_rate: float = 0.5):
    while True:
        i=0
        while i<2:
            txn = simulate_transaction(anomaly_rate)
            add_transaction(txn)
            i+=1
        unlabeled_transaction = [convert_to_unlabeled(txn) for txn in get_transactions()]
        transactions_dict = [txn.dict() for txn in unlabeled_transaction]
        transactions_json = json.dumps(transactions_dict, ensure_ascii=False, indent=4)
        # Forward to AWS API Gateway
        try:
            aws_api_url = "https://ilc8vdurx7.execute-api.ap-southeast-2.amazonaws.com/prod/transaction-simulation"
            # if isinstance(payload["timestamp"], datetime):
            #     payload["timestamp"] = payload["timestamp"].isoformat()

            req = requests.post(
                aws_api_url,
                json=transactions_dict,
                headers={"Content-Type": "application/json"}
            )
            req.raise_for_status()
            if req.status_code == 200:
                print(f"Transaction {transactions_dict} forwarded to AWS successfully.")
        except Exception as e:
            print(f"Failed to forward to AWS: {e}")
            print(transactions_json)
        break
        await asyncio.sleep(10)

@app.on_event("startup")
async def start_background_generation():
    asyncio.create_task(generate_transactions_periodically())
