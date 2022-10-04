# Day 26: NATO Alphabet Converter

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

data_file = pandas.read_csv("nato_phonetic_alphabet.csv")

# Get text and convert into individual characters
inputed_text = input("Input your text: ").upper()
convert = [x for x in inputed_text]

# My code
final = []
for charac in convert :
    try :
        for (index, row) in data_file.iterrows():
            if row.letter == charac :
                final.append(row.code)
    except :
        final.append(charac)

# Instructor Code
phonetic_dict = {row.letter : row.code for (index, row) in data_file.iterrows()}
output_list = [phonetic_dict[letter] for letter in inputed_text]



print(final)
print(output_list)


#Loop through rows of a data frame
for (index, row) in data_file.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

