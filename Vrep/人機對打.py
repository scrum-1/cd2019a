import vrep
import sys, math
import keyboard
# child threaded script: 
# 內建使用 port 19997 若要加入其他 port, 在  serve 端程式納入
#simExtRemoteApiStart(19999)
  
vrep.simxFinish(-1)
  
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
KickBallV = 360  
Move_Minus =-0.1        
Move_Plus =0.1
n=1
R_KickBallVel = (math.pi/180)*KickBallV
B_KickBallVel = -(math.pi/180)*KickBallV
if clientID!= -1:
    print("Connected to remote server")
else:
    print('Connection not successful')
    sys.exit('Could not connect')

errorCode,Sphere_handle=vrep.simxGetObjectHandle(clientID,'Sphere',vrep.simx_opmode_oneshot_wait)
errorCode,P1_handle=vrep.simxGetObjectHandle(clientID,'P1',vrep.simx_opmode_oneshot_wait)
errorCode,A1_handle=vrep.simxGetObjectHandle(clientID,'A1',vrep.simx_opmode_oneshot_wait)
errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,B1_handle=vrep.simxGetObjectHandle(clientID,'B1',vrep.simx_opmode_oneshot_wait)
errorCode,P2_handle=vrep.simxGetObjectHandle(clientID,'P2',vrep.simx_opmode_oneshot_wait)
errorCode,A2_handle=vrep.simxGetObjectHandle(clientID,'A2',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)
errorCode,B2_handle=vrep.simxGetObjectHandle(clientID,'B2',vrep.simx_opmode_oneshot_wait)

if errorCode == -1:
    print('Can not find left or right motor')
    sys.exit()
def start():
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

def stop():
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

def pause():
    errorCode = vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)

def getballposition():
    errorCode,position_A1R=vrep.simxGetObjectPosition(clientID,A1_handle,-1,vrep.simx_opmode_oneshot)
    errorCode,position_S=vrep.simxGetObjectPosition(clientID,Sphere_handle,-1,vrep.simx_opmode_oneshot)
    A1v=position_S[1] - position_A1R[1]
    AA1v=position_S[2] - position_A1R[2]
    while True:
        if A1v <= 0 and AA1v <= 0.005:
            errorCode,position_A1R=vrep.simxGetObjectPosition(clientID,A1_handle,-1,vrep.simx_opmode_oneshot)
            errorCode,position_S=vrep.simxGetObjectPosition(clientID,Sphere_handle,-1,vrep.simx_opmode_oneshot)
            A1v =position_S[1]- position_A1R[1]
            AA1v =position_S[0] - position_A1R[0]
            vrep.simxSetJointTargetVelocity(clientID,R1_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
          
        elif A1v > 0 and AA1v <= 0.005:
            errorCode,position_A1R=vrep.simxGetObjectPosition(clientID,A1_handle,-1,vrep.simx_opmode_oneshot)
            errorCode,position_S=vrep.simxGetObjectPosition(clientID,Sphere_handle,-1,vrep.simx_opmode_oneshot)
            A1v =position_S[1]- position_A1R[1]
            AA1v =position_S[0] - position_A1R[0]
            vrep.simxSetJointTargetVelocity(clientID,R1_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
              
        elif A1v <= 0 and AA1v > 0.005:
            errorCode,position_A1R=vrep.simxGetObjectPosition(clientID,A1_handle,-1,vrep.simx_opmode_oneshot)
            errorCode,position_S=vrep.simxGetObjectPosition(clientID,Sphere_handle,-1,vrep.simx_opmode_oneshot)
            A1v =position_S[1]- position_A1R[1]
            AA1v =position_S[0] - position_A1R[0]
            vrep.simxSetJointTargetVelocity(clientID,R1_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
          
        elif A1v > 0 and AA1v > 0.005:
            errorCode,position_A1R=vrep.simxGetObjectPosition(clientID,A1_handle,-1,vrep.simx_opmode_oneshot)
            errorCode,position_S=vrep.simxGetObjectPosition(clientID,Sphere_handle,-1,vrep.simx_opmode_oneshot)
            A1v =position_S[1]- position_A1R[1]
            AA1v =position_S[0] - position_A1R[0]
            vrep.simxSetJointTargetVelocity(clientID,R1_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
            
        try:
            if keyboard.is_pressed('w'): 
                vrep.simxSetJointTargetVelocity(clientID,R2_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('x'):  
                vrep.simxSetJointTargetVelocity(clientID,R2_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('d'):  
                vrep.simxSetJointTargetVelocity(clientID,P2_handle,0.05,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('s'):
                vrep.simxSetJointTargetVelocity(clientID,P2_handle,0,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('a'):  
                vrep.simxSetJointTargetVelocity(clientID,P2_handle,-0.05,vrep.simx_opmode_oneshot_wait)
            else:
                pass
        except:
            break
            
        MMMB = A1v*2
        vrep.simxSetJointTargetVelocity(clientID,P1_handle,MMMB,vrep.simx_opmode_oneshot_wait)

vrep.simxSetJointTargetVelocity(clientID,R1_handle,0,vrep.simx_opmode_oneshot_wait)
vrep.simxSetJointTargetVelocity(clientID,P2_handle,0,vrep.simx_opmode_oneshot_wait)

start()
getballposition()
stop()
