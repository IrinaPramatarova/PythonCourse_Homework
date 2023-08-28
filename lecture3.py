# Задача 1. Принтирайте следният текст на екрана:
#  “23 4.5 False John”.
# obj1 = 23
# obj2 = 4.5123456789
# obj3 = ' False John '

# print(' %d %.2f %s ' % (obj1 , obj2 , obj3 )) #example 1 to test 2 after decimal
# print(' %d %.4f %s ' % (obj1 , obj2 , obj3 )) #example 1 to test 4 numbers after decimal


# Задача: Попълнете празните полета, като използвате форматиращият метод format. 
# Празните места запълнете с вашето име и любими активности.

# obj1 = 'Peter'
# obj2 = 'swimming'
# obj3 = 'He'
# obj4 = 'his'

# print( "{}'s favorite sports is {}.".format(obj1, obj2))
# print( "{} is working on {} programming skills!".format(obj3 , obj4 ))

# Задача: Създайте променлива, paragraph, която да съдържа следното съдържание:
# "Python is a great language!", said Fred. "I don't ever remember having this much fun before. "
# paragraph = '"Python is a great language!", said Fred. "I don\'t ever remember having this much fun before. "'
# print(paragraph)

# *** Slide 17 ***

# Задача1 Създайте стринг, който да се казва school - да съдържа името на вашето училище.
# Използвате методите, които научихте за да промените стринга. 
# Ако е необходимо използвайте help функцията.

# school_name = 'school'
# school_name = '"Software Academy"'
# print(school_name)
# print( "The name of my school is {}.".format(school_name))
# print(f"{school_name}")

# Задача2 Създайте стринг, който да се казва country и присвоете на него стойност “usa”. 
#Създайте нов стринг, correct_country, чиято стойност да е държавата само с големи букви, 
#като използвате някой от стринг методите.

# country = 'usa'
# correct_country = country.upper()
# print(correct_country)

# Задача 3. Създайте стринг,  filename и му присвоете стойност “hello.py”. 
# Проверете дали стринга завършва на “.java”. 
# Намерете индексът на ”py”. Проверете и дали думата започва с ”world”.

# filename = 'hello.py'

# print(filename.endswith( '.java' )) #False
# print(filename.startswith( 'world' )) #False
# print(filename.startswith( 'hello' )) #just for test - True

# Задача 4. Опитайте се да принтирате стринг изцяло с главни букви.
# obj1 = ' Test if this string can be all caps'
# print( obj1.upper())

# Задача 5. Напишете програма, която да премахва ”$$” от името ”$$John Smith”. 
# Опитайте с .lstrip и .strip(). 
# За да видите описанието на двете функции използвайте следното help(“ ”.strip).

# name = '$$John Smith'

# print( name.lstrip('$$') )  #testing lstrip
# print( name.strip('$$') )  #testing strip

# name = '$$John Smith%'  #added % at the end to test better strip

# print( name.lstrip('$$') )  #testing lstrip
# print( name.strip('$$, %') )  #testing strip


# Задача 6. Програма по картинка:
row1 = '*' * 40  #Note: when center the text - 40!
row2 = '=' * 40
company = 'Coding Temple, Inc.'
address = '283 Franklin St.'
city = 'Boston, MA'

obj1 = 'Product Name'
obj2 = 'Product Price'
obj3 = 'Total'

product1= 'Books'
product2 = 'Computer'
product3 = 'Monitor'

product1_price = '$49.95'
product2_price = '$579.99'
product3_price = '$124.89'
total_price = '$754.83'

text = 'Thanks for shopping with us today!'

print(row1)
print(company.center(40))
print(address.rjust(26))  #How to: Как да подравня текста по горния ред, вместо да се ползва rjust?
print(city.rjust(20))

print(row2)
print(obj1, obj2.rjust(20))
print(product1 , product1_price.rjust(20))
print(product2 , product2_price.rjust(18))
print(product3 , product3_price.rjust(19))

print(row2)
print('{:^40}'.format(obj3))
print('{:^40}'.format(total_price))  #How to: Add $ next to the sum and center the text at one time?

print(row2)
print('\n')
print(text.center(40))
print('\n')
print(row1)

















