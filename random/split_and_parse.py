def parse_score(text):
    try:
        result: int = int(text)

        return result
    except Exception:
        return -1
        


def read_setting(settings, key):
    try:
        value = settings[key]
        
        return value
    except Exception:
        return "missing"    
        
def split_bill(total, people):
    if people == 0:
        return 0

    return total / people


read_setting({'theme': 'dark', 'mode': 'story'}, 'volume')