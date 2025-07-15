from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    transaction_id: str
    timestamp: str
    transaction_type: str
    amount: float
    currency: str
    sender_account: str
    receiver_account: str
    sender_bank: str
    receiver_bank: str
    channel: str
    province: str = Field(description="Province in Vietnam, or anomaly if outside Vietnam")
    city: str = Field(description="City in Vietnam, or anomaly if outside Vietnam")
    device_id: str
    is_new_device: bool
    user_id: str
    cif: Optional[str] = Field(default=None, description="Customer Information File")
    merchant_id: Optional[str] = Field(default=None)
    merchant_location: Optional[str] = Field(default=None)
    pos_id: Optional[str] = Field(default=None)
    qr_type: Optional[str] = Field(default=None)
    transaction_status: str
    latency_ms: int
    retry_count: int
    ip_address: str
    user_agent: str
    is_anomaly: Optional[bool] = Field(default=None, description="Anomaly label (True=anomaly, False=normal, None=unlabeled)")
    anomaly_type: Optional[str] = Field(default=None, description="Type of anomaly (e.g., 'high_amount', 'rare_location', etc.), or None if normal.")

class TransactionUnlabeled(BaseModel):
    transaction_id: str
    timestamp: str
    transaction_type: str
    amount: float
    currency: str
    sender_account: str
    receiver_account: str
    sender_bank: str
    receiver_bank: str
    channel: str
    province: str
    city: str
    device_id: str
    is_new_device: bool
    user_id: str
    cif: Optional[str] = None
    merchant_id: Optional[str] = None
    merchant_location: Optional[str] = None
    pos_id: Optional[str] = None
    qr_type: Optional[str] = None
    transaction_status: str
    latency_ms: int
    retry_count: int
    ip_address: str
    user_agent: str