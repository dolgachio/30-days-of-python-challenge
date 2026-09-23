squares: dict[str, int] = [{"height": 4, "width": 5}, {"height": 4, "width": 9}]

def area_sum(rectangles: list[dict[str, int]]) -> int:
    result: int = 0
    
    for item in rectangles:
        width: int = item['width'] or 1
        height: int = item['height'] or 1

        print(height, "height")
        print(width, "width")
        
        result += width * height

    return result

area_sum(squares)