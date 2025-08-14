import math
from typing import Optional, Tuple
from config.locations import JAKARTA_LOCATIONS

def get_coordinates_from_location_name(location_name: str) -> Optional[Tuple[float, float, str]]:
    """
    Mengkonversi nama lokasi menjadi koordinat
    Returns: (latitude, longitude, full_location_name) atau None jika tidak ditemukan
    """
    location_lower = location_name.lower().strip()
    
    # Cari exact match dulu
    if location_lower in JAKARTA_LOCATIONS:
        loc = JAKARTA_LOCATIONS[location_lower]
        return (loc["lat"], loc["lon"], loc["name"])
    
    # Cari partial match
    for key, value in JAKARTA_LOCATIONS.items():
        if location_lower in key or key in location_lower:
            return (value["lat"], value["lon"], value["name"])
    
    return None

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Menghitung jarak antara dua koordinat dalam kilometer menggunakan formula Haversine
    """
    R = 6371  # Radius bumi dalam km
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return R * c