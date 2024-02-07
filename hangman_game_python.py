import random
list_word = ["apple","mango","potato"]
chosen_word = random.choice(list_word)
life = 6
display = []
for letter in chosen_word:
    display.append("_")
print(display)
game_over = False
while(not game_over):
    guessed_letter = input("Guess a letter : ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if(letter == guessed_letter):
            display[position]=guessed_letter
    print(display)
    if(guessed_letter not in chosen_word):
        life = life - 1
        if(life == 0):
            game_over = True
            print("you lose")
    if "_" not in display:
        game_over == True
        print("you win")