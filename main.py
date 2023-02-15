# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

def get_names():
    with open('./Input/Names/invited_names.txt', 'r') as invited_names_file:
        names_list = invited_names_file.read().split('\n')
        return names_list


def replace_name(name):
    with open('./Input/Letters/starting_letter.txt', 'r') as letter_file:
        letter = letter_file.read().replace("[name]", name)
        with open(f'./ReadyToSend/{name}.txt', 'w') as new_letter_file:
            new_letter_file.write(letter)


names = get_names()
for name in names:
    replace_name(name)



# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
