# Ask user for the direction
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()
# determine which message to display
if direction == 'up':
    print("I am painting in the upward direction!")
elif direction == 'down':
    print("I am painting in the downward direction!")
elif direction == 'left':
    print("I am painting in the leftward direction!")
elif direction == 'right':
    print("I am painting in the rightward direction!")
else:
    print("i am not sure in which direction i am painting in !")