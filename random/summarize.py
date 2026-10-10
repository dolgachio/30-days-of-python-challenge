from typing import Optional

records  = {
    "alpha": [
        {"orders": 2, "points": 5},
        {"orders": 4, "points": 8},
    ],
    "beta": [
        {"orders": 1, "points": 2},
    ],
}


def summarize_user_records(records: dict[str, list[dict[str, int | None] | None]]) -> dict[str, int]:
    result: dict[str, int] = {
        'total_users': 0,
        'users_with_orders': 0,
        'total_orders': 0,
        'total_points': 0,
    }

    for key in records:
        
        for user_data in records[key]:
            total_orders_for_this_user = 0
            total_points_for_this_user = 0
           
            if user_data is None:
                continue
            
            result['total_users'] += 1
            
            if 'orders' in user_data and isinstance(user_data['orders'], int):
                total_orders_for_this_user += user_data['orders']
                    
            if 'points' in user_data and isinstance(user_data['points'], int):
                total_points_for_this_user += user_data['points']
        
            result['total_orders'] = result['total_orders'] + total_orders_for_this_user
            result['total_points'] = result['total_points'] + total_points_for_this_user
            
            if total_orders_for_this_user > 0:
                result['users_with_orders'] += 1
        
        
    return result

print(summarize_user_records(records))