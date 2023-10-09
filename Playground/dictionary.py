navn = "za"
alder = 20
by = "smørum"

dic = {
    "navn": "Zander",
    "alder": 20,
    "by": "Smørum"
}

print(dic)  # {'navn': 'Zander', 'alder': 20, 'by': 'Smørum'}

print(dic["by"])

personer = [{
    "navn": "Zander",
    "alder": 20,
    "by": "Smørum"
},
{
    "navn": "Oli",
    "alder": 17,
    "by": "Smørum"
}]

print(personer) # [{'navn': 'Zander', 'alder': 20, 'by': 'Smørum'}, {'navn': 'Oli', 'alder': 17, 'by': 'Smørum'}]

for item in personer:
    print(item["navn"])

keypad_dict = {0: [' '],
    2: ['A', 'B', 'C'],
    3: ['D', 'E', 'F'],
    4: ['G', 'H', 'I'],
    5: ['J', 'K', 'L'],
    6: ['M', 'N', 'O'],
    7: ['P', 'Q', 'R', 'S'],
    8: ['T', 'U', 'V'],
    9: ['W', 'X', 'Y', 'Z']}

print(keypad_dict[2][1])    
print(keypad_dict[9][2])    