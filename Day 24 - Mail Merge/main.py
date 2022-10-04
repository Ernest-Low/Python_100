#Day 24 - Mail Merge (Very minimal)


with open ("./Input/Letters/starting_letter.txt") as file :
    msg = file.read()

with open ("./Input/Names/invited_names.txt") as file :
    name = file.readlines()

for x in name :
    stripped_name = x.strip()
    with open (f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode = "w") as completed_letter :
        finished_letter = msg.replace("[name]", stripped_name)
        completed_letter.write(finished_letter)
