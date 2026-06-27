# Moog Light Synth V2

Source: https://www.instructables.com/Moog-Style-Synth-V2/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

![Intro 6](images/intro_06.jpg)

This synth is a pulse width modulated oscillator, routed through a light-controlled resonant low pass filter. The "growling" oscillator tonality is supplied via a PWM and an awesome high-resonance low pass filter. The oscillator is controlled via 2 Light dependent resistors (LDR) and gives you the ability to create amazing musical expression. The 10 “keys” give you different tones and allow you to play it like a keyboard

Also included is 2 Hex inverter drones, supplied via a 40106 IC. The 2 two adjustable drone oscillators give this synth three oscillators in total. You also have the ability to turn off the 2 hex inverter drones and just play around with the other oscillator.

I also added the ability to play the synth just with one potentiometer and the LDR’s. When combined with the echo/reverb feature you can really get some fantastic sounds from the synth.

Just watch the YouTube clip and you’ll see what I mean

Lastly, I have to give a shout out to Pete McBennett who designed this awesome circuit. Check out his YouTube channel here

You can check out the first one I built here


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

![Step 1: Parts image 3](images/step01_03.jpg)

![Step 1: Parts image 4](images/step01_04.jpg)

![Step 1: Parts image 5](images/step01_05.jpg)

![Step 1: Parts image 6](images/step01_06.jpg)

![Step 1: Parts image 7](images/step01_07.jpg)

![Step 1: Parts image 8](images/step01_08.jpg)

The Moog Synth

I have designed a PCB for this circuit so all you need to do is to send the gerber files to a PCB manufacturer like JLCPCB (Not affiliated) who will print the board for you. The circuit and board were put together using Eagle and all of the files including the schematic, board and gerber files can be found in a Google Drive link in the next step

The parts list is also available in my Google drive as an excel file and I have included as a PDF in this Instructable.

The Rest of the Parts:

1. Potentiometer Knobs - eBay

2. Echo/Reverb module - eBay

3. 2 X 50K Potentiomeners (for the echo/reverb module) - eBay

4. 10 X momentary switches - Ali Express

5. 2 X SPDT switches - eBay

6. Wire. I like to use computer ribbon cable. you can buy it on Ali Express or just visit a place where e-waste is dumped to get it for free

7. Li-po Battery - eBay. I used an old mobile battery to power the synth. They work great for projects like this and you can get them for free. check out this 'ible on how to find them and use them

8. Charging and voltage regulator module - eBay

9. Micro USB module - eBay

10. Water Decal - eBay

11. 40mm X 80mm X 10mm length of hard wood (for making the case) - Hardware store


## Step 2: The Moog Style Synth - Circuit and Board

![Step 2: The Moog Style Synth - Circuit and Board image 1](images/step02_01.jpg)

![Step 2: The Moog Style Synth - Circuit and Board image 2](images/step02_02.jpg)

![Step 2: The Moog Style Synth - Circuit and Board image 3](images/step02_03.jpg)

As mentioned in the previous step, you can find the schematic and board (designed in Eagle) in my Google drive. If you want to you can play around with these yourself in Eagle. I have also saved the gerber files which is what you need to send to a PCB manufacturer to print the board


## Step 3: Soldering the Components to the Board

![Step 3: Soldering the Components to the Board image 1](images/step03_01.jpg)

![Step 3: Soldering the Components to the Board image 2](images/step03_02.jpg)

![Step 3: Soldering the Components to the Board image 3](images/step03_03.jpg)

![Step 3: Soldering the Components to the Board image 4](images/step03_04.jpg)

![Step 3: Soldering the Components to the Board image 5](images/step03_05.jpg)

![Step 3: Soldering the Components to the Board image 6](images/step03_06.jpg)

Steps:

1. I always start with adding the resistors first to the board. They are usually the lowest part on the board and it makes it easy to do these first. Plus there are a heap of them so it's good to get them out of the way

2. Once I have all the resistors soldered I then work on other low profile parts such as the diodes.

3. Next I add the IC holders pin headers

4. After that I start to add on the taller components like the capacitors and transistors.

5. Lastly I add in the IC's and give it a test. Adding pin headers makes it pretty easy to test, you just need some female jumper leads and add the components onto the ends of these. It's always good practice to test any circuit you have made before you go the whole way and add it to the build. Nothing worse trying to troubleshoot when there are wires everywhere.


## Step 4: About the PCB

![Step 4: About the PCB image 1](images/step04_01.jpg)

The attached image shows the different connections to the PCB and how they are connected to the components. I've also included a glossary below which will help you understand what each of the connections to the PCB are for and what they do.

Out = Audio Out. To be able to hear the synth you will need to connected it to an amplifier or portable speaker. This connection will later be connected to the "in" on the echo Reverb Board

Base = Drone oscillator, 100K potentiometer

Tenor = Drone oscillator, 100K

Oscillator on/off = This is used to turn off the drone oscillator

LED = Power on/off indicator

Tone = Master tuning control, 50K potentiometer

PWM = 100K trimmer potentiometer. This "tunes" the pulse width modulated oscillator. You'll need to adjust this until you find the sweet spot

LDR 1 & 2 = This is where the Light Dependent Resistors are connected.

PWR = 9v power source to run the synth

Single/Multi Control = I added this so you can control the synth from just one potentiometer. You can also use the Tone pot to play around with the sound as well when using the single pot control. This is a lot of fun when you have echo on.

Switch = This turns on & off the single multi control

100K = This is the potentiometer that controls the synth when one single play

Switch 1 = One leg on each of the 10 momentary switches used to play the synth need to be connected together. They are then connected to the "Switch 1" connection on the PCB

Switch 2 = Consists of 10 connections, each on needs to be connected to one of the legs on the 10 momentary switches


## Step 5: Moding the Echo/Reverb Module

![Step 5: Moding the Echo/Reverb Module image 1](images/step05_01.jpg)

![Step 5: Moding the Echo/Reverb Module image 2](images/step05_02.jpg)

I did an Instructable on how to mod the echo and reverb module which can be found here. It's not really a mod per se, more just now to had the echo pot and what resistor to remove. I won't go through this in much detail here so if you need further instructions, check out the 'ible above.

Steps:

1. First you'll need to remove one of the SMD resistors (R27). I do this with an exacto knife and it seems to work well each time. Just get the tip of the knife on the side of the resistor and gently pry it up

2. Next, you will probably need to remove the reverb port which is soldered onto the board. If however you are able to connect the pot to the panel without having to remove it then just leave it on. If you have a de-soldering device then use this as the traces have a tendency to lift if you just add a soldering iron to it. If you don't then use a pair of wire cutters and just cut it away.

3. If you look on the board you will see that along with the 3 solder points for the pot that you just removed, there are 3 others near it. These ones are for controlling echo. You'll need to solder wires onto each of the solder points for reverb and echo control.

4. That's all you need to do for the moment. later on you will need to connect the wires to the each and reverb pots.


## Step 6: Creating the Front Panel

![Step 6: Creating the Front Panel image 1](images/step06_01.jpg)

To design the panels I used Inkscape, a vector graphics editor which you can download for free! There's a lot of information available on how to use it and I would suggest you do a couple of the basic tutorials to familiarize yourself with the different features if you haven't used it before

I did a couple video's on how to design knob scales and also make a front panel which I have included above.

There is even an extension that you can download so you can design knob scales easily and simply which you can download here

However, if you don't want to bother learning how to design your own, you can always just use mine which I have attached as a PDF. I have also includes the Inkscape file so you can play around with that as well if you want to.


## Step 7: Adding the Water Acrylic to the Front Panel

![Step 7: Adding the Water Acrylic to the Front Panel image 1](images/step07_01.jpg)

![Step 7: Adding the Water Acrylic to the Front Panel image 2](images/step07_02.jpg)

![Step 7: Adding the Water Acrylic to the Front Panel image 3](images/step07_03.jpg)

![Step 7: Adding the Water Acrylic to the Front Panel image 4](images/step07_04.jpg)

![Step 7: Adding the Water Acrylic to the Front Panel image 5](images/step07_05.jpg)

![Step 7: Adding the Water Acrylic to the Front Panel image 6](images/step07_06.jpg)

![Step 7: Adding the Water Acrylic to the Front Panel image 7](images/step07_07.jpg)

Steps:

1. Once you have your design you should print a few copies of it on normal A4 paper. This will allow you to use it as a template to decide how big to cut the opal acrylic. The acrylic will in the end be the front panel. I used opal coloured acrylic but you can use any colour you want.

2. Cut the acrylic panel to the right size. I used a band saw tio do this but you could do it by hand as well. Last time I did this I pre-drilled the holes. However, it makes it very hard to line up the decal so don't worry about pre-drilling.

3. Next, print the panel design directly onto decal paper and leave to dry for 30 minutes. You can also spray with clear acrylic as well to protect the ink but I didn't bother.

4. Add the water decal to the acrylic by Placing the decal into some warm water and once it start to lift off, carefully slide it onto the acrylic. Ensure everything is lined up right and remove any excess water.

5. Once fully dried, sprayb some clear acrylic paint on the panel and repeat 2 to 3 times.

5. Mark all of the sections with a punch that need to be drilled.

6. Drill out the holes to the right size using a stepped drill piece.


## Step 8: Making the Case

![Step 8: Making the Case image 1](images/step08_01.jpg)

![Step 8: Making the Case image 2](images/step08_02.jpg)

![Step 8: Making the Case image 3](images/step08_03.jpg)

![Step 8: Making the Case image 4](images/step08_04.jpg)

![Step 8: Making the Case image 5](images/step08_05.jpg)

![Step 8: Making the Case image 6](images/step08_06.jpg)

![Step 8: Making the Case image 7](images/step08_07.jpg)

used some strips of hardwood to make the case. It's used for edging and can be brought at any hardware store. The dimensions are 40mm X 10mm X 1000mm

Steps:

1. The first thing you need to do is to cut a groove along the wood in order to secure the panel into. I use a dremel with a router attachment to do this.

2. Secure the wood with some clamps and run the bit near the top of the wood. Take your time and make sure you keep the dremel nice and straight.

3. Measure and cut the wood to size. The best way to do this is to just slip in the front panel into the groove of the wood and measure where to make the cuts

4. Before you secure the front panel into the case, paint the top section and inside. When the panels in place it will make it hard to do and you might get paint on the panel. I used some clear stain to highlight the grain in the wood. The reason why you don't paint it all is you need to sand the wood once the case is complete.

5. Place the front panel into the grooves of the wood and use some PVC to glue it together. If you find the panel is a little big and the wood doesn't right then just remove a little of the acrylic along the edge with a sander.

6. Clamp and leave to dry for 12 hours.


## Step 9: Sanding the Case and Making a Base

![Step 9: Sanding the Case and Making a Base image 1](images/step09_01.jpg)

![Step 9: Sanding the Case and Making a Base image 2](images/step09_02.jpg)

![Step 9: Sanding the Case and Making a Base image 3](images/step09_03.jpg)

![Step 9: Sanding the Case and Making a Base image 4](images/step09_04.jpg)

![Step 9: Sanding the Case and Making a Base image 5](images/step09_05.jpg)

![Step 9: Sanding the Case and Making a Base image 6](images/step09_06.jpg)

![Step 9: Sanding the Case and Making a Base image 7](images/step09_07.jpg)

![Step 9: Sanding the Case and Making a Base image 8](images/step09_08.jpg)

![Step 9: Sanding the Case and Making a Base image 9](images/step09_09.jpg)

Once the glue is dry you can then use a sander to make the edges nice and clean. I also rounded off the top sections which gives it a bit of a softer look.

Steps:

1. If you have a belt sander then this will be an easy job. If not, a hand sander will suffice

2. Sand each of the sides of the case until the wood is smooth and level.

3. To round off the top sides of the case I agauin used to sander. Just rotate the section to be rounded on the sander until you get the desired effect.

BE CAREFUL - Check out the last image to see what I mean. I managed to touch the sander onto the front panel and scratched the name of the synth!

4. To finish, use some 400 grit sandpaper to smooth everything out.

5. The base is just a piece of ply wood. First, measure and cut to size

6. Place onto the bottom of the case and add some screws to hold it in place.

7. Use the sander again to smooth the edges and make them level with the case.

8. Un-screw the base and make a little mark on both the base and case so you know which ends go together


## Step 10: Adding the Componets to the Front Panel

![Step 10: Adding the Componets to the Front Panel image 1](images/step10_01.jpg)

![Step 10: Adding the Componets to the Front Panel image 2](images/step10_02.jpg)

![Step 10: Adding the Componets to the Front Panel image 3](images/step10_03.jpg)

![Step 10: Adding the Componets to the Front Panel image 4](images/step10_04.jpg)

![Step 10: Adding the Componets to the Front Panel image 5](images/step10_05.jpg)

![Step 10: Adding the Componets to the Front Panel image 6](images/step10_06.jpg)

![Step 10: Adding the Componets to the Front Panel image 7](images/step10_07.jpg)

![Step 10: Adding the Componets to the Front Panel image 8](images/step10_08.jpg)

This is pretty straight forward, just be careful not to scratch the front panel when you are scecuring the components.

Steps:

1. There are 10 momentary switches to add so you may as well start with these to get them out of the way

2. Next add the pots and the 3 SPDT switches

3. Then comes the audio socket

4. Lastly, you can add the potentiometer knobs as well.


## Step 11: Adding the Circuits and Battery to the Case

![Step 11: Adding the Circuits and Battery to the Case image 1](images/step11_01.jpg)

![Step 11: Adding the Circuits and Battery to the Case image 2](images/step11_02.jpg)

![Step 11: Adding the Circuits and Battery to the Case image 3](images/step11_03.jpg)

![Step 11: Adding the Circuits and Battery to the Case image 4](images/step11_04.jpg)

Now that you have the case, panel and PCB's done, it's time to start thinking about connecting everything together. Just before that happens though, you'll need to secure the battery and PCB's to the base of the synth.

Steps:

1. Lay all of the parts onto the back panel and work out the best place to locate them. For example, if you add the micro USB charging module at the top, then make sure that you locate the battery at the top as well.

2. Once you are happy with the layout, use some good, double sided tape and stick everything down. The great thing about using tape is it's easy to pull off the parts from the back of the wood if you need to. You could also screw down the boards later if you wanted to once everything has been tested

3. To be able to charge the battery, you will need to add a micro USB module somewhere on the case. The easiest way to do this is to make a small cut-out with a flat file at the bottom of the case. You can then add a little superglue and stick it in place. Later this will be connected to the charging module.


## Step 12: Connecting Everything Together

![Step 12: Connecting Everything Together image 1](images/step12_01.jpg)

![Step 12: Connecting Everything Together image 2](images/step12_02.jpg)

![Step 12: Connecting Everything Together image 3](images/step12_03.jpg)

![Step 12: Connecting Everything Together image 4](images/step12_04.jpg)

![Step 12: Connecting Everything Together image 5](images/step12_05.jpg)

![Step 12: Connecting Everything Together image 6](images/step12_06.jpg)

![Step 12: Connecting Everything Together image 7](images/step12_07.jpg)

Steps:

1. Lay the top and bottom sections of the case next to each to each other.

2. First thing you should do is complete any soldering that needs to be done. Solder the wires from the echo/reverb module to the relevant pots on the front panel

3. Next, stick the battery charger and voltage regulator module on top of the battery. If you want more details on how to use this module then I've done an Instructable on this as well which can be found here. Wire-up the battery to the module and connect to the on/off switch. Also set the voltage to 9V on the module via the micro pot on the module. You'll need a multimeter to do this

NOTE: The module will always draw a little bit of power so I always connect the on/off switch from the battery to the module. That way you stop the module from drawing power from the battery and draining it over time. it's only a very small amount but it will drain it over a few weeks

4. You'll also need to add a couple wires from the echo/reverb module to the output on the charging module to power it. Also connect the positive and ground from the moog light PCB to the out on the charging module

5. Solder any wires needed to the switches as well. If you are confused at all then reference the image on step 3.

6. Once all of the soldering is done, you can start to connect the pots up to the PCB. Again, reference the image on step 3 for how to orientate the pots.

7. Test to make sure everything is working as it should before closing it up.

NOTE: Remember that you need to set the PWM trimmer pot. To do this, turn on the synth and slowly turn the trimmer pot. Once you hear some sound, push down on one of the buttons until you get a clean, modulated sound.

TIP - if you find that the echo/reverb isn't working, disconnect it from the battery and connect it again. Sometimes they need resetting before they will work.


## Step 13: So How Do You Work the Thing!

![Step 13: So How Do You Work the Thing! image 1](images/step13_01.jpg)

![Step 13: So How Do You Work the Thing! image 2](images/step13_02.jpg)

![Step 13: So How Do You Work the Thing! image 3](images/step13_03.jpg)

That's a good question! Turns out luckily that its very easy to play. I'll go through what each of the controls do and some of the quirks that I found that you can play around with as well

Steps:

1. First lets play around with the 10 keys. make sure that the single/multi pot is turned off

2. Place you fingers over the 2 LDR's and start to play one of the keys. You should get a nice deep growl of a sound. Move your fingers away from the LDR's and the PWM will give you different tones

3. Turn on the drone synth and you'll get a low drone. play around with the base and tenor until you get the oscillators in sync or close to.

4. Now you can play the PMW synth with the drone synth in the background

5. Now turn up to 7 both he reverb and echo and start playing the synth. You will notice the sounds are fatter and have more dimension due to the echo. change the echo length and speed by turning the echo pot

6. Turn the Tune pot to change the pitch of the PMW synth. You can have it play higher or a real deep base low

7. Ok - so now it's time to play around with the single/multi pot. First turn it on. You'll hear the PMW synth constantly running.

8. Place your finger's over the LDR's and slowly turn the single/multi pot. Give it some echo as well and you'll get some awesome droney sounds coming out of the synth. Now slowly turn the tune pot to change the pitch. Give it a quick turn and the echo will kick in.

9. You can even play the keys at the same time and get some funky sounds coming out of the synth

10. There is a small glitch that I found in the tune pot. If you tune the pot to about 3 you'll notice that the synth pulses. Play around with this as it's almost like a basic arpeggiator which you can play to.

11. This is just some basic's to get you started. There is plenty more that this little synth can do - I'll leave it up tp you to experiment and find them


---
*72 images archived*
