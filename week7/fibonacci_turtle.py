from turtle import *

# Function returns list containing fibonacci sequence
def make_fibonacci(N):
    fib_list = [1, 1]
    for i in range(1, N - 1): 
        fib_list.append(fib_list[i] + fib_list[i - 1])
    return fib_list   

# Function takes a list and draws it like a staircase using turtle
def draw_list(my_list):
    color('red', 'yellow') # (Line color, Fill color)
    
    begin_fill() # Keep track of region you want to fill
    forward(10) # Move turtle forward a bit

    # Now we draw the list
    for num in my_list:
        left(90)# Turn upward
        forward(num) # Walk up a distance given by the number
        right(90) # Turn right
        forward(10) # Move a bit        
    
    end_fill() # Finished drawing
    
my_list = make_fibonacci(20)
draw_list(my_list)

# Just to check the fibonacci function
print(", ".join(map(str , my_list)))
