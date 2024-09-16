class Config:
    """
    Application configuration settings

    Attributes:
        fps: maximum allowed frames per second
        width: application GUI window width
        height: application GUI window height
        acc: player's acceleration coefficient 
        fric: player's friction coefficient
    """
    fps = 60

    # Screen Information
    width = 360
    height = 640

    # Movement
    acc = 1.2
    fric = -0.10
