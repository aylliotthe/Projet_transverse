from homescreen import HomeScreen

if __name__ == "__main__":
    screen = HomeScreen()

    while screen:
        screen = screen.run()

        if screen is True:
            screen = HomeScreen()

