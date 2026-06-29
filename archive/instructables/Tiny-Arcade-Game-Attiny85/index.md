# Tiny Arcade Game - Attiny85 Build

Source: https://www.instructables.com/Tiny-Arcade-Game-Attiny85/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

Hello beautiful people.

I've recently taken the leap into playing around with microcontrollers, specifically the 8 bit ATtiny85 and so far it's been a blast!

This Instructable goes through step by step how to build your own tiny arcade game. There are 7 different games that you can play and I've also created a custom keyring style mini PCB to add the components to.

For those new to ATtiny microcontrollers, It is a small, integrated, 8 pin IC, similar to the Arduino, but with much less IO pins, smaller memory and a smaller form factor. Don't let the smallness of the IC fool you, ATtiny85 microcontroller can perform a whole bunch of different functions on a single IC once it has been programmed. In this project we will be programming it with some arcade games.

Don't worry if you a totally new to all of this. I have created this project with beginners in mind so if you have some basic soldering skills and a computer you shouldn't have any issues building your own. I've used through hole components and off-the-shelf parts which you can buy cheaply from Ali-Express (or whoever you buy electronic components from). I've included links to all of the parts in the next step.

You will need to learn how to program the ATtiny as well. To make this as easy as possible, I've published an Instructable on this which you can find in step 3. I wanted to ensure that this Instructable had everything you needed to make your own.

The games available are your classic arcade games like Frogger, Space Attack, Breakout, Snake, Pong, and others. It still blows my mind that you can fit a whole game into one of these tiny IC's!

Check out the vid which shows the games in action.

Let's get building!


## Supplies

![Supplies image 1](images/step01_01.jpg)

![Supplies image 2](images/step01_02.jpg)

![Supplies image 3](images/step01_03.jpg)

![Supplies image 4](images/step01_04.jpg)

![Supplies image 5](images/step01_05.jpg)

![Supplies image 6](images/step01_06.jpg)

![Supplies image 7](images/step01_07.jpg)

The following parts list is for the Mini Arcade components. Step 2 has all of the information needed to program the ATtiny.

You will get 5 PCB's when you have them printed so you may as well ensure that you order enough parts to build 5!

Parts:

- PCB - See next step on how to get them printed
- ATtiny85 X 1 - Ali Express. Tip - Buy them in lots of 5 - it's cheaper and you can always use them in more games. Make sure you buy 'through hole' IC's
- OLED Display Module (SSD1306) - Ali Express Buy the single colour ones. Mine are white OLED but you can get them in blue as well.
- Buzzer (speaker) - Ali Express. I used the low profile ones like this Ali Express
- Resistors - metal film 1% - Ali Express
- 10K X 2
- 1K X 1
- 6.8K X 1
- Momentary Tactile Push Button X 3 - Ali Express.
- Micro on/off switch vertical - Ali Express you can also use these types as well - Ali Express
- CR2032 battery holder X 1 - Ali Express
- CR2032 Battery - Ali Express


## Step 1: The PCB & Schematic

![Step 1: The PCB & Schematic image 1](images/step02_01.png)

![Step 1: The PCB & Schematic image 2](images/step02_02.png)

![Step 1: The PCB & Schematic image 3](images/step02_03.png)

Firstly, all the files that you need to get the circuit board printed can be found in my GitHub Page. I've also included the Eagle files for the schematic and the board in my Google Drive so you can play around with these if you want to.

You’ll need to send the Gerber files to a PCB manufacturer like JLCPCB (Not affiliated) who will print the boards for you. Jump into my Google Drive link, download the Gerber file to your computer and then send them off to your PCB manufacturer of choice. Make sure you keep it zipped.

I've put together an Instructable on how to get your broads printed which you can find here.

NOTE: The manufacture will include an order number on the PCB. However, you can 'specify a location' once the Gerber files have been loaded. Click 'specify a location' when the board has been loaded and the manufacturer will add it to the back where I have indicated.


## Step 2: Adding the Components to the PCB

![Step 2: Adding the Components to the PCB image 1](images/step03_01.jpg)

![Step 2: Adding the Components to the PCB image 2](images/step03_02.jpg)

![Step 2: Adding the Components to the PCB image 3](images/step03_03.jpg)

![Step 2: Adding the Components to the PCB image 4](images/step03_04.jpg)

![Step 2: Adding the Components to the PCB image 5](images/step03_05.jpg)

![Step 2: Adding the Components to the PCB image 6](images/step03_06.jpg)

![Step 2: Adding the Components to the PCB image 7](images/step03_07.jpg)

![Step 2: Adding the Components to the PCB image 8](images/step03_08.jpg)

![Step 2: Adding the Components to the PCB image 9](images/step03_09.jpg)

The component list is quite low and as mentioned, I've only used through hole components (no SMD) so it's super simple to solder everything in place. Note that the PCB is double sided and the battery holder and on/off switch is added to the back of the PCB. The order that you add the components is important. If you add the OLED module before the battery holder you won't be able to get to the solder points for the battery holder so pay attention to the following steps

STEPS:

- As usual it's best to start with the lowest profile components which in this case is the resistors. These have been added to the PCB so they are hidden by the OLED module and also act as supports for the module. Solder these in place.
- Next solder the tactile switches into place
- You can now solder the programmed IC into place. If you add a IC socket you can always easily remove the ATtiny and re-program it with other games. It also allows you to remove the ATtiny if something goes wrong with the programming. I like to test the ATtiny first via a breadboard to make sure it is working correctly before soldering it into place.
- Now solder the buzzer (speaker) into place.
- Before you solder the OLED module, flip the PCB and solder into place the battery holder and on/off switch.
- Now you can solder the OLED into place.
- Add a battery to the back and turn on the game to make sure everything works.


## Step 3: Programming the ATtiny85

![Step 3: Programming the ATtiny85 image 1](images/step04_01.png)

![Step 3: Programming the ATtiny85 image 2](images/step04_02.jpg)

When I first started to investigate and learn how to program the ATtiny I was totally confused! The tutorials that I found on line didn't give a complete step by step guide and I had to work my way through a number of them to finally work out how to do it. Luckily for you I've recently put together an Instructable on exactly how to do this and it really isn't that hard.

You will however need to get yourself an Arduino Uno which you'll need to program the ATtiny. Again, I want to reiterate that this really isn't hard to do and if you follow the Instructable below you will be able to program your ATtiny with any of the games included in this Instructable

How to Program ATtiny with an Arduino

Once you know how to program an ATtiny, you are ready to install one of the games onto it.


## Step 4: Programming a Game on the ATtiny85 - Step 1

![Step 4: Programming a Game on the ATtiny85 - Step 1 image 1](images/step05_01.png)

![Step 4: Programming a Game on the ATtiny85 - Step 1 image 2](images/step05_02.png)

Now that you know how to program the ATtiny, it's time to try and add one of the games I have included. All of the games can be found in my GitHub Page in the 'Tiny Arcade - Games' folder and have been fully tested and work perfectly.

You will need to add a library to the Arduino. This couldn't be easier. As a matter of fact, Arduino have included a number of libraries that you just need to install directly from Arduino IDE. The library is needed so the ATtiny can drive the OLED screen

STEPS:

- In Arduino IDE go to Sketch / Include Libraries / Manage Libraries
- Type the following in the search bar - ssd1306xled which will bring up the sketch and then hit install.
- That's it! You have now added the library for the OLED module and there is nothing further to so.
- Now you can open the sketch for whatever game you want to program to the ATtiny and upload it via Arduino.
- Just click onto the sketch which will open Arduino and follow the steps above to load the game to the ATtiny.


## Step 5: Programming a Game on the ATtiny85 - Step 2

![Step 5: Programming a Game on the ATtiny85 - Step 2 image 1](images/step06_01.png)

![Step 5: Programming a Game on the ATtiny85 - Step 2 image 2](images/step06_02.png)

![Step 5: Programming a Game on the ATtiny85 - Step 2 image 3](images/step06_03.png)

Now that you have added the sdd1306xled library - you need to change a couple things under Tools to make suree everything works ok. If you don't do this then you might find that the games restart constantly.

STEPS:

- In the game sketch that you have opened go to: Tools / Override Clock Source and click on 'Internal Oscillator 8Mhz
- Next go to: Tools / Processor speed and click on 8Mhz Internal Ocsillator
- Lastly, go to: Tools / Brown Out Detection Level and click 1.8V. Actually not 100% sure you need to do this but it won't hurt
- Now you can upload the sketch into the ATtiny85.


## Step 6: Playing the Game

![Step 6: Playing the Game image 1](images/step07_01.jpg)

![Step 6: Playing the Game image 2](images/step07_02.jpg)

![Step 6: Playing the Game image 3](images/step07_03.jpg)

Most of the games are quite simple to play so you don't really need instructions on how to play them. I have included the instructions on how to play in the next step.

I haven't included Pacman or Tetris in this build. They are available but Pacman needs some additional steps and I didn't want to confuse anyone. Tetris uses a different style OLED so that's for another build.

If you are looking for other games then just do a search on Google for ATtiny85 games and see what you can find. Make sure you test them on a breadboard first before committing them to a PCB.

A lot of the games only use 2 buttons but I have included 3 (left, jump, right) so you can play multiple games on the one board

That's it! Build a bunch more using the other games and give them away to your friends and family.


## Step 7: Game Instructions

![Step 7: Game Instructions image 1](images/step08_01.jpg)

![Step 7: Game Instructions image 2](images/step08_02.jpg)

![Step 7: Game Instructions image 3](images/step08_03.jpg)

Bat Bonanza

Bat bonanza is a clone of the classic pong

- Pressing and releasing the left button cycles through modes, including two-player games and one-player modes with varying degrees of difficulty.
- Also, from standby, press and hold the left button to reset all settings
Breakout

- Use the left and right buttons to control the paddle at the bottom of the screen
Frogger

- Use the left & right buttons move the frog across the screen
- The middle button moves the frog forward
- From standby, press and hold left button to turn sound on and off
- From standby, press and hold left button with the right button held to reset high score
Run Dude run

- LEFT and RIGHT buttons move the little dude. Just don't let any missiles hit you!
Snake

- Classic snake game which only uses the left button to control the snake
Space Attack

- LEFT and RIGHT buttons move the spaceship
- Middle button to fire
- From standby, press and hold left button to turn sound on and off
- Press and hold left button with the right button held to reset high score
UFO & Stacker - 2 games on one ATtiny

- To play Stacker - press and release left button
- To play UFO - with the right button held, press and release left button
- To turn sound on and off - press and HOLD left button
- To reset high scores to zero - whilst HOLDING the right button, press and HOLD the left button


---
*37 images archived*
