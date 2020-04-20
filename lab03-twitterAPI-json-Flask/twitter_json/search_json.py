import json



def search(user, key):
    result = None
    if not result and isinstance(user, dict):
        for element in user.keys():
            if isinstance(user[element], list):
                for el in user[element]:
                    result = search(el, key)
                    if result: break
            elif isinstance(user[element], dict):
                result = search(user[element], key)
            elif element == key:
                result = user[element]
                break
            else:
                result = None
    return result


file = open('nasa1.json', encoding='utf-8')
nasa = json.load(file)
file.close()


print(search(nasa["users"], 'description'))



