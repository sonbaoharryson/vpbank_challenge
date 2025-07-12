from faker import Faker
import random
from models.transaction import Transaction

fake = Faker()

ANOMALY_TYPES = [
    "high_amount", "rare_location", "device_user_mismatch", "frequent_retries"
]

BANKS = ["ACB", "BIDV", "VCB", "MB", "TCB", "VPB", "SCB"]
CHANNELS = ["API", "ATM", "POS", "INTERNET", "MOBILE_APP"]
CURRENCIES = ["VND", "USD"]
TRANSACTION_TYPES = ["IBFT", "QR_PAYMENT", "BILL_PAYMENT", "WALLET_TRANSFER"]
STATUS = ["SUCCESS", "FAILED", "PENDING"]
USER_AGENTS = [
    "Windows 10", "MacOS Big Sur", "Ubuntu", "Android 12", "iOS 17", "Chrome 120", "Firefox 120", "Safari 17", "Edge 120",
    "Android 13", "iOS 18", "Chrome 121", "Firefox 121", "Safari 18", "Edge 121", "Android 14", "iOS 19", "Chrome 122",
    "Firefox 122", "Safari 19", "Edge 122", "Android 15", "iOS 20", "Chrome 123", "Firefox 123", "Safari 20", "Edge 123",
    "Android 16", "iOS 21", "Chrome 124", "Firefox 124", "Safari 21", "Edge 124", "Android 17", "iOS 22", "Chrome 125",
    "Firefox 125", "Safari 22", "Edge 125", "Android 18", "iOS 23", "Chrome 126", "Firefox 126", "Safari 23", "Edge 126",
    "Android 19", "iOS 24", "Chrome 127", "Firefox 127", "Safari 24", "Edge 127", "Android 20", "iOS 25", "Chrome 128",
    "Firefox 128", "Safari 25", "Edge 128", "Android 21", "iOS 26", "Chrome 129", "Firefox 129", "Safari 26", "Edge 129",
    "Android 22", "iOS 27", "Chrome 130", "Firefox 130", "Safari 27", "Edge 130", "Android 23", "iOS 28", "Chrome 131"
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