#  hi
import sqlite3
import xlsxwriter

from sqlite3 import Error




def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection



def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



mycon =  create_connection('C:\\RON\\SQLITE\\db\\ron.db')

myres = execute_read_query(mycon,"select * from r1")

for res in myres:
    print(res)
    

print ('hi')
a=2
b=3
print (a+b)  # another comment
# comment

a="aaa" + 3*'bbb'
print (a)
print (a[0:4])

c= len(a)
print (c)
# now list
squares = [1, 4, 9, 16, 25]
squares = squares + [30,32,34]
squares[4]=17
print (squares)

a, b = 0, 1
while a < 1000:
#    print(a, end=',')
    a, b = b, a+b

##a, b = 0, 1
##while a < 1000:
##    print(a)
##    a, b = b, a+b

# if and control
x=100
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')



# for example 
word = ['a','b','c','d','e']
print (word)

for i in word :
  print (i)

for i in range(5):
    print(i)


workbook = xlsxwriter.Workbook('hello_world.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()
