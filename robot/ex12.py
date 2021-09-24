from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for i in range(1,20):
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur != "red":
        robotArm.drop()
        robotArm.moveRight()
    else:
        for i in range(1,10):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(1,10):
            robotArm.moveLeft()
    
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()