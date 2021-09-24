from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
for i in range(1,11):
    for x in range(1,7):
        robotArm.moveRight();
        robotArm.grab()   
        robotArm.moveLeft();
        robotArm.drop();
    for j in range(1):
        robotArm.moveRight();
        robotArm.moveRight();


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()