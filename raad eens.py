import random
randomding = random.randint(1, 999)
randomding = randomding + 1
score = 0 
print(randomding)
keer = int(input('hoeveel keer wil je spelen? '))
for i in range(1, 21):
    x = int(input("raad je getal? \n"))
    if randomding ==x:
        print("correct")
        vraag3 = input("wil je nog een keer spelen? ")
        score = score + 1
        if vraag3 =="nee":
            break
    if randomding > x:
        print("het getal is hoger")
        vraag = input("wil je het nog een keer proberen? \n")
        if vraag =="nee":
            break
    else:
        print("het getal is lager?")
        vraag2 = input("wil je nog een keer proberen? ")
        if vraag2 == "nee":
            break
    x2 = randomding - x
    if x2 >= -50 <= 50:
        print("je bent warm")
    if x2 >= -20 <= 20:
        print("je bent heel warm")
    

print("je score is", score)


        
            

