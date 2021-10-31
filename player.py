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

def prime(number):
  if (number == 1):
    return False
  elif (number == 2):
    return True
  else:
    for i in range (2, number):
      if (number % i == 0):
        return False
    return True
while True:
  number = input("enter a number: ")
  if (number == "q"):
    break
  else:
    number = int(number)
    if (prime(number)):
      print(number,"is a prime number")
    else:
      print(number,"isn't a prime number")

def pisagor():
    pisagor_list = []
    for i in range(1,101):
        for j in range(1,101):
            c = (i ** 2 + j ** 2) ** 0.5
            if (c == int(c) ):
                pisagor_list.append((i,j,int(c)))
    return pisagor_list
for i in pisagor():
    print(i)

import random   
print ("""
number guessing game    
       """)
random_number = random.randint(0,50)
guess_right = 7
while True:
  guess = int(input("your guess: "))
  if (guess < random_number):
    print("say higher number!")
    guess_right -= 1
  elif (guess > random_number):
    print("say smaller number!")
    guess_right -= 1
  else:
    print("congratulations! Correct number")
    break
  if (guess_right == 0):
    print("guess right is over!")
    print("number: ", random_number)
    break

import random
class Remote_control():
  def __init__(self, tv_status = "off", tv_sound = 0, channel_list = ["trt"], channel = "trt"):
    self.tv_status = tv_status
    self.tv_sound = tv_sound
    self.channel_list = channel_list
    self.channel = channel
  def tv_open(self):
    if (self.tv_status == "on"):
      print("tv is already on")
    else:
      print("tv is on")
      self.tv_status = "on"
  def tv_closed(self):
    if (self.tv_status == "off"):
      print("tv is already off")
    else:
      print("tv is off")
      self.tv_status = "off"
  def sound_settings(self):
    while True:
      answer = input("sound down: '<'\nsound up: '>'\nexit: '|'")
      if (answer == "<"):
        if (self.tv_sound != 0):
          self.tv_sound -= 1
          print("sound: ", self.tv_sound)
      elif (answer == ">"):
        if (self.tv_sound != 100):
          self.tv_sound += 1
          print("sound: ", self.tv_sound)
      else:
        print("sound updated!", self.tv_sound)
        break
  def add_channel(self, channel_name):
    self.channel_list.append(channel_name)
    print("added channel!")
  def random_channel(self):
    rando = random.randint(0, len(self.channel_list)-1)
    self.channel = self.channel_list[rando]
    print("current channel: ", self.channel)
  def __len__(self):
    return len(self.channel_list)
  def __str__(self):
    return "tv status: {}\n sound: {}\n channel list: {}\n current channel: {}\n ".format(self.tv_status, self.tv_sound, self.channel_list, self.channel)
control = Remote_control()
print("""
      1.Turn on tv
      2.Turn off tv
      3.Sound settings
      4.Add channel
      5.Number of channels
      6.Random channel
      7.Tv informations
      Enter 'q' for exit
      """) 
while True:
  action = input("select the action: ")
  if (action == "q"):
    break
  elif (action == "1"):
    control.tv_open()
  elif (action == "2"):
    control.tv_closed()
  elif (action == "3"):
    control.sound_settings()
  elif (action == "4"):
    channel_names = input("enter the channel names: ")
    channel_list = channel_names.split(",")
    for added in channel_list:
      control.add_channel(added)
  elif (action == "5"):
    print("number of channels: ", len(control))
  elif (action == "6"):
    control.random_channel()
  elif (action == "7"):
    print(control)
  else:
    print("invalid action!")
  
def fibonacci():
    a = 1
    b = 1
    yield a
    yield b  
    while True:
        a,b = b, a+b
        yield b 
for number in fibonacci():
    if (number> 100000):
        break
    print(number)
    
import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
html_icerik = response.content
soup = BeautifulSoup(html_icerik, "html.parser")
a = float(input("enter rating: "))
titles = soup.find_all("td", {"class": "titleColumn"})
ratings = soup.find_all("td", {"class": "ratingColumn imdbRating"})
for title, rating in zip(titles, ratings):
  title = title.text
  rating = rating.text
  title = title.strip()
  title = title.replace("/n", "")
  if (float(rating) > a):
    print("Movie Name: {} Movie Rating: {}".format(title,rating))