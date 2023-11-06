def football_points(wins, draws, losses):
    points = wins * 3 + draws * 1 + losses * 0
    return points 

print(football_points(5,2,1))
