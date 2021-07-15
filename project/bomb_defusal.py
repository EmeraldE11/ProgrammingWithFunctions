import math, random, time


"""REMEMBER TO ADD TRY & EXCEPT CODE"""













def main():
    """configure bomb, present tutorial prompts, show where to find manual,
    define bomb characteristics, set and run live timer(if possible at all)
    (((create strike counter??? or one strike fail???)))"""

    modules = int(input("How many modules?"))


    print("Enter starting instructions")



    t = input("Enter the time in seconds: ")




    bomb(modules, t)

    # set win and lose prompts and conditions


def wires():
    """randomly decide how many wires (3-5), set each a random color, create priority
    list of which wire to cut position wise based on color count (likely organize
    wire position by color to avoid too much complexity)"""

    print("WIRE MODULE")

    # set win and lose conditions


def scrambler():
    """DESCRIPTION: A list of passwords can provide the win condition, but the word will be
    scrambled, and must be unscrambled in order for the win condition to be met.
    Will be made by creating two corresponding lists, one of the scrambled word, the other
    of the correct answer."""

    print("SCRAMBLER MODULE")

def color_text():
    """POSSIBLE IDEA, UNSURE IF ABLE TO CREATE
    a word will be displayed, the word will describe a color, but will also be displayed
    as a different color. User must input the color the word is displayed in, not
    the written prompt. multiple stages"""

    print("COLOR TEXT MODULE")

def binary():
    """displays an a letter or number in binary (ASCII as conversion), and user must
    input the correct corresponding character
    (((unsure whether to just use numbers or include ASCII)))"""

    print("BINARY MODULE")

def speed_button():
    """displays a character, user must replicate the display quickly. Displays
    a starting prompt to avoid user being caught unaware. Multiple stages
    (((Dependent on whether live timer is possible)))"""

    print("SPEED BUTTON MODULE")

def bomb (modules, time):
    
    countdown(int(time))

    option_list = ["wires","scrambler","color_text","binary","speed_button"]


    for _ in range(modules):
        challenge = random.choice(option_list)

        if challenge == "wires":
            wires()
        elif challenge == "scrambler":
            scrambler()
        elif challenge == "color_text":
            color_text()
        elif challenge == "binary":
            binary()
        elif challenge == "speed_button":
            speed_button()


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print("BOOM!!! You failed.")

main()