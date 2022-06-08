'''
Xuan Guo
CS5001, FALL 2020
LAB12
'''
import os
import collections

def main():
    network = collections.defaultdict(list)
    try:
        with open("/dwarves.txt", "r") as f:
            arr = f.readlines()
            for acc in arr:
                network[acc.split()[0]] = acc.split()[1:]
            f.close()
    except FileNotFoundError:
        print("file does not exist")
    
    name = input("Which of the 7 dwarves is logging in?\n")
    choice = ""
    while choice != "q":
        choice = input("Choose from one of the options below: \
            P: Print your friends list\nU <name>: Unfriend someone\nF <name>: \
                Friend someone\nQ: Quit\n").lower()
        if not choice:
            print("invalid input")
            return

        if choice == "p":
            print("Your friends:", " ".join(network[name]))
        elif choice.startswith("u"):
            if len(choice.split()) == 1:
                print("invalid input")
                return
            candidate = choice.split()[1]
            if candidate in network[name]:
                network[name].remove(candidate)
                print("{} has been unfriended.".format(candidate))
            else:
                print("{} is not your friend.".format(candidate))
        elif choice.startswith("f"):
            if len(choice.split()) == 1:
                print("invalid input")
                return
            candidate = choice.split()[1]
            if candidate in network[name]:
                print("{} Was already your friend.".format(candidate))
            else:
                network[name].append(candidate)
                print("{} has been friended.".format(candidate))
        with open("/dwarves.txt", "w") as fout:
            for key in network:
                fout.write(key + " " + " ".join(network[key])+"\n")

        


if __name__ == "__main__":
    main()