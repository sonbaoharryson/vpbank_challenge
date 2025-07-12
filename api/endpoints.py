from fastapi import APIRouter
from typing import List
from models.transaction import Transaction, TransactionUnlabeled
from storage.memory import get_transactions

router = APIRouter()

def convert_to_unlabeled(transaction: Transaction) -> TransactionUnlabeled:
    """Convert a labeled transaction to unlabeled by removing label fields."""
    return TransactionUnlabeled(
        transaction_id=transaction.transaction_id,
        transaction_date=transaction.transaction_date,
        transaction_type=transaction.transaction_type,
        amount=transaction.amount,
        currency=transaction.currency,
        sender_account=transaction.sender_account,
        receiver_account=transaction.receiver_account,
        sender_bank=transaction.sender_bank,
        receiver_bank=transaction.receiver_bank,
        channel=transaction.channel,
        location=transaction.location,
        device_id=transaction.device_id,
        user_id=transaction.user_id,
        transaction_status=transaction.transaction_status,
        latency_ms=transaction.latency_ms,
        retry_count=transaction.retry_count,
        ip_address=transaction.ip_address,
        user_agent=transaction.user_agent,
        is_new_device=transaction.is_new_device
    )

@router.get("/generated_transactions/labeled", response_model=List[Transaction])
def get_generated_transactions_labeled():
    return get_transactions()

@router.get("/generated_transactions/unlabeled", response_model=List[TransactionUnlabeled])
def get_generated_transactions_unlabeled():
    return [convert_to_unlabeled(txn) for txn in get_transactions()]