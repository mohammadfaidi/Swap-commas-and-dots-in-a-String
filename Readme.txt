

'''
Given a string, we need to replace all commas with dots and all dots with the commas. This can be achieved in two popular ways.
Examples:

Input : 14, 625, 498.002
Output : 14.625.498, 002


we can use traditiona way
replace (. , " ") and ...etc

Using maketrans and translate()

maketrans: This static method returns a translation table usable for str.translate(). This builds a translation table, which is a mapping of integers or characters to integers, strings, or None.

translate: This returns a copy of the string where all characters occurring in the optional argument are removed, and the remaining characters have been mapped through the translation table, given by the maketrans table.


intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))

th3s 3s str3ng 2x1mpl2....w4w!!!
'''

#maketrans create translation table
#in order to used tralation methoud we should used trasation table thats created by maketrans
