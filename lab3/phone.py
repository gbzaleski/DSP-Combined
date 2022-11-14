



#phonebook = {} # User -> [Numbers, ...]

def start():
    return {"#ALL" : []} # Diffent than all names

def add(pb, user, number):
    if number in pb["#ALL"]:
        return pb
        
    if user in pb:
        pb[user].append(number)
    else:
        pb[user] = [number]
    
    pb["#ALL"].append(number)
    return pb


def get_nums(pb, user):
    return pb[user]

def del_num(pb, user, number):
    if user in pb:
        if number in pb[user]:
            pb[user].remove(number)
    return pb

def print_all(pb):
    for user in pb:
        if user != "#ALL":
            print(user, end=": ")
            first = True
            for num in pb[user]:
                if first:
                    first = False
                else:
                    print(", ", end="")
                print(num, end="")
            print()

if __name__ == "__main__":

    tpb = start()
    tpb = add(tpb, "Janusz", 322323)
    tpb = add(tpb, "Krzysiek", 2137)
    tpb = add(tpb, "Janusz", "122-345-555")
    tpb = add(tpb, "Ania", 911)
    tpb = add(tpb, "Janusz", 911)
    print_all(tpb)


