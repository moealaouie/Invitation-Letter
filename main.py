file = 'Input/Names/invited_names.txt'
names = []

with open(file, 'r') as file:
    for line in file:
        name = line.strip()
        f = open(f"Output/ReadyToSend/letter_for_{name}.txt", "w")
        f.write(f"Dear {name},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nMoe")
        f.close()



