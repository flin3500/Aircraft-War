# Aircraft_War
This is the game I have done when I learn python, all of these are create by Mac OS

### Preparation

1. Pycharm 2020.1( I think other vision is also fine)

![Screen Shot 2020-07-25 at 10.15.32 am](/Users/lin/Desktop/Screen Shot 2020-07-25 at 10.15.32 am.png)

2. Pygame 2.0.0  **You must install v2.0.0+ in oder to success **

There are two ways to install pygame

One: Terminal -> ```python3 -m pip install -U pygame==2.0.0.dev6 --user```

Two: Pycharm -> Preference -> Project -> Project Interpreter -> + ->search pygame -> specify v2.0.0+

Then, use `python3 -m pygame.examples.aliens` to check if it is install successfully, if sucessful, it will run a game on your laptop.

3. Mac OS Catalina v 10.15.5

In this project, all the thing is based on MacOS

4. The image folder

This is the folder contains all the images we need

<br>

### Step 1: Use pygame to create GUI

1.1 Game init and quit   *(LN_01)*

```python
import pygame

pygame.init()			#init 
print("Game Coding...")	#coding
pygame.quit()			#quit
```

1.2 Coordinates   *(LN_02)*

```pygame.Rect(x,y,weith,height)``` is used to create a rectangle.

Upper left corner  is the origin (0,0). We can set all object based on that origin.

1.3 Create main window  *(LN_03)*

```pygame.display```

| `pygame.display.set_mode((width,height),flags,depth)` | Initilize the window        |
| ----------------------------------------------------- | --------------------------- |
| `pygame.display.update()`                             | update the things in window |

<br>

### Step 2: Use image folder

1. Use   ```pygame.image.load()```  load the image
2. Use the windows object to use ```window.blit(image object,(width,height))``` method to allocate the image
3. Use```pygame.display.update()``` to update all the window and see the outcome



2.1 Create background  *(LN_04)*

2.2 Create heroplane  *(LN_05)*

