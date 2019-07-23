train_schedule = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]
 
train_111 = train_schedule[7] ['frequency_in_minutes']
print(train_111)

train_80B = train_schedule[6] ['direction']
print(train_80B)

def get_direction(direction, train_schedule):
    for train in train_schedule:
        for value in train.values():
            if value == direction:
                print(train['train'])

get_direction('east', train_schedule)
get_direction('north', train_schedule)


trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]


trains_by_frequency = {}
for train in trains:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
        print(trains_by_frequency)
# north_bound = []
# for train in train_schedule:
#     for value in train.values():
#         if value == 'north':
#             north_bound.append(train["train"])

# print('North bound trains')
# print(north_bound)        
    

# east_bound = []
# for train in train_schedule:
#     for value in train.values():
#         if value == 'east':
#             east_bound.append(train["train"])
# print('East bound trains')
# print(east_bound)
