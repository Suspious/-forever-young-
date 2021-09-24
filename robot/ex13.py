from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
cijfer = 1
for i in range(1,8):
    robotArm.grab()
    for j in range(1,cijfer):
        robotArm.moveRight()
    robotArm.drop()
    cijfer = cijfer + 1 
    for k in range(1,cijfer): 
        robotArm.moveLeft()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()