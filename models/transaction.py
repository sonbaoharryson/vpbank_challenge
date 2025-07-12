from pydantic import BaseModel, Field
from typing import Optional

class Transaction(BaseModel):
    transaction_id: str
    transaction_date: str
    transaction_type: str
    amount: float
    currency: str
    sender_account: str
    receiver_account: str
    sender_bank: str
    receiver_bank: str
    channel: str
    location: str
    device_id: str
    user_id: str
    is_fraud: int
    transaction_status: str
    latency_ms: int
    retry_count: int
    ip_address: str
    user_agent: str
    is_new_device: bool
    anomaly_type: Optional[str] = Field(default=None, description="Type of anomaly injected, if any.") 