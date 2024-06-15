# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas as pd
# student_data_frame = pd.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
is_valid_input =  False

nato_file = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for index, row in nato_file.iterrows()}
# print(nato_dict.values())
# print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

while not is_valid_input:
    user_input = input("Enter the name: ").upper()

    try:
        phonetic_list = [nato_dict[letter] for letter in user_input]
        is_valid_input = True
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(phonetic_list)


