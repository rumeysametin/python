name = input("player name: ")
surname = input("player surname: ")
team = input("player team: ")
info = [name, surname, team]
print( "player name: {}\nplayer surname: {}\nplayer team: {}\n".format(info[0], info[1], info[2]) )

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
result = a * b * c
print("{} x {} x {} = {} dir".format(a,b,c,result))

a = int(input("a:"))
b = int(input("b:"))
c =  (a ** 2 + b ** 2) ** 0.5
print("Hipotenüs: ",c)

a= input("a:")
b = input("b:")
print("before\na: {} b: {}\n".format(a,b))
a,b = b,a
print("after\na: {} b: {}\n".format(a,b))

age = int (input("enter your age: "))
if age < 18 :
    print("you can't enter!")
else:
    print("you can enter")

print("""
İndex
""")
a = float(input("height: "))
b = int(input ("kilo: "))
c = b / (a*a)
print("index: ", c)
if (c < 18.5):
    print("thin")
elif (c < 25):
    print("normal")
elif (c < 30):
    print("overweight")
else:
    print("obese")
    
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if ( a>b and a>c ):
    print("largest number: a")
elif ( b>a and b>c ):
    print("largest number: b")
elif ( c>a and c>b ):
    print("largest number: c")
    
vize1 = int(input("Vize1:"))
vize2 = int(input("Vize2:"))
final = int(input("Final:"))
note =  vize1 * 3/10 + vize2 * 3/10 + final * 4/10
print("note: ", note)
if ( note >= 88 ):
  print ("AA") 
elif ( note>= 80 ):
  print ("BA")
elif ( note>= 73 ):
  print ("BB")
elif ( note>= 66 ):
  print ("CB")
elif ( note>= 60 ):
  print ("CC")
elif ( note>= 55 ):
  print ("DC")
elif ( note>= 50 ):
  print ("DD")
else:
  print ("you failed!")
  
print("""
user login
""")
sys_username = "michael"
sys_password = "0101"
right_of_enter = 3
while True:
  username = input ("username: ")
  password = input ("password: ")
  if (sys_username == username and sys_password != password):
    print ("password is wrong!")
    right_of_enter -= 1
  elif (sys_username != username and sys_password == password):
    print ("username is wrong!")
    right_of_enter -= 1
  elif (sys_username != username and sys_password != password):
    print ("username and password are wrong!")
    right_of_enter -= 1
  else:
    print ("logged in")
    break
  if (right_of_enter == 0):
    print("you finished your right of enter! ")
    break
  
number = int(input("Number:"))
i = 1
total = 0
while (i < number):
    if (number % i == 0):
        total += i
    i += 1
if (total == number):
    print(number,"is the perfect number.")
else:
    print(number,"isn't the perfect number.")
    
for x in range (1,11):
  print("******************")
  for y in range (1,11):
    print("{} * {} = {}".format(x, y, x*y))
    
print("numbers divisible by 3: ")
for i in range(1,50):
  if (i % 3 != 0):
    continue
  print( i)
  
list = [i for i in range(1,101) if i%2 == 0]
print(list)