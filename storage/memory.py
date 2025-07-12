from typing import List
from models.transaction import Transaction

MAX_GENERATED = 100
GENERATED_TRANSACTIONS: List[Transaction] = []

def add_transaction(txn: Transaction):
    GENERATED_TRANSACTIONS.append(txn)
    if len(GENERATED_TRANSACTIONS) > MAX_GENERATED:
        GENERATED_TRANSACTIONS.pop(0)

def get_transactions() -> List[Transaction]:
    return GENERATED_TRANSACTIONS