# Conway's Game of Life - Handheld COLOURED Version

Source: https://www.instructables.com/Conways-Game-of-Life-Handheld-COLOURED-Version/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

I'm back again with a new and improved version of my [Conway's Game of Life - Handheld Version](https://www.instructables.com/Conways-Game-of-Life-Handheld-Version-Powered-by-A/) This version has a number of improvements including, coloured screen, more games, different cell sizes and a lot cheaper to make! See below for the full game overview

Instead of using a Adafruit Trinket M0 (which are quite expensive), I've used a Raspberry Pi Pico Zero (which are cheap as chips!). I've also used a coloured TFT screen which are also inexpensive and gives the held held game a heap more options to play around with.

For those wondering what the hell is Conway's Game of Life - here's a description I used in my last build

The Game of Life is a cellular automation created by mathematician John Conway. It's what is known as a zero player game, meaning that its evolution and game play is determined by its initial state and requires no further input. You interact with the Game of Life by creating an initial configuration and observing how it evolves.

The game itself is based on a few, simple, mathematical rules consisting of a grid of cells that can either live, die or multiply. When the game is run, the cells can give the illusion that they are alive which is what makes this game so interesting.

There are actually many types of cellular automation and I have included some in this build.

Here is what you get in this updated hand held, coloured version. see the last step for a more detailed runthrough:

Main Menu Navigation

1. UP/DOWN: Navigate menu options
2. A: Select menu item
3. B: Go back to previous menu

Color Modes

1. All game modes support color! Press UP + DOWN together to toggle.

Game Rules

1. Hold button B down for 2 seconds in any game to bring up the rules for that game

Cell Size

1. There are 4 different cell sizes, from tiny to Large. Whist in a game, press left to change the size of the cell

Tools

Tools Menu Breakdown

1. Sound: ON/OFF - Toggles all game sounds on or off
2. Volume: Low/Medium/High
3. World: Toroid/Open - Controls what happens at the edges of the game board
4. Toroid = Wraparound edges (cells on the left edge are neighbors with cells on right edge, top wraps to bottom)
5. Open = Hard edges (cells at the edge have fewer neighbors, no wraparound)
6. Applies to ALL game modes (Conway's Life, Brian's Brain, Day & Night, Seeds, Cyclic CA)
7. Default: Toroid (wraparound)
8. Grid: ON/OFF - Shows/hides grid lines between cells
9. Only visible when cell size is 3px or larger (not on Tiny 2px cells)
10. Population: ON/OFF - Shows/hides the population counter overlay during gameplay
11. Gen: Current generation number
12. Pop: Current number of living cells
13. Trail Mode: ON/OFF - Shows fading trails behind cells as they die
14. In Mono mode = Gray fading trail (white → light gray → dark gray → black over 12 frames)
15. In Color mode = Colored fading trail using age-based colors

Game of Life Games

PRESET - Classic Patterns

1. Coe Ship - Spaceship that travels across the board
2. Gosper Glider Gun - Continuously spawns gliders
3. Diamond - 4-8-12 diamond pattern that evolves
4. Pulsar - Achim's p144 oscillator (period-144 pattern)
5. Glider - 56P6H1V0 spaceship pattern

RANDOM - Chaotic Evolution

SYMMETRIC - Creates symmetric initial patterns with different sizes

CUSTOM - Draw Your Own games

ALT GAMES - Alternative Cellular Automata

BRIAN'S BRAIN

DAY & NIGHT - Complementary rule set where birth/survival rules mirror each other.

SEEDS - "Exploding" automaton where cells live for exactly 1 generation.

CYCLIC CA - Multi-state cellular automaton where cells cycle through 6 states.

RULE EXPLORER - Create Custom Rules

Choose from 9 famous rule variations:

1. Conway (B3/S23) - Classic Game of Life
2. HighLife (B36/S23) - Like Conway, with replicators
3. Maze (B3/S12345) - Creates maze-like patterns
4. Coral (B3/S45678) - Grows coral-like structures
5. Seeds (B2/S) - Exploding patterns (same as Seeds mode)
6. Replicator (B1357/S1357) - Self-replicating patterns
7. 2x2 (B36/S125) - Stable 2x2 blocks common
8. NoDeath (B3/S012345678) - Cells never die once born
9. Diamoeba (B35678/S5678) - Diamond-shaped amoebas

Custom Rules - Create your own rules:

1. Navigation:
2. UP/DOWN: Switch between Birth and Survival rows
3. LEFT/RIGHT: Move cursor (0-8 neighbors)
4. A (short): Toggle number on/off
5. B (2 seconds): Start game with custom rules
6. B: Back to preset menu


## Supplies

![Supplies image 1](images/step01_01.jpg)

![Supplies image 2](images/step01_02.jpg)

![Supplies image 3](images/step01_03.jpg)

I have included a PDF of the parts list with links for all of the parts which you can find on this step in case you want to print it out etc. The PCB and front panel information can be found on the next step

PARTS:

Raspberry Pi Pico Zero X 1 - [Ali Express](https://www.aliexpress.com/w/wholesale-Raspberry-Pi-Pico-Zero.html?spm=a2g0o.home.search.0)

Charging & voltage step-up module X 1 - [Ali Express](https://www.aliexpress.com/item/1005005656423941.html?invitationCode=Z2RJS0ZlUjdWeXFvTWJjdCtIcWRwMmRJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&srcSns=sns_More&spreadType=socialShare&social_params=21926311787&bizType=ProductDetail&spreadCode=Z2RJS0ZlUjdWeXFvTWJjdCtIcWRwMmRJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&aff_fcid=32541398e7fa42cb8605beb5c28e25dc-1756343760169-03338-_mtlLJJx&tt=MG&aff_fsk=_mtlLJJx&aff_platform=default&sk=_mtlLJJx&aff_trace_key=32541398e7fa42cb8605beb5c28e25dc-1756343760169-03338-_mtlLJJx&shareId=21926311787&businessType=ProductDetail&platform=AE&terminal_id=626fe2c0a06b403387f3a97d33b76738&afSmartRedirect=y)

TFT Display 2.0 inch OLED LCD Drive IC ST7789V 240 X 320 X 1 - [Ali Express](https://www.aliexpress.com/w/wholesale-TFT-Display-2.0-inch-OLED-LCD-Drive-IC-ST7789V-240.html?spm=a2g0o.detail.search.0)

Battery -

Tactile Switch - [Ali Express](https://www.aliexpress.com/item/1005007076344493.html?invitationCode=Z2RJS0ZlUjdWeXBMbHJ1UzZEK2JNR2RJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&srcSns=sns_More&spreadType=socialShare&social_params=21926321283&bizType=ProductDetail&spreadCode=Z2RJS0ZlUjdWeXBMbHJ1UzZEK2JNR2RJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&aff_fcid=74110245658041378c13089ee305f490-1756352216155-08886-_mqidysZ&tt=MG&aff_fsk=_mqidysZ&aff_platform=default&sk=_mqidysZ&aff_trace_key=74110245658041378c13089ee305f490-1756352216155-08886-_mqidysZ&shareId=21926321283&businessType=ProductDetail&platform=AE&terminal_id=626fe2c0a06b403387f3a97d33b76738&afSmartRedirect=y)

On/Off Switch - [Ali Express](https://www.aliexpress.com/item/1005001517398513.html?spm=a2g0o.order_list.order_list_main.11.30491802K9cNyZ)

Buzzer -[Ali Express](https://www.aliexpress.com/w/wholesale-Buzzer-9032-5020-7525-9650-1230.html?spm=a2g0o.detail.search.0)

Micro Momentary Switch - [Ali Express](https://www.aliexpress.com/item/1005006956741903.html?spm=a2g0o.productlist.main.6.3714VtyYVtyYWA&aem_p4p_detail=202512012013053186468671941280003530927&algo_pvid=77e41f87-a64a-474c-910f-b4c95e360006&algo_exp_id=77e41f87-a64a-474c-910f-b4c95e360006-5&pdp_ext_f=%7B%22order%22%3A%228%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21AUD%213.23%212.75%21%21%2114.75%2112.54%21%402103129017646487854512530eb65b%2112000038853341475%21sea%21AU%21129764711%21X%211%210%21n_tag%3A-29919%3Bd%3Abadc4977%3Bm03_new_user%3A-29895&curPageLogUid=meKpY4AXI4Zs&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006956741903%7C_p_origin_prod%3A&search_p4p_id=202512012013053186468671941280003530927_2)

SMD Male Pin Headers - [Ali Express](https://www.aliexpress.com/item/1005008164411410.html?spm=a2g0o.order_list.order_list_main.47.30491802K9cNyZ)

M2 Screws - [Ali Express](https://www.aliexpress.com/item/1005007159750547.html?spm=a2g0o.order_list.order_list_main.23.30491802K9cNyZ)

M2 Spacers - [Ali Express](https://www.aliexpress.com/w/wholesale-spacer-M2-kit.html?spm=a2g0o.productlist.search.0)

Ribbon Wire - [Ali Express](https://www.aliexpress.com/item/1005007868158870.html?spm=a2g0o.productlist.main.5.c95f47bdP8JDuq&aem_p4p_detail=202601022008397380272548107300006821870&algo_pvid=2f9a9453-9b42-4b1b-85ab-ae9699014313&algo_exp_id=2f9a9453-9b42-4b1b-85ab-ae9699014313-4&pdp_ext_f=%7B%22order%22%3A%221354%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21AUD%212.27%212.22%21%21%2110.44%2110.23%21%402101ea8c17674133197688477ec307%2112000042656642090%21sea%21AU%21129764711%21X%211%210%21n_tag%3A-29919%3Bd%3Abadc4977%3Bm03_new_user%3A-29895&curPageLogUid=TGqy8VLWcAFl&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007868158870%7C_p_origin_prod%3A&search_p4p_id=202601022008397380272548107300006821870_5)


- [Parts List](pdfs/Parts List.pdf)

## Step 1: Getting the PCB & Front Panel Printed

![Step 1: Getting the PCB & Front Panel Printed image 1](images/step02_01.png)

![Step 1: Getting the PCB & Front Panel Printed image 2](images/step02_02.png)

![Step 1: Getting the PCB & Front Panel Printed image 3](images/step02_03.png)

We all have different levels of knowledge, so when it comes to a build like this I want to make sure that I'm providing enough information so anyone with basic soldering skills can make it. That includes ensuring there are instructions on how to get your own PCB's printed (which is super easy!).

So with that said, the first thing you will need to do is to get the front panel and PCB printed. I use [JLCPCB](https://jlcpcb.com/?from=VGS&utm_source=google&utm_medium=cpc&utm_campaign=14177189905&gad_source=1&gbraid=0AAAAABS1QqkiD3-WAMC-R-0N6a2KKPawu&gclid=CjwKCAjwwe2_BhBEEiwAM1I7sfAjCecAjlW7BgEzggjBf0WNDCA4-ZMBy2IrNS7NcwcA4naAhj0_2xoCA-4QAvD_BwE) (not affiliated) to get this done. The front panel is actually just a PCB without any components included! The front design is done in a program called [Inkscape](https://inkscape.org/) (available free) and the panel including the drilled holes is done in [Fusion 360](https://www.autodesk.com/products/fusion-360/personal) (also free!)

The files that you need to build your own Game of Life can be found in my [GitHub](https://github.com/lonesoulsurfer/Game_of_Life_Colour_Handheld) page. This includes the parts list, Gerber files for the PCB & front panel, schematic, Arduino script etc. Download the files to your computer

STEPS:

1. Send the Gerber files to a PCB manufacturer like [JLCPCB](https://jlcpcb.com/?from=VGBA&gad_source=1&gclid=CjwKCAiAjfyqBhAsEiwA-UdzJCxT2LUX1iS0CvS4HVuZlxetrU2JQNyu0nueQUivgEq7MzfoGlH54RoClQ8QAvD_BwE) who will print the PCB and front panel for you. Download all of the files from my [GitHub](https://github.com/lonesoulsurfer/Game_of_Life_Colour_Handheld)page to your computer and send the zipped Gerber files off to the PCB manufacturer of choice.
2. If you have no idea what any of the above means , then check out the Instructable I made on how to get your broads printed which can be found [here](https://www.instructables.com/How-to-Get-a-PCB-Printed-Using-Gerber-Files/).
3. NOTE: The manufacture will include an order number on both the PCB and front panel. It doesn't really matter where it is on the PCB but you don't want it on the front on the front panel!
4. Over at JLCPCB you can 'specify a location' once the Gerber files have been loaded so click this for the front panel and specify in the comment section that you want the order number on the back of the panel. The manufacturer will add it to the back where indicated.


## Step 2: Adding the Momentary Switches

![Step 2: Adding the Momentary Switches image 1](images/step03_01.jpg)

![Step 2: Adding the Momentary Switches image 2](images/step03_02.jpg)

![Step 2: Adding the Momentary Switches image 3](images/step03_03.jpg)

![Step 2: Adding the Momentary Switches image 4](images/step03_04.jpg)

The momentary switches used are SMD ones. Actually, I've ensured that all of the components on the PCB are not through hole ones. This keeps the back of the hand held game clean, stops you from getting pricked by sharp pins etc, and stops any potential grounding of pins that shouldn't be grounded. Plus it just looks a whole lot better!

STEPS:

1. You need to make sure that you add the ‘up’ and ‘down’ switches first. It just makes it easy if you do it in this order.
2. Add a little solder to one of the solder pads for the ‘up’ switch.
3. Place the switch on top of the pads and then heat up the solder to secure it into place. If it looks good, you can then secure the other 3 feet on the switch
4. Now do the same for the down switch
5. You can now add the left and right switches into place along with the A and B switches
6. There is one more momentary switch to add. This is a mirco momentary switch which is to be a rest for the raspberry Pi. I added this so you could easily reset the Pi and put it in Boot mode for when you want to update the sketch


## Step 3: Adding the Charging/boost Module

![Step 3: Adding the Charging/boost Module image 1](images/step04_01.jpg)

![Step 3: Adding the Charging/boost Module image 2](images/step04_02.jpg)

![Step 3: Adding the Charging/boost Module image 3](images/step04_03.jpg)

The charging and voltage booster module is a great little board. It allows you to add say a 3.6V battery like a mobile one, and you can increase the output voltage via a small potentiometer located on the board.

STEPS:

1. First, lets set the output voltage to 5V from the Charging & voltage booster module. Connect the module up to a power source (this could be mobile phone battery, variable power source or whatever you have around, as long as it is lower than 5V’s)
2. Now with a multimeter, check the voltage output. You need to try and get as close as possible to 5V’s so turn the potentiometer until you reach 5Vs.
3. Now you can add the module to the PCB. I added a little superglue to the bottom of the board to ensure it was secured into place
4. Add some solder to each of the solder points on the module and then add some wire from a resistor leg to each solder point.
5. Bend the wire down so it is touching the solder pad on the PCB and trim.
6. Add solder to the solder pad on the PCB and connect the wire to each. This will give you a good strong connection.


## Step 4: Adding the Raspberry Pi Zero

![Step 4: Adding the Raspberry Pi Zero image 1](images/step05_01.jpg)

![Step 4: Adding the Raspberry Pi Zero image 2](images/step05_02.jpg)

![Step 4: Adding the Raspberry Pi Zero image 3](images/step05_03.jpg)

The raspberry Pi Zero is another great little board. It has less GP pins then a normal Raspberry Pi Pico but the same amount of Ram. Plus, as I mentioned earlier, they are pretty cheap at about $4 each.

STEPS:

1. As everything is surface mount on the PCB, you need to first solder into place some SMD header pins. Add these to both sections on the PCB
2. Now, you can solder the Raspberry Pi Pico Zero into place on the header pins. Make sure that the USB connector is facing up.
3. If you wanted to, you could add small, male header pins to the Raspberry Pi so it is removeable


## Step 5: Adding the Rest of the Components to the PCB

![Step 5: Adding the Rest of the Components to the PCB image 1](images/step06_01.jpg)

![Step 5: Adding the Rest of the Components to the PCB image 2](images/step06_02.jpg)

![Step 5: Adding the Rest of the Components to the PCB image 3](images/step06_03.jpg)

![Step 5: Adding the Rest of the Components to the PCB image 4](images/step06_04.jpg)

Now you can go ahead and add the rest of the components to the PCB

STEPS:

1. Solder the toggle switch into place. You will note that this has 6 solder points. You can trim off the 3 solder points next to the actual switch if you want to and just solder this into place via the 3 at the back.
2. Next, lest solder the SMD male header pins for the screen. Now, you need to make sure that you solder these on straight or they won't line up with the female header pins on the screen.
3. Solder the buzzer into place.
4. To add the battery, first add some solder to the positive and negative solder points on the battery. Make sure your soldering iron is hot when doing this
5. Now add a resistor leg to each solder point and bend so they are lying flat with the battery.
6. Add a little superglue to the battery and glue into place.
7. Trim the wire if necessary and then solder onto the solder points on the PCB


## Step 6: Adding the Screen to the Front Panel

![Step 6: Adding the Screen to the Front Panel image 1](images/step07_01.jpg)

![Step 6: Adding the Screen to the Front Panel image 2](images/step07_02.jpg)

![Step 6: Adding the Screen to the Front Panel image 3](images/step07_03.jpg)

![Step 6: Adding the Screen to the Front Panel image 4](images/step07_04.jpg)

![Step 6: Adding the Screen to the Front Panel image 5](images/step07_05.jpg)

![Step 6: Adding the Screen to the Front Panel image 6](images/step07_06.jpg)

![Step 6: Adding the Screen to the Front Panel image 7](images/step07_07.jpg)

![Step 6: Adding the Screen to the Front Panel image 8](images/step07_08.jpg)

![Step 6: Adding the Screen to the Front Panel image 9](images/step07_09.jpg)

![Step 6: Adding the Screen to the Front Panel image 10](images/step07_10.jpg)

The screenis not directly connected to the PCB! It is first connected to the front panel using the M2 screws and spacers and then ribbon wire connects the screen to the PCB. Initially I wanted to have the screen connected via header pins but I couldn't get this to work due to the header pins being SMD and the sizing of the ones I had were wrong. I think I'll re-visit this part sometime and look at including ribbon cable connectors to both the PCB and bottom side of the front panel.

STEPS:

1. The TFT screen that I purchased had the header pins already soldered into place. You will need to remove these if yours is the same. Just heat up the solder on the pin and use a pair of pliers to pull out each of the pins. Make sure you remove as much solder from the top of the holes as well.
2. Place the screen against the front panel and secure it into place using some M2 X 8mm screws and nuts.
3. Now add a M2 X 6mm spacer onto each of the screws.
4. Add an M2 X 4mm screw to the holes in each corner of the front panel in each bottom corner. Don’t add nuts to these, just add a M2 X 8mm spacer to each one.
5. Now, to test fitment, place the PCB into place and push the screws through the holes in the PCB.
6. If the buttons fit ok, then you can now move onto attacheding the screen to the PCB.
7. I used computer ribbon wire to make the connections between the TFT screen and PCB. Trim the wire and tin the ends.
8. Now make small cuts between each wire - about 8 mm should be fine.
9. spread the wires out so they align with the solder points on the TFT screen.
10. Add some solder to the solderpoints on thescreen and then solder each wire to the solder points.
11. Now you can do the same thing for the solder points onthe PCB. To work out how long you need the wire, place the screen next to the PCB and then cut the wire where it meets up with the solder points on the PCB.
12. Now test fit the front panel and PCB again. You might need to squeeze the wire and bend it so it lays flat and doesn't add to much pressure to the inside components.

Now you are ready for testing so lets go and load up the Game of Life code to the Raspberry Pi


## Step 7: How to Upload to Raspberry Pi Zero

![Step 7: How to Upload to Raspberry Pi Zero image 1](images/step08_01.png)

In you haven't installed Arduino on your computer, then this is the first thing you should do. Just follow the below instructions which are straight forward and you wont have any issues with loading the code to the Raspberry Pi Zero.

STEPS:

1. Install Arduino IDE. Download from https://www.arduino.cc/en/software
2. Install version 2.0 or newer (recommended)
3. Install RP2040 Board Support
4. Open Arduino IDE
5. Go to File → Preferences
6. In "Additional Board Manager URLs", add:

https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json

1. Click OK
2. Go to Tools → Board → Boards Manager
3. Search for "pico"
4. Install "Raspberry Pi Pico/RP2040" by Earle F. Philhower
5. Install Required Libraries
6. Go to Sketch → Include Library → Manage Libraries and install:
7. Adafruit GFX Library
8. Adafruit ST7735 and ST7789 Library
9. Time to upload the code
10. Select the Board
11. Go to Tools → Board → Raspberry Pi RP2040 Boards
12. Select "Waveshare RP2040-Zero" (or "Raspberry Pi Pico" if Zero isn't listed)
13. Configure Settings. These need to be set under tools befoe youupload the sketch
14. Tools → CPU Speed: 133 MHz (default)
15. Tools → Optimize: Small (-Os) (default)
16. Tools → USB Stack: "Pico SDK"
17. Connect Your Board to the computer
18. Plug USB cable into RP2040-Zero
19. Board should appear as a COM/serial port
20. Select Port
21. Go to Tools → Port
22. Select the port that appears (usually shows as "RP2040" or similar)
23. Click the Upload button (right arrow icon)
24. Wait for "Done uploading" message


## Step 8: Attaching the PCB & Front Panel Together

![Step 8: Attaching the PCB & Front Panel Together image 1](images/step09_01.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 2](images/step09_02.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 3](images/step09_03.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 4](images/step09_04.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 5](images/step09_05.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 6](images/step09_06.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 7](images/step09_07.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 8](images/step09_08.jpg)

![Step 8: Attaching the PCB & Front Panel Together image 9](images/step09_09.jpg)

Once the code is loaded, it’s then time to connect the front panel and PCB. Don't worry, once the front panel is connected into place, you can still access the Raspberry Pi

STEPS:

1. Make sure that the front panel and PCB are correctly pushed together with everything lining-up right.
2. Now you can add a 4mm M2 screw to each of the holes in the PCB and screw them into the M2 spacers.
3. That’s it – you have now completed your very own Game of Life – Handheld game console


## Step 9: How to Use the Handheld Game of Life Coloured Version

![Step 9: How to Use the Handheld Game of Life Coloured Version image 1](images/step10_01.jpg)

![Step 9: How to Use the Handheld Game of Life Coloured Version image 2](images/step10_02.jpg)

Conway's Game of Life - Complete User Guide

Main Menu Navigation

1. UP/DOWN: Navigate menu options
2. A: Select menu item
3. B: Go back to previous menu

During Gameplay

1. UP: Increase speed (faster generations)
2. DOWN: Decrease speed (slower generations)
3. LEFT: Change cell size (Tiny → Small → Normal → Large)
4. RIGHT: ReB/Regenerate current pattern
5. UP + DOWN (together): Toggle COLOR/MONO mode
6. B (short press): Return to menu
7. B (2 second press): Show/hide game rules overlay

RESET Button (hold 2 seconds): Enter bootloader mode for updates

Edit Mode (Custom games)

1. D-Pad: Move cursor
2. A (short press): Toggle cell on/off
3. B (2 second press): Start game
4. B: Return to menu

Tools

Tools Menu Breakdown

1. Sound: ON/OFF - Toggles all game sounds on or off
2. Volume: Low/Medium/High
3. World: Toroid/Open - Controls what happens at the edges of the game board
4. Toroid = Wraparound edges (cells on the left edge are neighbors with cells on right edge, top wraps to bottom)
5. Open = Hard edges (cells at the edge have fewer neighbors, no wraparound)
6. Applies to ALL game modes (Conway's Life, Brian's Brain, Day & Night, Seeds, Cyclic CA)
7. Default: Toroid (wraparound)
8. Grid: ON/OFF - Shows/hides grid lines between cells
9. Only visible when cell size is 3px or larger (not on Tiny 2px cells)
10. Population: ON/OFF - Shows/hides the population counter overlay during gameplay
11. Gen: Current generation number
12. Pop: Current number of living cells
13. Trail Mode: ON/OFF - Shows fading trails behind cells as they die
14. In Mono mode = Gray fading trail (white → light gray → dark gray → black over 12 frames)
15. In Color mode = Colored fading trail using age-based colors

Main Menu Options

PRESET - Classic Patterns

1. Coe Ship - Spaceship that travels across the board
2. Gosper Glider Gun - Continuously spawns gliders
3. Diamond - 4-8-12 diamond pattern that evolves
4. Pulsar - Achim's p144 oscillator (period-144 pattern)
5. Glider - 56P6H1V0 spaceship pattern

RANDOM - Chaotic Evolution

1. Unpredictable patterns emerge
2. May stabilize into oscillators
3. May die out completely
4. Game shows statistics when it stabilizes or dies

SYMMETRIC - Creates symmetric initial patterns with different sizes

CUSTOM - Draw Your Own

1. Step 1: Choose Cell Size
2. Tiny (2px cells): 160x120 grid
3. Small (3px cells): 106x80 grid
4. Normal (4px cells): 80x60 grid
5. Large (8px cells): 40x30 grid
6. Step 2: Edit Mode
7. Red crosshair shows cursor position
8. Cursor blinks at 4Hz for visibility
9. White cells = alive, Black = dead
10. Move with D-pad, toggle cells with B
11. Step 3: Run
12. Hold B for 2 seconds to start
13. While running, hold B for 800ms to return to edit mode
14. Press B to return to menu

ALT GAMES - Alternative Cellular Automata

1. BRIAN'S BRAIN
2. Small: Compact symmetric cluster
3. Medium: Larger symmetric pattern (35% density)
4. Large: Very large sparse pattern (18% density)
5. Random: Scattered center-weighted distribution
6. Custom: Draw your own pattern
7. DAY & NIGHT- Complementary rule set where birth/survival rules mirror each other.
8. Very stable, creates intricate patterns
9. Day/Night metaphor in color mode
10. Often runs indefinitely
11. SEEDS - "Exploding" automaton where cells live for exactly 1 generation.
12. Random: Auto-generated 4-way symmetric pattern
13. Custom: Draw your own (choose cell size first)
14. CYCLIC CA - Multi-state cellular automaton where cells cycle through 6 states.
15. VrtclSym: Vertical mirror symmetry
16. 4WayRot: 4-way rotational symmetry
17. Random: Random pattern type and size

RULE EXPLORER - Create Custom Rules

1. Choose from 9 famous rule variations:
2. Conway (B3/S23) - Classic Game of Life
3. HighLife (B36/S23) - Like Conway, with replicators
4. Maze (B3/S12345) - Creates maze-like patterns
5. Coral (B3/S45678) - Grows coral-like structures
6. Seeds (B2/S) - Exploding patterns (same as Seeds mode)
7. Replicator (B1357/S1357) - Self-replicating patterns
8. 2x2 (B36/S125) - Stable 2x2 blocks common
9. NoDeath (B3/S012345678) - Cells never die once born
10. Diamoeba (B35678/S5678) - Diamond-shaped amoebas
11. Custom Rules- Create your own rules:
12. Navigation:
13. UP/DOWN: Switch between Birth and Survival rows
14. LEFT/RIGHT: Move cursor (0-8 neighbors)
15. B (short): Toggle number on/off
16. B (2 seconds): Start game with custom rules
17. B: Back to preset menu

How It Works:

1. Birth row: Select how many neighbors cause birth (0-8)
2. Survival row: Select how many neighbors keep cell alive (0-8)
3. Example: Conway's Life is B3 (birth on 3) / S23 (survive on 2 or 3)

Color Modes

1. All game modes support color! Press UP + DOWN together to toggle.


## Downloads

- [Parts List](pdfs/Parts List.pdf)

---
*46 images archived*
