'''
CS5001, Fall 2020
Xuan Guo, Zihan Wang, Qiong Peng, Yumeng An, Ruiqi Yang

This program identifies positive and negative reviews for user
'''

def main():
    filename = input("Enter the path to the IMDB dataset: ")
    good_review, bad_review = [], []
    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    review, label = line.split('\t')
                    if label.strip() == '1':
                        good_review.append(review.strip())
                    else:
                        bad_review.append(review.strip())
                except:
                    print("Error processing the file.")

        # part 2
        with open('Desktop/positive.txt', "w") as out:
            for review in good_review:
                out.write("%s\n" % review)
        with open('Desktop/negative.txt', "w") as out:
            for review in bad_review:
                out.write("%s\n" % review)
                
        # part 3
        user_input = ""
        while True:
            user_input = input("Which review to display? e.g. p 3: ")
            if user_input == "q":
                break
            try:
                label_input, index_input = user_input.split()
                label_input = label_input.strip()
                index_input = index_input.strip()
                if label_input.lower() == "p":
                    print(good_review[int(index_input)])
                elif label_input.lower() == "n":
                    print(bad_review[int(index_input)])
            except IndexError:
                print("Index out of range!")
            except ValueError:
                print("Invalid input. only include label and index separated by space. e.g. p 3")

    except FileNotFoundError:
        print("File not Found!")

if __name__ == "__main__":
    main()