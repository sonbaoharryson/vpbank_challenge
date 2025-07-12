from fastapi import APIRouter, Query
from typing import List
from models.transaction import Transaction
from services.simulation import simulate_transaction
from storage.memory import add_transaction, get_transactions
import asyncio

router = APIRouter()

@router.get("/transaction", response_model=Transaction)
def get_transaction(anomaly_rate: float = Query(0.1, ge=0, le=1)):
    return simulate_transaction(anomaly_rate)

@router.get("/transactions", response_model=List[Transaction])
def get_transactions_endpoint(count: int = Query(10, ge=1, le=100), anomaly_rate: float = Query(0.1, ge=0, le=1)):
    return [simulate_transaction(anomaly_rate) for _ in range(count)]

@router.get("/generated_transactions", response_model=List[Transaction])
def get_generated_transactions():
    return get_transactions() 