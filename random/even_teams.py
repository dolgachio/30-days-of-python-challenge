def get_even_and_odd_teams(players):
    even_players = []
    odd_players = []
    
    for i in range(0, len(players)):
        is_even = i % 2 == 0
        if is_even:
            even_players.append(players[i])
        else:
            odd_players.append(players[i])
            
    return even_players, odd_players

players = [
            "Harry",
            "Hermione",
            "Ron",
            "Ginny",
            "Fred",
            "Neville",
            "Draco",
            "Luna",
            "Cho",
            "Gregory",
            "Lee",
            "Michael",
            "Lavender",
            "Frank",
            "Anthony",
            "Allan",
        ]

result1, result2 = get_even_and_odd_teams(players)

print(result1, result2)
