# -*- coding: utf-8 -*-
"""
@author: GSS

Programming Assignment:
    
Subject: Information Theory And Coding

Problem statement: 
    Write a program to draw a table of codewords taking input
    as a random string by Lempel-Ziv method. 

Code by: Shashank G S
         4JN18EC081
                     
##################################################################
################## LEMPEL-ZIV ENCODING ###########################
##################################################################

Program to generate the dictionary using random string

"""
#switch to encode to either binary or text
print("---------------------------------------------------------------------------")
print("\nPRESS 1 if are applying LZ encoding method on binary numbers \n      2 if you are applying it on alphabets")
print("---------------------------------------------------------------------------")
x=int(input())

#taking input
if x == 1:
    print("Enter the random binary string without spaces, eg:- 010010101010010110000")
    input_str = input("Enter your String(in binary):")
if x == 2:
    print("Enter the random string, eg:- This_is_his_hit_")
    input_str = input("Enter your String:")
    
keys_dict = {}   
ind = 0
inc = 1
i=1

#function to make the codeword list
def codelist(cl,code):
    cl.append(code)
    return cl

#fuction to geneate the codeword
def codeword(dicto,phrase,x):
    if x==1:
        if(phrase=='0'):
            return format(0,'05b')
        if(phrase=='1'):
            return format(1,'05b')
        key=phrase[:-1]
        code=str(format(dicto[key],'04b'))+phrase[-1]
    if x==2:
        if(len(phrase)>1):
            key=phrase[:-1]
            code=str(dicto[key])+phrase[-1]
        if(len(phrase)==1):
            code='\u03C6'+phrase 
    return(code)

#making the dictionary
while True:
    if not (len(input_str) >= ind+inc):
        break
    sub_str = input_str[ind:ind + inc]
    if sub_str in keys_dict:
        inc += 1       
    else:
        keys_dict[sub_str] = i
        i=i+1
        ind += inc
        inc = 1

#printing the dictionary
print("The phrases are:\n")
print (list(keys_dict))
print("\n\n")

print ("{:<20} {:<20} {:<20} {:<20}".format('PHRASE', 'LOCATION' , 'LOCATION IN BINARY','CODEWORD')) 
print("---------------------------------------------------------------------------")
# print each data item. 

cl=[]
for value in keys_dict.items(): 
    phrase,location = value 
    cw=codeword(keys_dict,phrase,x)
    cl=codelist(cl,cw)
    print ("{:<20} {:<20} {:<20} {:<20}".format(phrase,location,format(location,'04b'),cw)) 
print("\n\n The code-word list is as follows\n")
print(cl)