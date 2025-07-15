from fastapi import APIRouter, HTTPException
from typing import List
from models.transaction import Transaction, TransactionUnlabeled
from storage.memory import get_transactions, add_transaction
import requests

router = APIRouter()

def convert_to_unlabeled(transaction: Transaction) -> TransactionUnlabeled:
    """Convert a labeled transaction to unlabeled by removing label fields."""
    return TransactionUnlabeled(
        transaction_id=transaction.transaction_id,
        timestamp=transaction.timestamp,
        transaction_type=transaction.transaction_type,
        amount=transaction.amount,
        currency=transaction.currency,
        sender_account=transaction.sender_account,
        receiver_account=transaction.receiver_account,
        sender_bank=transaction.sender_bank,
        receiver_bank=transaction.receiver_bank,
        channel=transaction.channel,
        province=transaction.province,
        city=transaction.city,
        device_id=transaction.device_id,
        is_new_device=transaction.is_new_device,
        user_id=transaction.user_id,
        cif=transaction.cif,
        merchant_id=transaction.merchant_id,
        merchant_location=transaction.merchant_location,
        pos_id=transaction.pos_id,
        qr_type=transaction.qr_type,
        transaction_status=transaction.transaction_status,
        latency_ms=transaction.latency_ms,
        retry_count=transaction.retry_count,
        ip_address=transaction.ip_address,
        user_agent=transaction.user_agent
    )

@router.get("/generated_transactions/labeled", response_model=List[Transaction])
def get_generated_transactions_labeled():
    return get_transactions()

@router.get("/generated_transactions/unlabeled", response_model=List[TransactionUnlabeled])
def get_generated_transactions_unlabeled():
    return [convert_to_unlabeled(txn) for txn in get_transactions()]

@router.post("/generated_transactions/labeled", response_model=Transaction)
def post_generated_transaction_labeled(txn: Transaction):
    add_transaction(txn)
    # Forward to AWS API Gateway
    aws_api_url = "https://i6zvrxpu46.execute-api.ap-southeast-2.amazonaws.com/Prod/transcation_simulation"  # TODO: Replace with your actual URL
    try:
        response = requests.post(aws_api_url, json=txn.dict())
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to forward to AWS: {e}")
    return txn