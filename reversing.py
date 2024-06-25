##A python program for inputing a string as a list of characters from console, delete at least 2 characters, reverse the
##resultant string and print it.

word=input('Enter string')#For entering a string
word=word[:-2]#for deleting atleast 2 charaters
word=word[::-1]#for reversing the resultant string
print(f'The reversed string after removal of 2 characters {word}')#for displaying the final reversed string