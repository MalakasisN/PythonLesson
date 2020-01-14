import csv

order_index = 0
season_index = 1
episode_index = 2
character_killed_index = 3
killer_index = 4
method_index = 5
method_cat_index = 6
reason_index = 7
location_index = 8
allegiance_index = 9
importance_index = 10

data = []
with open('game-of-thrones-deaths-data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    header = f.readline().strip().split(',')
    for ls in reader:
        d = {
            'order': int(ls[order_index]),
            'season': int(ls[season_index]),
            'episode': int(ls[episode_index]),
            'character_killed': ls[character_killed_index],
            'killer': ls[killer_index],
            'method': ls[method_index],
            'method_cat': ls[method_cat_index],
            'reason': ls[reason_index],
            'location': ls[location_index],
            'allegiance': ls[allegiance_index],
            'importance': int(ls[importance_index]) if ls[importance_index] else 1,
        }
        data.append(d)