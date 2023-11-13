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
