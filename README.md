A Bot that automates Raiding in a game call Bit Heroes.

I couldn't get any of the bot on GitHub to work on my machine so I created one using Python.

The bot functions based on coordinates of certain objects in game. During the raid, it will take a screenshot every 2 seconds to detect:

1, if any familiars appear. If so, the bot will try to persuade them using gold
2, if any member of the raid team dies, the bot will try to revive them using medium potions

Assumptions:

All coordinates assume a screen resolution of 1920x1080, and Chrome maximized with the Bookmarks Toolbar enabled.
Game must be in cinematic mode on Kongregate website and scroll all the way up. This is to ensure all coordinates are correct.

Requirements:

1, Python installed with OpenCV, pyautogui, numpy, mss
2, Run the run.py

Future Updates:

I will try to clean up the code and add more functionalities when I have time. But for now this bot satisfies my gaming need.
