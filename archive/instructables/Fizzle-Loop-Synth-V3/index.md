# Fizzle Loop Synth V3 (555 Timer)

Source: https://www.instructables.com/Fizzle-Loop-Synth-V3/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)


## Step 1: Parts

![Step 1: Parts image 1](images/step02_01.jpg)

![Step 1: Parts image 2](images/step02_02.jpg)

![Step 1: Parts image 3](images/step02_03.jpg)

![Step 1: Parts image 4](images/step02_04.jpg)

![Step 1: Parts image 5](images/step02_05.jpg)

![Step 1: Parts image 6](images/step02_06.jpg)

![Step 1: Parts image 7](images/step02_07.jpg)

![Step 1: Parts image 8](images/step02_08.jpg)

Parts:1.       Resistors.Use metal film ones – they are better quality and cost about the same as other ones.  Also, buy them in assorted lots on eBay-          4.7K X 2-          3.3K X 2-          7.5K-          3.6K-          1.5K2.       CapacitorsYou can also buy these in assorted lots on eBay, which I suggest you do-          100uf X 2-          220uf-          22uf-          47uf-          2.2uf3.       Making a vactrol-          5mm white LED X 2  – eBay-          LDR (Light Dependent Resistor) X 2  - eBay-          Heat shrink (needs to be able to fit over the LED so 5 mm should be fine.4.       10K Potentiometers X 6 – eBay5.       Potentiometer knobs X 6 - eBay6.       555 Timer X 3 – eBay7.       3mm LED X 2 – eBay8.       SPDT Switches X 2 – eBay.9.       0.5W 8ohm speaker – eBay.  You can use a larger one if you want to I used a small one as my case was small.10.   3.5mm output jack socket – eBay11.   9v Battery12.   9V battery holder – eBay13.   Prototype Board – eBay14. Momentary Switches X 2 – eBayIf you also want to add a amp to increase the volume – then you will also need the following parts14.   Small amp module – eBay15. 10K pot (This is one of the 6 that I have included above)16.   Some type of case to add everything into.  I used an old torch I had lying around.


## Step 2: About the Circuit

![Step 2: About the Circuit image 1](images/step03_01.jpg)

![Step 2: About the Circuit image 2](images/step03_02.jpg)

![Step 2: About the Circuit image 3](images/step03_03.jpg)

At first glance, the circuit might look a little complicated but it's really pretty simple. The best way to make this synth is in stages which is how I will explain each step in making the circuit.  You'll also notice that I have included 2 schmatics, the 2nd one includes a amp module and volume pot.  It's not necessary to add this but it will dramatically increase the volume.  However, I did add an output socket so you can just plug it into a portable speaker to increase the colume.  If you also download Fritzing you can play around with the schematics yourself.I'll go through what each 555 timer does and will try to explain some of the features and how the synth works.  555 Timer 1 & 21. Both 1 & 2 timers are basically a flashing LED circuits.  To be able to control the speed of the LED on each 555 IC, there are 2 different capacitor values.  These are connected to a SPDT switch which allows you to change the speed of the LED's2. Also connected to each IC is a 10K pot.  This also allows you to control the speed of the LED's.  Vacrol1. IC timers 1 & 2 are also connected to a vacrol.  Inside the vactrol is an LED and a Light dependant resistor (LDR).  There is a pot connected to each which controls the brightness of the LED's which changes the pitch and tone2. Check out the next step on what a vacrol is.555 Timer 31. Lastly, IC 3 generates different sounds depending on the brightness of light.  There is also a pot that controls pitch.2.  IC 3 is connected to IC's 1 and 2 via 2 vactrols.  When you connect the LED's to the LDR's (which is what a vacrol is) you have a fizzle loop synth!So to summarise - LED's blink at different rates and brightness's which create rhythms and beats controlled by various pots and switches.   fizzle+loop+synth+with+amp.fzzDownloadfizzle+loop+synth+without+amp.fzzDownload


## Step 3: What's a Vacrol?

![Step 3: What's a Vacrol? image 1](images/step04_01.jpg)

![Step 3: What's a Vacrol? image 2](images/step04_02.gif)

A vacrtol is made from 2 common component, an LED and a Light Dependant Resistor (LDR).  The parts are incorporated into one package  and face each other.  I use heat shrink which seems to work well as a casing.  It’s important that the only light that the photo cell can detect is from the LED. If outside light is able to reach the photo cell, then it will interfere with the performance and sound, that’s why you need to add something like heat shrink to protect them.When wired-up, the Vactrol acts like a potentiometer - applying a voltage to the Vactrol's LED has the same effect as turning up the knob on the potentiometer.  Now if you dim the LED or flash it (like in the Fizzle Loop Synth) and hook it up to a 555 timer, then you can generate different tones and rhythms.Next I'll go through how to easily make your own vacrol.  You will need 2 for this project


## Step 4: Making a Vactrol

![Step 4: Making a Vactrol image 1](images/step05_01.jpg)

![Step 4: Making a Vactrol image 2](images/step05_02.jpg)

![Step 4: Making a Vactrol image 3](images/step05_03.jpg)

![Step 4: Making a Vactrol image 4](images/step05_04.jpg)

![Step 4: Making a Vactrol image 5](images/step05_05.jpg)

![Step 4: Making a Vactrol image 6](images/step05_06.jpg)

![Step 4: Making a Vactrol image 7](images/step05_07.jpg)

Steps:1. Cut a small length of heat shrink tube. The LED and photo cell need to be able to fit inside snuggly.  You also want to have a little excess heat shrink so you can pinch it together once heated and ensure no light can enter the vacrol. 2. Place the LED into the heat shrink with the legs facing out and also do the same for the photo cell. Make sure that they are touching inside the heat shrink.  Also mark the ground leg on the LED so you know which one is which3. Heat the heat shrink and start to shrink it. Start with the LED end first and when it has shrink enough, grab some pliers and flatten the end of the heat shrink so it is sealed shut. 4. Do the same for the LDR5. Make 2 of these 6. That’s it! You have made an important component to the fizzle loop synth


## Step 5: Making the Circuit - IC Timer 1 and 2

![Step 5: Making the Circuit - IC Timer 1 and 2 image 1](images/step06_01.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 2](images/step06_02.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 3](images/step06_03.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 4](images/step06_04.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 5](images/step06_05.jpg)

As mentioned earlier, I'm not going to go through a step by step process on how to add each component to the circuit.  I'm going to assume you have put circuits together and my schematic makes some sense.  I will go through a few interesting parts of building this section of the circuit. The first 2 timers are pretty much identical in how they are connected to the board.  The only difference is a switch connected to the 2nd IC.The LEDYou may have noticed that there is an LED by itself, connected to pin 3, along with the vactol.  This LED acts as a visual when creating tunes and flashes at the same time as the LED inside the vacrolWiresYou'll need to add wires to the circuit board which will be connected to the pots and switches later on.  I use computer ribbon cable wire for this as it's strong, thin and you can pick it up for free at most ewaste recycle places.  Add all of the wires to the circuit board first and make sure you give yourself enough length on each as they will need to be connected later on once the circuit is completed.Adding the Vactrol1. Solder the legs of the LED's and LDR directly to the prototype board2.  Ensure that the LED legs are facing down and the positive leg is closest to the timer3.  Connect the positive LED leg to pin 3 and the ground to ground on the prototype board4.  Connect one of the legs of the LDR to positive, the other will be connected to pin 6 on 555 timer 3Check out the next step on how the caps are attached to the SPDT switches


## Step 6: Making the Circuit - IC Timer 3

![Step 6: Making the Circuit - IC Timer 3 image 1](images/step07_01.jpg)

![Step 6: Making the Circuit - IC Timer 3 image 2](images/step07_02.jpg)

![Step 6: Making the Circuit - IC Timer 3 image 3](images/step07_03.jpg)

![Step 6: Making the Circuit - IC Timer 3 image 4](images/step07_04.jpg)

555 IC 3 is the timer that gives you your tunes.  It's actually a basic light thermin based on the slidersynth by Deno which I have also built here.  I've taken it a few steps further with the fizzle loop synth but basically it uses the same concepts.  I'll go through a few highlights of this section of the buildSteps:1. There's a 10K pot that is connected to pin 6 and ground.  This is used to control the overall pitch of the synth.  You could use a 5K pot as well for this section.  Just experiment and work out what works best for you.2. You will also notice that there is a momentary switch connected to the vactol on the 2nd IC and also connected to pin 7 on IC 3.  This momentary switch should always be on and is only off when you push it down.  It changes the tone when pushed down3.  After experimenting a little I worked out that connecting pins 3 on both both IC 2 and 3 you can get an interesting drum type sound.  Adding a switch to this section allows you to change between rythum and drums.4.  Lastly I included a 3.5mm jack socket.  This allows you to plug it into an amp for a louder sound.  I definitly suggest you add an output socket so you can really pump up the volumne.


## Step 7: Adding Capacitors Directly to the Switches

![Step 7: Adding Capacitors Directly to the Switches image 1](images/step08_01.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 2](images/step08_02.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 3](images/step08_03.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 4](images/step08_04.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 5](images/step08_05.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 6](images/step08_06.jpg)

One of the aims in making the circuit was to try and reduce the size as most as possible.  I had to if I wanted it to fit inside a small case such as the flashlight case that I used in this project.  Because of this I decided not to solder the capacitors connected to pin 2 to the prototype board but directly to the SPDT switch.Steps:1. Solder the positive legs of the 100uf cap to the first pin on the switch, the 220uf to the middle pin and the 330uf cap to the last pin 2.  Do the same again for the other caps for 555 timer 2.  There are different cap values for this timer - you just need to make sure that they are connected in descending order, 10k 22k and 47k2. For each switch, connect all of the ground legs of the caps together.  These will be connected to pin 2 on 555 timers later on 3. The other pins on each of the switches can also be connected together.  These will be connected to ground on the prototype board later.


## Step 8: Making the Case - Adding the Components

![Step 8: Making the Case - Adding the Components image 1](images/step09_01.jpg)

![Step 8: Making the Case - Adding the Components image 2](images/step09_02.jpg)

![Step 8: Making the Case - Adding the Components image 3](images/step09_03.jpg)

![Step 8: Making the Case - Adding the Components image 4](images/step09_04.jpg)

![Step 8: Making the Case - Adding the Components image 5](images/step09_05.jpg)

![Step 8: Making the Case - Adding the Components image 6](images/step09_06.jpg)

![Step 8: Making the Case - Adding the Components image 7](images/step09_07.jpg)

![Step 8: Making the Case - Adding the Components image 8](images/step09_08.jpg)

![Step 8: Making the Case - Adding the Components image 9](images/step09_09.jpg)

![Step 8: Making the Case - Adding the Components image 10](images/step09_10.jpg)

![Step 8: Making the Case - Adding the Components image 11](images/step09_11.jpg)

The case I used is an old flashlight that I had lying around.  The lens section was a perfect spot to add a small speaker.  The case is a tight fit for all of the electronics but I wanted tpo make a pocket sized flzzle loop synth this time. Steps:1. First you need to design the layout of the pots and switches.  This is an important part, especially if you are using a small case like I did in thsis build.2. You'll also need to take into consideration how everything will fit inside the case.  Wires, battery and the circuit board will need to be cramed inside so make sure you plan this out too.3.  Once you have planned out the build it's then time to start to add the components.  Drill the holes in the case  and attach all of the pots, switches and LED's needed for the build.


## Step 9: Wiring-up the Circuit

![Step 9: Wiring-up the Circuit image 1](images/step10_01.jpg)

![Step 9: Wiring-up the Circuit image 2](images/step10_02.jpg)

![Step 9: Wiring-up the Circuit image 3](images/step10_03.jpg)

![Step 9: Wiring-up the Circuit image 4](images/step10_04.jpg)

![Step 9: Wiring-up the Circuit image 5](images/step10_05.jpg)

![Step 9: Wiring-up the Circuit image 6](images/step10_06.jpg)

![Step 9: Wiring-up the Circuit image 7](images/step10_07.jpg)

![Step 9: Wiring-up the Circuit image 8](images/step10_08.jpg)

![Step 9: Wiring-up the Circuit image 9](images/step10_09.jpg)

The case should now have all of the components added to it ready for wiring.  Wire for some odd reason takes up a fair amount of space inside a case so you should try to make the wires a short as possible.  Also, it's good practice to be able to remove the circuit board out of the case so you can fix any issues with the connections if necessary.Steps:1. Place the circuit board inside the case.  Also place the battery in the case to make sure you have enough room for everything.2. Start to connect each of the compents to the wires on the circuit board.  Take your time and make sure that each wire is connected correctly.3. Trim the excess wire before soldering onto each component.4.  If you want to add an audio amp and volume pot - check out the next step.4. Once all the wires are connected add the battery and test.  If nothing happens, you'll have to check over your connections and see if any are incorrect.  If it works then congrats, you have made your very own fizzle loop synth. Now to add the knobs and work out how this thing works


## Step 10: Adding an Audio Amp and Volume Pot

![Step 10: Adding an Audio Amp and Volume Pot image 1](images/step11_01.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 2](images/step11_02.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 3](images/step11_03.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 4](images/step11_04.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 5](images/step11_05.jpg)

Once I had built the synth I decided that adding a small amp and volume pot would allow me to really annoy everyone in the house.  It's a easy add-on and definitely worth including in the build.  The amp I used can be picked-up on eBay for cheap and I have included a link in the parts section.Steps:1. Check out the schematic.  I have highlighted the added amp and pot and also where they are connected.  In the schematic the symbol for the amp is missing the ground wires for input and output.  Check out the other schematic which I did which will also help work out hownto wire this up2. Connect the ground and positive on the amp to the 9v battery.3. The input section on the amp should be connected as follows: positive to pin 3 on the 3rd 555 IC and ground to the ground section on the circuit board4. The output should be connected as follows: positive to the positive solder point on the speaker and the ground to the ground solder point on the speaker5. To add a volume pot I found that the best place to connect it is to the output socket.  If you add it directly to the speaker I found that it caused some interference to the synth and changed the sound.  Adding it to the socket isolates it from the speaker and stops the interference.


## Step 11: Adding the Knobs and How to Play the Synth

![Step 11: Adding the Knobs and How to Play the Synth image 1](images/step12_01.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 2](images/step12_02.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 3](images/step12_03.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 4](images/step12_04.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 5](images/step12_05.jpg)

The final part of the build is to add some knobs to the build.  You are now ready to start experimenting and making some awesome sounds. Check out the image attached which shows what each knob and switch does.  Don’t be afraid to experiment with different capacitor values on the switches or different resistor values on the LED’s.  These are a tonne of different options on these parts and you can get many different sounds by changing them.  You could also look at changing the potentiometer values as well, which would give you a different range of sounds.You could even add another flashing LED 555 timer and tie this into the light Theremin 555 timer (timer 3 on the schematic).  Maybe add a switch to each 555 timer so you can turn it off or no.There are a tonne of mods you could do, so make sure you try some different set-ups before you build your own


---
*69 images archived*
