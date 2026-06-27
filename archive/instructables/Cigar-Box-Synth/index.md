# Cigar Box Synth

Source: https://www.instructables.com/Cigar-Box-Synth/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)


## Step 1: Parts - Circuit

![Step 1: Parts - Circuit image 1](images/step02_01.jpg)

![Step 1: Parts - Circuit image 2](images/step02_02.jpg)

![Step 1: Parts - Circuit image 3](images/step02_03.jpg)

![Step 1: Parts - Circuit image 4](images/step02_04.jpg)

![Step 1: Parts - Circuit image 5](images/step02_05.jpg)

![Step 1: Parts - Circuit image 6](images/step02_06.jpg)

![Step 1: Parts - Circuit image 7](images/step02_07.jpg)

![Step 1: Parts - Circuit image 8](images/step02_08.jpg)

![Step 1: Parts - Circuit image 9](images/step02_09.jpg)

Parts:Potentiometers1.       4 X 100K - eBay2.       3 X 500K - eBay3.       10K – eBay4.       Knobs for the Pots - eBay  I brought these ones and these onesCapacitors1.       1uf – eBay2.       10uf - eBay3.       2 X 10nf – eBayResistors1.       470R – eBay2.       1K – eBay3.       100K – eBayIC’s1.       555 – eBay2.       556 – eBay3.       4107 - eBayOther Parts1.       4 X Red LED’s and 1 X white - eBay      2.       4 X 1N4148 Diode – eBay3.       Speaker Jack – eBay4.       Speaker – eBay5. Toggle Switches – eBay6. On/off switch - eBay6.       AA Battery Holder (4 X AA) – eBay7.       Batteries8.       Thin wire9.      Case to store the synth in.  I used a cigar box - eBay10. Prototyping Board - eBay11. Computer fan cover - I don't think you can get the exact one that I used any longer but you can get similar


## Step 2: The Circuit

![Step 2: The Circuit image 1](images/step03_01.png)

![Step 2: The Circuit image 2](images/step03_02.jpg)

![Step 2: The Circuit image 3](images/step03_03.jpg)

![Step 2: The Circuit image 4](images/step03_04.jpg)

![Step 2: The Circuit image 5](images/step03_05.jpg)

Before you even start to think about making this, I strongly suggest that you breadboard the circuit first.  I found the schematic a little confusing at first because I couldn’t work out how everything was attached to ground.  It wasn’t until I started to put it together that I realised that the designer used black and blue for ground. Once you breadboard everything up and it’s working, it’s time then to get cracking on the soldering.


## Step 3: Adding the IC's

![Step 3: Adding the IC's image 1](images/step04_01.jpg)

![Step 3: Adding the IC's image 2](images/step04_02.jpg)

![Step 3: Adding the IC's image 3](images/step04_03.jpg)

![Step 3: Adding the IC's image 4](images/step04_04.jpg)

First thing to do is to solder the IC’s into the Prototyping board. The board that I used was too large and I had to cut some off at the end.  However, I’d rather have too much board then not enough…Steps:1.       Solder on the 4017 IC first.  I orientated all of the IC’s with the notch on the left so make sure you do the same or the steps will be back to front for you.2.       Next, solder on the 555 IC.  Leave yourself a little room between each IC.3.       Lastly, solder on the 556 IC.


## Step 4: Adding the Connectors on the 4017 IC

![Step 4: Adding the Connectors on the 4017 IC image 1](images/step05_01.jpg)

![Step 4: Adding the Connectors on the 4017 IC image 2](images/step05_02.jpg)

![Step 4: Adding the Connectors on the 4017 IC image 3](images/step05_03.jpg)

![Step 4: Adding the Connectors on the 4017 IC image 4](images/step05_04.jpg)

![Step 4: Adding the Connectors on the 4017 IC image 5](images/step05_05.jpg)

The following steps will go through how to connect all of the IC’s together.  A leg on an IC I will call pin and I will start with the 4017 IC.  Adding wires to connect the potentiometers will come after all of the IC and components have been added to the board.   The jumper wires that I used a solid core wire which I find a lot easier to use then normal wire.The images in the ‘ible are in sequential order so you can use these to help guide you if necessary.  Make sure you have the schematic handy as well.Steps:1.       First connect pin 8 on the 4017 to pin 1 on the 555.  2.       Next connect pins 15 and 103.       Pin 13 is to be connected to ground.  The prototyping board I used has a ground and positive strip around the outside which really makes things easy when connecting all of the ground and positive wires.4.       Connect pin 14 on the 4017 to pin 3 on the 5555.       Lastly, connect pin 18 to the positive section on the prototyping board6.       You will need to add some wires to pins 2, 3, 4 and 7 later which will be connected to the pots.  I find that it’s easier to add these wires later as they just get in the way.


## Step 5: Adding the Parts and Connectors on the 555 IC

![Step 5: Adding the Parts and Connectors on the 555 IC image 1](images/step06_01.jpg)

![Step 5: Adding the Parts and Connectors on the 555 IC image 2](images/step06_02.jpg)

![Step 5: Adding the Parts and Connectors on the 555 IC image 3](images/step06_03.jpg)

![Step 5: Adding the Parts and Connectors on the 555 IC image 4](images/step06_04.jpg)

![Step 5: Adding the Parts and Connectors on the 555 IC image 5](images/step06_05.jpg)

![Step 5: Adding the Parts and Connectors on the 555 IC image 6](images/step06_06.jpg)

Steps:1.       Connect the 1 uf capacitor to pin 2 to ground, making sure that the positive wire on the capacitor is connected to the IC.2.       Next you need to add a 1k resistor and an LED to pin 3.  As the LED will be connected to the board with wires, I left this off for the time being and connected just the 1k resistor.  The resistor needs to be attached to pin 2 and ground.  Make sure that you leave a couple of holes between the pin and resistor so you can add the LED wires later3.       Connect pins 2 and 6 together4.       Add a 100k resistor between pins 6 and 75.       Connect pins 4 and 8 together6.       Lastly, connect pin 8 to positive7.       Adding the Potentiometer will come later


## Step 6: Adding the Parts and Connectors on the 556 IC

![Step 6: Adding the Parts and Connectors on the 556 IC image 1](images/step07_01.jpg)

![Step 6: Adding the Parts and Connectors on the 556 IC image 2](images/step07_02.jpg)

![Step 6: Adding the Parts and Connectors on the 556 IC image 3](images/step07_03.jpg)

![Step 6: Adding the Parts and Connectors on the 556 IC image 4](images/step07_04.jpg)

![Step 6: Adding the Parts and Connectors on the 556 IC image 5](images/step07_05.jpg)

![Step 6: Adding the Parts and Connectors on the 556 IC image 6](images/step07_06.jpg)

![Step 6: Adding the Parts and Connectors on the 556 IC image 7](images/step07_07.jpg)

![Step 6: Adding the Parts and Connectors on the 556 IC image 8](images/step07_08.jpg)

Steps:1.       Connect pins 1 and 2 together with a 1k resistor2.        Connect pins 2 and 6 together3.       Connect pin 6 to ground with a 10 nf capacitor4.       Connect pin 7 to ground5.       Connect pins 5 and 8 together6.       Connect pins 14 and 10 together7.       Connect pins 4 and 14 together8.       Connect pin 14 to positive9.       Connect pin 12 to ground using another 10 nf capacitor.There is 1 more connection to make in the next step on the 556


## Step 7: Adding More Parts and Connectors on the 556 IC

![Step 7: Adding More Parts and Connectors on the 556 IC image 1](images/step08_01.jpg)

![Step 7: Adding More Parts and Connectors on the 556 IC image 2](images/step08_02.jpg)

![Step 7: Adding More Parts and Connectors on the 556 IC image 3](images/step08_03.jpg)

Steps:1.       Connect the negative leg of a 10uf capacitor to pin 9.  The positive leg should be soldered also to the board but make sure you solder this to a spot not connected to anything else.  You will be soldering a wire to this leg to add a volume pot later on.2.       That’s it for the IC connections and components.  You next have to start adding wires for all of the connections that you need to make.  These will be attached to the pots, switches etc that first you need to attach to the case.


## Step 8: Adding the Wires

![Step 8: Adding the Wires image 1](images/step09_01.jpg)

![Step 8: Adding the Wires image 2](images/step09_02.jpg)

![Step 8: Adding the Wires image 3](images/step09_03.jpg)

![Step 8: Adding the Wires image 4](images/step09_04.jpg)

As this step is very hard to show in photographs, I will just go through which pins you need to add wires to for each IC.  Make sure that you use long wires as you can always trim them later.  Also, make sure you use thin wire.  It takes up a surprisingly large amount of space and can cause issues when adding to your case.  I pulled my wires from a NES controller copy that I had lying around.   Try and add the same coloured wire for each pot as it it easier to identify them later when you have to solder them to the solder points on the pots.Steps4017 IC1.       Attach wires to pins 2, 3, 4 and 7555 IC1.       Attach wires to pin 3 and to the resistor that is also in line with pin 3.  Remember that this is for the LED which will be attached to the case.  Actually, I made a slight change on this and decided to connect this LED up to a switch so I could turn it off.  It was a little annoying and I used a white LED which was very bright.  This LED indicates the speed of the synth.2.       Add wires to pins 7 and 8556 IC1.       Attach wires to the positive leg of the 10uf capacitor2.       Attach wires to pins 13 and also add one to positive3.       Attach a wire to pin 1 and also another to positiveYou will also need to add another wire to the positive which will be connected to the switch.It's time now to put the circuit board aside and start to work on the case.


## Step 9: Adding the Speaker

![Step 9: Adding the Speaker image 1](images/step10_01.jpg)

![Step 9: Adding the Speaker image 2](images/step10_02.jpg)

![Step 9: Adding the Speaker image 3](images/step10_03.jpg)

![Step 9: Adding the Speaker image 4](images/step10_04.jpg)

![Step 9: Adding the Speaker image 5](images/step10_05.jpg)

Now onto the Cigar box which will be the case to house all the electronics.  You could use whatever you want as long as it has enough room to fit all the parts.  I dig cigar boxes though.  They are ready made, look cool and have plenty of room to add the parts.Steps:1.       First thing to do is to remove the lid.  I find that it’s a lot easier to work with the lid removed.2.       Next have a think about your design and where you want to put all of the components.  Once you have a design in mind it’s time to add the speaker3.       Measure and cut a hole out for the speaker.  Secure it to the lid with some small screws.


## Step 10: Adding the Pots and On/Off Switch

![Step 10: Adding the Pots and On/Off Switch image 1](images/step11_01.jpg)

![Step 10: Adding the Pots and On/Off Switch image 2](images/step11_02.jpg)

![Step 10: Adding the Pots and On/Off Switch image 3](images/step11_03.jpg)

![Step 10: Adding the Pots and On/Off Switch image 4](images/step11_04.jpg)

![Step 10: Adding the Pots and On/Off Switch image 5](images/step11_05.jpg)

![Step 10: Adding the Pots and On/Off Switch image 6](images/step11_06.jpg)

![Step 10: Adding the Pots and On/Off Switch image 7](images/step11_07.jpg)

Next thing to do is to add the potentiometers.  As you can see from my design below, I added the 3 main pot to the bottom, the 4 tone sequencers around the speaker. Steps:1.       Carefully measure and drill out the holes for the 3 main pots.2.       Secure these in place.  If you want to use the same ones as me – then you can find them here3.       Next do the same for the sequencers.4.       Add the on/off switch and volume pot.5.       Add the red LED's above the sequencer pots.  Drill small holes above each one and super glue into place.  orientate the LED's so the short leg is on the left.  This will help you to know the polarities and also attached to the pot leg.6.      Lastly, add the white LED above the pot that will be the speed knob.


## Step 11: Wiring the 4 Sequencers

![Step 11: Wiring the 4 Sequencers image 1](images/step12_01.jpg)

![Step 11: Wiring the 4 Sequencers image 2](images/step12_02.jpg)

![Step 11: Wiring the 4 Sequencers image 3](images/step12_03.jpg)

![Step 11: Wiring the 4 Sequencers image 4](images/step12_04.jpg)

![Step 11: Wiring the 4 Sequencers image 5](images/step12_05.jpg)

Ok – now it’s time to start to wire-up the sequencers.  If you look at the schematic, you can see that there are diodes, LED’s and wires from the 4017 IC attached to the pots.  They are also all connected as well.  Steps:1.       The first thing to do is to connect all of the pots together.  How you attach the legs of the pots will determine how to tone is controlled.  I decided to connect all of the pot legs on the right together.   Add a small piece of wire between each one and solder to the right hand side leg of the pot as shown in the images.2.       Next you need to solder the positive leg of the LED (the longest one) to the left hand side leg of the pot.  Do this for each of the sequencers.  Make sure that you connect a 470R resistor to the last LED and also to the pot.  3.       Solder the negative leg of the LED to each other4.       Next you need to add a diode to each of the middle legs of the pots.  Connect the other ends of the diodes together


## Step 12: Final Wiring

![Step 12: Final Wiring image 1](images/step13_01.jpg)

![Step 12: Final Wiring image 2](images/step13_02.jpg)

![Step 12: Final Wiring image 3](images/step13_03.jpg)

![Step 12: Final Wiring image 4](images/step13_04.jpg)

![Step 12: Final Wiring image 5](images/step13_05.jpg)

![Step 12: Final Wiring image 6](images/step13_06.jpg)

![Step 12: Final Wiring image 7](images/step13_07.jpg)

Now it’s time to do the final wiring.  You will need to solder all of the wires from the circuit board to the pots, switches, etc.  Take your time when doing this and try not to get too tangled!Steps:1.       I started with the main pots first.  Carefully solder each of the wires to the legs of the pots.  If you look at the schematic, it tells you which legs to solder too.  However, it’s easy to get the direction wrong and you might find that turning the speed up actually turns it down.  If this happens, just de-solder the wire that is connected to the IC and solder onto the other leg of the pot.2.       Next solder the wires to the sequencer pots.  3.       Attach the wires for the switch and add the battery holderNow it’s time for the big test!  Add some batteries and see if you get any sound out of your synth.  If you don’t, try and turn the volume to full and turn the sequencer pots to mid-way.  Also make sure that the circuit board isn’t shorting – there are a lot of solder points and if they touch the back of a pot for example, they can connect and short.Usually when I do a build like this I get nothing first time and have to go over everything.  This time however I managed to get everything right first go!  Amazing considering how impatient I am.If yours doesn’t work, then you will need to go over and check your work – sorry…


## Step 13: Attaching the Circuity Board and Lid

![Step 13: Attaching the Circuity Board and Lid image 1](images/step14_01.jpg)

![Step 13: Attaching the Circuity Board and Lid image 2](images/step14_02.jpg)

![Step 13: Attaching the Circuity Board and Lid image 3](images/step14_03.jpg)

![Step 13: Attaching the Circuity Board and Lid image 4](images/step14_04.jpg)

![Step 13: Attaching the Circuity Board and Lid image 5](images/step14_05.jpg)

![Step 13: Attaching the Circuity Board and Lid image 6](images/step14_06.jpg)

![Step 13: Attaching the Circuity Board and Lid image 7](images/step14_07.jpg)

![Step 13: Attaching the Circuity Board and Lid image 8](images/step14_08.jpg)

Steps:1.       In order for the board not to shirt, you will need to add plastic or something similar underneath the board.  2.       Add some hot glue to the bottoms of the pots and glue the plastic down.  Don’t add too much in case you need to get to the wires later on.3.       Next add a small amount of hot glue to the plastic and stick down the circuit board4.       Re-attach the lid to the base of the cigar box.5.       Add a little Velcro to the bottom of the battery holder and stick into place6.       Test again to make sure everything is working as it should.


## Step 14: Final Touches

![Step 14: Final Touches image 1](images/step15_01.jpg)

![Step 14: Final Touches image 2](images/step15_02.jpg)

![Step 14: Final Touches image 3](images/step15_03.jpg)

![Step 14: Final Touches image 4](images/step15_04.jpg)

![Step 14: Final Touches image 5](images/step15_05.jpg)

![Step 14: Final Touches image 6](images/step15_06.jpg)


---
*86 images archived*
