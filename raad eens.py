import random
randomding = random.randint(1, 9)
randomding = randomding + 1
score = 0 
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

print("je score is", score)


        
            

