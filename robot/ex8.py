from RobotArm import RobotArm;robotArm = RobotArm('exercise 8');
robotArm.moveRight();
for i in range(7):
    for k in range(8):
        robotArm.grab();
    for k in range(8):
            robotArm.moveRight();
    robotArm.drop() 
    for j in range(1,9):
            robotArm.moveLeft();
robotArm.wait();