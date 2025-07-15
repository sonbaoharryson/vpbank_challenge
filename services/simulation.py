from faker import Faker
import random
from models.transaction import Transaction
from datetime import datetime
fake = Faker()

ANOMALY_TYPES = [
    "high_amount", "rare_location", "device_user_mismatch", "frequent_retries", "foreign_location"
]

BANKS = ["ACB", "BIDV", "VCB", "MB", "TCB", "VPB", "SCB"]
CHANNELS = ["API", "ATM", "POS", "INTERNET_BANKING", "MOBILE_APP", "POS"]
CURRENCIES = ["VND"]
TRANSACTION_TYPES = ["IBFT", "QR_PAYMENT", "BILL_PAYMENT", "WALLET_TOPUP"]
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

# Vietnamese provinces and cities (sample, can be expanded)
VIETNAM_PROVINCES = [
    ("Hà Nội", "Quận Ba Đình"),
    ("Hà Nội", "Quận Hoàn Kiếm"),
    ("Hà Nội", "Quận Hai Bà Trưng"),
    ("Hà Nội", "Quận Đống Đa"),
    ("Hà Nội", "Quận Tây Hồ"),
    ("Hà Nội", "Quận Cầu Giấy"),
    ("Hà Nội", "Quận Thanh Xuân"),
    ("Hà Nội", "Quận Hoàng Mai"),
    ("Hà Nội", "Quận Long Biên"),
    ("Hà Nội", "Quận Bắc Từ Liêm"),
    ("Hà Nội", "Quận Nam Từ Liêm"),
    ("Hà Nội", "Quận Hà Đông"),
    ("Hà Nội", "Huyện Ba Vì"),
    ("Hà Nội", "Huyện Chương Mỹ"),
    ("Hà Nội", "Huyện Đan Phượng"),
    ("Hà Nội", "Huyện Đông Anh"),
    ("Hà Nội", "Huyện Gia Lâm"),
    ("Hà Nội", "Huyện Hoài Đức"),
    ("Hà Nội", "Huyện Mê Linh"),
    ("Hà Nội", "Huyện Mỹ Đức"),
    ("Hà Nội", "Huyện Phú Xuyên"),
    ("Hà Nội", "Huyện Phúc Thọ"),
    ("Hà Nội", "Huyện Quốc Oai"),
    ("Hà Nội", "Huyện Sóc Sơn"),
    ("Hà Nội", "Huyện Thạch Thất"),
    ("Hà Nội", "Huyện Thanh Oai"),
    ("Hà Nội", "Huyện Thanh Trì"),
    ("Hà Nội", "Huyện Thường Tín"),
    ("Hà Nội", "Huyện Ứng Hòa"),
    ("Hà Nội", "Thị xã Sơn Tây"),

    ("Hồ Chí Minh", "Thành phố Thủ Đức"),
    ("Hồ Chí Minh", "Quận 1"),
    ("Hồ Chí Minh", "Quận 2"),
    ("Hồ Chí Minh", "Quận 3"),
    ("Hồ Chí Minh", "Quận 4"),
    ("Hồ Chí Minh", "Quận 5"),
    ("Hồ Chí Minh", "Quận 6"),
    ("Hồ Chí Minh", "Quận 7"),
    ("Hồ Chí Minh", "Quận 8"),
    ("Hồ Chí Minh", "Quận 10"),
    ("Hồ Chí Minh", "Quận 11"),
    ("Hồ Chí Minh", "Quận 12"),
    ("Hồ Chí Minh", "Quận Bình Tân"),
    ("Hồ Chí Minh", "Quận Bình Thạnh"),
    ("Hồ Chí Minh", "Quận Tân Bình"),
    ("Hồ Chí Minh", "Quận Tân Phú"),
    ("Hồ Chí Minh", "Quận Phú Nhuận"),
    ("Hồ Chí Minh", "Quận Gò Vấp"),
    ("Hồ Chí Minh", "Huyện Bình Chánh"),
    ("Hồ Chí Minh", "Huyện Củ Chi"),
    ("Hồ Chí Minh", "Huyện Hóc Môn"),
    ("Hồ Chí Minh", "Huyện Nhà Bè"),
    ("Hồ Chí Minh", "Huyện Cần Giờ"),

    ("Đà Nẵng", "Quận Hải Châu"),
    ("Đà Nẵng", "Quận Thanh Khê"),
    ("Đà Nẵng", "Quận Sơn Trà"),
    ("Đà Nẵng", "Quận Ngũ Hành Sơn"),
    ("Đà Nẵng", "Quận Liên Chiểu"),
    ("Đà Nẵng", "Quận Cẩm Lệ"),
    ("Hải Phòng", "Quận Hồng Bàng"),
    ("Hải Phòng", "Quận Lê Chân"),
    ("Hải Phòng", "Quận Ngô Quyền"),
    ("Hải Phòng", "Quận Kiến An"),
    ("Hải Phòng", "Quận Hải An"),
    ("Hải Phòng", "Quận Đồ Sơn"),
    ("Hải Phòng", "Quận Dương Kinh"),
    ("Hải Phòng", "Huyện An Dương"),
    ("Hải Phòng", "Huyện An Lão"),
    ("Hải Phòng", "Huyện Bạch Long Vĩ"),
    ("Hải Phòng", "Huyện Cát Hải"),
    ("Hải Phòng", "Huyện Kiến Thụy"),
    ("Hải Phòng", "Huyện Thủy Nguyên"),
    ("Hải Phòng", "Huyện Tiên Lãng"),
    ("Hải Phòng", "Huyện Vĩnh Bảo"),

    # Cần Thơ
    ("Cần Thơ", "Quận Ninh Kiều"),
    ("Cần Thơ", "Quận Bình Thủy"),
    ("Cần Thơ", "Quận Cái Răng"),
    ("Cần Thơ", "Quận Ô Môn"),
    ("Cần Thơ", "Quận Thốt Nốt"),
    ("Cần Thơ", "Huyện Cờ Đỏ"),
    ("Cần Thơ", "Huyện Phong Điền"),
    ("Cần Thơ", "Huyện Thới Lai"),
    ("Cần Thơ", "Huyện Vĩnh Thạnh"),

    # Bình Dương
    ("Bình Dương", "Thành phố Thủ Dầu Một"),
    ("Bình Dương", "Thành phố Thuận An"),
    ("Bình Dương", "Thành phố Dĩ An"),
    ("Bình Dương", "Thị xã Bến Cát"),
    ("Bình Dương", "Thị xã Tân Uyên"),
    ("Bình Dương", "Huyện Bàu Bàng"),
    ("Bình Dương", "Huyện Dầu Tiếng"),
    ("Bình Dương", "Huyện Phú Giáo"),
    ("Bình Dương", "Huyện Bắc Tân Uyên"),

    # Đồng Nai
    ("Đồng Nai", "Thành phố Biên Hòa"),
    ("Đồng Nai", "Thành phố Long Khánh"),
    ("Đồng Nai", "Huyện Trảng Bom"),
    ("Đồng Nai", "Huyện Long Thành"),
    ("Đồng Nai", "Huyện Nhơn Trạch"),
    ("Đồng Nai", "Huyện Xuân Lộc"),
    ("Đồng Nai", "Huyện Định Quán"),
    ("Đồng Nai", "Huyện Thống Nhất"),
    ("Đồng Nai", "Huyện Tân Phú"),
    ("Đồng Nai", "Huyện Vĩnh Cửu"),
    ("Đồng Nai", "Huyện Cẩm Mỹ"),

    # Khánh Hòa
    ("Khánh Hòa", "Thành phố Nha Trang"),
    ("Khánh Hòa", "Thành phố Cam Ranh"),
    ("Khánh Hòa", "Thị xã Ninh Hòa"),
    ("Khánh Hòa", "Huyện Cam Lâm"),
    ("Khánh Hòa", "Huyện Diên Khánh"),
    ("Khánh Hòa", "Huyện Khánh Sơn"),
    ("Khánh Hòa", "Huyện Khánh Vĩnh"),
    ("Khánh Hòa", "Huyện Vạn Ninh"),
    ("Khánh Hòa", "Huyện Trường Sa"),
     ("Quảng Ninh", "Thành phố Hạ Long"),
    ("Quảng Ninh", "Thành phố Cẩm Phả"),
    ("Quảng Ninh", "Thành phố Uông Bí"),
    ("Quảng Ninh", "Thành phố Móng Cái"),
    ("Quảng Ninh", "Thị xã Đông Triều"),
    ("Quảng Ninh", "Thị xã Quảng Yên"),
    ("Quảng Ninh", "Huyện Vân Đồn"),
    ("Quảng Ninh", "Huyện Ba Chẽ"),
    ("Quảng Ninh", "Huyện Bình Liêu"),
    ("Quảng Ninh", "Huyện Cô Tô"),
    ("Quảng Ninh", "Huyện Đầm Hà"),
    ("Quảng Ninh", "Huyện Hải Hà"),
    ("Quảng Ninh", "Huyện Tiên Yên"),

    # Lâm Đồng
    ("Lâm Đồng", "Thành phố Đà Lạt"),
    ("Lâm Đồng", "Thành phố Bảo Lộc"),
    ("Lâm Đồng", "Huyện Bảo Lâm"),
    ("Lâm Đồng", "Huyện Cát Tiên"),
    ("Lâm Đồng", "Huyện Đạ Huoai"),
    ("Lâm Đồng", "Huyện Đạ Tẻh"),
    ("Lâm Đồng", "Huyện Di Linh"),
    ("Lâm Đồng", "Huyện Đơn Dương"),
    ("Lâm Đồng", "Huyện Đức Trọng"),
    ("Lâm Đồng", "Huyện Lạc Dương"),
    ("Lâm Đồng", "Huyện Lâm Hà"),

    # Gia Lai
    ("Gia Lai", "Thành phố Pleiku"),
    ("Gia Lai", "Thị xã An Khê"),
    ("Gia Lai", "Thị xã Ayun Pa"),
    ("Gia Lai", "Huyện Chư Păh"),
    ("Gia Lai", "Huyện Chư Prông"),
    ("Gia Lai", "Huyện Chư Pưh"),
    ("Gia Lai", "Huyện Chư Sê"),
    ("Gia Lai", "Huyện Đắk Đoa"),
    ("Gia Lai", "Huyện Đắk Pơ"),
    ("Gia Lai", "Huyện Ia Grai"),
    ("Gia Lai", "Huyện Ia Pa"),
    ("Gia Lai", "Huyện KBang"),
    ("Gia Lai", "Huyện Kông Chro"),
    ("Gia Lai", "Huyện Krông Pa"),
    ("Gia Lai", "Huyện Mang Yang"),
    ("Gia Lai", "Huyện Phú Thiện"),

    # Thừa Thiên Huế
    ("Thừa Thiên Huế", "Thành phố Huế"),
    ("Thừa Thiên Huế", "Thị xã Hương Thủy"),
    ("Thừa Thiên Huế", "Thị xã Hương Trà"),
    ("Thừa Thiên Huế", "Huyện A Lưới"),
    ("Thừa Thiên Huế", "Huyện Nam Đông"),
    ("Thừa Thiên Huế", "Huyện Phong Điền"),
    ("Thừa Thiên Huế", "Huyện Phú Lộc"),
    ("Thừa Thiên Huế", "Huyện Phú Vang"),
    ("Thừa Thiên Huế", "Huyện Quảng Điền"),

    # Nghệ An
    ("Nghệ An", "Thành phố Vinh"),
    ("Nghệ An", "Thị xã Cửa Lò"),
    ("Nghệ An", "Thị xã Thái Hòa"),
    ("Nghệ An", "Thị xã Hoàng Mai"),
    ("Nghệ An", "Huyện Anh Sơn"),
    ("Nghệ An", "Huyện Con Cuông"),
    ("Nghệ An", "Huyện Diễn Châu"),
    ("Nghệ An", "Huyện Đô Lương"),
    ("Nghệ An", "Huyện Hưng Nguyên"),
    ("Nghệ An", "Huyện Kỳ Sơn"),
    ("Nghệ An", "Huyện Nam Đàn"),
    ("Nghệ An", "Huyện Nghi Lộc"),
    ("Nghệ An", "Huyện Nghĩa Đàn"),
    ("Nghệ An", "Huyện Quế Phong"),
    ("Nghệ An", "Huyện Quỳ Châu"),
    ("Nghệ An", "Huyện Quỳ Hợp"),
    ("Nghệ An", "Huyện Quỳnh Lưu"),
    ("Nghệ An", "Huyện Tân Kỳ"),
    ("Nghệ An", "Huyện Thanh Chương"),
    ("Nghệ An", "Huyện Tương Dương"),
    ("Nghệ An", "Huyện Yên Thành"),
]


FOREIGN_PROVINCES = [
    # Laos
    ("Laos", "Vientiane Prefecture"),
    ("Laos", "Vientiane Province"),
    ("Laos", "Luang Prabang"),
    ("Laos", "Champasak"),
    ("Laos", "Savannakhet"),
    # (còn 13 tỉnh khác trong tổng số 17)

    # Thailand
    ("Thailand", "Bangkok"),
    ("Thailand", "Chiang Mai"),
    ("Thailand", "Chiang Rai"),
    ("Thailand", "Chon Buri"),
    ("Thailand", "Phuket"),
    # (còn 71 tỉnh khác trong tổng số 76)

    # Cambodia
    ("Cambodia", "Phnom Penh"),
    ("Cambodia", "Battambang"),
    ("Cambodia", "Siem Reap"),
    ("Cambodia", "Kampong Cham"),
    ("Cambodia", "Preah Sihanouk"),
    # (còn 20 tỉnh khác trong tổng số 25)

    # USA (bang + DC)
    ("USA", "California"),
    ("USA", "Texas"),
    ("USA", "New York"),
    ("USA", "Florida"),
    ("USA", "Illinois"),
    ("Laos", "Attapeu"),
    ("Laos", "Bokeo"),
    ("Laos", "Bolikhamsai"),
    ("Laos", "Houaphanh"),
    ("Laos", "Khammouane"),
    ("Laos", "Luang Namtha"),
    ("Laos", "Oudomxay"),
    ("Laos", "Phongsaly"),
    ("Laos", "Salavan"),
    ("Laos", "Sekong"),
    ("Laos", "Xaisomboun"),
    ("Laos", "Xayaboury"),
    ("Laos", "Xieng Khouang"),

    # Thailand (tiếp tục)
    ("Thailand", "Nakhon Ratchasima"),
    ("Thailand", "Udon Thani"),
    ("Thailand", "Khon Kaen"),
    ("Thailand", "Nakhon Sawan"),
    ("Thailand", "Nakhon Pathom"),
    ("Thailand", "Songkhla"),
    ("Thailand", "Surat Thani"),
    ("Thailand", "Ayutthaya"),
    ("Thailand", "Rayong"),
    ("Thailand", "Saraburi"),
    ("Thailand", "Trang"),
    ("Thailand", "Ubon Ratchathani"),
    ("Thailand", "Lampang"),

    # Cambodia (tiếp tục)
    ("Cambodia", "Kampot"),
    ("Cambodia", "Koh Kong"),
    ("Cambodia", "Kampong Thom"),
    ("Cambodia", "Takeo"),
    ("Cambodia", "Ratanakiri")
]

def simulate_transaction(anomaly_rate: float = 0.5) -> Transaction:
    anomaly = None
    is_foreign = False
    if random.random() < anomaly_rate:
        anomaly = random.choice(ANOMALY_TYPES)
        if anomaly == "rare_location" or anomaly == "foreign_location":
            is_foreign = True
    amount = round(random.uniform(10000, 5_000_000), 2)
    device_id = f"DEVICE_{random.randint(1, 20)}"
    user_id = f"USER_{random.randint(100, 999)}"
    retry_count = random.randint(0, 2)
    latency_ms = random.randint(100, 5000)
    if anomaly == "high_amount":
        amount = round(random.uniform(100_000_000, 1_000_000_000), 2)
    if anomaly == "device_user_mismatch":
        device_id = f"DEVICE_{random.randint(21, 40)}"
        user_id = f"USER_{random.randint(1000, 2000)}"
    if anomaly == "frequent_retries":
        retry_count = random.randint(5, 10)
        latency_ms = random.randint(5000, 20000)
    # Province/city selection
    if is_foreign:
        province, city = random.choice(FOREIGN_PROVINCES)
    else:
        province, city = random.choice(VIETNAM_PROVINCES)
    # Merchant and other new fields
    merchant_id = f"MER_{random.randint(1000, 9999)}"
    merchant_location = city if not is_foreign else f"{city}, {province}"
    pos_id = f"POS_{random.randint(100, 999)}"
    qr_type = random.choice(["STATIC", "DYNAMIC", None])
    cif = f"CIF_{random.randint(100000, 999999)}"
    return Transaction(
        transaction_id=fake.unique.bothify(text='TXN#####'),
        timestamp=datetime.now().isoformat(),
        transaction_type=random.choice(TRANSACTION_TYPES),
        amount=amount,
        currency=random.choice(CURRENCIES),
        sender_account=fake.bothify(text='????####'),
        receiver_account=fake.bothify(text='????####'),
        sender_bank=random.choice(BANKS),
        receiver_bank=random.choice(BANKS),
        channel=random.choice(CHANNELS),
        province=province,
        city=city,
        device_id=device_id,
        is_new_device=random.choice([True, False]),
        user_id=user_id,
        cif=cif,
        merchant_id=merchant_id,
        merchant_location=merchant_location,
        pos_id=pos_id,
        qr_type=qr_type,
        transaction_status=random.choice(STATUS),
        latency_ms=latency_ms,
        retry_count=retry_count,
        ip_address=fake.ipv4_public(),
        user_agent=random.choice(USER_AGENTS),
        is_anomaly=(anomaly is not None),
        anomaly_type=anomaly
    ) 