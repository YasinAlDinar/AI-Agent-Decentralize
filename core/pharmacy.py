from typing import Dict, List
from utils.data import load_pharmacy_data
from utils.geolocation import calculate_distance, get_coordinates_from_location_name
from config.locations import get_available_locations

def search_pharmacy_by_medicine_and_location(medicine_name: str, location_name: str, max_distance: float = 10.0) -> Dict:
    """
    Mencari apotek yang memiliki obat tertentu berdasarkan nama lokasi
    """
    # Dapatkan koordinat dari nama lokasi
    location_info = get_coordinates_from_location_name(location_name)
    if not location_info:
        return {
            "success": False,
            "error": f"Lokasi '{location_name}' tidak ditemukan.",
            "available_locations": get_available_locations()
        }
    
    user_lat, user_lon, full_location_name = location_info
    
    data = load_pharmacy_data()
    results = []
    
    for pharmacy in data["pharmacies"]:
        # Cek apakah apotek memiliki obat yang dicari
        has_medicine = any(
            medicine_name.lower() in med["name"].lower() 
            for med in pharmacy["medicines"]
        )
        
        if has_medicine:
            # Hitung jarak dari user ke apotek
            distance = calculate_distance(
                user_lat, user_lon, 
                pharmacy["latitude"], pharmacy["longitude"]
            )
            
            if distance <= max_distance:
                # Cari detail obat yang tersedia
                available_medicines = [
                    med for med in pharmacy["medicines"] 
                    if medicine_name.lower() in med["name"].lower()
                ]
                
                pharmacy_info = {
                    "name": pharmacy["name"],
                    "address": pharmacy["address"],
                    "phone": pharmacy["phone"],
                    "distance": round(distance, 2),
                    "latitude": pharmacy["latitude"],
                    "longitude": pharmacy["longitude"],
                    "available_medicines": available_medicines,
                    "google_maps_url": f"https://maps.google.com/?q={pharmacy['latitude']},{pharmacy['longitude']}"
                }
                results.append(pharmacy_info)
    
    # Sort berdasarkan jarak terdekat
    results.sort(key=lambda x: x["distance"])
    
    return {
        "success": True,
        "location_used": full_location_name,
        "results": results,
        "medicine_searched": medicine_name
    }

def get_nearest_pharmacies_by_location(location_name: str, max_distance: float = 5.0, limit: int = 5) -> Dict:
    """
    Mendapatkan apotek terdekat dari nama lokasi
    """
    # Dapatkan koordinat dari nama lokasi
    location_info = get_coordinates_from_location_name(location_name)
    if not location_info:
        return {
            "success": False,
            "error": f"Lokasi '{location_name}' tidak ditemukan.",
            "available_locations": get_available_locations()
        }
    
    user_lat, user_lon, full_location_name = location_info
    
    data = load_pharmacy_data()
    results = []
    
    for pharmacy in data["pharmacies"]:
        distance = calculate_distance(
            user_lat, user_lon,
            pharmacy["latitude"], pharmacy["longitude"]
        )
        
        if distance <= max_distance:
            pharmacy_info = {
                "name": pharmacy["name"],
                "address": pharmacy["address"],
                "phone": pharmacy["phone"],
                "distance": round(distance, 2),
                "latitude": pharmacy["latitude"],
                "longitude": pharmacy["longitude"],
                "total_medicines": len(pharmacy["medicines"]),
                "google_maps_url": f"https://maps.google.com/?q={pharmacy['latitude']},{pharmacy['longitude']}"
            }
            results.append(pharmacy_info)
    
    # Sort berdasarkan jarak dan batasi hasil
    results.sort(key=lambda x: x["distance"])
    
    return {
        "success": True,
        "location_used": full_location_name,
        "results": results[:limit]
    }