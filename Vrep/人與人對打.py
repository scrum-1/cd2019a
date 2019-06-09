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

errorCode,P1_handle=vrep.simxGetObjectHandle(clientID,'P1',vrep.simx_opmode_oneshot_wait)
errorCode,A1_handle=vrep.simxGetObjectHandle(clientID,'A1',vrep.simx_opmode_oneshot_wait)
errorCode,R1_handle=vrep.simxGetObjectHandle(clientID,'R1',vrep.simx_opmode_oneshot_wait)
errorCode,B1_handle=vrep.simxGetObjectHandle(clientID,'B1',vrep.simx_opmode_oneshot_wait)
errorCode,P2_handle=vrep.simxGetObjectHandle(clientID,'P2',vrep.simx_opmode_oneshot_wait)
errorCode,A2_handle=vrep.simxGetObjectHandle(clientID,'A2',vrep.simx_opmode_oneshot_wait)
errorCode,R2_handle=vrep.simxGetObjectHandle(clientID,'R2',vrep.simx_opmode_oneshot_wait)
errorCode,B2_handle=vrep.simxGetObjectHandle(clientID,'B2',vrep.simx_opmode_oneshot_wait)
#vrep.simxSetJointTargetVelocity(clientID,P1_handle,-6,vrep.simx_opmode_oneshot_wait)
vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
while True:
    try:
            if keyboard.is_pressed('w'): 
                errorCode = vrep.simxSetJointTargetVelocity(clientID,R1_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('x'):  
                errorCode = vrep.simxSetJointTargetVelocity(clientID,R1_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('a'):  
                errorCode = vrep.simxSetJointTargetVelocity(clientID,P1_handle,0.1,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('s'):  
                errorCode = vrep.simxSetJointTargetVelocity(clientID,P1_handle,0,vrep.simx_opmode_oneshot_wait)
                errorCode = vrep.simxSetJointTargetVelocity(clientID,R1_handle,0,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('d'):  
                errorCode =  vrep.simxSetJointTargetVelocity(clientID,P1_handle,-0.1,vrep.simx_opmode_oneshot_wait)
            if keyboard.is_pressed('8'): 
                errorCode = vrep.simxSetJointTargetVelocity(clientID,R2_handle,R_KickBallVel,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('2'):  
                errorCode = vrep.simxSetJointTargetVelocity(clientID,R2_handle,B_KickBallVel,vrep.simx_opmode_oneshot_wait) 
            elif keyboard.is_pressed('6'):  
                errorCode = vrep.simxSetJointTargetVelocity(clientID,P2_handle,0.1,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('5'):  
                errorCode = vrep.simxSetJointTargetVelocity(clientID,P2_handle,0,vrep.simx_opmode_oneshot_wait)
                errorCode = vrep.simxSetJointTargetVelocity(clientID,R2_handle,0,vrep.simx_opmode_oneshot_wait)
            elif keyboard.is_pressed('4'):  
                errorCode =  vrep.simxSetJointTargetVelocity(clientID,P2_handle,-0.1,vrep.simx_opmode_oneshot_wait)
            else:
                pass
    except:
            break

#vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)