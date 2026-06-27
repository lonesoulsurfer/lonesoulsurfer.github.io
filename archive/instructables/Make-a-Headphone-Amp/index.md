# Make a Headphone Amp V2

Source: https://www.instructables.com/Make-a-Headphone-Amp/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)


## Step 1: About the Amp Circuit I Choose to Build

![Step 1: About the Amp Circuit I Choose to Build image 1](images/step02_01.jpg)

The amp is built using op amp 5532.  The op amp is a low-distortion, low-noise device, which can drive low-impedance loads to a full voltage swing while maintaining low distortion. Furthermore, it is fully output short-circuit proof.  I’ve included the datasheet on the op amp in case anyone is interested.The other positives about this op amp is it’s cheap, you only need 1 for the circuit and you don’t have to worry about virtual grounds or trying to separate the input and output grounds.  Also, when you first look at the schematic it might seem that there are 2 op amp IC’s.  There is actually only one and is done this way so it is easier to design.The end result is a high quality, high performance portable device that is relatively easy to build and will change the way you listen to music from your phone.ne5532.pdfDownloadschematic.fzzDownload


## Step 2: Tools and Parts

![Step 2: Tools and Parts image 1](images/step03_01.jpg)

![Step 2: Tools and Parts image 2](images/step03_02.jpg)

Parts:It might seem like you need a lot of parts buts most can be purchased in bulk and if you already mess about with electronics then you will probably have most of the components already.  1.       10K duel gang Potentiometer – eBay2.       Potentiometer knob - eBay3.       2 X 18K Resistor – metal film – eBay4.       4 X 68K resistor – metal film – eBay5.       47K resistor - eBay6.       5mm LED – eBay7.       NE5532 IC – eBay (10 IC's for just over a dollar!)8.       8 pin socket holder - eBay9.       SPDT switch - eBay10.   3 X 4.7uf capacitor – eBay11.   2 X 22pf ceramic capacitor – eBay12.   3 X 220uf capacitor – eBay13.   2 X 3.5mm stereo jack socket – eBay14.   Prototype board - eBay15.   9v battery holder - eBay16.   9v battery17.   Wires18.   Case.  I used a small tin case - check out eBay if you want to use one similar.  You could use a tobacco tin or an altoids tin or something similar - eBay19.   You’ll also need a male to male 3.5mm cord - eBayTools1.       Drill2.       Soldering iron3.       Pliers4.       Wire cutters5.       The usual, basic tools that you have in your tool box


## Step 3: Making the Circuit - Part 1

![Step 3: Making the Circuit - Part 1 image 1](images/step04_01.jpg)

![Step 3: Making the Circuit - Part 1 image 2](images/step04_02.jpg)

![Step 3: Making the Circuit - Part 1 image 3](images/step04_03.jpg)

![Step 3: Making the Circuit - Part 1 image 4](images/step04_04.jpg)

First thing to do is to take a good look at the circuit design and breadboard it to make sure it works for you. NOTE – Although it might look like there are 2 IC's in the schematic, it's actually only one which has been split.  This allows for a clearer schematicSteps:1.       Solder the 8 pin socket into the prototype board.  Make sure you give yourself enough room on either side if the socket, you can always trim the prototype board later once you have finished the circuit2.       Solder one of the 68K resistors to pins 1 and 2 and also another to pins 6 and 73.       Solder a 22pf cap to exactly the same pins


## Step 4: Making the Circuit - Part 2

![Step 4: Making the Circuit - Part 2 image 1](images/step05_01.jpg)

![Step 4: Making the Circuit - Part 2 image 2](images/step05_02.jpg)

![Step 4: Making the Circuit - Part 2 image 3](images/step05_03.jpg)

As you are building the circuit, you’ll start to run out ofroom quickly on pins 2 and 3 on the IC.  Just make sure that you try and make room for all of the components.  Steps:1.       Next, you need to add the 220uf capacitors for the output socket.  2.       Solder the positive leg on the cap to pin 1 on the IC.  Solder the ground leg to a solder point on the prototype board that is open3.       Solder the positive leg on another 220uf cap to pin 7 on the IC.  Again, solder the ground leg to a solder point that is open4.       Pin 3 needs to have 3 components attached to it.  2 68K resistors need to be connected to pin 3.  One then needs to be connected to ground and the other positive.5.        Next, you need to add a 4.7uf cap.  Solder the positive leg to pin 3 and the ground leg to ground on the prototype boardSee I told you it starts to get a little squashy on the board


## Step 5: Making the Circuit - Part 3

![Step 5: Making the Circuit - Part 3 image 1](images/step06_01.jpg)

![Step 5: Making the Circuit - Part 3 image 2](images/step06_02.jpg)

![Step 5: Making the Circuit - Part 3 image 3](images/step06_03.jpg)

![Step 5: Making the Circuit - Part 3 image 4](images/step06_04.jpg)

![Step 5: Making the Circuit - Part 3 image 5](images/step06_05.jpg)

Steps:1.       Solder an 18k resistor to pin 2 on the IC.  The other leg solder to an open solder point on the prototype board2.       Next, solder the positive leg of a 4.7uf cap to the other leg of the 18k resistor.  The other leg solder to a spare solder point on the board.  This will later be connected to the potentiometer and output section of the amp.3.       Now you need to do the same thing for the other channel on your headphones.  This time, add a 18K resistor to pin 6 on the IC.  The ground leg on the cap solder to an open solder point on the prototype board4.       Solder the positive leg from a 4.7uf cap to the other leg of the 18K resistor – same as pin 2.  Solder the ground leg to an open solder point on the prototype board5.       Connect pin 4 to ground 6.       Connect pin 8 to positive7.      You also need to connect pins 3 and 5 together.  I do this underneath the circuit with aresistor leg.


## Step 6: Making the Circuit - Part 4

![Step 6: Making the Circuit - Part 4 image 1](images/step07_01.jpg)

![Step 6: Making the Circuit - Part 4 image 2](images/step07_02.jpg)

![Step 6: Making the Circuit - Part 4 image 3](images/step07_03.jpg)

![Step 6: Making the Circuit - Part 4 image 4](images/step07_04.jpg)

![Step 6: Making the Circuit - Part 4 image 5](images/step07_05.jpg)

![Step 6: Making the Circuit - Part 4 image 6](images/step07_06.jpg)

That’s all of the components connected.  I later decided to add an LED as well so just follow the below if you want to do this as well.Steps:1.       First connect both the ground and positive bus strips on the prototype board with some wire2.       Next, add 4 lengths of wire to ground bus strip 3.       Add a couple of wires to the ground legs on the 4.7uf caps 4.       Do the same to the ground legs on the 220uf caps5.       You also need to add a wire to each of the positive and ground bus strips for power6.       If you want to add an LED “on” indicator, solder a 20k resistor to ground and then to a spare solder point.  Solder a wire to the other end of the resistor.7.       Lastly, trim the circuit board to size.  That’s it for the board, now it’s time to build the case


## Step 7: Pick a Case

![Step 7: Pick a Case image 1](images/step08_01.jpg)

![Step 7: Pick a Case image 2](images/step08_02.jpg)

![Step 7: Pick a Case image 3](images/step08_03.jpg)

Picking the right case in my opinion, is just as important as getting the electronics working.  It took me awhile to find just the right tin for this project, which a friend actually gave to me.  Initially I made a couple of different ones out of wood but I didn’t go with a wood case in the end as it just wasn’t working for me.If you are looking for an old tin case, then you can always try eBay.  Just type in Tobacco tin and you’ll come across heaps of them.  You can also use an Altoids tine which you can now buy in many different designsSteps:1.       The most important thing about finding the right case is to ensure that you will be able to fit the battery and circuit inside.  You’ll also need to add a couple of 3.5mm sockets, a switch and a volume pot to it so make sure you have a little wiggle room for all of the components2.       Place the circuit inside the case and if necessary, trim the edges so you can push it right up against the side of the case3.       If everything fits ok then you can start to drill all of the holes needed to add the components


## Step 8: Adding the Auxiliary Parts to the Case

![Step 8: Adding the Auxiliary Parts to the Case image 1](images/step09_01.jpg)

![Step 8: Adding the Auxiliary Parts to the Case image 2](images/step09_02.jpg)

![Step 8: Adding the Auxiliary Parts to the Case image 3](images/step09_03.jpg)

![Step 8: Adding the Auxiliary Parts to the Case image 4](images/step09_04.jpg)

![Step 8: Adding the Auxiliary Parts to the Case image 5](images/step09_05.jpg)

![Step 8: Adding the Auxiliary Parts to the Case image 6](images/step09_06.jpg)

As there isn’t much room in the case, you will need to really think about where you add all of the axillary components.  Don’t just start drilling holes into the case, place the circuit and battery inside it and think about the best spots to add the sockets etc.  Remember, the amp will probably sit in your pockets so you need to think about having the sockets facing up etc.Steps1.            Drill 2 holes for the 3.5mm sockets.  Try to put these close together and have them so if the case is in your pocket, they will be facing upwards.2.            Drill a hole for the SPDT switch 3.            Drill a hole for the potentiometer4.            You can’t see it in the images, but you also need to drill a small hole for the LED.  Try to get this as close to the switch as possible.5.            Once all of the holes are drilled, you can then add all of the auxiliary parts to the case.


## Step 9: Wiring-up the Circuit and Toubleshooting

![Step 9: Wiring-up the Circuit and Toubleshooting image 1](images/step10_01.jpg)

![Step 9: Wiring-up the Circuit and Toubleshooting image 2](images/step10_02.jpg)

![Step 9: Wiring-up the Circuit and Toubleshooting image 3](images/step10_03.jpg)

![Step 9: Wiring-up the Circuit and Toubleshooting image 4](images/step10_04.jpg)

![Step 9: Wiring-up the Circuit and Toubleshooting image 5](images/step10_05.jpg)

![Step 9: Wiring-up the Circuit and Toubleshooting image 6](images/step10_06.jpg)

![Step 9: Wiring-up the Circuit and Toubleshooting image 7](images/step10_07.jpg)

![Step 9: Wiring-up the Circuit and Toubleshooting image 8](images/step10_08.jpg)

It’s now time to solder the wires from the circuit board to the auxiliary parts on the case.  This can be a little fiddly, especially if you gave a small case.  Wires take up a surprising amount of room so make sure you trim them as much as you can before attaching them.  You want to make sure though that you can lift the circuit board up and check underneath and problem solve if necessary.Steps:1.       Place the circuit board into the case2.       Using the schematic as a reference, solder each wire to the corresponding component.  3.       Trim the wires beforehand though and make sure that they are as short as possible.  This helps to reduce the space wires take-up and can help with better sound quality (the less the distance between components, the shorter the signal has to travel.4.        Once you have everything connected, you are ready to test.  Plug in a battery and turn on the switch.  If the LED come on then that’s the first good sign.  Now add a lead to the input and plug it into your phone (or MP3 player)5.       Plug your headphones into the output socket and play some music.  Make sure, though you don’t have the volume turned right up on the amp.6.       If you can hear music, congrats you managed to make the circuit without any mistakes.  If you hear nothing, then you’ll need to troubleshoot.Troubleshooting1.       Check the solder joins on the prototype board and make sure none are cross soldered2.       Double check the wiring to the components and make sure that these are wired-up correctly.3.       If you only hear out of one speaker, check that you have connected the sockets correctly.  Usually, the larger solder lug on the socket is ground.  The other 2 are either the inputs or outputs.  It doesn’t matter though in what order you wire these up to the prototype board.  Also, make sure you have connected pins 3 and 5 together or only 1 speaker will work.4.       Make sure that you have connected the IC correctly.  I managed to connect pin 8 to ground instead of positive.


## Step 10:


---
*41 images archived*
