RT1_Assignment #1
=================

This repository contains my solution for the first assignment of RT1 in which we were asked to make a robot grab golden boxes and place them near each other.

## Initialization

### The Grabber

The robot is equipped with a grabber, capable of picking up a token which is in front of the robot and within 0.4 metres of the robot's centre. To pick up a token, we call the `R.grab` method. The `R.grab` function returns `True` if a token was successfully picked up, or `False` otherwise.

```python
 R.grab()
```
To release the token we use the method:

```python
 R.release()
```

### Global variables:

<br>a_th : The threshold for controlling the linear distance. </br>
d_th : The threshold for controlling the orientation.

<br> silverList = [] : List contains the codes of silver boxes.</br>
goldenList = [] : List contains the codes of golden boxes.	

The code is composed of different functions that I created:

### Drive and Turn functions:

These two functions are the same of exercice 1, they're functions that make the robot drive forward with fixed speed or Turn with specific orientation.

## Initialization
- Initialize the robot and set threshold values for linear distance (`a_th`) and orientation (`d_th`).
- Create empty lists to store grabbed golden tokens (`goldenList`).

## Functions

### `drive(speed, seconds):`
Set linear velocity for the robot.

### `turn(speed, seconds):`
Set angular velocity for the robot.

# Golden Token Grabber Algorithm

This repository contains my solution for the first assignment of RT1 in which we were asked to make a robot grab golden boxes and place them near each other.

## Initialization
- Initialize the robot and set threshold values for linear distance (`a_th`) and orientation (`d_th`).
- Create empty lists to store grabbed golden tokens (`goldenList`).

## Functions

### `drive(speed, seconds):`
Set linear velocity for the robot.

### `turn(speed, seconds):`
Set angular velocity for the robot.

### `find_golden_token():`
    Find the closest golden token that has not been grabbed.
    ```python
        # Function to find the closest golden token
        def find_golden_token():
            dist = 100
            rot_y = -1
            code_of_token = -1
            for token in R.see():
                if token.dist < dist and token.info.code not in goldenList:
                    dist = token.dist
                    rot_y = token.rot_y
                    code_of_token = token.info.code
                    print(token.info.code)
            if dist == 100:
                return -1, -1, -1
            else:
                return dist, rot_y, code_of_token

                
### `find_golden_token1():`
 
           ```python
             # Function to find the closest golden token in the list of grabbed tokens
             def find_golden_token1():
                 dist = 100
                 rot_y = -1
                 code_of_token = -1
                 for token in R.see():
                     if token.dist < dist and token.info.code in goldenList:
                         dist = token.dist
                         rot_y = token.rot_y
                         code_of_token = token.info.code
                 if dist == 100:
                     return -1, -1, -1
                 else:
                     return dist, rot_y, code_of_token

### ' golden_grabber(rot_y, dist, code_of_token): '
  <pre>
    Grab the golden token using orientation and distance.
  </pre>
### 'go_to_golden_and_release(rot_y, dist, code_of_token):'
<pre>
     Move to the collected golden boxes and release the token.
</pre>

### 'Main Algorithm'
<pre>
     In the main() function:
     Search for the first golden token and grab it using golden_grabber.
     Release the grabbed token, turn, and drive to prepare for the next stage.
     Continue the loop until there are 6 golden tokens in goldenList.
     In each iteration:
     Find the closest free golden token using find_golden_token.
     Grab the golden token using golden_grabber.
     Find the collected golden boxes and release the token using go_to_golden_and_release.
     Complete the mission by driving backward and turning.
</pre>
      
     
