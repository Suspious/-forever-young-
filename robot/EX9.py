from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
for i in range(1,5):
    for i in range(1,5):
        robotArm.grab()
        for j in range(1,7):
            robotArm.moveRight()
        robotArm.drop()
        for k in range(1,6):
            robotArm.moveLeft()
    for l in range(1,5):
        robotArm.moveLeft()
        
        
# Na jouw code wachten tot het sluiten van de window
robotArm.wait();