import asyncio
from config.locations import get_available_locations
from utils.helpers import get_user_inputs
from core.pharmacy import search_pharmacy_by_medicine_and_location, get_nearest_pharmacies_by_location

def process_command(message: str) -> str:
    """
    Memproses perintah dari user
    """
    try:
        if message.lower() == "help":
            help_text = f"""
🏥 PHARMACY FINDER AGENT - BANTUAN PENGGUNAAN

Format pesan yang didukung:

1. Mencari obat tertentu:
   search:[nama_obat]:[nama_lokasi]
   Contoh: search:paracetamol:monas

2. Mencari apotek terdekat:
   nearest:[nama_lokasi]
   Contoh: nearest:kemang

3. Melihat daftar lokasi:
   locations

4. Bantuan:
   help

📍 Lokasi yang tersedia:
{get_available_locations()}
            """
            return help_text
        
        if message.lower() == "locations":
            return f"📍 Daftar lokasi yang tersedia:\n\n{get_available_locations()}"
        
        parts = message.split(":")
        
        if len(parts) < 2:
            return "❌ Format pesan tidak valid. Ketik 'help' untuk bantuan."
        
        command = parts[0].lower().strip()
        
        if command == "search" and len(parts) >= 3:
            medicine_name = parts[1].strip()
            location_name = parts[2].strip()
            
            if not medicine_name or not location_name:
                return "❌ Nama obat dan lokasi tidak boleh kosong."
            
            result = search_pharmacy_by_medicine_and_location(medicine_name, location_name)
            
            if not result["success"]:
                response = f"❌ {result['error']}\n\n📍 Lokasi yang tersedia:\n{result['available_locations']}"
                return response
            
            results = result["results"]
            if not results:
                return f"❌ Maaf, tidak ditemukan apotek yang memiliki '{medicine_name}' dalam radius 10 km dari {result['location_used']}."
            else:
                response = f"🔍 Ditemukan {len(results)} apotek yang memiliki '{medicine_name}' di sekitar {result['location_used']}:\n\n"
                
                for i, pharmacy in enumerate(results[:5], 1):
                    response += f"{i}. 🏥 **{pharmacy['name']}**\n"
                    response += f"   📍 {pharmacy['address']}\n"
                    response += f"   📞 {pharmacy['phone']}\n"
                    response += f"   🚶 Jarak: {pharmacy['distance']} km\n"
                    response += f"   🗺️ Google Maps: {pharmacy['google_maps_url']}\n"
                    response += f"   💊 Obat tersedia:\n"
                    
                    for med in pharmacy['available_medicines']:
                        response += f"      - {med['name']}: Rp {med['price']:,}\n"
                    response += "\n"
                    
                return response
        
        elif command == "nearest" and len(parts) >= 2:
            location_name = parts[1].strip()
            
            if not location_name:
                return "❌ Nama lokasi tidak boleh kosong."
            
            result = get_nearest_pharmacies_by_location(location_name)
            
            if not result["success"]:
                response = f"❌ {result['error']}\n\n📍 Lokasi yang tersedia:\n{result['available_locations']}"
                return response
            
            results = result["results"]
            if not results:
                return f"❌ Tidak ditemukan apotek dalam radius 5 km dari {result['location_used']}."
            else:
                response = f"🏥 Ditemukan {len(results)} apotek terdekat dari {result['location_used']}:\n\n"
                
                for i, pharmacy in enumerate(results, 1):
                    response += f"{i}. 🏥 **{pharmacy['name']}**\n"
                    response += f"   📍 {pharmacy['address']}\n"
                    response += f"   📞 {pharmacy['phone']}\n"
                    response += f"   🚶 Jarak: {pharmacy['distance']} km\n"
                    response += f"   💊 Total obat: {pharmacy['total_medicines']} jenis\n"
                    response += f"   🗺️ Google Maps: {pharmacy['google_maps_url']}\n\n"
                    
                return response
        
        else:
            return "❌ Format pesan tidak valid. Ketik 'help' untuk melihat format yang benar."
        
    except Exception as e:
        return f"❌ Terjadi kesalahan: {str(e)}\nKetik 'help' untuk bantuan penggunaan."

async def interactive_mode():
    """
    Mode interaktif yang meminta input nama obat dan lokasi secara terpisah
    """
    print("🏥 PHARMACY FINDER AGENT - INTERACTIVE MODE")
    print("=" * 50)
    print("🔍 Cara menggunakan:")
    print("1. Masukkan nama obat yang dicari")
    print("2. Masukkan lokasi Anda")
    print("3. Ketik 'exit' untuk keluar")
    print("4. Ketik 'help' untuk bantuan")
    print("5. Ketik 'locations' untuk melihat daftar lokasi")
    print("=" * 50)
    
    while True:
        try:
            print("\n" + "="*30)
            user_input = input("💬 Pilih menu (search/nearest/help/locations/exit): ").strip().lower()
            
            if user_input in ['exit', 'quit', 'q']:
                print("👋 Terima kasih telah menggunakan Pharmacy Finder Agent!")
                break
            
            if user_input == 'help':
                result = process_command('help')
                print(f"\n🤖 Response:\n{result}")
                continue
            
            if user_input == 'locations':
                result = process_command('locations')
                print(f"\n🤖 Response:\n{result}")
                continue
            
            if user_input == 'search':
                medicine_name, location_name = get_user_inputs()
                command = f"search:{medicine_name}:{location_name}"
                result = process_command(command)
                print(f"\n🤖 Response:\n{result}")
                
            elif user_input == 'nearest':
                print("\n🔍 PENCARIAN APOTEK TERDEKAT")
                print("=" * 40)
                location_name = input("📍 Lokasi Anda (contoh: monas, kemang, senayan): ").strip()
                
                if not location_name:
                    print("❌ Mohon masukkan nama lokasi!")
                    continue
                
                command = f"nearest:{location_name}"
                result = process_command(command)
                print(f"\n🤖 Response:\n{result}")
                
            else:
                print("❌ Menu tidak valid. Pilih: search/nearest/help/locations/exit")
            
        except KeyboardInterrupt:
            print("\n\n👋 Terima kasih telah menggunakan Pharmacy Finder Agent!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")