from faker import Faker
import random
from models.transaction import Transaction

fake = Faker()

ANOMALY_TYPES = [
    "high_amount", "rare_location", "device_user_mismatch", "frequent_retries"
]

BANKS = ["ACB", "BIDV", "VCB", "MB", "TCB", "VPB"]
CHANNELS = ["API", "ATM", "POS", "INTERNET", "MOBILE_APP"]
CURRENCIES = ["VND", "USD"]
TRANSACTION_TYPES = ["IBFT", "QR_PAYMENT", "BILL_PAYMENT", "WALLET_TRANSFER"]
STATUS = ["SUCCESS", "FAILED", "PENDING"]
USER_AGENTS = [
    "Windows 10", "MacOS Big Sur", "Ubuntu", "Android 12", "iOS 17"
]

def simulate_transaction(anomaly_rate: float = 0.1) -> Transaction:
    anomaly = None
    is_fraud = 0
    if random.random() < anomaly_rate:
        anomaly = random.choice(ANOMALY_TYPES)
        is_fraud = 1
    amount = round(random.uniform(10000, 5_000_000), 2)
    location = fake.city()
    device_id = f"DEVICE_{random.randint(1, 20)}"
    user_id = f"USER_{random.randint(100, 999)}"
    retry_count = random.randint(0, 2)
    latency_ms = random.randint(100, 5000)
    if anomaly == "high_amount":
        amount = round(random.uniform(100_000_000, 1_000_000_000), 2)
    if anomaly == "rare_location":
        location = fake.country()
    if anomaly == "device_user_mismatch":
        device_id = f"DEVICE_{random.randint(21, 40)}"
        user_id = f"USER_{random.randint(1000, 2000)}"
    if anomaly == "frequent_retries":
        retry_count = random.randint(5, 10)
        latency_ms = random.randint(5000, 20000)
    return Transaction(
        transaction_id=fake.unique.bothify(text='TXN#####'),
        transaction_date=fake.date_time_this_year().strftime('%Y-%m-%d %H:%M:%S'),
        transaction_type=random.choice(TRANSACTION_TYPES),
        amount=amount,
        currency=random.choice(CURRENCIES),
        sender_account=fake.bothify(text='????####'),
        receiver_account=fake.bothify(text='????####'),
        sender_bank=random.choice(BANKS),
        receiver_bank=random.choice(BANKS),
        channel=random.choice(CHANNELS),
        location=location,
        device_id=device_id,
        user_id=user_id,
        is_fraud=is_fraud,
        transaction_status=random.choice(STATUS),
        latency_ms=latency_ms,
        retry_count=retry_count,
        ip_address=fake.ipv4_public(),
        user_agent=random.choice(USER_AGENTS),
        is_new_device=random.choice([True, False]),
        anomaly_type=anomaly
    ) 