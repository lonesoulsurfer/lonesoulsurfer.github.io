# Fizzle Loop Synth II

Source: https://www.instructables.com/Fizzle-Loop-Synth-II/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

This is my 2nd version of the fizzle loop synth and this time I use 4 x 555 times (yes you heard me right!)

Its circuit is really just 2 flashing LED circuits and also a light Theremin circuit mashed together. I’ve added a potentiometer to each LED to be able to dim it along with the ability to change capacitor and resistor values via switches. This gives you the ability to change the sound, tone and speed of the synth making for a much more varied sound machine then the first Fizzle Loop synth.

I also used 2 vactrol’s (check out step 3 on what these are if you haven’t heard of them before) which connect the flashing LED’s circuits to the light Theremin circuit.

After a bit of experimenting I found that the values on the resistors and caps I choose gave me a good range of sound. I strongly encourage you if you do make one of these, to do your own experimentation to find what works best for you.

Check out the video of the synth in action


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

![Step 1: Parts and Tools image 4](images/step01_04.jpg)

![Step 1: Parts and Tools image 5](images/step01_05.jpg)

![Step 1: Parts and Tools image 6](images/step01_06.jpg)

I didn't bother showing images of all of the parts - I don't want to scare you off!

Parts for the circuit

1. 4 X 555 Timers – [eBay](https://www.ebay.com.au/itm/10-20-50-NEW-NE555N-NE555-DIP-8-High-Precision-Oscillator-Timer-IC-Timer-Chip/222661294015?hash=item33d7a5b7bf%3Am%3AmWkES_XElGF_RKXc5FY0pUw&var=521514365068)

2. 2 X 22uf Capacitors – [eBay](https://www.ebay.com.au/itm/120pcs-1uF-470uF-12-Types-Electrolytic-Capacitors-Assortment-Kit-Assorted-Set/351774763287?epid=2113501882&hash=item51e768e917:g:knwAAOSwSwpbaUUR)

3. 2 X 10uF Capacitors – [eBay](https://www.ebay.com.au/itm/120pcs-1uF-470uF-12-Types-Electrolytic-Capacitors-Assortment-Kit-Assorted-Set/351774763287?epid=2113501882&hash=item51e768e917:g:knwAAOSwSwpbaUUR)

4. 2 X 0.1uf (103) Capacitors - [eBay](https://www.ebay.com.au/itm/450pcs-10Value-50V-10pF-100nF-Ceramic-Capacitors-Assortment-Assorted-Kit-Box/163087715384?hash=item25f8c90c38:g:Dn0AAOSwKJZbGjdI)

5. 2 X 10K resistors – [eBay](https://www.ebay.com.au/itm/600pcs-30-Value-1-4W-Resistance-1-Metal-Film-Resistor-Assorted-Kit-Each-20pcs/282857372402?epid=22016229248&hash=item41db9cfaf2:g:ZfMAAOSwBahVSH49)

6. 2 X 1.5K resistors – [eBay](https://www.ebay.com.au/itm/600pcs-30-Value-1-4W-Resistance-1-Metal-Film-Resistor-Assorted-Kit-Each-20pcs/282857372402?epid=22016229248&hash=item41db9cfaf2:g:ZfMAAOSwBahVSH49)

7. 1k Resistor - [eBay](https://www.ebay.com.au/itm/600pcs-30-Value-1-4W-Resistance-1-Metal-Film-Resistor-Assorted-Kit-Each-20pcs/282857372402?epid=22016229248&hash=item41db9cfaf2:g:ZfMAAOSwBahVSH49)

8. 3 X 500K Potentiometer – [eBay](https://www.ebay.com.au/itm/10pcs-Guitar-Potentiometer-A500K-Split-Shaft-Pots-Audio-Tone-Switch-Control-New/263890658531?epid=623933707&hash=item3d711be4e3:g:wW8AAOSwiFtbe4Kc)

9. 2 X 100K Potentiometer – [eBay](https://www.ebay.com.au/itm/5-x-100K-ohm-B100K-Top-Adjustment-Dual-Linear-Potentiometer-Pots-Q0B1/302461097029?epid=1153220041&hash=item466c161445:g:tKsAAOSwXLpZw3Ig)

10. 1 X 5K Potentiometer - [eBay](https://www.ebay.com.au/itm/10PCS-5K-Ohm-B5K-Knurled-Shaft-Linear-Rotary-Taper-Potentiometer/232458669052?hash=item361f9dcbfc:g:uKIAAOSwXGtZm-aY)

11. 4 X 5mm White LED’s – [eBay](https://www.ebay.com.au/itm/50PCS-5MM-LED-WATERCLEAR-RED-GREEN-BLUE-YELLOW-WHITE/112851069914?hash=item1a4672abda%3Am%3AmU4gBiy--CuF9BXwMsdgeMg&var=413267733848)

12. 2 X Photo Cells – [eBay](https://www.ebay.com.au/itm/30PCS-Photoresistor-GL5516-LDR-CDS-5mm-Light-Dependent-Resistor-Sensor-Arduino/123284262861?hash=item1cb4508fcd:g:0MAAAOSwBgVbEOWL)

13. 8 ohm speaker – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR2.TRC0.A0.H0.X8+ohm+speaker.TRS0&_nkw=8+ohm+speaker&_sacat=0)

14. Proto board – [eBay](https://www.ebay.com.au/itm/10x-DIY-Prototype-Paper-PCB-Experiment-Board-Bakelite-Circuit-Board-4-8x13-3cm/142759746052?hash=item213d24da04:g:sFUAAOSwcEha0XL3)

15. Lots of thin wire. I use computer cables to get from my local tip.

16. Heat shrink (used to make the vactrol so will need to be big enough to fit a 5mm LED and photo cell inside.

17. 6 X AA batteries (equals 9v). You could also just use a 9v battery.

18. 6 X AA Battery holder – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR12.TRC2.A0.H0.X6+x+aa+battery+holder.TRS0&_nkw=6+x+aa+battery+holder&_sacat=0)

19. On/off switch for the power - [eBay](https://www.ebay.com.au/itm/5PCS-Blue-LED-Light-12V-Car-Boat-Round-Rocker-ON-OFF-Toggle-Switch-HOTSYSTEM-AU/172573456828?epid=728904450&hash=item282e2df9bc:g:8RAAAOSwSlBYxktg)

20. 4 X on/off toggle switches –[eBay](https://www.ebay.com.au/itm/10pcs-3-Pin-SPDT-ON-ON-Mini-Toggle-Switch-6A-125VAC-Mini-Switches-New/380752503888?hash=item58a69e2450:g:3HIAAOxy-8pSaL9M)

21. Audio out jack - eBay

Parts for the case

1. Case. I used a cigar box which you can easily get from eBay

2. Knobs – I used following ones

[Skull knobs](https://www.ebay.com.au/itm/3pcs-Skull-Head-Electric-Guitar-Knobs-Control-Volume-Tone/232333763720?epid=873680866&hash=item36182be488:g:YxMAAOSwaeRZFppI)

[Small knobs](https://www.ebay.com.au/itm/5X-Useful-Volume-Control-Rotary-Knobs-For-6mm-Dia-Knurled-Shaft-Potentiometer/111831954006?epid=24009482719&hash=item1a09b43256:g:tAEAAOSwv-NWU8zx)

[Large knobs](https://www.ebay.com.au/itm/5-set-Rotary-Potentiometer-Knobs-Caps-with-5Pcs-Counting-Dial-0-100-Scale-MZ/202125337635?hash=item2f0f9be423:g:lzkAAOSwdrhZnrN6)

3. Speaker cover. I haven’t been able to find the one I used on the net but here is a similar one

4. Small screws, nuts and bolts

Tools

1. Soldering Iron

2. Drill

3. Hole bit

4. Wire cutters

5. Screwdrivers, spanners, etc

6. Hot Glue


## Step 2: The Flashing LED Circuit

![Step 2: The Flashing LED Circuit image 1](images/step02_01.jpg)

![Step 2: The Flashing LED Circuit image 2](images/step02_02.jpg)

The first image below shows the original flashing LED circuit and the 2nd shows how I modified it. In the original, you controlled the speed of the LED by the 100K Potentiometer. The 10K resistor between pins 6 and 7 control how fast the LED will flash. A lower resistor will make the LED flash faster.

In the modified circuit, I have added another potentiometer at pin 3 which now allows you to control the brightness of the potentiometer. You can also see that I have added a switch for the resistors on pins 6 and 7 which give the ability to change the speed of the LED. I have also added another switch on pin 2 and an extra capacitor so I can switch between these as well which also gives you more ability to change the sound.

Lastly, you can see that I have added another LED which is connected to a 7.5k resistor. This LED goes on the outside of the synth so I can visually see how fast and how bright the LED inside the vactrol is flashing

I would suggest that you build the original circuit first and get this going. Then experiment by adding different value resistors and caps to see what happens to the LED.


## Step 3: The Light Theremin and Final Circuit

![Step 3: The Light Theremin and Final Circuit image 1](images/step03_01.jpg)

![Step 3: The Light Theremin and Final Circuit image 2](images/step03_02.jpg)

The first circuit in the images is the light Theremin and it doesn’t really have any modifications. The only thing different is the 2 CdS cells or photo cells are added into vactrol’s. I also added a 500K potentiometer to one of the photo cells. This helps change the tone and adds another way to change the sound.

The next circuit is the final circuit with both Flashing LED and Theremin circuits joined together. You may notice that in the flashing LED circuit on the left, that there is a 10K potentiometer to control the brightness of the LED. I found that a 100K pot had too much resistance and was turning the LED off when turned about half way on this circuit.

Lastly, I’m not going to go through step by step instructions on how to put the circuit together. It will just be too long and I’m going to assume that you at least know how to breadboard and solder circuits.


## Step 4: What Is a Vactrol?

![Step 4: What Is a Vactrol? image 1](images/step04_01.jpg)

![Step 4: What Is a Vactrol? image 2](images/step04_02.jpg)

A Vactrol acts like a potentiometer - applying a voltage to the Vactrol's LED has the same effect as turning up the knob on the potentiometer.

It consists of two components incorporated into one package: a light-emitting diode (LED), and a photoresistor (a resistor whose resistance drops when it is exposed to light)

It’s important that the only light that the photo cell can detect is from the LED. If outside light is able to reach the photo cell, then it will interfere with the performance and sound, that’s why you need to add something like heat shrink to protect them.


## Step 5: Making a Vactrol

![Step 5: Making a Vactrol image 1](images/step05_01.jpg)

![Step 5: Making a Vactrol image 2](images/step05_02.jpg)

![Step 5: Making a Vactrol image 3](images/step05_03.jpg)

![Step 5: Making a Vactrol image 4](images/step05_04.jpg)

Steps:

1. Cut a small length of heat shrink tube. The LED and photo cell need to be able to fit inside.

2. Place the LED into the heat shrink with the legs facing out and also the same for the photo cell. Make sure that they are touching inside the heat shrink.

3. Heat the heat shrink and start to shrink it. Start with one end first and when it has shrink enough, grab some pliers and flatten the end of the heat shrink so it is sealed shut.

4. Do the same for the other end

5. That’s it! You have made an important component to the fizzle loop synth


## Step 6: 1st Circuit - LED Flasher

![Step 6: 1st Circuit - LED Flasher image 1](images/step06_01.jpg)

![Step 6: 1st Circuit - LED Flasher image 2](images/step06_02.jpg)

![Step 6: 1st Circuit - LED Flasher image 3](images/step06_03.jpg)

![Step 6: 1st Circuit - LED Flasher image 4](images/step06_04.jpg)

Steps:

1. Start with the first flashing LED circuit and solder it to a protoboard as far left as possible

2. I didn’t wire-up all of the potentiometers, switches etc as I will do this once the circuit is complete. However, add wires to the solder points in preparation.

3. I added a couple of female pin headers for the capacitors. This way i can change them out if I want to for other values and get different timing and sounds out of the synth.

4. Lastly, test the circuit to make sure that it works. I just added the wires, LED and Pot to a breadboard and tested to make sure the LED flashed.

5. Once you have this first circuit working, you should then add the Vactrol. I have included a separate step on how to make one of these and also what they are. You can also buy them if you want to but they are very simple to make so I would suggest just doing your own

6. Solder the vactrol into place making sure you note the polarities of the LED legs when attaching them to the 555 ic and positive.


## Step 7: 2nd Circuit - Light Theremin

![Step 7: 2nd Circuit - Light Theremin image 1](images/step07_01.jpg)

![Step 7: 2nd Circuit - Light Theremin image 2](images/step07_02.jpg)

![Step 7: 2nd Circuit - Light Theremin image 3](images/step07_03.jpg)

Next section to add to the protoboard is the Theremin circuit.

Steps:

1. Carefully follow the schematic when adding to the protoboard

2. Remember to connect the vactrol to the section where the photo cells are connected. Connect the first vactrol to the LED flashing circuit you have already added to the protoboard. The other one you can wait until you have built the last flashing LED circuit

3. Make sure you test this circuit as well before you attach it to the vactrol. All I did was add a couple of photo cells (CdS cell) to the pins on the 555's, added a speaker and some power and made sure that the light theremin was working correctly. It's definitely worth taking the time to test - I messed-up 2 boards before I got it right and it was all due to not testing.


## Step 8: 3rd Circuit - the Last Flashing LED

![Step 8: 3rd Circuit - the Last Flashing LED image 1](images/step08_01.jpg)

![Step 8: 3rd Circuit - the Last Flashing LED image 2](images/step08_02.jpg)

![Step 8: 3rd Circuit - the Last Flashing LED image 3](images/step08_03.jpg)

Steps:

1. Build and complete the last flashing LED circuit and add this to the right of the Theremin circuit.

2. Test and make sure that an LED flashes

3. Next, solder the LED section to the Vactrol making sure your polarities are right.

4. You will probably use most of the protoboard so make sure that the case you choose is big enough to house the whole thing.

That’s pretty much it for the circuit. It’s now time to start on the case


## Step 9: A Few Ad-hoc Changes

![Step 9: A Few Ad-hoc Changes image 1](images/step09_01.jpg)

![Step 9: A Few Ad-hoc Changes image 2](images/step09_02.jpg)

![Step 9: A Few Ad-hoc Changes image 3](images/step09_03.jpg)

It took me 3 tries before I got this circuit right! The first 2 half worked but I couldn't trouble shoot them to work out why they wouldn't work properly. Each time I re-started the circuit I add a couple new ideas which I'll go through now.

Adding IC sockets

I usually just solder the IC directly to the circuit board. The problem with doing this way is you can't remove the IC if it doesn't work. Well you can but you have to de-solder and everything just starts to become a mess. In the 3rd iteration I added IC sockets so I could easily change them if I needed to.

Making the Capacitors Changeable

This wasn't necessary but I thought if I wanted to get different sounds out of the synth, then making the capacitors easily changeable would allow me to change the sounds later on. I just used some female headers and soldered them onto the circuit board. the legs of the capacitors fit inside them.

Testing

I know that this is probably self evident, but I tend to rush when I'm making and sometimes skip the testing stages. On the final board I tested each circuit (both flashing LED's and light theremin) to ensure they worked before I finally attached them altogether. It meant that I had to add a couple of temporary parts each time but it was worth it.


## Step 10: Adding the Switches and Knobs to the Case

![Step 10: Adding the Switches and Knobs to the Case image 1](images/step10_01.jpg)

![Step 10: Adding the Switches and Knobs to the Case image 2](images/step10_02.jpg)

![Step 10: Adding the Switches and Knobs to the Case image 3](images/step10_03.jpg)

![Step 10: Adding the Switches and Knobs to the Case image 4](images/step10_04.jpg)

![Step 10: Adding the Switches and Knobs to the Case image 5](images/step10_05.jpg)

![Step 10: Adding the Switches and Knobs to the Case image 6](images/step10_06.jpg)

![Step 10: Adding the Switches and Knobs to the Case image 7](images/step10_07.jpg)

I used a cigar box for the case. I find that they have a lot of room inside to add all of the parts and they also look pretty damn cool. I also added the knobs and switches first before the speaker. This way I could work out the best position once all of the other parts had been added. I'm going to assume you too have a cigar box for your case as well.

Steps:

1. First drill 3 holes and add the 500K pots.

2. Next, I secured the knobs to the pots

3. Add a toggle switch above the 2 500K pots on either side

3. Next I added the 100K pots above the 2 toggle switches

4. Then add a toggle switch above each 100k pot

The switches allow you to change the speed and sound of the pot underneath it.


## Step 11: Speaker and LED's

![Step 11: Speaker and LED's image 1](images/step11_01.jpg)

![Step 11: Speaker and LED's image 2](images/step11_02.jpg)

![Step 11: Speaker and LED's image 3](images/step11_03.jpg)

![Step 11: Speaker and LED's image 4](images/step11_04.jpg)

![Step 11: Speaker and LED's image 5](images/step11_05.jpg)

![Step 11: Speaker and LED's image 6](images/step11_06.jpg)

![Step 11: Speaker and LED's image 7](images/step11_07.jpg)

![Step 11: Speaker and LED's image 8](images/step11_08.jpg)

![Step 11: Speaker and LED's image 9](images/step11_09.jpg)

Steps:

1. First I added the LED's. You don't have to add LED's but I find that they are a good visual indication on the speed and brightness of the LED's in the vactrols.

2. Use a hole bit on a drill and make a hole in the top of the cigar box just big enough to fit the speaker inside

3. I added a computer fan cover next over the speaker to protect it. To do this I also needed to add some spaces to ensure the fan cover wasn't touching the speaker. Secure in place with some small screws and nuts.

So that's pretty much for the lid of the case. I added a few extra switches later on which I'll go through in the next step.


## Step 12: Soldering the Circuit Board to the Pots and Switches

![Step 12: Soldering the Circuit Board to the Pots and Switches image 1](images/step12_01.jpg)

![Step 12: Soldering the Circuit Board to the Pots and Switches image 2](images/step12_02.jpg)

![Step 12: Soldering the Circuit Board to the Pots and Switches image 3](images/step12_03.jpg)

![Step 12: Soldering the Circuit Board to the Pots and Switches image 4](images/step12_04.jpg)

![Step 12: Soldering the Circuit Board to the Pots and Switches image 5](images/step12_05.jpg)

Once you have added all of the switches and pots, it’s time to solder the circuit board to them. This isn’t really a hard step, it just needs a little patience to sort out the wires and where they are to be attached. It’s up to you on how you want to configure the different effects and sounds – I’ll go through how I laid-out my synth but you may want to do it totally different

Steps:

1. The 2 large pots on the left and right of the synth are used to control the brightness of the LED in the Vactrol

2. The toggle switch above each of the large knobs are used to switch between the 2 capacitors

3. The large pot in the middle is connected to the vactrol

4. The 2 smaller knobs control the speed of the LED flashing. You need to join the wires from pin 7 and positive on the 555

5. The 2 toggle switches above this are joined to the 2 resistors so you can change the valve of them and make the LED flash faster

6. You’ll also need to attach the speaker wires to the speaker. There is a 5K pot also used to volume control but as I added this into the body of the cigar box, I decided just to solder direct to the speaker for testing purposes

7. Lastly, solder the LED wires from the circuit board to the LED’s in the cigar box. These help you visually see what is happening inside the Vactrol

8. Add some power and test to make sure you are getting sounds out of the board. Play around with the pots and make sure they work ok. If not, check over your wiring and connections and trouble shoot to try and fix the problem.


## Step 13: Power and Final Wiring

![Step 13: Power and Final Wiring image 1](images/step13_01.jpg)

![Step 13: Power and Final Wiring image 2](images/step13_02.jpg)

![Step 13: Power and Final Wiring image 3](images/step13_03.jpg)

![Step 13: Power and Final Wiring image 4](images/step13_04.jpg)

![Step 13: Power and Final Wiring image 5](images/step13_05.jpg)

![Step 13: Power and Final Wiring image 6](images/step13_06.jpg)

After you have tested and are happy with how it sounds, the next step is to add the volume pot, on/off switch and audio out jack

Steps:

1. Attach the batteries to the on/off switch and also the circuit board

2. Next solder the speaker wires to the volume pot

3. For the audio out, solder a couple wires to the positive and negative terminals on the speaker and attach these to the audio out. You can also add a 10uf cap from the positive wire to the positive terminal on the jack which will help clean-up the sound.


## Step 14: Bonus! Change the Sound by Adding Some Capacitors

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 1](images/step14_01.jpg)

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 2](images/step14_02.jpg)

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 3](images/step14_03.jpg)

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 4](images/step14_04.jpg)

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 5](images/step14_05.jpg)

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 6](images/step14_06.jpg)

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 7](images/step14_07.jpg)

![Step 14: Bonus! Change the Sound by Adding Some Capacitors image 8](images/step14_08.jpg)

Adding the extra capacitors to the speaker to get different sounds only occurred to me by accident. However, it can really help clear-up the sound and also add some delay depending on the size of the capacitor.

I added a couple of momentary switches to I could turn these on when I wanted to along with a couple of SPTD (toggle) switches to be able to keep them on all of the time

Momentary Switches

Steps:

1. Add a couple of momentary switches to the top of the cigar box. I placed mine just above the first lot of switches.

2. Next, add a couple of toggle switches to the cigar box. As this mod was an afterthought, I didn’t have much room to add them. In the end I found a little space at the top of the box and added them there.

3. Next you need to add a capacitor to each of the momentary switches. Solder one leg of a 1uf capacitor to one of the legs on the momentary switch and do the same for a 10uf (to the other momentary switch. You can use whatever capacitor values you want – I just found that these gave some nice variances in sound.

4. Next, solder a wire from the leg of each capacitor to positive on the speaker.

5. Lastly, add another wire to the other solder point on the momentary switch and attach this to ground.

Test to see what happens when you push the switches down. You should get a rise in pitch and some cool delay as the capacitor charges and then releases.

Toggle Switches

Steps:

1. Add a couple wires to the solder points on the switch.

2. Solder one to the speakers positive and the other to the capacitor

3. Lastly solder the other wire from the switch to ground


---
*67 images archived*
