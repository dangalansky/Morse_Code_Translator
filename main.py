#list of the alphabet. including numbers, spaces, periods and commas
alpha = [' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '.', ',']
#create list of corresponding morse code characters
morse = [' ', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-', '-...', '-.-.',
         '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.',
         '...', '-', '..-', '...-', '.--', '.--.', '-.--', '--..', '.-.-.-', '--..--']
#input for user to type what they wish to translate
to_trans = input('Type what you want to translate: ')

#create new list from user input
morse_list = []
for letter in to_trans:
    morse_idx = alpha.index(letter.lower())
    morse_list.append(morse[morse_idx])

#join list elements back into string
final_translation = ' '.join(morse_list)

#print final string, translated into international morse code
print(final_translation)

