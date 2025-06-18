#ripped this from chat gpt, needed to understand how the axis work on the joystick
# now i understand:
#the axis on the right stick from top to bottom is Axis '3'
# right to left on the right stick is Axis '2'
#top to bottom on left stick is axis '1'
# left to right on the right stick is axis '0'

import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller connected.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Controller: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")

# Store previous values to detect changes
prev_axis_values = [0.0] * joystick.get_numaxes()
threshold = 0.05  # Ignore small noise

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check each axis for change
    for i in range(joystick.get_numaxes()):
        val = joystick.get_axis(i)
        prev_val = prev_axis_values[i]

        # Only print if changed significantly
        if abs(val - prev_val) > threshold:
            print(f"Axis {i}: {val}")
            prev_axis_values[i] = val

pygame.quit()
