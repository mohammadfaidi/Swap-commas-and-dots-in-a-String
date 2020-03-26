

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


#method1
def swap(str):
    #maketrans b3mal translation table
    #min $han 2st5damh traslate lazam 2st5dam transation table wb3mlh min 5lal maketrans
    maketrans = str.maketrans
    final = str.translate(maketrans(', .'   ,       '., '))
    return final



string = "14, 625, 498.002"
print(swap(string))

#method 2
def Replace(str1):
    str1 = str1.replace(', ', 'third')
    str1 = str1.replace('.', ', ')
    str1 = str1.replace('third', '.')
    return str1


string2= "14, 625, 498.002"
print(Replace(string2))


#method 3
def Replace(str3):
    str1 = str3.replace(', ', '.')
    str1 = str3.replace('.', ', ')
    return str3


string3= "14, 625, 498.002"
print(Replace(string3))
