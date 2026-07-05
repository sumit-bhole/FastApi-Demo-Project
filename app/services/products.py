import json
from pathlib import Path
from typing import List, Dict

Data_File = Path(__file__).parent.parent / "data" / "products.json"


def load_products() -> List[Dict]:
    if not Data_File.exists():
        return []
    with open(Data_File, "r", encoding="utf-8") as file:
        return json.load(file)

def get_all_products() -> List[Dict]:
    return load_products()


