from unittest import TestCase
import pygame


class Test(TestCase):
    def test_con_movement(self):
        pygame.init()
        pygame.joystick.init()
        count = pygame.joystick.get_count()
        if count == 0:
            print("No controller connected.")
            self.fail()

        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Controller: {joystick.get_name()}")
        print(f"Number of axes: {joystick.get_numaxes()}")

        while True:
            for i in range(joystick.get_numaxes()):
                print("boo",joystick.get_axis(i))

        # while joystick.get_axis(1) ==  0.0:
        #     pass
        # print('kaboom')
        # self.assertGreater(joystick.get_numaxes(),4)
        # up_down=0
        # left_right=1
        # self.assertGreater(joystick.get_axis(up_down),0)
        # self.assertGreater(joystick.get_axis(left_right),0)
        #
        # prev_axis_values = [0.0] * joystick.get_numaxes()
        # threshold = 0.05  # Ignore small noise
        #
        # print(f"Controller: {joystick.get_name()}")
        # print(f"Number of axes: {joystick.get_numaxes()}")
        #
        # # Store previous values to detect changes
        # prev_axis_values = [0.0] * joystick.get_numaxes()
        # threshold = 0.05  # Ignore small noise
        #
        # running = True
        # while running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             running = False
        #
        #     # Check each axis for change
        #     for i in range(joystick.get_numaxes()):
        #         val = joystick.get_axis(i)
        #         prev_val = prev_axis_values[i]
