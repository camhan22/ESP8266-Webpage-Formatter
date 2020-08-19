import codecs
import os

file_name = input("Enter the file name of the file to convert: ") #Get the file name to work on
file=codecs.open(file_name,'r') #Open the file
file_name = os.path.splitext(file_name)[0]+'.txt'

output = open(file_name,'w+')
text = file.read() #Read the string to operate on
char_num = 0 #Start at the beginning after the first open bracket
page_name = input("Enter the name of the page to be converted: ")


def insert_quote(string, index):
    return string[:index] + '"' + string[index:]

def insert_slash(string, index):
    return string[:index] + '\\' + string[index:]


while char_num < len(text) - 1: #Go on until reached one before end of file
    #Add escaping characters first
    if text[char_num] == '\"':
        text = insert_slash(text,char_num)
        char_num = char_num + 1

    #Add quotes to beginning and end now
    elif text[char_num] == '>' and text[char_num+1] == '\n':
        text = insert_quote(text,char_num+1)
        char_num = char_num + 1 #skip one char since we inserted a new one

    elif text[char_num] == '<' and (text[char_num-1] == '\t' or text[char_num-1] == '\n'):
        text = insert_quote(text,char_num)
        char_num = char_num + 1 #skip one character or it causes an infinite loop

    #Add the beginning and end quotes to the entire block of text
    elif char_num == 0 and text[char_num] != '"':
        text = insert_quote(text,char_num)

    elif char_num == len(text)-2 and text[char_num+1] != '"':
        text = text + '\"'
                            
    char_num = char_num + 1 #Increment the char num

text = "String " + page_name + " =\n" + text + ";"

output.seek(0)
print(text)
output.write(text)
file.close()
output.close()
input("press enter to quit...")
