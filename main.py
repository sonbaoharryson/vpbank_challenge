from fastapi import FastAPI
from api.endpoints import router
from services.simulation import simulate_transaction
from storage.memory import add_transaction
import asyncio

app = FastAPI(title="Bank Transaction Simulation API")
app.include_router(router)

async def generate_transactions_periodically(anomaly_rate: float = 0.1):
    while True:
        txn = simulate_transaction(anomaly_rate)
        add_transaction(txn)
        await asyncio.sleep(5)

@app.on_event("startup")
async def start_background_generation():
    asyncio.create_task(generate_transactions_periodically())