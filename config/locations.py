# Dictionary lokasi terkenal di Jakarta dengan koordinatnya
JAKARTA_LOCATIONS = {
    "monas": {"lat": -6.1751, "lon": 106.8249, "name": "Monas (Monumen Nasional)"},
    "plaza indonesia": {"lat": -6.1944, "lon": 106.8229, "name": "Plaza Indonesia"},
    "senayan": {"lat": -6.2088, "lon": 106.8456, "name": "Senayan City"},
    "kemang": {"lat": -6.2615, "lon": 106.8106, "name": "Kemang Village"},
    "melawai": {"lat": -6.2421, "lon": 106.7997, "name": "Melawai"},
    "sudirman": {"lat": -6.2146, "lon": 106.8131, "name": "Sudirman"},
    "roxy": {"lat": -6.1833, "lon": 106.7914, "name": "Roxy Mas"},
    "kebon jeruk": {"lat": -6.1689, "lon": 106.7678, "name": "Kebon Jeruk"},
    "mangga dua": {"lat": -6.1389, "lon": 106.8333, "name": "Mangga Dua"},
    "kelapa gading": {"lat": -6.1581, "lon": 106.9106, "name": "Kelapa Gading"},
    "cempaka putih": {"lat": -6.1667, "lon": 106.8667, "name": "Cempaka Putih"},
    "pondok indah": {"lat": -6.2642, "lon": 106.7831, "name": "Pondok Indah"},
    "thamrin": {"lat": -6.1944, "lon": 106.8229, "name": "Thamrin"},
    "gambir": {"lat": -6.1751, "lon": 106.8249, "name": "Gambir"},
    "jakarta pusat": {"lat": -6.1751, "lon": 106.8249, "name": "Jakarta Pusat"},
    "jakarta selatan": {"lat": -6.2615, "lon": 106.8106, "name": "Jakarta Selatan"},
    "jakarta barat": {"lat": -6.1689, "lon": 106.7678, "name": "Jakarta Barat"},
    "jakarta utara": {"lat": -6.1389, "lon": 106.8333, "name": "Jakarta Utara"},
}

def get_available_locations() -> str:
    """
    Mengembalikan daftar lokasi yang tersedia
    """
    locations = [f"• {key.title()} ({value['name']})" for key, value in JAKARTA_LOCATIONS.items()]
    return "\n".join(sorted(locations))