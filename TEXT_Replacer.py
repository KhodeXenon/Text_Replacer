__coder__ = "KhodeXenon"
__my_email__ = "KhodeXenon@gmail.com"
def TextReplace(file_name) :
    '''a function for replacing a word in a text file'''

    #checking file extension
    file_check = file_name.split(".")
    if (file_check[-1]).lower() != "txt" :
        print("Invalid file type !")
    # checking file extension

    #try to open a file if exists
    else :
        try:
            with open(file_name) as overal_text_file :
                processing_text = overal_text_file.read()
    # try to open a file if exists

        except FileNotFoundError :
            print("The file does not exist !")

        else:
    # get inputs from the user about words
            wanna_find_word = input("Which word are you searching :").lower()
            replace_to = input("Replace to which word :")
    # get inputs from the user about words
    # create a new file with new name and new replaced content
            new_text = processing_text.replace(wanna_find_word , replace_to)
            new_file_name = "newReplaced_" + file_name
            with open(new_file_name, "w") as new_overal_text_file :
                new_overal_text_file.write(new_text)
            open_or_not = input("Do yo want to open the new text file ? (y) :")
            if open_or_not == "y" or open_or_not == "yes" :
                import os
                os.system("start " + new_file_name)

    # create a new file with new name and new replaced content


running_status = True
while running_status :
    print("[-------------------------]")
    file_name = input("Text file name :")
    TextReplace(file_name)
    print()
    again_or_not = input("again ? (Yes or No) :").lower()
    print("[-------------------------]")
    if again_or_not == "y" or again_or_not == "yes" :
        running_status = True
    else:
        running_status = False
        print("quit ...")

input()

