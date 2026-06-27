# Electronic Cricket Game

Source: https://www.instructables.com/Electronic-Cricket-Game/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step02_01.jpg)

![Step 1: Parts and Tools image 2](images/step02_02.jpg)

![Step 1: Parts and Tools image 3](images/step02_03.jpg)

![Step 1: Parts and Tools image 4](images/step02_04.jpg)

![Step 1: Parts and Tools image 5](images/step02_05.jpg)

The project is made up of 2 different circuits.  One for the actual cricket game and one for scoring.  I have listed the parts for each circuit belowCricket Game Parts1.       Perf Board - eBay2.       555 Timer IC – eBay3.       4017 IC - eBay4.       2 X 12K Resistors – eBay6. 50K Potentiometer - eBay. This is used instead of the 100R resistor on the LED's.  It gives you the ability to control the brightness of the LED's7.       1uf Capactor – eBay8.       10p (0.01) Capacitor – eBay9.       2.2 uf Capacitor – eBay (you may have noticed that this isn’t in the schematic.  I use this later in the build so the player has the ability to slow down the LED’s if they wish to.  It isn’t necessary to add this if you don’t want to10.   Momentary Button – eBay11.   2 X red LED’s - eBay12.   4 X Green LED’s13.   2 X Blue LED’s14.  50K Potentiometer - eBay.  This is used instead of the 100R resistor on the LED's.  It gives you the ability to control the brightness of the LED's15. On/off switch - eBay16.  9V Battery Holder - eBay17.  9 V BatteryScoring Circuit Parts1.       2 X 7 Segment displays – eBay2.       10K Resistor - eBay3.       20K resistor – eBay4.       2 X Momentary switches – eBay5.       555 IC – eBay6.       2 X 4026 IC’s – eBay7.       Perf Board – eBay


## Step 2: Bread-boarding the Circuits

![Step 2: Bread-boarding the Circuits image 1](images/step03_01.png)

![Step 2: Bread-boarding the Circuits image 2](images/step03_02.png)

![Step 2: Bread-boarding the Circuits image 3](images/step03_03.gif)

![Step 2: Bread-boarding the Circuits image 4](images/step03_04.gif)

First things first - you should always breadboard your circuits first to make sure that the work.  The initial schematic that I used for the scoreboard worked really well but I accidentally deleted it and couldn't find it again on-line.  I did find another and it seemed to do the trick.Once you have made the circuits and everything is working as it should be, it's then time to move onto soldering the first one together which will be the actual cricket game. You can find the original circuit design website for the cricket game hereYou can find the original circuit design website for the scoreboard here


## Step 3: Cricket Match Game - Circuit

![Step 3: Cricket Match Game - Circuit image 1](images/step04_01.png)

![Step 3: Cricket Match Game - Circuit image 2](images/step04_02.jpg)

This circuit is pretty straight forward but like the scoreboard, it will need a lot of wires to connect all of the LED's together.  Note that there is a 100R resistor that connects the negative from the LED's to ground.  I decided to replace this with a 50K potentiometer so I could dim the LED's as they were very bright.  Up to you though if you want to replace it or not.Also, this game could be replaced with any game you want.  If football is your sport or baseball, then adapting this would be very easy - you just need a different scoring system.I also added a couple of Capacitors to the 555 IC so I could change the speed of the flashing LED's.  You can either have it on fast mode or slow mode in case you keep on going out!


## Step 4: Soldering the IC's and Wiring the 555

![Step 4: Soldering the IC's and Wiring the 555 image 1](images/step05_01.jpg)

![Step 4: Soldering the IC's and Wiring the 555 image 2](images/step05_02.jpg)

![Step 4: Soldering the IC's and Wiring the 555 image 3](images/step05_03.jpg)

![Step 4: Soldering the IC's and Wiring the 555 image 4](images/step05_04.jpg)

![Step 4: Soldering the IC's and Wiring the 555 image 5](images/step05_05.jpg)

I'll go through each of the steps and in most of them I have progressive images to help.  However, I did make a coulple of mistakes which I had to fix up later and will highlight these as I go along.Steps:1.  First solder the 555 and 4017 IC to a perf board.  You can see that the perf board that I used has 2 solder strips on either side which I will be using to connect the positive and negative connections.2.  Next solder pin 1 from the 555 to ground3.  The capacitor attached to pin 2 controls the speed of the LED's.  To be able to change the speed of the LED's I added a 2.2uf capacitor as well.  Solder both positive legs of each capacitor to pin 2 and solder the negative legs to areas on the perf board that aren't used.  You will later attach wires to these and then to a switch.


## Step 5: Continuing to Wire the 555

![Step 5: Continuing to Wire the 555 image 1](images/step06_01.jpg)

![Step 5: Continuing to Wire the 555 image 2](images/step06_02.jpg)

![Step 5: Continuing to Wire the 555 image 3](images/step06_03.jpg)

![Step 5: Continuing to Wire the 555 image 4](images/step06_04.jpg)

Steps:1.  Pins 2 and 6 need to be soldered together.  I just added a small piece of wire to the underside of the circuit as you can see in the image below2.  Next you need to solder pin 4 and 8 to positive3  The 2 12K resistors need to be added next.  solder one to pin 6 and 7 and one to pin 7 and somewhere blank of the perf board.  You will attaching a wire to this and to positive later for the switch to play the game


## Step 6: Continuing to Wire the 555

![Step 6: Continuing to Wire the 555 image 1](images/step07_01.jpg)

![Step 6: Continuing to Wire the 555 image 2](images/step07_02.jpg)

![Step 6: Continuing to Wire the 555 image 3](images/step07_03.jpg)

Steps:1.  It's now time to add a wire from the 555 IC to 4017 IC.  Solder a wire to pin 3 on the 555 to pin 14 on the 40172.  Next solder a 10K resistor to pin 3 on the 555 to ground3.  Next you need to solder the 0.01 capacitor from pin 5 to ground.


## Step 7: Wiring the 4017 - Attach the Ground Wires

![Step 7: Wiring the 4017 - Attach the Ground Wires image 1](images/step08_01.jpg)

![Step 7: Wiring the 4017 - Attach the Ground Wires image 2](images/step08_02.jpg)

![Step 7: Wiring the 4017 - Attach the Ground Wires image 3](images/step08_03.jpg)

That's it for the 555, it's now time to move onto the 4017 ICSteps:1.  Attach pins 8, 11 and 13 to ground


## Step 8: 4017 IC Pin 16, 9 and 15

![Step 8: 4017 IC Pin 16, 9 and 15 image 1](images/step09_01.jpg)

![Step 8: 4017 IC Pin 16, 9 and 15 image 2](images/step09_02.jpg)

Steps:1.  Solder pin 16 to positive2.  Pins 9 and 15 need to be attached together.  T do this just add a bridging wire to each of the pins.That's all of the circuit board wiring that needs to be done.  Now it's time to add all of the wires for the switches and LED's


## Step 9: Adding the Wires

![Step 9: Adding the Wires image 1](images/step10_01.jpg)

![Step 9: Adding the Wires image 2](images/step10_02.jpg)

![Step 9: Adding the Wires image 3](images/step10_03.jpg)

Steps:1.  First attach the wires for the game switch.  You need to attach one to the 12K resistor and also one to positive2.  Next you need to attach wires to the capacitors and also a wire to ground.  You might notice that I soldered 2 wires to ground but you only need one.  3.  Add a wire to the positive and negative sections.  These will provide power to the circuit3.  Lastly you will need to soldered all of the 8 wires for the LED's.  Just follow the schematic which shows which pins to solder the wires to.Done!  It's time to move onto the case and add the LEDs switches and knobs for the game


## Step 10: Modding the Case

![Step 10: Modding the Case image 1](images/step11_01.jpg)

![Step 10: Modding the Case image 2](images/step11_02.jpg)

![Step 10: Modding the Case image 3](images/step11_03.jpg)

![Step 10: Modding the Case image 4](images/step11_04.jpg)

![Step 10: Modding the Case image 5](images/step11_05.jpg)

I was lucky to find an almost perfect case for this game build.  It was an old battery tester and had plenty of room inside for all of the electronics.  You could use a cigar box which was also something I was considering until I stumbled across this little beauty.Steps:1.  First I pulled the case apart2.  Next I removed any old electronics and also removed any plastic gussets which were taking up room inside the case3.  Lastly I gave it a good clean


## Step 11: Adding the 7 Segment Displays

![Step 11: Adding the 7 Segment Displays image 1](images/step12_01.jpg)

![Step 11: Adding the 7 Segment Displays image 2](images/step12_02.jpg)

![Step 11: Adding the 7 Segment Displays image 3](images/step12_03.jpg)

![Step 11: Adding the 7 Segment Displays image 4](images/step12_04.jpg)

![Step 11: Adding the 7 Segment Displays image 5](images/step12_05.jpg)

![Step 11: Adding the 7 Segment Displays image 6](images/step12_06.jpg)

You will need to decide where to put the scoreboard.  After a bit of thought, I found the best spot was on the clear plastic cover of the battery tester.Steps:1.  First I made a couple of cuts into the plastic cover.  This was so I could push the pins from the 7 segment display though them.2.  Once I was happy with how it was fitting, I added some superglue and secured them to the front of the cover.Remember, this might be completely different from the way that you attach yours so  just work out what is best for you


## Step 12: Front Cover for Game

![Step 12: Front Cover for Game image 1](images/step13_01.png)

![Step 12: Front Cover for Game image 2](images/step13_02.jpg)

![Step 12: Front Cover for Game image 3](images/step13_03.jpg)

![Step 12: Front Cover for Game image 4](images/step13_04.jpg)

To make the front cover I just got an image from the net and sized it to fit onto the front of my case.  As you case will probably be different to mine, just find the image you want to used and size it for your case.I went through a few before I decided on the final one.  That's because I had some trouble gluing it down.  I used spray adhesive first but the paper didn't sit flat.  I then added some thin cardboard to the back and glued it down with some modge podge which seemed to do the trickThe little "X's" on the image is where I added LED's.  I used a hole punch to make the holes


## Step 13: Switches and LED's

![Step 13: Switches and LED's image 1](images/step14_01.jpg)

![Step 13: Switches and LED's image 2](images/step14_02.jpg)

![Step 13: Switches and LED's image 3](images/step14_03.jpg)

![Step 13: Switches and LED's image 4](images/step14_04.jpg)

Once you have built the game circuit, it's then time to mod the case.  You could make both circuits first I guess but I wanted to make sure the game section worked before starting on the scoring section.Steps:1.  Drill the holes for the LED's.  I used the artwork (a spare one I printed off) as a template and drilled the holes where indicated on the cover2.  Next I super glued the LED's into place making sure that the polarities were all in the same direction.3.  The switches came next.  You will need to attach the following switches - momentary switches, one for the game activation, one for scoring and one to re-set the scoreboard.  - on/off toggle switch to turn everything on and off.- Lastly, a switch need to be added to be able to change the speed of the flashing LED's.  This needs to be a on/off/on switch4.  Work out the best place to add these switches, drill the holes and secure them into place.  Wiring everything will come soon.


## Step 14: Wiring the LED's

![Step 14: Wiring the LED's image 1](images/step15_01.jpg)

![Step 14: Wiring the LED's image 2](images/step15_02.jpg)

![Step 14: Wiring the LED's image 3](images/step15_03.jpg)

![Step 14: Wiring the LED's image 4](images/step15_04.jpg)

![Step 14: Wiring the LED's image 5](images/step15_05.jpg)

![Step 14: Wiring the LED's image 6](images/step15_06.jpg)

Steps:1.  First you need connect all of the negative together.   Bend the legs over and solder all of the negatives to each other.2.  I had to add a jumper wire to the LED's to each group of 4.3.  Next thing to do is to solder all of the LED wires from the circuit to the positive legs on the LED's.  If you solder them in order on the schematic then they will flash in sequence.  As I wanted to try and make it as random as possible I mixed the sequence up and just soldered them to random legs on the LED's


## Step 15: Soldering the Switches

![Step 15: Soldering the Switches image 1](images/step16_01.jpg)

![Step 15: Soldering the Switches image 2](images/step16_02.jpg)

![Step 15: Soldering the Switches image 3](images/step16_03.jpg)

![Step 15: Soldering the Switches image 4](images/step16_04.jpg)

Steps:1.  First switch I started with was the change of speed for the LED's.  Solder one of the wires from the capacitors to the first solder point on the switch.2.  Solder the wire from the negative section on the circuit board to the middle solder point.3.  Lastly, solder the wire from the other capacitor to the last solder point on the switch.  This will allow you now to change the speed of the LED's from very fast, random flashing to more of a slower, repetitive  flashing.4.  Attach the positive wire that was soldered on for power to the solder point on the toggle switch.  Solder another wire on the other solder point on the switch.  This will be connected to the battery5.  Lastly, you need to solder the wires to pay the game to the momentary switch.Now everything is wired up, test to make sure the game is working by adding a 9v battery to the positive and negative wires and making sure the game works.  Are the LED's flashing?  good, next hit the game button which will stop the LED's flashing and only have one on.  If everything works as it should, move onto the next circuit, if not, faut find the circuit and try and identify the issue.


## Step 16: 7 Segment Display - Score Counter

![Step 16: 7 Segment Display - Score Counter image 1](images/step17_01.png)

Now it's time to start the scoring circuit.  There were a couple of issues with the design which I have fixed on the attached schematic.  Make sure you breadboard the circuit first and make sure you understand the design.Strangely, the design wasn't quite right and I found that it was missing connections to pin 16 on both 4026 IC's.  I have added these in along with a momentary switch on pin 15 on the 2nd IC.  the switch is used to re-set the scoreboard but you could also scrap this and just turn the game off and on.


## Step 17: Adding IC 's and Wiring the 555

![Step 17: Adding IC 's and Wiring the 555 image 1](images/step18_01.jpg)

![Step 17: Adding IC 's and Wiring the 555 image 2](images/step18_02.jpg)

![Step 17: Adding IC 's and Wiring the 555 image 3](images/step18_03.jpg)

![Step 17: Adding IC 's and Wiring the 555 image 4](images/step18_04.jpg)

Steps:1.  First thing to do is to solder on the IC's.  Solder the 555 first and then the 2 4026 IC's into place.  Give yourself some space between them as you might need to run wires between the IC's2. I'll start with the wiring of the 555.  connect pin 1 to ground3.  Connect pin 2 and positive with a 10k resistor4.  Connect pin 4 and 8 to positive


## Step 18: Wiring the 555 - Continued

![Step 18: Wiring the 555 - Continued image 1](images/step19_01.jpg)

![Step 18: Wiring the 555 - Continued image 2](images/step19_02.jpg)

![Step 18: Wiring the 555 - Continued image 3](images/step19_03.jpg)

![Step 18: Wiring the 555 - Continued image 4](images/step19_04.jpg)

![Step 18: Wiring the 555 - Continued image 5](images/step19_05.jpg)

Steps:1.  Connect pins 6 and 7 together.  I just added some extra solder to the pins2.  Connect the 22uf capacitor to pin 6.  for those eagle eyed out there you will notice that I connected it to pin 5!  I changed this later but it should of been pin 63.  Next I added a couple of jumper wires to connect the positive and ground solder runs on the board.4.  Lastly connect pin 3 from the 555 to pin 1 on the second 4026 IC.


## Step 19: Wiring the 4026 IC's

![Step 19: Wiring the 4026 IC's image 1](images/step20_01.jpg)

![Step 19: Wiring the 4026 IC's image 2](images/step20_02.jpg)

![Step 19: Wiring the 4026 IC's image 3](images/step20_03.jpg)

![Step 19: Wiring the 4026 IC's image 4](images/step20_04.jpg)

I connected the 2nd 4026 IC up first Steps:1.  Connect pin 2 to ground2.  Connect pin 3 to positive3.  Connect pin 15 to ground4.  Connect pin 16 to positive


## Step 20: Wiring the 4026 IC's - Continued

![Step 20: Wiring the 4026 IC's - Continued image 1](images/step21_01.jpg)

![Step 20: Wiring the 4026 IC's - Continued image 2](images/step21_02.jpg)

![Step 20: Wiring the 4026 IC's - Continued image 3](images/step21_03.jpg)

![Step 20: Wiring the 4026 IC's - Continued image 4](images/step21_04.jpg)

Now it's time to wire-up the first 4026 IC.  This is connected exactly the same as the 2nd IC, except there is a wire connecting both of the together which is included in the steps.Steps:1.  Connect pin 1 on the first 4026 IC to pin 5 on the 2nd IC2.  Connect pin 2 to ground3.  Connect pin 3 to positive 4.  Connect pin 15 to ground 5.  Connect pin 16 to positive


## Step 21: Adding the Wires.

![Step 21: Adding the Wires. image 1](images/step22_01.jpg)

![Step 21: Adding the Wires. image 2](images/step22_02.jpg)

![Step 21: Adding the Wires. image 3](images/step22_03.jpg)

![Step 21: Adding the Wires. image 4](images/step22_04.jpg)

![Step 21: Adding the Wires. image 5](images/step22_05.jpg)

![Step 21: Adding the Wires. image 6](images/step22_06.jpg)

Now it's time to solder on all of the wires for the 7 segment displays and a few other wires for switches and powerSteps:1.  First solder wire to pin 2 on the 555 and then ground.  This will be attached to the momentary switch to change the numbers on the scorecard2.  Next it's time to attach the 8 wires needed for the 7 segment displays.  I did the first 4026 first and then wired up the second one.  Solder each wire to the relevant pins on the 4026.3.  After soldering all of the wires to the circuit board I then put them in order and secured them in place with a thin wire which I soldered into place on the perf board.4.  Do the same for the other 4026.5.  Next, solder a wire from pin 15 on the 2nd 4026 and another to positive.  These will be attached to a momentary switch so you can re-set the scoreboard.6.  Lastly, solder a wire to positive and ground.  This will be attached the other boards (the game board) to the positive and ground section and will power it.That's all of the wiring done.  Now it's just a simple task of attaching all of the wires to the 7 segment displays and switches!


## Step 22: Soldering the Wires to the 7 Segment Displays

![Step 22: Soldering the Wires to the 7 Segment Displays image 1](images/step23_01.jpg)

![Step 22: Soldering the Wires to the 7 Segment Displays image 2](images/step23_02.jpg)

![Step 22: Soldering the Wires to the 7 Segment Displays image 3](images/step23_03.jpg)

![Step 22: Soldering the Wires to the 7 Segment Displays image 4](images/step23_04.jpg)

Now the fun part - soldering all of the wires to the solder points on the 7 segment displays!Steps:1.  Tin all of the solder points on the 7 segment displays.2.  Tin all of the wires on the 4026 IC's3.  Start with pin 6 on the first 4026 IC and solder to the relevant pin on the 7 segment display.4.  Continue to carefully solder the wires to each of the pins on the display making sure that they are correctly soldered to the right pins.5.  Once they are all soldered into place do the same for the other 4026.6.  You also need to attach a wire from the bottom, middle pin on each of the 7 segment displays to ground as well.


## Step 23: Final Wiring

![Step 23: Final Wiring image 1](images/step24_01.jpg)

![Step 23: Final Wiring image 2](images/step24_02.jpg)

![Step 23: Final Wiring image 3](images/step24_03.jpg)

![Step 23: Final Wiring image 4](images/step24_04.jpg)

![Step 23: Final Wiring image 5](images/step24_05.jpg)

![Step 23: Final Wiring image 6](images/step24_06.jpg)

![Step 23: Final Wiring image 7](images/step24_07.jpg)

Steps:1.  Solder the wires from the 555 and ground to the momentary switch which will change the scoreboard2.  Solder the wire from pin 15 of the 4026 IC and the positive wire to another momentary switch.  This will allow you to re-set the scoreboard.3.  Solder the other positive wire to the positive section on the 555 circuit and do the same for the ground.  This will power the scoreboard.4.   Lastly, wire the ground wire from the battery holder to the 555 timer ground section.  Solder the positive wire from the 555 circuit to the on/off switch.5.  Attach a battery and see if everything works.  If you are lucky (I wasn't) the scoreboard will come on and the LED's will be flashing madly.  If not, you'll need to check your connections and make sure there are no short circuits anywhere.


## Step 24: Done

![Step 24: Done image 1](images/step25_01.jpg)

![Step 24: Done image 2](images/step25_02.jpg)

![Step 24: Done image 3](images/step25_03.jpg)

![Step 24: Done image 4](images/step25_04.jpg)

Now it is time to sit back and get a good cricket match started.I usually make the rule up that you cannot go out first ball and you have to go out twice before it’s the next players turn.   Have fun and don’t forget to post an image if you make your own


---
*100 images archived*
