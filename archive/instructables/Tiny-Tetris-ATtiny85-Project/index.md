# Tiny Tetris - ATtiny85 Project

Source: https://www.instructables.com/Tiny-Tetris-ATtiny85-Project/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)


## Supplies

![Supplies image 1](images/step02_01.jpg)

![Supplies image 2](images/step02_02.jpg)

![Supplies image 3](images/step02_03.jpg)

![Supplies image 4](images/step02_04.jpg)

![Supplies image 5](images/step02_05.jpg)

![Supplies image 6](images/step02_06.jpg)

The parts list can also be found on my GitHub page. The PCB info can be found on the next stepPARTS:ATtiny85 - Ali ExpressBuzzer - Ali ExpressOLED 1306 Screen - Ali ExpressMicro switch horizontal slide - Ali ExpressMomentary Buttons X 4 The ones I used are about 2mm high - Ali ExpressResistors - Ali Express2 X 10K1 X 1K1 X 2.2KCR2032 battery holder - Ali ExpressCR2032 battery - Ali ExpressOptional - Key Chain - Ali Express


## Step 1: Getting the PCB Printed

![Step 1: Getting the PCB Printed image 1](images/step03_01.jpg)

![Step 1: Getting the PCB Printed image 2](images/step03_02.jpg)

Firstly, all the files that you need to get the circuit board printed can be found in my GitHub Page. I've also included the Eagle files for the schematic and the board in my GitHub Page so you can play around with these if you want to as well.You’ll need to send the Gerber files to a PCB manufacturer like JLCPCB (Not affiliated) who will print the boards for you. Download the repository on my GitHub page to your computer and then send the Gerber files off to your PCB manufacturer of choice. Make sure you keep it zipped.I've put together an Instructable on how to get your broads printed which you can find here.NOTE: The manufacture will include an order number on the PCB. However, you can 'specify a location' once the Gerber files have been loaded. Click 'specify a location' and add a note saying - 'please add the order number to the back of the board.


## Step 2: Adding the Components to the PCB

![Step 2: Adding the Components to the PCB image 1](images/step04_01.jpg)

![Step 2: Adding the Components to the PCB image 2](images/step04_02.jpg)

![Step 2: Adding the Components to the PCB image 3](images/step04_03.jpg)

![Step 2: Adding the Components to the PCB image 4](images/step04_04.jpg)

The component list is quite low and as mentioned, I've only used through hole components (no SMD) so it's super simple to solder everything in place. Note that the PCB is double sided and the battery holder and on/off switch is added to the back of the PCB. The order that you add the components is important. If you add the OLED screen before the battery holder you won't be able to get to the solder points for the battery holder so pay attention to the order of the stepsSTEPS:As usual, it's best to start with the lowest profile components which in this case is the resistors. These have been added to the PCB so they are hidden by the OLED screen and also act as supports for the screen. Solder these in place.Next solder the tactile switches into place.  I have used low profile buttons which I think would well on this PCB.Now solder the buzzer (speaker) into place.Before you solder the OLED screen into place, flip the PCB and solder into place the battery holder and on/off switch.Now you can solder the OLED screen into place.Don't solder in the ATtiny85 yet - we first need to program it


## Step 3: How to Program an ATtiny85

![Step 3: How to Program an ATtiny85 image 1](images/step05_01.png)

![Step 3: How to Program an ATtiny85 image 2](images/step05_02.png)

![Step 3: How to Program an ATtiny85 image 3](images/step05_03.jpg)

When I first started to investigate and learn how to program the ATtiny85 I was totally confused! The tutorials that I found on line didn't give a complete step by step guide and I had to work my way through a number of them to finally work out how to do it. Luckily for you I've recently put together an Instructable on exactly how to do this and it really isn't that hard.You will however need to get yourself an Arduino Nano which you'll use to program the ATtiny85. Again, I want to reiterate that this really isn't hard to do and if you follow the Instructable below you will be able to program your ATtiny85 with the Tetris sketchHow to Program ATtiny85 with an ArduinoI have also done an Instructable on building your own programmer for the ATtiny85. You can go all out and get a PCB printed or you can just breadboard the programmer.Programmer for the ATtiny85Once you know how to program an ATtiny85, you are ready to install Tetris onto it.


## Step 4: Uploading the Sketch to the ATtiny85

![Step 4: Uploading the Sketch to the ATtiny85 image 1](images/step06_01.jpg)

![Step 4: Uploading the Sketch to the ATtiny85 image 2](images/step06_02.jpg)

![Step 4: Uploading the Sketch to the ATtiny85 image 3](images/step06_03.jpg)

![Step 4: Uploading the Sketch to the ATtiny85 image 4](images/step06_04.jpg)

If you don't have the sdd1306xled library added to Arduino IDE - then you will need to add this.Adding the SDD1306XLED Library to Arduino IDEIn Arduino IDE go to Sketch / Include Libraries / Manage LibrariesType the following in the search bar - ssd1306xled which will bring up the sketch and then hit install.Uploading the Tetris Sketch to the ATtiny85STEPS:Open up the 'ATtiny85-Tetris-Gold IDE file which will open it up in Arduino IDEEnsure that the Arduino is set as 'Arduino as ISP'Go to 'tools' and make sure that the processor speed is set to 8Mhz Internal Oscillator. Also change the Override Clock Source to 'Internal Oscillator 8Mhz'Now select the ATtiny85 in the dropdown and burn the bootloaderYou can now upload the sketch via 'upload Using Programmer'CAUTION!If you get a message that says that sketch is too big, then you will need to reduce the size of the sketch. You can do this by changing the following:Tools / Print Support / change to 'Hex Only Support'Tools / Brown Out Detection Level / change to 'Disabled'Now try again to load the sketch. It should be good now to load


## Step 5: Testing the ATtiny85 Before Soldering Into the PCB

![Step 5: Testing the ATtiny85 Before Soldering Into the PCB image 1](images/step07_01.jpg)

I went al out and soldered together a separate PCB so I could test the ATtiny85 before I soldered it into place.  The test PCB included a 8 IC socket so I could easily add and remove the ATtiny85.  You don't have to do this but It will save you a lot of possible headaches if you find that something went wrong with the programming of the ATtiny85.You could also just breadboard the circuit as well which is probably just as easy and you won't waste a board!  I'm planning to do a few of these so I wanted a more permanent testing board.


## Step 6: Adding the ATtiny85 to the PCB

![Step 6: Adding the ATtiny85 to the PCB image 1](images/step08_01.jpg)

![Step 6: Adding the ATtiny85 to the PCB image 2](images/step08_02.jpg)

Final step!Now that you have tested the ATtiny85 and it works, you can now solder it into place onto the PCB.STEPS:Place the ATtiny85 into the PCBAdd a little solder to one leg to hold it into placeNow solder the rest of the legs to the the PCBAdd a battery and play away!Hard Mode and Ghost OnThere are a couple of bonus plays that you can activate.Ghost On.This adds a ghost piece that makes it a lot easier to position the pieces as they move down the screen. I would highly recommend turning this on when you playHold down 'drop' and turn on the gamepush 'left' whist still holding down 'drop' until you see 'Ghost on' appear on the screennow release 'drop' and push it againIt plays an extra long version of the song but it is well worth itHard ModeThis adds a whole stack of pieces to the start of the gameHold down 'drop' and turn on the gamehold down 'left' whist still holding down 'drop' until you see 'hard mode' appear on the screennow release 'drop' and push it again


---
*25 images archived*
