from __future__ import print_function

import time
from sr.robot import *



R = Robot()
a_th = 1.5 # The threshold for controlling the linear distance
d_th = 0.4 # The threshold for controlling the orientation


#silverList = [] # a list to count the number of silver tokens grabbed and save their codes.
goldenList = [] # a list to count the number of golden tokens and save their codes.
goldenList2=[]


def drive(speed, seconds):
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0
	
	
def sign(a):
	if a < 0:
		return -1
	else:
		return 1
		
		
		
def turn(speed, seconds):
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = -speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0
	
	
	
	
def find_golden_token():

	dist=100
	for token in R.see() : # if the robot sees the token, it checks if it's golden and it has no silver box paired with it (not in list of golden boxes)
		if token.dist < dist and token.info.code not in goldenList:
			dist=token.dist
			rot_y=token.rot_y
			code_of_token=token.info.code
			print(token.info.code)
			
	if dist==100:
		return -1, -1, -1
	else:
		
		return dist, rot_y, code_of_token



def find_golden_token1():

	dist=100
	for token in R.see() : # if the robot sees the token, it checks if it's golden and it has no silver box paired with it (not in list of golden boxes)
	        
	        print("number is :",len(goldenList))
	      
	        if len(goldenList)==0:
	            print("test")
	            #R.release()
	            
		elif token.dist < dist  and token.info.code == goldenList[-2] and len(goldenList)!=0:
			dist=token.dist
			rot_y=token.rot_y
			code_of_token=token.info.code
			
	if dist==100:
		return -1, -1, -1
	else:
		
		return dist, rot_y, code_of_token






def golden_grabber(rot_y,dist,code_of_token):

    """This function works using the distance and orientation returned by the 
    function 'find_silver_token' and it tends to update the distatnce and the orientation of the 
    silver token each time using the functions turn and drive to reach the box. and also it is used to grab
    the token and append the list of silver tokens"""

    while(dist<0):
       #This loop works if the silver boxes are too far from the robot, so the loop makes the robot turn untill it finds a token.
        turn(-5,10)
        dist, rot_y, code_of_token = find_golden_token()
    while (rot_y >= a_th or rot_y<=-a_th) : #This loop tries to find the exact orientation of the silver box
        turn(sign(rot_y-a_th) * 10,0.001) #I used the sign to make the robot turn with the right orientation
        dist, rot_y,code_of_token = find_golden_token()
    while (dist >= d_th) : #This loop drives the robot to the golden token.
        drive(30,0.01)
        dist, rot_y, code_of_token = find_golden_token()
    #goldenList.append(code_of_token)
    print("Got you golden box number:",len(goldenList))
    R.grab()
    goldenList.append(code_of_token)
    turn(20,0.1)	




def go_to_golden_and_release(rot_y,dist,code_of_token):
    """This function works with the same principle of the function silver grabber, except 
    that it search for the nearest golden box and release the silver box near it """
    while(dist<0):
        turn(-5,0.01)
        dist, rot_y, code_of_token = find_golden_token1()
    while (rot_y >= a_th or rot_y<=-a_th) :
        turn(sign(rot_y-a_th) * 10,0.001)
        dist, rot_y, code_of_token= find_golden_token1()
    while (dist >= 1.5*d_th) :
        drive(40,0.01)
        dist, rot_y, code_of_token= find_golden_token1()
    R.release()
   
    print("Found you golden box number:",len(goldenList))
    drive(-30,0.8)


def main():

    while (len(goldenList)==0):
      
        """Let's start our task by finding the silver box using the following function"""
        dist, rot_y, code_of_token = find_golden_token()
        """This if statement to make the robot turn until it found a golden box"""
        if dist==-1:
            turn(10,0.1)
            continue
        
        golden_grabber(rot_y,dist,code_of_token)
        
        
        
        #goldenList.append(code_of_token)
        print(goldenList[0])
        R.release()
        turn(20,3)
        drive(10,3)
        
        
        

        
    while (len(goldenList)<6 and len(goldenList )!=0):
        """Let's start our task by finding the silver box using the following function"""
        print("test3")
        print(goldenList[0])
        dist, rot_y, code_of_token = find_golden_token()
        """This if statement to make the robot turn until it found a golden box"""
        if dist==-1:
            turn(10,0.1)
            continue
        
        golden_grabber(rot_y,dist,code_of_token)
        
        dist1, rot_y1, code_of_token1 = find_golden_token1()
        """Now we have the orientation and the distance of the closest golden box so we ask
        the robot to go and release the silver box near to it"""
        go_to_golden_and_release(rot_y1,dist1,code_of_token1)
        print("")		
    drive(-30,2)
    turn(20,0.5)
    print("Mission completed")




main()
