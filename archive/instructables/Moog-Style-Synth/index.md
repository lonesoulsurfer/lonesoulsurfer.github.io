# Moog Style Synth

Source: https://www.instructables.com/Moog-Style-Synth/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

First and foremost, I have to give a massive shout out to Pete McBennett who designed this awesome circuit. When I came across it on YouTube I couldn't believe the sound that he managed to get out of a handful of components. The synth has a MASSIVE sound and really growls with heavy bass through a good speaker.

The synth is a pulse width modulated oscillator, routed through a light-controlled resonant low pass filter. The "growling" oscillator tonality is supplied via a PWM and a awesome high-resonance low pass filter.

The light-control aspect which is controlled through 2 Light dependent resistors (LDR), gives amazing musical expression. The heart of the circuit is 5 op amps (LM358) and also a 2 Hex inverter drone synths via a CD40106 IC. The 2 two adjustable drone oscillators give this synth a total of three oscillators.

The only addition that I included was an additional circuit with a couple of vactrols (LED and LDR facing each other, covered by heatshrink. check this ible on how to make one. This function turns the synth into an arpeggiator type synth and is a tonne of fun to play.

Ok that's enough babbling, time to watch the video and see this bad boy in action. If you like what you see and want to make your own, then unfortunately you'll have to keep reading.

Hackaday have also reviewed this build so if you want to check that out just click the link


## Step 1: Parts Moog Synth Circuit

![Step 1: Parts Moog Synth Circuit image 1](images/step01_01.jpg)

![Step 1: Parts Moog Synth Circuit image 2](images/step01_02.jpg)

![Step 1: Parts Moog Synth Circuit image 3](images/step01_03.jpg)

![Step 1: Parts Moog Synth Circuit image 4](images/step01_04.jpg)

![Step 1: Parts Moog Synth Circuit image 5](images/step01_05.jpg)

![Step 1: Parts Moog Synth Circuit image 6](images/step01_06.jpg)

Here's the parts list. It's a bit of a big one. The case is from an old calculator which I gutted. You will need to design your own case and I have suggested one to use below.

1. Resistors make sure that they are 1%. You will notice that there are some weird values for the top 10 resistors. These values are so the synth is in tune. I couldn’t manage to find the exact ones so used the closest values. You can also buy them in bulk on eBay and get most if not all of the values needed

a. 10K X 4

b. 4.5K

c. 8.2K

d. 7.5K X 2

e. 3.4K

f. 6.2K

g. 5.6K

h. 5K

i. 2.2K

j. 38K

k. 100K X 11

l. 47K X 3

m. 22K X 4

n. 470K

o. 82K X 3

p. 390K

q. 120K

r. 33K

2. Capacitors

a. 0.15uf (150nf) - eBay

b. 2.2uf- eBay

c. 4.7uf X 4- eBay

d. .001uf (1nf) X 2- eBay.

e. 0.1uf (100nf) X 2- eBay

3. IC’s

a. CD40106- eBay

b. Lm358 X 5- eBay

4. Pots

a. 50K - eBay

b. 100K X 3- eBay

5. LDR’s X 2- eBay


## Step 2: Arpeggiator Circuit Parts and Others

![Step 2: Arpeggiator Circuit Parts and Others image 1](images/step02_01.jpg)

![Step 2: Arpeggiator Circuit Parts and Others image 2](images/step02_02.jpg)

![Step 2: Arpeggiator Circuit Parts and Others image 3](images/step02_03.jpg)

![Step 2: Arpeggiator Circuit Parts and Others image 4](images/step02_04.jpg)

![Step 2: Arpeggiator Circuit Parts and Others image 5](images/step02_05.jpg)

Parts:

Arpeggiator Circuit

1. 555 Timer - eBay

2. 10K pot - eBay

3. 1M duel pot - eBay

4. 100R resistor - eBay. Buy them in assorted lots

5. 1K resistor X 2

6. 470R resistor

8. Transistor BC547 - eBay

9. Vactol X 2. (LDR and LED inside a piece of heat shrink). You can make your own easily - just check out this instructable

10. Prototype Board - eBay

Power

You can just a 9v battery to power the circuits or do what I did and use a mobile phone battery and a charging/voltage regulator.

Check out this instructable on how to use a mobile phone battery to power the circuits

Other Parts

1. SPDT switches X 3 - eBay

2. Momentary switches X 10 - eBay

3. Pot knobs X 7 - eBay

4. A whole lot of wire. I like to use ribbon wire

5. Case. Mine is an old calculator. Use whatever you think would be cool

6. Acrylic sheets - eBay

7. Audio Output Jack - 3.5mm and 6.35mm - eBay


## Step 3: The "Moog" Circuit Schematic

![Step 3: The "Moog" Circuit Schematic image 1](images/step03_01.jpg)

This is the schematic that you will need to build. It's the main circuit and is the one created by Pete McBennett. I didn't do any changes to this schematic as it doesn't need any changes. However, go crazy with it and try some modifications to see what you can get out of it.

Make sure you breadboard it first so you can test and understand how it all goes together.

I did add another circuit so I could control the LDR's with flashing LED's through a couple of vacrols. This circuit is in the next step and is optional to add.


## Step 4: Vactrol Circuit for Arpeggiator Sound Effect

![Step 4: Vactrol Circuit for Arpeggiator Sound Effect image 1](images/step04_01.jpg)

![Step 4: Vactrol Circuit for Arpeggiator Sound Effect image 2](images/step04_02.jpg)

This circuit creates an arpeggiator effect using some vactols (this this 'ible on how to make ta vactol, also known as a opticoupler). It gives the synth another sound effect which is fun to play around with. However, it isn't necessary to add this circuit if you don't want to.

NOTE: I forgot to add the capacitor from p[in 2 on the 555 timer initially. I have updated the schematic and it now incluides it.

The first schematic shows the circuit which has 2 vactrols and is essentially a flashing LED circuit. The LED's pulse which the LDR's in the vactrol detect and you get some cool, rhythmic sound effects.

The second schematic shows how I connected this circuit up to the main one. I used a DPDT switch to be able to turn on and off the arpeggiator effect. Hopefully it isn't too confusing on how I connected the 2 circuits together, it took me ages for some reason to work out the best way to connect them via the switch. There's probably a better way so experiment and see how you go. I have also included the fritzing files so you can mess about with them f you want to.


## Step 5: Breadboard

![Step 5: Breadboard image 1](images/step05_01.jpg)

![Step 5: Breadboard image 2](images/step05_02.jpg)

I can't stress more to breadboard these circuits before you even think about soldering. The main "moog" circuit is quite complex and may take a couple of tries before you get it right.

Keep at it though as I can guarantee that the circuit is correct and works amazingly. There are a bunch of mods that you could do to the actual circuit but I pretty much left it as is. Once you have the "moog" circuit working, you can then add the arpeggiator circuit and have a play around with that.

If you are happy with how it sounds, next it's time to solder all those components together - gulp!


## Step 6: The "Moog" Synth Circuit - Part 1

![Step 6: The "Moog" Synth Circuit - Part 1 image 1](images/step06_01.jpg)

![Step 6: The "Moog" Synth Circuit - Part 1 image 2](images/step06_02.jpg)

![Step 6: The "Moog" Synth Circuit - Part 1 image 3](images/step06_03.jpg)

I was going to do a step by step guide on how to put the circuit together but it would be too tedious (and boring for you). So instead I've taken a few images of putting the circuit together and will go through the steps just in a general fashion.

Steps:

1. First, you need to make sure that your prototype board is going to be big enough. It;s a big circuit and will take up a fair bit of room. I've added a link in the parts section to the one that I used. I use these n most of my electronic projects and they are great

2. Start with the U1 & U2 op-amp section and add all of the components as per the schematic.

3. I always like to double check the connections before I move onto the next op-amp. It's easier to work out if you have forgotten to connect something when you have just added the parts.

4.


## Step 7: The "Moog" Synth Circuit - Part 2

![Step 7: The "Moog" Synth Circuit - Part 2 image 1](images/step07_01.jpg)

![Step 7: The "Moog" Synth Circuit - Part 2 image 2](images/step07_02.jpg)

![Step 7: The "Moog" Synth Circuit - Part 2 image 3](images/step07_03.jpg)

![Step 7: The "Moog" Synth Circuit - Part 2 image 4](images/step07_04.jpg)

Steps:

1. Next I added U2 op-amp and started to connect the components as per the schematic.

2. It's interesting to note that there are a couple of resistors that need to be connected to different legs on the op-amp. You can see in the images that I went around the op-amp in order to connect these. You could go across the top of it but it makes it hard to remove the op-amp if it is faulty.

3. The other thing you may note is, it's very similar layout to the first one.


## Step 8: The "Moog" Synth Circuit - Part 3

![Step 8: The "Moog" Synth Circuit - Part 3 image 1](images/step08_01.jpg)

![Step 8: The "Moog" Synth Circuit - Part 3 image 2](images/step08_02.jpg)

![Step 8: The "Moog" Synth Circuit - Part 3 image 3](images/step08_03.jpg)

Steps:

1. Next up is to add op-amp U3.

2. A couple things to note are the following.

a. You need to connect pin 7 from U1 to pin 2 on U3.

b. You also need to connect pin 7 from U2 to pin 6 on U3 with a 100K resisitor.

3. Again, it's a good time to check over all your connections and ensure everything is in the right spot and nothing is missing.


## Step 9: The "Moog" Synth Circuit - Part 4

![Step 9: The "Moog" Synth Circuit - Part 4 image 1](images/step09_01.jpg)

![Step 9: The "Moog" Synth Circuit - Part 4 image 2](images/step09_02.jpg)

![Step 9: The "Moog" Synth Circuit - Part 4 image 3](images/step09_03.jpg)

![Step 9: The "Moog" Synth Circuit - Part 4 image 4](images/step09_04.jpg)

Steps:

1. Time to add op-amps 4 and 5.

2. Remember to try and keep everything pretty tight on the prototype board. There's still one more IC to add to complete the schematic.

3. You'll also notice that the LDR's are connected to U4 and U5. You'll need to add some wires a little later to these connections and a few others.


## Step 10: The "Moog" Synth Circuit - Part 5

![Step 10: The "Moog" Synth Circuit - Part 5 image 1](images/step10_01.jpg)

![Step 10: The "Moog" Synth Circuit - Part 5 image 2](images/step10_02.jpg)

![Step 10: The "Moog" Synth Circuit - Part 5 image 3](images/step10_03.jpg)

![Step 10: The "Moog" Synth Circuit - Part 5 image 4](images/step10_04.jpg)

![Step 10: The "Moog" Synth Circuit - Part 5 image 5](images/step10_05.jpg)

Onto the final stretch now (at least for the Moog circuit!)

Steps:

1. Add the 40106 IC

2. Add all of the components and make the connections

3. It got a little tight towards the end as you can see but I managed to add the components on the prototype board

4. Time to add the wires so you can connect the circuit to all the controls


## Step 11: The "Moog" Synth Circuit - Part 6

![Step 11: The "Moog" Synth Circuit - Part 6 image 1](images/step11_01.jpg)

![Step 11: The "Moog" Synth Circuit - Part 6 image 2](images/step11_02.jpg)

There's a whole lot of wires that you now need to add.

Steps:

1. Follow the schematic and start to add the necessary wires. I always try and connect longer wires then needed, better for them to be too long then too short. Plus once you place the circuit into the case you can trim to length.

2. There are extra wires added so I can connect the arpeggiator circuit as well. It would have been nice to have had room to add the arpeggiator circuit as well to the moog prototype board but I ran out of room

3. I use ribbon computer wire for most of my projects as I can get it for free at my local e-waste centre.

4. At this stage you can test the circuit if you want to. You will need to add all of the controls like the potentiometers etc and power it up. I did this to ensure the circuit worked and amazingly it did first go! Usually I forget something or solder something in the wrong spot.


## Step 12: Making the Arpeggiator Circuit

![Step 12: Making the Arpeggiator Circuit image 1](images/step12_01.jpg)

![Step 12: Making the Arpeggiator Circuit image 2](images/step12_02.jpg)

![Step 12: Making the Arpeggiator Circuit image 3](images/step12_03.jpg)

![Step 12: Making the Arpeggiator Circuit image 4](images/step12_04.jpg)

![Step 12: Making the Arpeggiator Circuit image 5](images/step12_05.jpg)

![Step 12: Making the Arpeggiator Circuit image 6](images/step12_06.jpg)

![Step 12: Making the Arpeggiator Circuit image 7](images/step12_07.jpg)

As I have already mentioned, this circuit is really just a simple LED flasher, made from a 555 timer.

Steps:

1. Add the 555timer to the prototype board

2. Use the schematic and start to connect the rest of the components

3. You will need to also make a couple of vactrols. They're simple to make and you only need some heat-shrink, white LED and a LDR. I did an 'ible on how to make one which can be found here.

4. The circuit will need to be wired up to a switch later on so that's why there is 2 wires connected to one of the LDR legs on each vactrol. You need to be able to turn off the LDR's on the moog circuit when you want to use the arpeggitor and vice versa. This is done with a DPDT switch. I also found it necessary to turn off power to the arpeggiator when the moog was on as you can here a slight ticking if they are on at the same time.


## Step 13: Making the Case From an Old Calculator

![Step 13: Making the Case From an Old Calculator image 1](images/step13_01.jpg)

![Step 13: Making the Case From an Old Calculator image 2](images/step13_02.jpg)

![Step 13: Making the Case From an Old Calculator image 3](images/step13_03.jpg)

![Step 13: Making the Case From an Old Calculator image 4](images/step13_04.jpg)

![Step 13: Making the Case From an Old Calculator image 5](images/step13_05.jpg)

![Step 13: Making the Case From an Old Calculator image 6](images/step13_06.jpg)

I found this old calculator at a junk shop. It must of been used in a mechanics shop as it was full of oil and filthy. As it no longerb worked I thought I'd repurpose it and give it another life. You could also use a small keyboard or just build your own enclusre out of a cigar box or something just as cool. I'll go thrugh the next steps and tell you want I had to do in order to make this into the synth.

Steps:

1. First I had to pull the calculator apart.

2. Once I had it apart and had all of the insides out of it, I next gave it a long soak and cleaned it up best I could,

3. I was thinking about using the original key pad as the keys in the synth but decided against this.


## Step 14: Modifying the Calculator Case

![Step 14: Modifying the Calculator Case image 1](images/step14_01.jpg)

![Step 14: Modifying the Calculator Case image 2](images/step14_02.jpg)

![Step 14: Modifying the Calculator Case image 3](images/step14_03.jpg)

![Step 14: Modifying the Calculator Case image 4](images/step14_04.jpg)

![Step 14: Modifying the Calculator Case image 5](images/step14_05.jpg)

As I needed space for all of the switches and pots, I decided to remove some pieces of plastic on the front of the case and replace this section with some coloured acrylic.

Steps:

1. First I removed the 2 pieces of plastic strip that separated the calculator keys. I cut them away and filed down the cuts to make them smooth and flush.

2. Next, I removed the section that showed the numbers. This was recessed so it was a little tricker to remove. I used a dremel and some wire cutters to remove most of the plastic. I then filed and sanded the edges as smooth as I could get them. I wanted the finish to look like the plastic had never been there.


## Step 15: On/Off Switch

![Step 15: On/Off Switch image 1](images/step15_01.jpg)

![Step 15: On/Off Switch image 2](images/step15_02.jpg)

![Step 15: On/Off Switch image 3](images/step15_03.jpg)

![Step 15: On/Off Switch image 4](images/step15_04.jpg)

I'm not too sure why I didn't use the original switch, I think I wanted a red though for a couple reasons, first, it is the colour of the acrylic I used and second, I had a red one lying around.

Steps:

1. In order to fit the switch into place, I had to enlarge the original switch hole. I used some files to do this.

2. Once the hole was large enough i pushed the switch into place.

3. I had to add some hot glue around the switch on the inside to keep it in place as it was a little loose.


## Step 16: Micro USB Adapter

![Step 16: Micro USB Adapter image 1](images/step16_01.jpg)

![Step 16: Micro USB Adapter image 2](images/step16_02.jpg)

![Step 16: Micro USB Adapter image 3](images/step16_03.jpg)

![Step 16: Micro USB Adapter image 4](images/step16_04.jpg)

![Step 16: Micro USB Adapter image 5](images/step16_05.jpg)

Next thing I did was to add a micro USB adapter for charging the battery.

Steps:

1. I made a small, retanglar hole in the back of the case, just large enough for the micro USB to poke through

2. To hold the USB adapter in place I added a small piece of acrylic and glued it down along with the USB adpater. Be careful when using superglue or any glue on something like this as you don't want to get any inside the USB.


## Step 17: LDR's and a Couple of Audio Inputs

![Step 17: LDR's and a Couple of Audio Inputs image 1](images/step17_01.jpg)

![Step 17: LDR's and a Couple of Audio Inputs image 2](images/step17_02.jpg)

![Step 17: LDR's and a Couple of Audio Inputs image 3](images/step17_03.jpg)

![Step 17: LDR's and a Couple of Audio Inputs image 4](images/step17_04.jpg)

![Step 17: LDR's and a Couple of Audio Inputs image 5](images/step17_05.jpg)

![Step 17: LDR's and a Couple of Audio Inputs image 6](images/step17_06.jpg)

![Step 17: LDR's and a Couple of Audio Inputs image 7](images/step17_07.jpg)

The synths moog sound is controlled with a couple of LDR's. These needed to be placed close together in order to be able to easily cover them with your hand. I went with an extrnal speaker/amp on this build. Initially I was going to include a LM386 op-amp but I didn't like the sound that it generated. I found that a good portable speaker or guitar amp works best and gives you awesome, deep bass sounds.

Steps:

1. First, I found a good spot on the calculator to add the LDR's.

2. Next, I drilled 4 small holes for the LDR legs to go through and glued them into place.4

3. I wanted to be able to play this either througha 3.5mm or 6mm jack so I added tho input sockets. I drilled a couple holes into the back and secured them into place.


## Step 18: Adding Some Acrylic Sheets to Fill-up All Those Holes I Made

![Step 18: Adding Some Acrylic Sheets to Fill-up All Those Holes I Made image 1](images/step18_01.jpg)

![Step 18: Adding Some Acrylic Sheets to Fill-up All Those Holes I Made image 2](images/step18_02.jpg)

![Step 18: Adding Some Acrylic Sheets to Fill-up All Those Holes I Made image 3](images/step18_03.jpg)

![Step 18: Adding Some Acrylic Sheets to Fill-up All Those Holes I Made image 4](images/step18_04.jpg)

![Step 18: Adding Some Acrylic Sheets to Fill-up All Those Holes I Made image 5](images/step18_05.jpg)

![Step 18: Adding Some Acrylic Sheets to Fill-up All Those Holes I Made image 6](images/step18_06.jpg)

In order to be able to add the buttons, switches and pots into the calculator, I added some red acrylic pieces. It doesn't look red in the images as it is protected by a paper covering. This is how I added it to the body of the calculator.

Steps:

1. First, I measured the 2 gaping holes I made in the body of the calculator to work out the dimensions I had to cut the acrylic.

2. Next I carefully cut the acrylic pieces, one for the top section which I will be adding 4 pots later on and one for the bottom section which will house the momentary switches, a couple other pots and some switches.

3. In order to hold the bottom section into place I utilized the some of the mounting holes already in the calculator case. I measured and drilled holes into the acrylic and after a little adjustment I managed to secure the bottom section into the calculator quite well. I later added some washes and screws to really secure it.

4. The top section I went with some epoxy glue (not preferable but it does the job). However, before I glued it into place I needed to add the pots first.


## Step 19: Adding Some Pots (and a Couple of Switches)

![Step 19: Adding Some Pots (and a Couple of Switches) image 1](images/step19_01.jpg)

![Step 19: Adding Some Pots (and a Couple of Switches) image 2](images/step19_02.jpg)

![Step 19: Adding Some Pots (and a Couple of Switches) image 3](images/step19_03.jpg)

![Step 19: Adding Some Pots (and a Couple of Switches) image 4](images/step19_04.jpg)

![Step 19: Adding Some Pots (and a Couple of Switches) image 5](images/step19_05.jpg)

![Step 19: Adding Some Pots (and a Couple of Switches) image 6](images/step19_06.jpg)

![Step 19: Adding Some Pots (and a Couple of Switches) image 7](images/step19_07.jpg)

![Step 19: Adding Some Pots (and a Couple of Switches) image 8](images/step19_08.jpg)

This step will show where I added the pots. As with most of these types of projects, I made a change at the 11th hour so you might notice some changes later. The reason for the change is a modified the circuit so I could add a way to control the synth with only one pot. This pot by-passes the momentary switches and allows you to play it without them.

Steps:

1. I went with adding the 4 main pots into the top panel. These are the pots that control the 40106 IC oscillators (2 on the right) and the tuning and PWM from the synth.

2. I measured and drilled the holes and secured the pots into place

3. The SPDT switch in the top right hand is to be ale to turn off the oscillator off if you want to.

4. I then added the 2 pots to control the arpeggiator. The one in the top section is for the modulation and the other is for speed. I later moved these both together and located them on the left on the calculator.

5. The 2 switches you can see do the following; turn off the power to the arpeggiator and the other allows you to turn either the synth or arpeggiator on or off.


## Step 20: Adding the Momentary Switches and Resistors

![Step 20: Adding the Momentary Switches and Resistors image 1](images/step20_01.jpg)

![Step 20: Adding the Momentary Switches and Resistors image 2](images/step20_02.jpg)

![Step 20: Adding the Momentary Switches and Resistors image 3](images/step20_03.jpg)

![Step 20: Adding the Momentary Switches and Resistors image 4](images/step20_04.jpg)

![Step 20: Adding the Momentary Switches and Resistors image 5](images/step20_05.jpg)

![Step 20: Adding the Momentary Switches and Resistors image 6](images/step20_06.jpg)

![Step 20: Adding the Momentary Switches and Resistors image 7](images/step20_07.jpg)

![Step 20: Adding the Momentary Switches and Resistors image 8](images/step20_08.jpg)

I added the momentary switches near the end of the build as it took some time to find the ones I wanted to use. I’m still not 100% happy with the ones I ended up with but they were the best ones out of all I tested. You want them to have low resistance when pushed down and all the ones I brought were either too big or had high resistance.

Steps:

1. First, I measured where I needed to drill the 10 holes for the switches.

2. I carefully drilled the holes (didn’t want to crack the acrylic) and removed the protective covering on the acrylic

3. I next added each of the momentary switches into place and secured them tightly’

4. Now I had to add the resistors. This is pretty straight forward however, I did manage to wire this the wrong way the first time. You need to make sure that SW10 on the schematic is actually the first switch out of the 10.

5. Solder the resistors in series between each of the switches legs. The other leg on the switches need to be connected as well. I used resistor legs to connect all of these together.

6. Laslty, I connected pin 1 from U1A IC to the last switch and connected leg 6 from U1A to a 38.3K resistor and connected this to the first switch.


## Step 21: Adding the Battery and Charging/Voltage Meter Module

![Step 21: Adding the Battery and Charging/Voltage Meter Module image 1](images/step21_01.jpg)

![Step 21: Adding the Battery and Charging/Voltage Meter Module image 2](images/step21_02.jpg)

![Step 21: Adding the Battery and Charging/Voltage Meter Module image 3](images/step21_03.jpg)

![Step 21: Adding the Battery and Charging/Voltage Meter Module image 4](images/step21_04.jpg)

![Step 21: Adding the Battery and Charging/Voltage Meter Module image 5](images/step21_05.jpg)

![Step 21: Adding the Battery and Charging/Voltage Meter Module image 6](images/step21_06.jpg)

The synth will need 9v power supply. You could use a 9v battery but I prefer to use a rechargeable one. There is a great little module that you can get in eBay that have a charger and voltage regulator build into one. This means you can use Li-Po or Li-Ion batteries to run the synth. I like to use old mobile batteries and have done an Instructable on how to do this which can be found here.

Steps:

1. Connect the module input solder points to the battery terminals.

2. Secure the battery in place inside the case. I like to use double-sided tape to secure parts into place.

3. You then need to connect both the circuits (the moog circuit and the arpeggiator circuit) to the module. Add a couple of wires to ground on each circuit if you haven’t already and solder these to the output solder points on the module.

4. I found that you need to isolate the arpeggiator circuit when the moog synth is playing or you will hear a slight “tapping” sound. To do this, I added a separate on/off switch for the power on the arpeggiator circuit and coonected both on/off switches to the module.


## Step 22: Connecting All Those Wires

![Step 22: Connecting All Those Wires image 1](images/step22_01.jpg)

![Step 22: Connecting All Those Wires image 2](images/step22_02.jpg)

![Step 22: Connecting All Those Wires image 3](images/step22_03.jpg)

It’s now time to connect all of the wires to their respective part.

Steps:

1. If you haven't already, secure the 2 circuits into the base of the case.

2. Place the top of the case side by side with the base. This will ensure that when you cut and solder all of the wires, you will be able to open the top up and lay it flat next to the base.

3. Start by placing a wire close to the part that it needs to be soldered to, then trim, and solder it. Wire seems to take up more room then you expect so make sure you trim to the minimum size the wire can be.

4. Keep on working through each of the wires and solder them to their respective part.

5. You may have noticed on some of the images that I didn’t put the momentary switches in until last. The reason being I couldn’t find the right ones. I brought quite a few different types and in the end I had to compromise due to the size of the calculator and ease of use.

6. Once you have everything wired-up, it’s time to give it a test run.


## Step 23: So What Next?

![Step 23: So What Next? image 1](images/step23_01.jpg)

![Step 23: So What Next? image 2](images/step23_02.jpg)

![Step 23: So What Next? image 3](images/step23_03.jpg)

![Step 23: So What Next? image 4](images/step23_04.jpg)

Now that you have finished your synth, it’s time to see what she can do.

First, plug-in a speaker to the audio output.

It’s quite simple to play the synth – you just need to turn it on, cover the LDR’s and start to push the momentary switches. You can tune the keys with the master tune pot and use the PWM pot to find that sweet spot.

Now flick on the 2 drone oscillators. You can use the two pots to tune this as well and get them to play in sync. Play around with the LDR’s and keys and see what sounds you can get out of it

To play the arpeggiator, just turn it on and start to play with the pots for speed and modulation.

I also added a pot that bypasses the momentary switches (keys) so you can play the synth with just one pot and the LDR’s. That’s a lot of fun to do and you can also play the arpeggiator with the one pot as well.

I also used my Echo and Reverb box (make your own here) and played the synth through that as well. You get some great depth of sound when you hook it up to the synth. I definitely recommend that you also make one of these as it takes the synth to another sonic level.

Experiment and see what sounds you can get out of your synth.


---
*110 images archived*
