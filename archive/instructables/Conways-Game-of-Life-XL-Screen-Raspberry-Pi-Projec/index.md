# Conway's Game of Life XL Screen - Raspberry Pi Project

Source: https://www.instructables.com/Conways-Game-of-Life-XL-Screen-Raspberry-Pi-Projec/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

![Intro 6](images/intro_06.jpg)

I'm back again with a new and improved version of my [Conway's Game of Life Coloured Version](https://www.instructables.com/Conways-Game-of-Life-Handheld-COLOURED-Version/). This biggest and most obvious improvement is the size of the TFT screen. The Game of Life is meant to be played on a large field and this screen measures 3.5" compared to 2" which is what I used in the last coloured screen build.

For those wondering what the hell is Conway's Game of Life - here's a description I used in my last build

The Game of Life is a cellular automation created by mathematician John Conway. It's what is known as a zero player game, meaning that its evolution and game play is determined by its initial state and requires no further input. You interact with the Game of Life by creating an initial configuration and observing how it evolves.

The game itself is based on a few, simple, mathematical rules consisting of a grid of cells that can either live, die or multiply. When the game is run, the cells can give the illusion that they are alive which is what makes this game so interesting.

So what do you get in this build?

My Game of Life Colour Arcade is a feature-rich cellular automaton and arcade gaming console built on a Raspberry Pi Pico (RP2040) with a 3.5" 480×320 colour TFT display and six buttons.

At its core is Conway's Game of Life (GOL), but the project goes far beyond the classic GOL— it includes over a dozen simulation modes and 13 preset patterns, from iconic spaceships like the Coe Ship and MWSS to methuselahs like Acorn and R-Pentomino, glider guns, and oscillators. A custom edit mode lets you draw your own starting patterns cell by cell.

Beyond Conway's rules, the device runs six alternative cellular automata: Day & Night, Seeds, Brian's Brain, Cyclic CA, Wireworld, and Langton's Ant, as well as Wolfram's 1D elementary automata with all 255 rules. A GOL Rule Explorer lets you define custom birth and survival conditions and watch them evolve in real time.

Visual features include age-based colour gradients, soft fade trails, grid overlay, a population counter, and three cell sizes. Settings like brightness, speed, and sound are all adjustable in-game.

On top of all the simulations, the device doubles as a mini arcade cabinet with three games — a Star Wars game of my own design, Breakout Beyond, and Gyruss — all navigated from a clean scrolling menu system.


## Supplies

![Supplies image 1](images/step01_01.jpg)

![Supplies image 2](images/step01_02.jpg)

![Supplies image 3](images/step01_03.jpg)

![Supplies image 4](images/step01_04.jpg)

![Supplies image 5](images/step01_05.jpg)

![Supplies image 6](images/step01_06.jpg)

![Supplies image 7](images/step01_07.jpg)

![Supplies image 8](images/step01_08.jpg)

I have included a PDF of the parts list with links for all of the parts which you can find on this step in case you want to print it out etc. Unlike the last build, I have used more through hole components. Firstly, to make it easier to build, and second, I have included a back to this now which covers the solder joints.

The PCB and front panel information can be found on the next step

PARTS:

Raspberry Pi Pico Zero X 1 - [Ali Express](https://www.aliexpress.com/w/wholesale-Raspberry-Pi-Pico-Zero.html?spm=a2g0o.home.search.0)

Charging & voltage step-up module X 1 - [Ali Express](https://www.aliexpress.com/item/1005005656423941.html?invitationCode=Z2RJS0ZlUjdWeXFvTWJjdCtIcWRwMmRJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&srcSns=sns_More&spreadType=socialShare&social_params=21926311787&bizType=ProductDetail&spreadCode=Z2RJS0ZlUjdWeXFvTWJjdCtIcWRwMmRJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&aff_fcid=32541398e7fa42cb8605beb5c28e25dc-1756343760169-03338-_mtlLJJx&tt=MG&aff_fsk=_mtlLJJx&aff_platform=default&sk=_mtlLJJx&aff_trace_key=32541398e7fa42cb8605beb5c28e25dc-1756343760169-03338-_mtlLJJx&shareId=21926311787&businessType=ProductDetail&platform=AE&terminal_id=626fe2c0a06b403387f3a97d33b76738&afSmartRedirect=y)

TFT Display 3.5inch ST7796S/ST7796U LCD Display 1 - [Ali Express](https://www.aliexpress.com/item/1005007090411446.html?spm=a2g0o.order_list.order_list_main.11.6e0a1802Vh7xOd)

Battery - I like to recycle [old mobile batteries](https://www.instructables.com/Use-Old-Mobile-Batteries-to-Power-Anything-Almost/) on these builds. You can also buy them and this one would work fine - [Ali Express](https://www.aliexpress.com/item/1005007768846321.html?spm=a2g0o.productlist.main.27.37e80CxJ0CxJos&algo_pvid=04ff8e46-fd07-48df-87fe-3ba663b46c33&algo_exp_id=04ff8e46-fd07-48df-87fe-3ba663b46c33-26&pdp_ext_f=%7B%22order%22%3A%22191%22%2C%22spu_best_type%22%3A%22price%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21AUD%2112.46%2111.59%21%21%2160.02%2155.83%21%4021030a6217725876016324977e8463%2112000042141150414%21sea%21AU%21129764711%21X%211%210%21n_tag%3A-29919%3Bd%3Abadc4977%3Bm03_new_user%3A-29895&curPageLogUid=MjolbnGyNA4R&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005007768846321%7C_p_origin_prod%3A)

Momentary switches X 6 - [Ali Express](https://www.aliexpress.com/item/4000550502648.html?spm=a2g0o.order_list.order_list_main.23.9d7a1802AofMHf)

On/Off Switch X 2 - [Ali Express](https://www.aliexpress.com/item/32828124825.html?invitationCode=U0ZjejE5SDZUR3Rvd3A4dlNzTHhPMmRJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&srcSns=sns_More&spreadType=socialShare&social_params=21930568662&bizType=ProductDetail&spreadCode=U0ZjejE5SDZUR3Rvd3A4dlNzTHhPMmRJWDI2Qmpid1BLbVJRSE91aHMvTWpmdlBzNkVmWTlBPT0&aff_fcid=78cd7743d6d84c87a62a111f31d5ed0d-1756352449635-03501-_mMmygFX&tt=MG&aff_fsk=_mMmygFX&aff_platform=default&sk=_mMmygFX&aff_trace_key=78cd7743d6d84c87a62a111f31d5ed0d-1756352449635-03501-_mMmygFX&shareId=21930568662&businessType=ProductDetail&platform=AE&terminal_id=626fe2c0a06b403387f3a97d33b76738&afSmartRedirect=y)

Buzzer - [Ali Express](https://www.aliexpress.com/w/wholesale-9042-buzzer.html?spm=a2g0o.detail.search.0)

Micro Momentary Switch - [Ali Express](https://www.aliexpress.com/item/1005006956741903.html?spm=a2g0o.productlist.main.6.3714VtyYVtyYWA&aem_p4p_detail=202512012013053186468671941280003530927&algo_pvid=77e41f87-a64a-474c-910f-b4c95e360006&algo_exp_id=77e41f87-a64a-474c-910f-b4c95e360006-5&pdp_ext_f=%7B%22order%22%3A%228%22%2C%22eval%22%3A%221%22%2C%22fromPage%22%3A%22search%22%7D&pdp_npi=6%40dis%21AUD%213.23%212.75%21%21%2114.75%2112.54%21%402103129017646487854512530eb65b%2112000038853341475%21sea%21AU%21129764711%21X%211%210%21n_tag%3A-29919%3Bd%3Abadc4977%3Bm03_new_user%3A-29895&curPageLogUid=meKpY4AXI4Zs&utparam-url=scene%3Asearch%7Cquery_from%3A%7Cx_object_id%3A1005006956741903%7C_p_origin_prod%3A&search_p4p_id=202512012013053186468671941280003530927_2)

Male Pin Headers - [Ali Express](https://www.aliexpress.com/w/wholesale-pin-headers-single-row.html?spm=a2g0o.productlist.search.0)

Low profile female pin headers - [Ali Express](https://www.aliexpress.com/item/1005004122312694.html?spm=a2g0o.order_list.order_list_main.17.e1b71802izp4AU)

M2 Screws - [Ali Express](https://www.aliexpress.com/item/1005007159750547.html?spm=a2g0o.order_list.order_list_main.23.30491802K9cNyZ)

M2 Spacers - [Ali Express](https://www.aliexpress.com/w/wholesale-spacer-M2-kit.html?spm=a2g0o.productlist.search.0)


- [Parts List](pdfs/Parts List.pdf)

## Step 1: Getting the PCB & Front + Back Panels Printed

![Step 1: Getting the PCB & Front + Back Panels Printed image 1](images/step02_01.jpg)

![Step 1: Getting the PCB & Front + Back Panels Printed image 2](images/step02_02.jpg)

![Step 1: Getting the PCB & Front + Back Panels Printed image 3](images/step02_03.png)

![Step 1: Getting the PCB & Front + Back Panels Printed image 4](images/step02_04.png)

![Step 1: Getting the PCB & Front + Back Panels Printed image 5](images/step02_05.png)

We all have different levels of knowledge, so when it comes to a build like this I want to make sure that I'm providing enough information so anyone with basic soldering skills can make it. That includes ensuring there are instructions on how to get your own PCB's printed (which is super easy!).

So with that said, the first thing you will need to do is to get the front panel and PCB printed. I use [JLCPCB](https://jlcpcb.com/?from=VGS&utm_source=google&utm_medium=cpc&utm_campaign=14177189905&gad_source=1&gbraid=0AAAAABS1QqkiD3-WAMC-R-0N6a2KKPawu&gclid=CjwKCAjwwe2_BhBEEiwAM1I7sfAjCecAjlW7BgEzggjBf0WNDCA4-ZMBy2IrNS7NcwcA4naAhj0_2xoCA-4QAvD_BwE) (not affiliated) to get this done. The front and back panel are actually just PCB's without any components included! The design on the panels is done in a program called [Inkscape](https://inkscape.org/) (available free) and the actual panel itself (the outline, drilled holes etc) is done in [Fusion 360](https://www.autodesk.com/products/fusion-360/personal) (also free for now...)

The files that you need to build your own Game of Life can be found in my [GitHub](https://github.com/lonesoulsurfer/Conways_Game_of_Life__Large_Screen) page. This includes the parts list, Gerber files for the PCB & front panel, schematic, Code etc. Download all the files to your computer

STEPS:

- Download all of the files from my [GitHub](https://github.com/lonesoulsurfer/Conways_Game_of_Life__Large_Screen) page to your computer and send the zipped Gerber files off to the PCB manufacturer of choice such as [JLCPCB](https://jlcpcb.com/?from=VGBA&gad_source=1&gclid=CjwKCAiAjfyqBhAsEiwA-UdzJCxT2LUX1iS0CvS4HVuZlxetrU2JQNyu0nueQUivgEq7MzfoGlH54RoClQ8QAvD_BwE) who will print the PCB and front panel for you.
- If you have no idea what any of the above means , then check out the Instructable I made on how to get your broads printed which can be found [here](https://www.instructables.com/How-to-Get-a-PCB-Printed-Using-Gerber-Files/).


## Step 2: A Note on Changes to Design

![Step 2: A Note on Changes to Design image 1](images/step03_01.png)

This build is the first iteration and I have made a number of improvements to the design which I have listed below.

PCB and Panels

- I have included 2 extra screw connections in both the top corners. This helps makes the build a lot secure and stronger.
- Moved components where possible, away from the edge of the PCB. I thought that this might help if someone wants to look at 3D print a case. Switches etc all remain easily accessable
- I changed the orientation of the charging module
- Moved the slide switch to isolate the charging module to the side of the panel


## Step 3: Adding the Screen to the Front Panel

![Step 3: Adding the Screen to the Front Panel image 1](images/step04_01.jpg)

![Step 3: Adding the Screen to the Front Panel image 2](images/step04_02.jpg)

![Step 3: Adding the Screen to the Front Panel image 3](images/step04_03.jpg)

![Step 3: Adding the Screen to the Front Panel image 4](images/step04_04.jpg)

![Step 3: Adding the Screen to the Front Panel image 5](images/step04_05.gif)

![Step 3: Adding the Screen to the Front Panel image 6](images/step04_06.gif)

![Step 3: Adding the Screen to the Front Panel image 7](images/step04_07.gif)

![Step 3: Adding the Screen to the Front Panel image 8](images/step04_08.gif)

![Step 3: Adding the Screen to the Front Panel image 9](images/step04_09.gif)

![Step 3: Adding the Screen to the Front Panel image 10](images/step04_10.gif)

![Step 3: Adding the Screen to the Front Panel image 11](images/step04_11.gif)

![Step 3: Adding the Screen to the Front Panel image 12](images/step04_12.gif)

The following step ensures that you can remove the front panel easily and without having to de-solder anything. This is important, especially for maintenance, battery changes, troubleshooting etc. You may notice that in the images, the screws I used are quite long. I changed these out to shorter ones that just managed to fit. You can use long ones but you will need to trim them at some stage.

STEPS:

- First, trim the tops of the header pins where they are soldered.  You just want to remove a small bit of the top of the header pin so they won’t interfere with the front panel.
- In the front panel, there are 4 holes where the TFT screen will be attached.  Add a 20mm M2 screw (I like to use hex socket head screws) to each and then add a M2 nut to secure the screws into place
- Now, place the screen on top of the screws and align it to the front panel.  The screen should sit flat to the front panel as the nuts you added earlier act like spacers.
- Now - you need to add a small M2 spacer (5mm) to each of the screws. Use the smallest one in the assorted pack that I have recommended to get in the parts list
- Remove the plastic section off the male header pin.  This will ensure that they fir right in the female header pin
- You can now add the low profile female header pins to the male ones on the TFT screen and do a test fit.  You will need to trim the male header pins a little in order for them to sit right in the female header.  What I usually do here is, lay a female header pins on top of the male ones and mark out how much to cut of the male header pins.  It probably about 3mm that you need to remove.
- Don’t solder the female header pins yet to the PCB, we’ll do that near the end


## Step 4: Adding the Raspberry Pi Zero

![Step 4: Adding the Raspberry Pi Zero image 1](images/step05_01.jpg)

![Step 4: Adding the Raspberry Pi Zero image 2](images/step05_02.jpg)

STEPS:

- This is straight forward.  Add male header pins to the Pi.  I like to solder 1 leg into place for each side before I commit to soldering the rest.
- You can then add it to the PCB and solder the rest of the pins to the Pi.  This will ensure all of the pins are straight
- Now you can solder the Pi to the PCB


## Step 5: Adding the Switches & Buzzer

![Step 5: Adding the Switches & Buzzer image 1](images/step06_01.jpg)

![Step 5: Adding the Switches & Buzzer image 2](images/step06_02.jpg)

![Step 5: Adding the Switches & Buzzer image 3](images/step06_03.jpg)

![Step 5: Adding the Switches & Buzzer image 4](images/step06_04.jpg)

![Step 5: Adding the Switches & Buzzer image 5](images/step06_05.jpg)

![Step 5: Adding the Switches & Buzzer image 6](images/step06_06.gif)

![Step 5: Adding the Switches & Buzzer image 7](images/step06_07.gif)

STEPS:

- First, solder both the slide switches to the PCB. you might be wondering why I have added 2 slide switches? One is an on/off switch and isolates the battery. The other is used when charging and isolates the Raspberry Pi. If I just had the switch to the Raspberry Pi, then the voltage regulator used in this build would slowly drain the battery as it draws a very small amount of power in standby.
- Now you can add the momentary switches. I have changed these from being tactile to silent momentary buttons. Tactile ones can hurt your fingers are some time and the ones in this build are softer and I think gives the game a better finish.
- There is also a SMD momentary switch that is included to reset the Pi. you don't really have to include this if you don't want to - up to you.
- Place the buzzer into the holes in the PCB, making sure that it is orientated right ( there is a plus symbol on top of the buzzer which needs to be on the left when soldering it into place.
- Do a test fit here as well just to make sure everything is going right.


## Step 6: Adding the Charging/boost Module

![Step 6: Adding the Charging/boost Module image 1](images/step07_01.jpg)

![Step 6: Adding the Charging/boost Module image 2](images/step07_02.jpg)

![Step 6: Adding the Charging/boost Module image 3](images/step07_03.gif)

![Step 6: Adding the Charging/boost Module image 4](images/step07_04.gif)

The charging and voltage booster module is a great little board. It allows you to add say a 3.6V battery like a mobile one, and you can increase the output voltage via a small potentiometer located on the board.

STEPS:

- First, lets set the output voltage to 5V from the Charging & voltage booster module. Connect the module up to a power source (this could be mobile phone battery, variable power source or whatever you have around, as long as it is lower than 5V’s)
- Now with a multimeter, check the voltage output. You need to try and get as close as possible to 5V’s so turn the potentiometer until you reach 5Vs.
- Now you can add the module to the PCB. I added a little superglue to the bottom of the board to ensure it was secured into place
- Add some solder to each of the solder points on the module and then add some wire from a resistor leg to each solder point.
- Bend the wire down so it is touching the solder pad on the PCB and trim.
- Add solder to the solder pad on the PCB and connect the wire to each. This will give you a good strong connection.


## Step 7: Adding the Battery

![Step 7: Adding the Battery image 1](images/step08_01.jpg)

![Step 7: Adding the Battery image 2](images/step08_02.jpg)

![Step 7: Adding the Battery image 3](images/step08_03.jpg)

Now you can go ahead and add the rest of the components to the PCB

STEPS:

- To add the battery, first add some solder to the positive and negative solder points on the battery. Make sure your soldering iron is hot when doing this
- Now add a resistor leg to each solder point and bend so they are lying flat with the battery.
- Add a little superglue to the battery and glue into place.
- Trim the wire if necessary and then solder onto the solder points on the PCB


## Step 8: Soldering the Female Header for the Screen to the PCB

![Step 8: Soldering the Female Header for the Screen to the PCB image 1](images/step09_01.jpg)

![Step 8: Soldering the Female Header for the Screen to the PCB image 2](images/step09_02.gif)

Ok - nearing the end now of the build. The last thing to do is to solder the female pins for the screen to the PCB.

STEPS:

- Carefully place the front panel into place. Make sure that the screws align to the holes in the PCB and once pushed into place, ensure the pins on the female header pins (which should be on the male header pins connected to the TFT screen) align to the holes into the PCB. You might need to push them slightly with a small screwdriver to align them.
- add 6 X nuts to each of the screws to secure the front panel to the PCB.  You will be adding the back panel in the next step
- Once the screen is in place, do a final check of everything before soldering the female header to the PCB.
- Now you can solder the legs into place.
- Before you start to think about adding the bottom panel and adding nuts to the screws, lets go and add the code to the Pi


## Step 9: Adding the Back Panel

![Step 9: Adding the Back Panel image 1](images/step10_01.jpg)

![Step 9: Adding the Back Panel image 2](images/step10_02.jpg)

![Step 9: Adding the Back Panel image 3](images/step10_03.gif)

In this build, I added a back panel. So in total there is a front panel, PCB and back panel. I did this for a couple reasons. first, it ensures that non of the solder points are being touched with your fingers which can cause shorts, it is more comfortable to hold and I wanted to make this easier to build then the version beforehand which had a lot of SMD parts. The only concern is the additional cost of getting the back panel printed. However - I think it is worth it.

STEPS:

- The screws used should just have enough thread left after you add the back panel to attached a nut
- Carefully screw a nut to each of the ends of the screws.  I found that 2 of the screws were just too short so I didn't bother adding a nut to these.  The back cover is securely on so it won't matter.
- The other option is to add longer screws and then cut them to size.


## Step 10: How to Upload to Raspberry Pi Zero

![Step 10: How to Upload to Raspberry Pi Zero image 1](images/step11_01.png)

Download the [GitHub](https://github.com/lonesoulsurfer/Conways_Game_of_Life__Large_Screen) Files.

If you haven't installed Arduino on your computer, then this is the first thing you should do. Just follow the below instructions which are straight forward and you wont have any issues with loading the code to the Raspberry Pi Zero. If you find that you are having issues, then ask Claude (AI) for help. This is what I do when I get stuck and it always manages to sort it out for me!

STEPS:

- Install Arduino IDE. Download from https://www.arduino.cc/en/software
- Install version 2.0 or newer (recommended)
- Install RP2040 Board Support
- Open Arduino IDE
- Go to File → Preferences
- In "Additional Board Manager URLs", add:
https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json

- Click OK
- Go to Tools → Board → Boards Manager
- Search for "pico"
- Install "Raspberry Pi Pico/RP2040" by Earle F. Philhower
- Install Required Libraries
- Go to Sketch → Include Library → Manage Libraries and install:
- Adafruit GFX Library
- Adafruit ST7735 and ST7789 Library
- Time to upload the code
- Select the Board
- Go to Tools → Board → Raspberry Pi RP2040 Boards
- Select "Waveshare RP2040-Zero"
- Configure Settings. These need to be set under tools before you upload the sketch
- Tools → CPU Speed: 133 MHz (default)
- Tools → Optimize: Small (-Os) (default)
- Tools → USB Stack: "Pico SDK"
- Connect Your Board to the computer
- Plug USB cable into RP2040-Zero
- Board should appear as a COM/serial port
- Select Port
- Go to Tools → Port
- Select the port that appears (usually shows as "RP2040" or similar)
- Click the Upload button (right arrow icon)
- Wait for "Done uploading" message


## Step 11: In Depth Review of All the Game Functions

![Step 11: In Depth Review of All the Game Functions image 1](images/step12_01.jpg)

![Step 11: In Depth Review of All the Game Functions image 2](images/step12_02.gif)

**In-Game Controls (All Simulation Modes)**

Up - Increase simulation speed

Down - Decrease simulation speed

Left - Cycle cell size (Small 3px → Normal 4px → Large 8px)

Right - Reset / regenerate the current pattern

Up + Down - colour mode

SET (hold) - Start simulation from edit mode

SET (hold, running) - Return to edit mode (Custom/Seeds/Brian's Brain only)

B (short press) - Return to menu

B (hold ~1 second) - Show/hide rules and information panel

**Tools Menu**

- Grid Lines — overlays a faint grid matching the current cell size
- Population Counter — shows live cell count and generation number during simulation
- Trail Mode — dying cells leave a soft 20-step fade trail rather than disappearing instantly
- Colour Mode — age-based colouring (young cells are one colour, older cells shift through the spectrum)
- Toroidal World — when on, edges wrap around so the board is a torus; when off, edges are hard boundaries
- Brightness — four levels (25%, 50%, 75%, 100%)
- Auto-Cycle / Screensaver — automatically switches to a random game mode or Wolfram rule every 300 generations; useful as a display piece
- Sound settings (enabled/disabled, three volume levels) are also accessible here and saved to EEPROM.
**Hardware & Setup**

The device runs on a Raspberry Pi Pico / RP2040 connected to a 3.5" ST7796S/ST7796U TFT display (480×320 pixels) via SPI. Six buttons handle all navigation and gameplay — Up, Down, Left, Right, SET (A), and B. A buzzer on GPIO 26 provides sound effects and music. Display brightness is PWM-controlled, and all settings (sound, volume, brightness) are saved to EEPROM so they persist between power cycles.

**Main Menu**

On startup the device boots directly into the main scrolling menu with eight sections:

- Presets — hand-crafted Conway's Life patterns
- Random — randomised Conway's Life
- Symmetric — procedurally generated symmetric patterns
- Custom — draw your own pattern
- Rule Explorer — define custom birth/survival rules
- Alt Games — alternative cellular automata
- Tools — display and simulation settings
- Arcade — three built-in arcade games
Navigate with Up/Down, select with SET, go back with B.

**Conway's Life Modes**

**Presets (13 patterns)**

Each preset loads a famous Life pattern centred on screen. Press SET once to open it, then A to start the simulation. While paused you can press Left to change cell size (the pattern rescales and redraws) or Right to reset it back to its starting state.

1 - Coe Ship. Puffer-type spaceship that leaves debris trails

2 - Gosper Gun. The first glider gun ever discovered — period 30

3 - Diamond. Symmetric expanding diamond pattern

4 - Achim p144. Rare period-144 oscillator

5 - 56P6H1V0. High-period spaceship

6 - LWSS Convoy. Three Lightweight Spaceships in formation

7 - MWSS. Middleweight Spaceship — 8 cells, speed c/2

8 - Pulsar. Period-3 oscillator with 4-fold symmetry, 48 cells

9 - Pentadecathlon. 15 oscillator made from a modified 10-cell row

10 - R-Pentomino. 5-cell seed that runs for 1,103 generations

11 - Acorn. 7-cell methuselah running 5,206 generations

12 - Simkin Gun. Smallest known glider gun — 36 cells, period 120

13 - Queen Bee. Period-30 oscillator, the first of its kind ever found

**Random**

Fills the board with random live cells at approximately 30% density. Immediately starts running. Press Right to re-randomise.

**Symmetric**

Generates a random pattern with one of three symmetry types — vertical, horizontal, or rotational — in small, medium, or large sizes. Good for producing interesting structured chaos.

**Custom**

Puts the board into edit mode with a blinking red crosshair cursor. Move the cursor with Up/Down/Left/Right. Press SET to toggle a cell on or off. When happy with your pattern, hold SET for about a second to start the simulation. Hold SET again to return to edit mode. Press B to go back to the menu.

**Rule Explorer**

Lets you define your own cellular automaton by setting custom Birth (B) and Survival (S) rules — the same notation used by Life (B3/S23). Choose from 12 built-in rule presets or enter your own bit-by-bit. The simulation runs with your rules applied to a random starting board.

Included preset rules:

- High Life, 34 Life, Diamoeba, Replicator, Long Life, Maze, Coral, 2x2, Dry Life, Amoeba, Coagulate, Gnarl
**Alternative Cellular Automata (Alt Games)**

**Brian's Brain**

A three-state automaton (On, Dying, Off) producing a constantly moving stream of light-speed "signals." Choose from small, medium, large, or random seedings, or draw a custom starting pattern.

**Day & Night (B3678/S34678)**

A symmetric ruleset where dead and live regions are interchangeable. Dense regions survive and grow in a way that mirrors the original — creating organic, blob-like patterns.

**Seeds (B2/S)**

Every live cell dies every generation but any dead cell with exactly two live neighbours is born. Creates explosive, constantly moving patterns that never stabilise.

**Cyclic CA**

A multi-state automaton where cells cycle through states 0→1→2→…→N→0. Cells advance only when they have a neighbour in the next state. Produces stunning rotating spiral waves. Choose small, medium, or large seedings.

**Wireworld**

A four-state automaton (Empty, Wire, Electron Head, Electron Tail) that models digital logic circuits. Electrons travel along wires, interact at junctions, and can form AND gates and clocks. The built-in demo includes a working circuit layout.

**Langton's Ant**

A single ant on a grid follows two rules: turn right on a white cell (flip it black), turn left on a black cell (flip it white). After ~10,000 chaotic steps it spontaneously builds a repeating diagonal "highway." Toggle age-colour mode with Up+Down to see a heat map of how often each cell has been visited.

**Wolfram 1D Automata**

One-dimensional elementary cellular automata — a single row of cells evolves downward according to one of 255 possible rules. Each rule produces a unique pattern, from pure chaos (Rule 30) to the Sierpinski triangle (Rule 90) to a Turing-complete system (Rule 110). Seven named presets are provided or you can enter any rule number direct

**Arcade Games**

Accessed from main menu item 8. Three games are available. In all three, press A + B together at any time to exit directly back to the main menu.

**Star Wars**

A first-person Star Wars game inspired by the 80's arcade game. Progress through multiple stages: Womp Rat Training, Space Battle, Death Star Approach, Surface Run, and the Exhaust Port shot. Features full Star Wars music (Main Theme, Binary Sunset, Imperial March, Victory Fanfare), sound effects, TIE fighters, laser cannons, proton torpedoes, and a dramatic finale sequence. Press B on the title screen to exit.

Controls:

- Up/Down/Left/Right — move crosshair / pilot ship
- SET — fire
- A + B — exit to main menu
- Up + Down -  in start up screen will take you into a games menu where you can play any of the games or watch the cinematic shorts
**Breakout Beyond**

A feature-rich Breakout variant with a neon aesthetic. The paddle sits at the bottom, bricks at the top. Features include combo multipliers, spin physics, multiball, shield power-ups, bomb bricks, and hard bricks across 20 levels.

Controls:

- Left/Right — move paddle
- B — speed boost
- SET — launch ball / pause
- A + B (hold) — exit to main menu
**Gyruss**

A circular shoot-em-up inspired by the 1983 Konami arcade classic. Your ship orbits around the edge of the screen shooting inward at waves of enemies that fly in formation patterns.

Controls:

- Left/Right — rotate ship around the ring
- SET or B — fire
- Up (hold) — smart bomb
- A + B (hold) — exit to main menu


## Downloads

- [Parts List](pdfs/Parts List.pdf)

---
*56 images archived*
