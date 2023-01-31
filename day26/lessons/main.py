import pandas

# Dictionary Comprehension
data = pandas.read_csv("phonetic_alphabet_data.csv") 
phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

is_on = True
while is_on == True:
    word = input("Enter a word: ").upper()
    if word == "EXIT":
        is_on = False
    # List Comprehension
    output_list = [phonetic_dictionary[letter] for letter in word]
    print(output_list)