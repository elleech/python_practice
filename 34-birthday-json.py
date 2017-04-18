import json

# Create a JSON file
def birth_json(new):
    birthdays = {
        'Albert Einstein': '03/14/1879',
        'Benjamin Franklin': '01/17/1706',
        'Ada Lovelace': '12/10/1815',
        }
    birthdays.update(new)
    with open('scientists.json', 'w') as file:
        json.dump(birthdays, file)
    file.close()

# Read the JSON file and modify it if needed
file = open('scientists.json', 'r')
data = json.load(file)
print('Welcome to the birthday dictionary.\nWe know the birthdays of:')
for i in data.keys(): print('   ' + i)

while True:
    whose = input("Who's birthday do you want to look up? ")
    if whose in data:
        print("{}'s birthday was {}.".format(whose, data[whose]))
        break
    else:
        print("Too bad. That name doesn't exist.")
        insert = input('Do you want to add the info? Y/N ').upper()
        if insert == 'Y':
            date = input("When was {}'s birthday? ".format(whose))
            data.update({whose:date})
            with open('scientists.json', 'w') as file:
                json.dump(data, file)
        else:
            continue
file.close()
