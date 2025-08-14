import json

def load_pharmacy_data():
    """
    Memuat data apotek dari file JSON
    """
    try:
        with open('pharmacy_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File pharmacy_data.json tidak ditemukan!")
        return {"pharmacies": []}