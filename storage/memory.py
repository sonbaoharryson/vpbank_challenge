from typing import List
from models.transaction import Transaction

MAX_GENERATED = 100
GENERATED_TRANSACTIONS: List[Transaction] = []

def add_transaction(txn: Transaction):
    if len(GENERATED_TRANSACTIONS) >= MAX_GENERATED:
        GENERATED_TRANSACTIONS = []
    GENERATED_TRANSACTIONS.append(txn)

def get_transactions() -> List[Transaction]:
    return GENERATED_TRANSACTIONS
