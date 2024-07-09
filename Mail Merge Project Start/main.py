#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as f_names:
    name_list = f_names.readlines()
    print(name_list)
for name in name_list:
    na = name.strip('\n')
    print(na)
    with open(f"Output/ReadyToSend/{na}.txt", mode="w") as new_later:
        with open("Input/Letters/starting_letter.txt") as example:
            example_text = example.read()
            new_later.write(f"{example_text.replace('[name]',na)}")
