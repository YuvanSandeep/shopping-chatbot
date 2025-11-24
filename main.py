import time
print("Hello, I am a chatbot and I will ask you some questions for info, this won't be used for anything")
time.sleep(3)
name = input("What is your name?")
print("Hello", name)
Age = int(input ("What is your age?"))
Gender = input ("What is your gender?")
continent = input ("What continent do you live in?")
schoolwhat = input ("Do you still go to school?")
job = input ("What job/future job do you have?")
item_1 = input ("What is the first item you want to buy?")
if (Age > 4 and Age < 10):
    print ("I would suggest you buying a remote controlled car")
if (Age > 9 and Age < 19):
    print ("I'd suggest you buying a new gaming set")
if (Age > 18 and Age < 101):
    print ("I would suggest you buying a fitness band or a sweatband with something to start working out with or just some groceries for cooking")
if (job =="doctor" ):
    print ("I think you should buy a stethoscope")
if (job == "finance"):
    print ("I think you should buy a notebook to write stuff down")
if (job == "engineer"):
    print ("I think you should buy some tools or something that can help you inspect better")
if (schoolwhat == "yes"):
    print ("Maybe you should buy some pencils or some books and a pencil case")
if (continent == "africa" or continent =="australia"):
    print ("Buy some short sleeves or a handheld fan")
if (continent == "europe" or continent == "north america"):
    print ("Buy some jackets/coats and some sunscreen if it is summer")
if (continent == "asia" or continent == "south america"):
    print ("Buy a jacket and some short sleeves because it can be both ways in asia/south america")
if (Gender == "girl"):
    print ("Buy a Hairbrush please")
if (Gender == "boy"):
    print ("Buy a comb or some hair gel please")