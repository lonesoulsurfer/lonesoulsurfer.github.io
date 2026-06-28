# Crystal Skull Light Theremin 

Source: https://www.instructables.com/Crystal-Skull-Light-Theremin/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

I’ve been playing around with 555 timers a lot recently and decided to make myself a light Theremin. After some searching I found one which uses 2 photo cells and is kinda similar to an Atari punk console but without the pots.

I came up with the idea of adding the Theremin inside a resin skull! I had the mould of the skull lying around from another project and have been wanting to use it again for some time. The photo cells sit inside the skull and to play the Theremin you wave your hands around the skull to change the light hitting the photo cells which in turn changes the pitch of the Theremin.

I have included a step by step walkthrough of building the circuit for anyone new to electronics. It’s pretty straight forward though for anyone who has played around with circuits before.

Check out the video to see it in action.


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

![Step 1: Parts and Tools image 4](images/step01_04.jpg)

![Step 1: Parts and Tools image 5](images/step01_05.jpg)

![Step 1: Parts and Tools image 6](images/step01_06.jpg)

Parts:

Circuit

1. 2 X Photo Cells – [eBay](https://www.ebay.com.au/itm/20-30-50PCS-LDR-CDS-Photoresistor-Light-Dependent-Resistor-Sensor-GL5516/352201096453?hash=item5200d23d05:m:mYdhQMBERV5OlIHqc6GpO7g)

2. 1 X 5K Pot – [eBay](https://www.ebay.com.au/itm/5K-Ohm-16mm-Linear-Potentiometer-18T-Spline-Single-Horizontal-PCB-Pot-Alpha-B5K/253032246845?hash=item3ae9e5ae3d:g:Hz0AAOSwgv5ZXtFs)

3. 2 X 555 Timers – [eBay](https://www.ebay.com.au/itm/NE555-NE555P-Timer-IC-Texas-Instruments-8-DIP-Pack-of-10/162293413409?epid=22006040298&hash=item25c970f621:g:ctkAAOSwsGdasYLX)

4. .01 Capacitor has “104” on it – [eBay](https://www.ebay.com.au/itm/10-20-50Pcs-0-01uF-10N-50V-Z5U-5mm-Ceramic-Capacitor/162896826853?hash=item25ed6851e5:m:mWvX7a2XOFzP2cZrCzakCOw)

5. 1k Resistor – [eBay](https://www.ebay.com.au/itm/100PCS-1-4W-Metal-Film-Resistor-0-25W-1-Full-Range-of-Values-0-to-10M/262943308104?hash=item3d38a47948:m:m9AAPzkedx9P_upvXOpgF9Q)

6. 8 Ohm Speaker – [eBay](https://www.ebay.com.au/sch/i.html?_odkw=8ohm+5w&_osacat=0&_from=R40&_trksid=m570.l1313&_nkw=8ohm+5w+speaker&_sacat=0)

7. 9v Battery Holder – [eBay](https://www.ebay.com.au/itm/5PCS-9V-Battery-Holder-Box-Case-Pack-with-Wire-Lead-Cover-ON-OFF-Switch-New/162321778230?_trkparms=aid%3D555019%26algo%3DPL.BANDIT%26ao%3D1%26asc%3D20151005190540%26meid%3Dd959197c30854aa984249a7f1b1d00f6%26pid%3D100505%26rk%3D1%26rkt%3D1%26%26itm%3D162321778230&_trksid=p2045573.c100505.m3226)

8. 9v battery

9. Switch – [eBay](https://www.ebay.com.au/itm/Mini-Toggle-Switch-3-Way-On-On-On-6A-125VAC-3A-250VAC-6-Pin-4-Guitar-Bass-Pickup/282478510954?hash=item41c508036a:g:2tUAAOSw~FJZGSzG)

10. Perf board – [eBay](https://www.ebay.com.au/itm/Small-Breadboard-Layout-Prototyping-Board/253529968034?epid=944019644&hash=item3b07904da2:g:174AAOSwdkZbDziC:sc:AU_StandardDelivery!3796!AU!-1)

11. wire

12. Flickering [LED](https://www.ebay.com.au/itm/20pcs-3mm-Orange-Candle-Light-Flicker-Ultra-Bright-Flickering-LED-Leds-Lamp-New/321640252279?hash=item4ae340c377:g:q~kAAOSwYGFUs6Nr) – eBay (Optional. I decided to add an LED so it could be used as a lamp as well)

Resin Skull

1. Resin – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR12.TRC2.A0.H0.Xclear+casting+resin.TRS0&_nkw=clear+casting+resin&_sacat=0)

2. Skull Mould – [Etsy](https://www.etsy.com/au/listing/98703693/handmade-supercast-skull-latex-mould)

3. Copper wire – [eBay](https://www.ebay.com.au/itm/K-S-Round-Brass-Rod-2mm-Diameter-4-9863/122353517406?epid=682558292&hash=item1c7cd6835e:g:do8AAOSwr~lYoGPm)

4. Box for the skull to be mounted on and electronics to be stored in – up to you want you use.

Tools

1. Mixing cups for the resin

2. Soldering iron and solder

3. Pliers

4. Wire cutters

5. Drill

6. Ply wood (used to hold the mould in place)

7. Jigsaw


## Step 2: Making the Circuit - Adding the 555 Timers

![Step 2: Making the Circuit - Adding the 555 Timers image 1](images/step02_01.png)

![Step 2: Making the Circuit - Adding the 555 Timers image 2](images/step02_02.jpg)

![Step 2: Making the Circuit - Adding the 555 Timers image 3](images/step02_03.jpg)

The first thing to do is to add the 555 timers to the perf board

Steps:

1. Place the timers into the perf board making sure that they are close together as shown below. Also make sure that the little notch on the side is on the left hand side. This will orientate the 555 time correctly.

2. Solder all of the legs to the perf board


## Step 3: Making the Circuit - Pins 1, 2 and 6 on the First 555 Timer

![Step 3: Making the Circuit - Pins 1, 2 and 6 on the First 555 Timer image 1](images/step03_01.jpg)

![Step 3: Making the Circuit - Pins 1, 2 and 6 on the First 555 Timer image 2](images/step03_02.jpg)

![Step 3: Making the Circuit - Pins 1, 2 and 6 on the First 555 Timer image 3](images/step03_03.jpg)

![Step 3: Making the Circuit - Pins 1, 2 and 6 on the First 555 Timer image 4](images/step03_04.jpg)

![Step 3: Making the Circuit - Pins 1, 2 and 6 on the First 555 Timer image 5](images/step03_05.jpg)

![Step 3: Making the Circuit - Pins 1, 2 and 6 on the First 555 Timer image 6](images/step03_06.jpg)

The little legs on the 555 timers I will be calling pins and I will start with the 555 timer furthest of the left of the perf board. The perf board that I used has a section for all of the negative and positive connections to be soldered to. I find that this type of board is best to use in these projects

Steps:

1. Solder a wire to pin 1 and ground

2. Solder the 1k resistor to pins 2 and 7

3. Solder the 0.1 capacitor to pin 2 and ground

4. Lastly, solder a wire from pin 2 to 6. I usually do this underneath as shown in the below images with a leg from a resistor.


## Step 4: Making the Circuit - Pins 3 and 4 on the First 555 Timer

![Step 4: Making the Circuit - Pins 3 and 4 on the First 555 Timer image 1](images/step04_01.jpg)

![Step 4: Making the Circuit - Pins 3 and 4 on the First 555 Timer image 2](images/step04_02.jpg)

![Step 4: Making the Circuit - Pins 3 and 4 on the First 555 Timer image 3](images/step04_03.jpg)

Steps:

1. Solder a wire to pin 3 on the first 555 timer to pin 2 on the 2nd 555 timer

2. Solder a wire from pin 4 to positive


## Step 5: Making the Circuit - Pins 6 and 8 on the First 555 Timer

![Step 5: Making the Circuit - Pins 6 and 8 on the First 555 Timer image 1](images/step05_01.jpg)

To be able to connect the photo cells inside the resin skull, you will need to add 2 wires to the first 555 timer and 2 to the other one. I will do this a bit later

Steps:

1. Solder pin 8 to positive section on the circuit board

That’s all of the wiring for the first 555 timer. It’s now time to move onto the next one


## Step 6: Making the Circuit - Pins 1 and 3 on the Second 555 Timer

![Step 6: Making the Circuit - Pins 1 and 3 on the Second 555 Timer image 1](images/step06_01.jpg)

![Step 6: Making the Circuit - Pins 1 and 3 on the Second 555 Timer image 2](images/step06_02.jpg)

Steps:

1. Solder a wire to pin 1 and ground

2. Solder a long wire to pin 3. This will be attached to the 5K potentiometer. To connect a pot, you need to solder the end of the wire to the first 2 solder points on the pot.

3. We will solder the end of the wire from pin 3 to the potentiometer a little later on


## Step 7: Making the Circuit - Pins 4, 6 and 7 on the Second 555 Timer

![Step 7: Making the Circuit - Pins 4, 6 and 7 on the Second 555 Timer image 1](images/step07_01.jpg)

![Step 7: Making the Circuit - Pins 4, 6 and 7 on the Second 555 Timer image 2](images/step07_02.jpg)

![Step 7: Making the Circuit - Pins 4, 6 and 7 on the Second 555 Timer image 3](images/step07_03.jpg)

![Step 7: Making the Circuit - Pins 4, 6 and 7 on the Second 555 Timer image 4](images/step07_04.jpg)

Steps:

1. Solder a wire to pin 4 to positive

2. Solder the other 0.1 capacitor to pin 6 and ground. You will have to add a wire in order for the legs of the capacitor to reach both points as shown below.

3. Turn the board over and add some solder to legs 6 and 7 so they connect

4. Add a long wire to pin 7 on BOTH the 555 timers. these will connect to the Photo cells. You will also need to add a couple of wires to the positive section which is in the next step


## Step 8: Making the Circuit - Pin 8, 6 and Speaker Connection Second 555 Timer and Testing

![Step 8: Making the Circuit - Pin 8, 6 and Speaker Connection Second 555 Timer and Testing image 1](images/step08_01.jpg)

![Step 8: Making the Circuit - Pin 8, 6 and Speaker Connection Second 555 Timer and Testing image 2](images/step08_02.jpg)

![Step 8: Making the Circuit - Pin 8, 6 and Speaker Connection Second 555 Timer and Testing image 3](images/step08_03.jpg)

Steps:

1. Solder a wire to pin 8 to the positive section

2. Solder 3 long wires to the positive section. 2 will be used for the photo cells and the other to the positive end of the speaker.

3. Lastly solder 2 long wires to both the ground and positive sections on the perf board. These will be used to power the circuit

4. That’s all of the wiring done. Now it’s time to test. Connect a 9v battery to the circuit via the wires added for power.

5. Next, either solder the photo cells to the ends of the wires or used a bread board to make the connections.

6. Add power and test to make sure that when you cover either photo cell you get different tones from the circuit. If one doesn’t do anything, check your connections and test again.


## Step 9: Resin Skull - Preparing the Mould

![Step 9: Resin Skull - Preparing the Mould image 1](images/step09_01.jpg)

![Step 9: Resin Skull - Preparing the Mould image 2](images/step09_02.jpg)

![Step 9: Resin Skull - Preparing the Mould image 3](images/step09_03.jpg)

Steps:

1. On a piece of ply board, trace around the base of the mould

2. Next, make the trace outline you just did smaller by about 15mm. This is so the mould will sit inside the ply wood

3. Drill a hole in the inside of the circle so you can use a jigsaw to cut out the section marked

4. Cut out the area and place the skull mould inside to make sure it fits correctly.

5. Lastly, secure the ply wood so it is raised and also even.


## Step 10: Resin Skull - Adding the Photo Cells

![Step 10: Resin Skull - Adding the Photo Cells image 1](images/step10_01.jpg)

![Step 10: Resin Skull - Adding the Photo Cells image 2](images/step10_02.jpg)

![Step 10: Resin Skull - Adding the Photo Cells image 3](images/step10_03.jpg)

![Step 10: Resin Skull - Adding the Photo Cells image 4](images/step10_04.jpg)

![Step 10: Resin Skull - Adding the Photo Cells image 5](images/step10_05.jpg)

In order to be able to add the photo cells to the inside of the skull, you will need to first solder them to some copper wire

Steps:

1. Cut 4 lengths of copper wire. They will need to be about 150mm each in length

2. Slight bend the ends of each of the wire so when you attach the photo cells, they will face outwards inside the skull

3. Trim the legs on the photo cells and solder onto the ends of the copper wire. Do this for both


## Step 11: Resin Skull - Adding the Photo Cells

![Step 11: Resin Skull - Adding the Photo Cells image 1](images/step11_01.jpg)

![Step 11: Resin Skull - Adding the Photo Cells image 2](images/step11_02.jpg)

![Step 11: Resin Skull - Adding the Photo Cells image 3](images/step11_03.jpg)

![Step 11: Resin Skull - Adding the Photo Cells image 4](images/step11_04.jpg)

Next thing to do is to work out a way to hold the photo cells into place whist the resin sets hard

Steps:

1. Find a small piece of wood that is about 15mm wide and long enough to sit on top of the skull mould

2. Place one of the photo cells against the wood and tape into place

3. Go and check that the photo cell sits where you want it to in the skull and is not touching the sides of the mould.

4. Do the same for the other photo cell

5. Place onto the mould in preparation for the resin to be poured


## Step 12: Mixing and Pouring the Resin

![Step 12: Mixing and Pouring the Resin image 1](images/step12_01.jpg)

![Step 12: Mixing and Pouring the Resin image 2](images/step12_02.jpg)

![Step 12: Mixing and Pouring the Resin image 3](images/step12_03.jpg)

Your skull mould is ready to pour the resin

Steps:

1. Carefully mix the resin as per the instructions. Make sure you take your time when stirring so you don’t introduce any large bubbles.

2. Once thoroughly mixed, carefully pour the resin into the skull mould.

3. As resin does shrink once it is cured, it’s best to slightly overfill the mould

4. Leave to dry for 24 hours. If you are like me you will be tempted to start poking around earlier but it really is best to let the resin totally cure before trying to remove it from the mould


## Step 13: Polishing the Skull

![Step 13: Polishing the Skull image 1](images/step13_01.jpg)

![Step 13: Polishing the Skull image 2](images/step13_02.jpg)

![Step 13: Polishing the Skull image 3](images/step13_03.jpg)

![Step 13: Polishing the Skull image 4](images/step13_04.jpg)

![Step 13: Polishing the Skull image 5](images/step13_05.jpg)

![Step 13: Polishing the Skull image 6](images/step13_06.jpg)

![Step 13: Polishing the Skull image 7](images/step13_07.gif)

When you pull the skull out of the resin it will probablycome out dull looking. Now it’s time to start polishing


## Step 14: Speaker, Switch and Volume Knob

![Step 14: Speaker, Switch and Volume Knob image 1](images/step14_01.jpg)

![Step 14: Speaker, Switch and Volume Knob image 2](images/step14_02.jpg)

![Step 14: Speaker, Switch and Volume Knob image 3](images/step14_03.jpg)

![Step 14: Speaker, Switch and Volume Knob image 4](images/step14_04.jpg)

![Step 14: Speaker, Switch and Volume Knob image 5](images/step14_05.jpg)

You could make a box for the skull and electronics if you wanted to. I went down the path of least resistance and used a wooden box I had lying around.

Steps:

1. Decide where you want to add the speaker onto the box. Mark and cut out the hole using a hole saw drill bit.

2. Next secure the speaker into the hole of the box with some screws

3. Drill a couple of small holes, one for the 5K pot and the other for the on/off switch. Attach these parts to the box.


## Step 15: Add the Crystal Skull

![Step 15: Add the Crystal Skull image 1](images/step15_01.jpg)

![Step 15: Add the Crystal Skull image 2](images/step15_02.jpg)

You don’t actually secure the skull to the box in this part, you just make the holes in the box for the copper wires inside the skull to go through.

Steps:

1. Mark on the box where you need to drill for the copper rod to go into. You will need to drill 4 holes for each of the wires

2. Drill the holes and make sure that the copper rods in the skull fit into the holes correctly and that the skull sits nice and flat.


## Step 16: Wiring the Switch and Battery

![Step 16: Wiring the Switch and Battery image 1](images/step16_01.jpg)

![Step 16: Wiring the Switch and Battery image 2](images/step16_02.jpg)

The switch is a 3 way switch. This means that whist in the middle everything is off. If you move it up or down then you either turn on the Theremin or LED. First I will wire-up the Circuit board for the Theremin.

Steps:

1. Solder a positive wire from the circuit board to one of the solder points on the switch. It would be on one of the ends

2. Next, solder the positive wire from the battery holder to the middle solder point on the switch.

3. Solder the negative wire from the battery to the negative section on the circuit board


## Step 17: Wiring the Photo Cells

![Step 17: Wiring the Photo Cells image 1](images/step17_01.jpg)

![Step 17: Wiring the Photo Cells image 2](images/step17_02.jpg)

Now it’s time to wire the photo cells to the circuit board.

Steps:

1. Place the skull back onto the top of the case and push the copper wires through

2. Wire one of the positive wires from the circuit board to the first copper wire in the skull

3. Next, solder the wire from pin 7 on the first 555 timer to the other copper wire

4. Do the same thing for the other photo cell.

5. To keep the skull in place, bend the copper wires over as shown below.


## Step 18: Adding the Volume Knob and Speaker

![Step 18: Adding the Volume Knob and Speaker image 1](images/step18_01.jpg)

![Step 18: Adding the Volume Knob and Speaker image 2](images/step18_02.jpg)

Steps:

1. Solder the wire from pin 3 on the 2nd 555 timer to the potentiometer. When you solder this wire, you need to solder it to the first 2 solder points on the pot.

2. Next, solder a wire from the last solder point on the pot to the negative solder point on the speaker

3. Lastly, solder one of the wires that you soldered to the positive section on the circuit board to the positive solder point on the speaker

At this stage you can test the Theremin and make sure that everything is working. You should be able to change the pitch and tone of the 555 by waving your hands in front of the photo cells. If nothing happens try turning the volume switch to full. If nothing happens still, you may have to go over the circuit board to make sure you have wired everything up correctly.


## Step 19: Adding the LED

![Step 19: Adding the LED image 1](images/step19_01.jpg)

![Step 19: Adding the LED image 2](images/step19_02.jpg)

![Step 19: Adding the LED image 3](images/step19_03.jpg)

Nearly there!

Steps:

1. Drill a small hole into the lid of the case under the skull. Needs to be big enough to fit a 3mm LED

2. Solder a 40K resistor (or whatever you have that is close) to the negative leg of the LED.

3. Solder a wire to the end of the resistor and to the positive leg on the LED.

4. Add some heat shrink to each of the legs.

5. Super glue into place

6. Attach the positive wire to the other solder point on the switch (the opposite to the one that the Theremin circuit is attached to)

7. Solder the negative wire to the negative solder point on the circuit board

8. Test to make sure the LED come on

DONE!


## Step 20: Done

![Step 20: Done image 1](images/step20_01.jpg)

![Step 20: Done image 2](images/step20_02.jpg)

Now that you have finished, it’s time to play with your Theremin. I find that it works best not in direct sunlight or really bright lights, this could be different however for your build. Playing your light Theremin is pretty simple, you just wave your hands in front of the photo cells to change the pitch and tones.

After a while you start to work out how to make different sound effects by moving your hands slightly to change pitch.

I have managed to get some interesting sounds out of the light Theremin but you definitely wouldn’t use it to entertain your friends unless you want to un-friend them! Some of the tones generated are pretty harsh to anyone within earshot.


---
*71 images archived*
