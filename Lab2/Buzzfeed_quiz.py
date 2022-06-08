'''

Xuan Guo
CS 5001, Fall 2020

This program asks user 3 questions and determines which characters in
Harry Potter their personality close to.
'''

def main():

    print("Our Harry Potter quiz asks three questions, \
        each with three possible answers:")
    print("When planning a trip, you...")
    print("A: Find the hot parties.")
    print("B: Sorts out all the logistics.")
    print("C: Lets everyone else take charge.")
    ans1 = str(input("Your answer: ")).lower()
    print("")

    print("What are you most afraid of?")
    print("A: Not being accepted.")
    print("B: Losing someone close to me.")
    print("C: Looking stupid in front of others.")
    ans2 = str(input("Your answer: ")).lower()
    print("")

    print("WWhat was your favorite toy as a kid?")
    print("A: She-Ra")
    print("B: He-Man")
    print("C: Video games")
    ans3 = str(input("Your answer: ")).lower()
    print("")

    vaild_ans = ["a", "b", "c"]
    final_ans = [ans1, ans2, ans3]
    for index, value in enumerate(final_ans):
        if value in vaild_ans:
            final_ans[index] = value
        else:
            final_ans[index] = "a"
    
    if final_ans[0] == "a" and final_ans[1] == "b":
        check_ans = "ab"
    elif final_ans[0] == "a" and final_ans[1] == "c":
        check_ans = "ac"
    elif final_ans[0] == "b":
        check_ans = "b"
    elif final_ans[0] == "c" and final_ans[1] == "b":
        check_ans = "cb"
    elif final_ans[0] == "c" and final_ans[1] == "c":
        check_ans = "cc"
    else:
        check_ans = final_ans[0] + final_ans[1] + final_ans[2]
        
    ans_rule = {"aaa" : "Ginny", "aab" : "Draco", "aac" : "Sirius",
    "ab" : "Dobby", "ac" : "Voldemort", "b" : "Hermione", "caa" : "Luna",
    "cab" : "Hagrid", "cac" : "Ron", "cb" : "Tonks", "cc" : "Slughorn"}  
    for key, value in ans_rule.items():
        if key == check_ans:
            print("Your Harry Potter character is: " + str(value))
            break

if __name__ == "__main__":
    main()