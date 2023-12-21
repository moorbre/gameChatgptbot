import pygame


## arrow keys not working
def gamepad_listener():
    # Initialize pygame
    pygame.init()

    # Check for available gamepads
    if not pygame.joystick.get_count():
        print("No gamepad found.")
        return

    # Initialize the first gamepad
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print("Gamepad connected: {}".format(joystick.get_name()))

    try:
        # Run the gamepad event loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                # Check for gamepad events
                if event.type == pygame.JOYAXISMOTION:
                    print("Axis {} moved to {}".format(event.axis, joystick.get_axis(event.axis)))
                elif event.type == pygame.JOYBUTTONDOWN:
                    print("Button {} pressed".format(event.button))
                elif event.type == pygame.JOYBUTTONUP:
                    print("Button {} released".format(event.button))

    except KeyboardInterrupt:
        print("Gamepad listener terminated.")

gamepad_listener()