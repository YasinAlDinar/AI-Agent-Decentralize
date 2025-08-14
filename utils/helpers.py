from typing import Tuple

def get_user_inputs() -> Tuple[str, str]:
    """
    Meminta input nama obat dan lokasi dari user
    """
    print("\n🔍 PENCARIAN OBAT DI APOTEK")
    print("=" * 40)
    
    # Input nama obat
    while True:
        medicine_name = input("💊 Nama obat yang dicari: ").strip()
        if medicine_name:
            break
        print("❌ Mohon masukkan nama obat yang valid!")
    
    # Input lokasi
    while True:
        location_name = input("📍 Lokasi Anda (contoh: monas, kemang, senayan): ").strip()
        if location_name:
            break
        print("❌ Mohon masukkan nama lokasi!")
    
    return medicine_name, location_name