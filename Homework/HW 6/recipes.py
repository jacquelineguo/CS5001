'''
Xuan Guo
CS5001, Fall 2020

This program helps user to write a new recipe or read an exist recipe
'''


EMPTY_STR = ""
FILE_FORMAT = ".txt"


def check_choices(choice, choices_lst):
    '''
        Function -- check_choices
            Check if the user entered choice is valid
        Parameters:
            choice -- the user's choice to enter
            choices_lst -- a list contains valid user choices
        Returns:
            Raise ValueError if the user's enter is not valid
    '''
    if choice not in choices_lst:
        raise ValueError


def separate_ing(ing):
    '''
        Function -- separate_ing
            Separate a string with comma and remove the beginning and
            ending spaces
        Parameters:
            ing -- a string contains variety ingredients separate by comma
        Returns:
            A list with different ingredients as each element and removed the
            beginning and ending spaces
    '''
    ing = ing.split(",")
    ing_new = [item.strip() for item in ing]
    return ing_new


def check_ingredients(ing):
    '''
        Function -- check_ingredients
            Check if the user entered ingredients is valid
        Parameters:
            ing -- a string contains variety ingredients separate by comma
        Returns:
            True if the user inputed ingredients list has at least one
            none-empty element, False otherwise
    '''
    ing_lst = separate_ing(ing)
    VALID_LEN = 1
    IS_INVALID = len(ing_lst) < VALID_LEN or\
        (len(ing_lst) == VALID_LEN and EMPTY_STR in ing_lst)
    if IS_INVALID:
        return False
    for item in ing_lst:
        if item != EMPTY_STR:
            return True
    return False


def clean_file_name(name):
    '''
        Function -- clean_file_name
            Convert a file name to a valid file name
        Parameters:
            name -- a file name entered by user as a string
        Returns:
            The converted name in lowercase and replaced white space to
            underscores, removed any leading or trailing whitespace and
            remaining non-alphanumeric characters, then add “.txt” to the end
    '''
    name = name.strip().replace(" ", "_").lower()
    file_name = ""
    for item in name:
        if item.isalnum():
            file_name += item
        elif item == "_":
            file_name += item
    return file_name + FILE_FORMAT


def check_empty_name(file_name):
    '''
        Function -- check_empty_name
            Check if the file name is empty
        Parameters:
            file_name -- a string which express a text file name
        Returns:
            True if the file name not equal to ".txt", False otherwise
    '''
    return file_name == FILE_FORMAT


def create_file(file_name):
    '''
        Function -- create_file
            Write a file with given file name
        Parameters:
            file_name -- a valid text file name
        Returns:
            An opened writing file
    '''
    file_path = file_name
    file = open(file_path, "w")
    return file


def write_recipe(file, recipe_name, ing_lst, time, directions):
    '''
        Function -- write_recipe
            Write the recipe name, ingredients, cooking time, and directions to
            a given file
        Parameters:
            file -- a writing file
            recipe_name -- a string contains the recipe name
            ing_lst -- a list contains the ingredients
            time -- an integer which express the time in minutes
            directions -- a string which contains the cooking directions
        Returns:
            A closed writing file which contains recipe name, ingredients,
            cooking time, and cooking directions
    '''
    BLANK_LINE = "\n"
    ING_TITLE = "Ingredients:"
    file.write(recipe_name + BLANK_LINE + BLANK_LINE + ING_TITLE + BLANK_LINE)
    for item in ing_lst:
        file.write(item + BLANK_LINE)
    time_info = "Time: " + str(time) + " minutes"
    DIR = "Directions:"
    time_dir = BLANK_LINE + time_info + BLANK_LINE + BLANK_LINE + DIR +\
        BLANK_LINE + directions
    file.write(time_dir)
    file.close()


def read_file(file_name):
    '''
        Function -- read_file
            Read the file contents of a given file
        Parameters:
            file_name -- a string of file name
        Returns:
            The read contents of the asking file
    '''
    file = open(file_name, "r")
    file_contents = file.read()
    file.close()
    return file_contents


def check_ing_format():
    '''
        Function -- check_ing_format
            Check if the user entered ingredients is not empty and valid, keep
            asking the user to enter the valid ingredients if it's not valid
        Parameters:
            No Parameters
        Returns:
            No Returns
    '''
    valid_ing = False
    while valid_ing is False:
        ingredients = input(
            "Enter the ingredients on one line. "
            "Separate each ingredient with a comma. "
            )
        if not check_ingredients(ingredients):
            print("Recipe must have at least one ingredient.")
        else:
            ing_lst = separate_ing(ingredients)
            valid_ing = True
    return ing_lst


def check_time():
    '''
        Function -- check_time
            Check if the user entered time input is an integer and greater than
            zero, if not valid, then keep asking user to enter a valid time
        Parameters:
            No Parameters
        Returns:
            No Returns
    '''
    valid_time = False
    ZERO = 0
    time_error = "Invalid time. Must be an integer greater than or equal to 0."
    while valid_time is False:
        try:
            time = int(input("Enter the time needed in minutes: "))
            if time < ZERO:
                raise ValueError
            else:
                valid_time = True
        except ValueError:
            print(time_error)
    return time


def check_file_name(file_name):
    '''
        Function -- check_file_name
            Check if the user entered a valid file name (file name is not
            empty), if not valid, continuing to ask user to enter a valid one
        Parameters:
            file_name -- a string contains a file name
        Returns:
            A valid file name
    '''
    while check_empty_name(file_name):
        print("Unable to create the filename.")
        file_name = input(
            "Enter a string containing only letters, numbers, and spaces "
        )
        file_name = clean_file_name(file_name)
    return file_name


def is_empty_name(file_name):
    '''
        Function -- is_empty_name
        Parameters:
            file_name -- a user given file name
        Returns:
            Raise a FileNotFoundError if the file name dose not exist
    '''
    if check_empty_name(file_name):
        raise FileNotFoundError


def main():
    valid_choice = False
    NEW_RECIPE = 1
    READ = 2
    QUIT = 3
    CHOICES = [NEW_RECIPE, READ, QUIT]
    while valid_choice is False:
        try:
            user_choice = int(input(
                "MENU: 1 - Save a new recipe, 2 - Read a recipe, 3 - Quit "
                ))
            check_choices(user_choice, CHOICES)
            if user_choice == NEW_RECIPE:
                ing_lst = check_ing_format()
                directions = input("Enter the directions (1 paragraph only): ")
                time = check_time()
                recipe_name = input("Enter a name for the recipe: ")
                file_name = clean_file_name(recipe_name)
                file_name = check_file_name(file_name)
                file = create_file(file_name)
                write_recipe(file, recipe_name, ing_lst, time, directions)
                print(recipe_name + " recipe saved to " + file_name)
            elif user_choice == READ:
                recipe_name = input("Enter the name of the recipe: ")
                file_name = clean_file_name(recipe_name)
                try:
                    is_empty_name(file_name)
                    file_contents = read_file(file_name)
                    print(file_contents)
                except FileNotFoundError:
                    print("Unable to read " + file_name)
            else:
                valid_choice = True
        except ValueError:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
