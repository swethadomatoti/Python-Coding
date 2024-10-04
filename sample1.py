#write a program to create a string and
# obtain stating 2 characters and last 2 characters from string
# and if string length is less than 2 return then return empty string
def retrive_string(string):
    if len(string)<2:
        return ' '
    return string[0:2]+string[-2:]
s=retrive_string('swetha')
print(s)



