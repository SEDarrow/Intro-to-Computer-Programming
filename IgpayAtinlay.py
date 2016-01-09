# IgpayAtinlay.py
# Shannon Zarich and Sarah Darrow
# Smz29 and Sd1209
# 11/2/15
#
# This program translates sentences into Pig Latin

def pig_latin(sentence):
    sentence = sentence.split(" ")
    output = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in sentence:
        for letter in range(len(word)):
            if word[letter] == 'q':
                letter += 2
                break
            if(word[letter] in vowels):
                break
        if(word.lower() == word):
            output += word[letter:] + word[:letter].lower() + 'ay'+ ' '
        else:
            if word[letter:] != '':
                output += word[letter:].capitalize() + word[:letter].lower() + 'ay'+ ' '
            else:
                output +=  word[:letter].capitalize() + 'ay'+ ' '
    print(output)
        
def main():
    another = 'y'
    while(another == 'y'):
        entered = str(input("Input a string which you would like to turn into a Pig Latin sentence: "))
        pig_latin(entered)
        another = str(input("Do you want to translate another sentence? (y/n): "))
        print('')
        
main()