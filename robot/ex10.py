from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
cijfer = 10
for i in range(1,6):
    robotArm.grab()
    for x in range(1,cijfer):
        robotArm.moveRight()
    robotArm.drop()
    cijfer = cijfer - 1 
    for i in range(1,cijfer):
        robotArm.moveLeft()
    cijfer = cijfer - 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
