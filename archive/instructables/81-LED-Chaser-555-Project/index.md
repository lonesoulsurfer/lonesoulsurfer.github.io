# 81 LED Chaser - 555 Project

Source: https://www.instructables.com/81-LED-Chaser-555-Project/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

![Intro 6](images/intro_06.jpg)

If you have ever checked out 555 projects on the net, you may have come across an LED chaser. For those old enough, it's the same thing that Kitt used in Knight Rider!

However, where most LED chasers use around 10 LED's, this build uses a matrix of 9 X 9 LEDS, making a total of 81!

The other difference in this build to your normal LED chaser is it includes two pulse width generators, curtesy of 2 555 timers. This allows you to make some really interesting patterns and shapes via 2 potentiometers that control the X and Y axis. I also included the ability to change the speed from slow to fast for each axis which gives you even more ability to change the patterns produced.

I have also designed a PCB for this build so you can easily build your own. There is quite a bit of soldering (81 LED's plus heaps of transistors) so be prepared for an hour of soldering!

The end project however is definitely worth all that soldering. It's a really fun and interesting build and I've been playing with every day.

The build was inspired by a project created by Eddy Bergman. He has built some great circuits and if you are interested in building a modular synth then this is the place to go!

Lastly, I build a small enclosure and designed a front panel to complete the build

Note - it's not easy to film a lot of LED's moving around due to the recording frame rate of a phone. What you see in the video looks different to what you see in real life.

Hackster have also done a review of this project which can be found here


## Supplies

![Supplies image 1](images/step01_01.jpg)

![Supplies image 2](images/step01_02.jpg)

![Supplies image 3](images/step01_03.jpg)

![Supplies image 4](images/step01_04.jpg)

Below are the components need to build this project.

Step 1 has the information around the PCB.

Step 2 has the parts list for the case and front panel

The best way to buy electronics is in bulk and I have added a link to each. I also used 5mm square LED's and they look awesome! You can also use round ones as well but I highly recommend that you just buy the square ones. I got 1000 for $14!

Lastly, I have attached a PDF of the parts list and it can also be found on my Google Drive

Components for the Circuit

- Capacitor polarized - eBay
- 1uf X 2
- 470uf X 1
- Capacitor polyester
- 220nf X 2 - eBay
- Switch - 6 pin X 4 - eBay Note that these are 7mm X 7mm self locking switches. They come in 2 states, normally open or closed so the orientation in the PCB is important.
- Switch cap - ali express
- IC
- 4017 X 2 - eBay
- 555 X 2 - eBay
- IC Socket
- 16 pin X 2 - eBay
- 8 pin X 2
- LED
- square or round 5mm X 81 - eBay (this is for the square ones)
- JST Connector Mini X 1 - Ali Express
- Resistor - eBay
- 3.3K X 1
- 220R X 9
- 10K X 11
- Transistor - BC547 X 18 - eBay
- Potentiometer - Linear 9mm vertical 100K X 2 - Ali Express
Parts for Front Panel and Case

- Opal Acrylic A5 - eBay
- Clear, adhesive A4 label - eBay
- Hardwood edging (for the case) 40mm x 8mm x 1M - any hardware store
Powering the PCB.

You can use a 9v battery but I like to re-use old mobile batteries.

- Mobile battery - If you want to find them just visit your local e-waste or check in the top drawer for an old phone! You can always just buy a new one on eBay as well...
- Power module (this will increase the voltage from 3.7v to 9v - Ali Express
- USB charging module (so you can charge the battery up) - Ali Express


- [Parts List - 81 LED Chaser](pdfs/Parts List - 81 LED Chaser.pdf)

## Step 1: Printing the PCB

![Step 1: Printing the PCB image 1](images/step02_01.jpg)

![Step 1: Printing the PCB image 2](images/step02_02.jpg)

The board is actually 2 sided. On one side are all of the components like capacitor, resistors, IC's etc. On the other side is the potentiometers and switches.

To have the board printed, save the gerber zip file in the Google Drive files to your computer and email it to your favourite PCB manufacturer. I use JLCPCB (not affiliated) who do a good job of printing the boards and are quick as well. If you are thinking 'what the hell is a gerber file!', then check this 'ible out which is a step by step guide on how to get a PCB printed.

If you would like to play around with the schematic and board in Eagle, well I have also provided these in my Google Drive. You can also find a PDF of the schematic in this step

You might have noticed that the board looks a little different to mine. Well that's because I made a couple improvements - you're welcome!


- [81 LED Chaser - Schematic](pdfs/81 LED Chaser - Schematic.pdf)

## Step 2: Adding the Components to the PCB - LED's

![Step 2: Adding the Components to the PCB - LED's image 1](images/step03_01.jpg)

![Step 2: Adding the Components to the PCB - LED's image 2](images/step03_02.jpg)

![Step 2: Adding the Components to the PCB - LED's image 3](images/step03_03.jpg)

![Step 2: Adding the Components to the PCB - LED's image 4](images/step03_04.jpg)

![Step 2: Adding the Components to the PCB - LED's image 5](images/step03_05.jpg)

![Step 2: Adding the Components to the PCB - LED's image 6](images/step03_06.gif)

![Step 2: Adding the Components to the PCB - LED's image 7](images/step03_07.gif)

As the board is 2 sided, the component sequence is important to get right. The first thing to start with is the LED's. I was going to build a jig to ensure that they were all straight but didn't have to in the end as the LED's are flat on top!

STEPS:

- Place 9 LED's in the first top row and add 1 in each of the bottom corners.
- Carefully flip the PCB and ensure that the LED's are all still in place. To do this I just put some pressure on the legs whilst flipping the board.
- Make sure that the lags are all sitting up straight and start to add some solder to 1 leg of each LED. Once done you can check to make sure that they are all sitting flat and straight. if any are not straight, then just slightly twist it with some tweezers to straighten it up.
- Add solder to the other legs if everything is good
- Do this another 9 times! actually - it doesn't take very long once you get into the swing of things.


## Step 3: Adding the Components to the PCB - Continued

![Step 3: Adding the Components to the PCB - Continued image 1](images/step04_01.jpg)

![Step 3: Adding the Components to the PCB - Continued image 2](images/step04_02.jpg)

![Step 3: Adding the Components to the PCB - Continued image 3](images/step04_03.jpg)

![Step 3: Adding the Components to the PCB - Continued image 4](images/step04_04.jpg)

![Step 3: Adding the Components to the PCB - Continued image 5](images/step04_05.jpg)

![Step 3: Adding the Components to the PCB - Continued image 6](images/step04_06.jpg)

![Step 3: Adding the Components to the PCB - Continued image 7](images/step04_07.gif)

![Step 3: Adding the Components to the PCB - Continued image 8](images/step04_08.gif)

![Step 3: Adding the Components to the PCB - Continued image 9](images/step04_09.gif)

Once the LED's are soldered into place, flip the PCB and start work on the components on the other side.

STEPS:

- As always, start with the lowest profile parts - in this case it's the resistors
- I usually then add the IC sockets. It's definitely a good idea using these as it makes the job of replacing a possible faulty IC extremely easy!
- Add the transistors (there are 18 of them1) and caps and add the IC's into place
- Once all of the components have been added, flip the board again and add the switches and potentiometers. It's a little tight when soldering but just take your time and make sure you don't bridge any of the legs on the switches.
- Note that the switches need to be orientated a certain way. They come in 2 states, normally open and normally closed, you want to add them to the board so that the switch is normally open and when pushed down it is closed. If you look at the back of the switch there is a small indent, that it the top of the switch so make sure that the indent is at the top when soldering to the board.
- The last thing to do is to add some power and test the board. If you find that an LED isn't coming on, check the solder points. If still nothing, you might have to replace it.
- Have a play around with the board and see what patterns you can generate


## Step 4: Designing the Front Panel

![Step 4: Designing the Front Panel image 1](images/step05_01.jpg)

![Step 4: Designing the Front Panel image 2](images/step05_02.jpg)

![Step 4: Designing the Front Panel image 3](images/step05_03.jpg)

![Step 4: Designing the Front Panel image 4](images/step05_04.jpg)

![Step 4: Designing the Front Panel image 5](images/step05_05.jpg)

![Step 4: Designing the Front Panel image 6](images/step05_06.jpg)

I decided to keep the front panel pretty simple - there is already enough going on with all those LED's. I designed the front panel to fit directly onto the PCB.

I use inkscape to design my front panels. You can find the raw files in my Google drive in case you want to play around with them

STEPS:

- Use the attached PDF copy of the front panel design.
- The front panel needs to be printed on clear, adhesive paper. You can get this from eBay and have added a link to the parts page.
- NOTE - as mentioned above, I made some designs to the PCB which might mean that the panel doesn't align with the pots and switches any longer. You might have to make some fine adjustments to the panel in inkscape if you intend to use it.
- Cut out one of the images and carefully place onto the opal acrylic and remove any air bubbles.
- Cut the acrylic to size if you haven't already
- To ensure the colours on the front panel don't get scratched, spray a few coats of clear acrylic onto the front panel. Make sure you give it a good coating each time and leave for an hour to dry before applying the next one. I used a satin finish clear coat on the final design.


- [81 LED Chaser](pdfs/81 LED Chaser.pdf)

## Step 5: Drilling and Making the Cutouts in the Front Panel

![Step 5: Drilling and Making the Cutouts in the Front Panel image 1](images/step06_01.jpg)

![Step 5: Drilling and Making the Cutouts in the Front Panel image 2](images/step06_02.jpg)

![Step 5: Drilling and Making the Cutouts in the Front Panel image 3](images/step06_03.jpg)

![Step 5: Drilling and Making the Cutouts in the Front Panel image 4](images/step06_04.jpg)

![Step 5: Drilling and Making the Cutouts in the Front Panel image 5](images/step06_05.jpg)

![Step 5: Drilling and Making the Cutouts in the Front Panel image 6](images/step06_06.jpg)

Time to drill out the holes for the pots and switches and also cut out the section for the LED's.

STEPS:

- I like to use a stepped drill bit to make the holes in the front panel. Carefully drill out each of the holes for the pots and switches
NOTE: I highly recommend to use a drmel for the next step. It makes the job relatively easy. You could also use a small saw to remove the section

- Attach a small cutting wheel to the dremel and carefully cut away the square section in the panel for the LED's
- Tidy up the edges with a file and then see how the PCB fits. Re-work any sections if necessary until the PCB fits nicely into the front panel
NOTE: if you wanted to diffuse the LED's you could use some 2mm red acrylic and you wouldn't even have to make the cutout for the LED's!

- You may notice that the screws that I used to connect the PCB to the front panel look a little odd. That's because I have used the original PCB design and I didn't take into account how the screws would look like in the panel. This has now been fixed in the new design
- Place the PCB into the front panel, mark where to drill the 4 holes to mount it and drill.
- Test to make sure that the PCB and front panel can be secured and then remove the PCB.


## Step 6: Making the Case

![Step 6: Making the Case image 1](images/step07_01.jpg)

![Step 6: Making the Case image 2](images/step07_02.jpg)

![Step 6: Making the Case image 3](images/step07_03.jpg)

![Step 6: Making the Case image 4](images/step07_04.jpg)

![Step 6: Making the Case image 5](images/step07_05.jpg)

![Step 6: Making the Case image 6](images/step07_06.jpg)

![Step 6: Making the Case image 7](images/step07_07.jpg)

![Step 6: Making the Case image 8](images/step07_08.jpg)

![Step 6: Making the Case image 9](images/step07_09.jpg)

![Step 6: Making the Case image 10](images/step07_10.jpg)

I decided to make the case have a slight angle so when you viewed the LED's they would be more in line with your eyes if you were sitting down.

STEPS:

- The first thing you need to do is to cut a groove along the wood in order to secure the panel into. I used a dremel with a router attachment to do this.
NOTE: If you don't have one then you could always just stick the panel to the top of the case - easy!

- Secure the wood with some clamps and run the bit near the top of the wood. Take your time and make sure you keep the dremel nice and straight.
- Measure and cut the wood to size. The best way to do this is to just slip in the front panel into the groove of the wood and measure where to make the cuts
- To give the case an angle, I just cut the side pieces of wood so the top section was higher than the bottom. Have a look at the images and you'll see what I mean...
- Place the front panel into the grooves of the wood and with a small nail gun like a brad nailer, connect the sides together. You can also just glue them as well if you want to - I just get impatient waiting for the glue to dry!
- For the base you can use some thin ply wood. Secure it in place with some screws before sanding
- Use a sander to clean-up the edges of the case. I use a belt sander to do this which is the quick way. You could also just do it by hand as well.
- If you are brave you can also sand the top section. Just be careful that you don't sand the front panel!
- To finish off the wood I added some clear gloss on the body of the frame and base. Leave to dry for a few hours, give it a light sand and add another coat


## Step 7: Adding Power

![Step 7: Adding Power image 1](images/step08_01.jpg)

![Step 7: Adding Power image 2](images/step08_02.jpg)

![Step 7: Adding Power image 3](images/step08_03.jpg)

![Step 7: Adding Power image 4](images/step08_04.jpg)

![Step 7: Adding Power image 5](images/step08_05.jpg)

![Step 7: Adding Power image 6](images/step08_06.jpg)

![Step 7: Adding Power image 7](images/step08_07.jpg)

![Step 7: Adding Power image 8](images/step08_08.jpg)

You could power everything by a 9V battery. I like to use rechargeable batteries for my builds and have decided to use an old mobile battery to power everything.

STEPS:

- The step up power module (used to change the voltage from 3.7v to 9v) needs to be formatted to output 9v's. To do this you need to connect the top 2 solder pads with some solder. They are tiny so just add a little solder to your soldering iron and dab it on.
- Add a dab of superglue to the back of the power module and glue it close to the battery terminals
- Connect the input of the module to the battery using a couple resister legs
- To be able to charge the battery, you will need to be able to access the USB C module. The easiest way is to make a small cutout into the side of the case and glue the USB module to it. You can then connect the USB module to the input on the charging module (the same solder points as the power module
- Lastly, connect a couple wires to the output of the power module and connect these to the power in on the PCB


## Step 8: Pulling Everything Together

![Step 8: Pulling Everything Together image 1](images/step09_01.jpg)

![Step 8: Pulling Everything Together image 2](images/step09_02.jpg)

![Step 8: Pulling Everything Together image 3](images/step09_03.jpg)

![Step 8: Pulling Everything Together image 4](images/step09_04.jpg)

![Step 8: Pulling Everything Together image 5](images/step09_05.jpg)

![Step 8: Pulling Everything Together image 6](images/step09_06.jpg)

STEPS:

- First, connect the PCB to the front panel using some small screws and nuts
- Connect the power to the PCB
- Screw into place the back panel
- Add a couple of potentiometer knobs to the pots
- Turn on and enjoy!


## Downloads

- [Parts List - 81 LED Chaser](pdfs/Parts List - 81 LED Chaser.pdf)
- [81 LED Chaser - Schematic](pdfs/81 LED Chaser - Schematic.pdf)
- [81 LED Chaser](pdfs/81 LED Chaser.pdf)

---
*64 images archived*
