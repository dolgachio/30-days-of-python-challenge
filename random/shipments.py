from typing import Optional

shipments = {
    "north": [
        ("boots", 4, "Denver"),
        ("coats", None, "Denver"),
        ("hats", 2, None),
    ],
    
    "south": [
        ("other", 77, "Kyiv"),
        ("corn", 88, "Kyiv"),
        ("pops", 2, None),
    ]
}

# {
#     "north": {
#         "Denver": [("boots", 4), ("coats", 3)],
#         "unassigned": [("hats", 2)],
#     }
# }

from typing import Optional

def organize_shipments(shipments: dict[str, list[tuple[str, Optional[int], Optional[str]]]], fallback_quantity: int | None) -> dict[str, dict[str, list[tuple[str, int]]]]:

    result: dict[str, dict[str, list[tuple[str, int]]]] = {}
    
    for key in shipments:
        if key not in result:
            result[key] = {}
        
        shipment = shipments[key]
        
        for item in shipment:
            item_name, item_quantity, item_city = item

            quantity = item_quantity or fallback_quantity
            city_key_to_save = item_city or 'unassigned'
            is_city_not_added = city_key_to_save not in result[key]
            
            if bool(quantity) and is_city_not_added:
               result[key][city_key_to_save] = []    

            if bool(quantity):
                product_to_save: tuple[str, int] = (item_name, quantity)
                result[key][city_key_to_save].append(product_to_save)
                
                            
    return result
     
print(organize_shipments(shipments, 3))