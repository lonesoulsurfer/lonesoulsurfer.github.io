# Make Your Own Headphone Amp V1

Source: https://www.instructables.com/Make-Your-Own-Headphone-Amp/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

I never really thought much about headphone amps until I tried one. I used to think it was all a bit of a gimmick. Why would you need a separate amp to drive the speakers in your headphones! It’s only when you try a headphone amp that you realise the benefits and sound quality improvement possible from a separate amp. The only problem is, you’ll never be able to listen to music again without one!

You can buy an off-the-shelf one if you want to but I’m going to assume you’re reading this because you’d rather build your own. The build itself isn’t too difficult, although you will need some soldering and circuit experience to make this. If you have never done any circuit building, then you should start with this ‘ible which I did some time ago to help beginners.

The heart of the amp is 2 X LM386 IC’s. Unlike some headphone amps, you can run this one on a 9v battery but because of this, you need to be careful how you hook-up the ground connections. I’ll take you through this in the following steps.

Lastly, I’ll be building a few more of these and comparing different models in future ‘ibles.


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

Parts:

1. 2 X LM386 IC – eBay

Resistors. Use the metal film type, which are superior to the carbon ones, at least for this project

2. 10 Ohm – eBay

3. 18K – eBay

Capacitors. Make sure you use good, audio ones for the best possible sound. The electrolytic ones should be low leakage; low impedance type and the ceramic should be metal film, polypropylene. I have added links to eBay for these types of caps

4. 4 X 10uf – eBay

5. 3 X 470 uf eBay

6. 3 X 0.1uf - eBay

7. 100k duel gang potentiometer – eBay

8. 2 X 3.5mm stereo jack sockets – eBay

9. 9v Battery

10. 9V Battery holder – eBay

11. DPST toggle switch – eBay

12. Knob – eBay

13. Male to male audio cable 3.5mm - eBay

You can also add a charging socket which will require a 330 Ohm resistor as well as a socket. I’ll probably add this later so left it in the circuit diagram.

14. Case. I found a great case at Jaycar (electronics shop in Aust) which has its own battery compartment. It’s a little on the larger size but makes the job of fitting everything inside a pretty easy one. You can get them on eBay too


## Step 2: Separating Input and Output Grounds

![Step 2: Separating Input and Output Grounds image 1](images/step02_01.jpg)

Before you start to build this amp, you should read the below which goes through how to hook-up the ground connections. The important thing to remember is to separate the input and output grounds. If you don’t then you will get oscillations which will be auditable through the headphones.

So what does it mean to keep the input and output grounds separated? Basically it means to connect all of the input grounds in the circuit together and all of the output grounds together. They are then connected together by a single connection.

The following at all input grounds so will need to be connected together on the prototype board. Ground input from the socket, volume control ground pin, pins 2 and 4 of both IC's. All others are output grounds.

All I did to separate the grounds was to add the input connections along one of the vertical bus strips and the output next to them on the other vertical bus strip. This way you can connect the bus strips together at one point.


## Step 3: Making the Circuit Pins 1, 2 & 4

![Step 3: Making the Circuit Pins 1, 2 & 4 image 1](images/step03_01.jpg)

![Step 3: Making the Circuit Pins 1, 2 & 4 image 2](images/step03_02.jpg)

![Step 3: Making the Circuit Pins 1, 2 & 4 image 3](images/step03_03.jpg)

![Step 3: Making the Circuit Pins 1, 2 & 4 image 4](images/step03_04.jpg)

![Step 3: Making the Circuit Pins 1, 2 & 4 image 5](images/step03_05.jpg)

![Step 3: Making the Circuit Pins 1, 2 & 4 image 6](images/step03_06.jpg)

I’ll go through how you make one channel of the circuit. The other is built exactly the same.

Steps:

1. First, solder an IC socket header for the LM386 IC to the prototype board

2. Connect pins 2 and 4 to the input ground

3. Add a 18K resistor to pin 1 and connect the other leg to a spare spot on the prototype board close to pin 5.


## Step 4: Making the Circuit - Pins 5

![Step 4: Making the Circuit - Pins 5 image 1](images/step04_01.jpg)

![Step 4: Making the Circuit - Pins 5 image 2](images/step04_02.jpg)

![Step 4: Making the Circuit - Pins 5 image 3](images/step04_03.jpg)

![Step 4: Making the Circuit - Pins 5 image 4](images/step04_04.jpg)

![Step 4: Making the Circuit - Pins 5 image 5](images/step04_05.jpg)

![Step 4: Making the Circuit - Pins 5 image 6](images/step04_06.jpg)

![Step 4: Making the Circuit - Pins 5 image 7](images/step04_07.jpg)

Steps:

1. Add the positive leg on the 470uf capacitor to pin 5 on the IC

2. Next, you need to add a 10uf capacitor to the leg of the 18K resistor and the other leg of the 470uf cap. Actually, there are a few parts that need to be added to the ground leg of this cap so make sure you plan this out first before you start to solder everything to the prototype board.

3. Attach the .01 cap to the same ground leg on the 470uf cap and the other leg to an empty spot.

4. Lastly, add a 10 ohm resistor to the .01 cap and solder the other leg to the output strip bus ground


## Step 5: Making the Circuit - Pins 6 & 7 and the Next Channel

![Step 5: Making the Circuit - Pins 6 & 7 and the Next Channel image 1](images/step05_01.jpg)

![Step 5: Making the Circuit - Pins 6 & 7 and the Next Channel image 2](images/step05_02.jpg)

![Step 5: Making the Circuit - Pins 6 & 7 and the Next Channel image 3](images/step05_03.jpg)

![Step 5: Making the Circuit - Pins 6 & 7 and the Next Channel image 4](images/step05_04.jpg)

![Step 5: Making the Circuit - Pins 6 & 7 and the Next Channel image 5](images/step05_05.jpg)

![Step 5: Making the Circuit - Pins 6 & 7 and the Next Channel image 6](images/step05_06.jpg)

Steps:

1. Pin 6 needs to be connect to positive bus strip

2. Connect the positive end of the 10uf cap to pin 7

3. Connect the ground leg on the 10uf cap to the output ground

4. That’s the main components in the first channel. You now need to build a duplicate exactly the same. One channel is for the left hand side speaker and the other for the right hand side. The 2 circuits will be connected via headphone sockets, wires and potentiometer


## Step 6: Making the Circuit - Battery Caps and Wires

![Step 6: Making the Circuit - Battery Caps and Wires image 1](images/step06_01.jpg)

![Step 6: Making the Circuit - Battery Caps and Wires image 2](images/step06_02.jpg)

![Step 6: Making the Circuit - Battery Caps and Wires image 3](images/step06_03.jpg)

![Step 6: Making the Circuit - Battery Caps and Wires image 4](images/step06_04.jpg)

![Step 6: Making the Circuit - Battery Caps and Wires image 5](images/step06_05.jpg)

![Step 6: Making the Circuit - Battery Caps and Wires image 6](images/step06_06.jpg)

Next thing to do is to add all of the wires that are needed to attach the circuit to the other components.

Steps:

1. You need to connect a couple of capacitors from positive to ground on the circuit board. This helps reduce noise. Solder a 470uf cap and a .01 cap from positive to ground

Wiring

Volume potentiometer and input socket

1. Solder a wire to input ground which will be attached to the right solder point on the pot,

2. A wire on each of pin 3 on the IC which will be connected to the middle solder point on the pot

3. Solder a couple of wires onto the input socket which should be connected to the tip and ring solder points on the socket

4. Solder a wire to the ground solder point on the input socket and then connected to the input ground bus on the circuit board

Output Socket

1. Solder a couple of wires to the negative leg on the 470uf cap. These will be connected to the tip and ring solder points on the output socket

2. Solder a wire to the ground solder point on the input socket and then connected to the output ground bus on the circuit board

Battery

1. Solder a wire to ground and another to positive for the battery holder. One of these will be connected to the switch later on


## Step 7: Wiring the Connections

![Step 7: Wiring the Connections image 1](images/step07_01.jpg)

![Step 7: Wiring the Connections image 2](images/step07_02.jpg)

![Step 7: Wiring the Connections image 3](images/step07_03.jpg)

![Step 7: Wiring the Connections image 4](images/step07_04.jpg)

![Step 7: Wiring the Connections image 5](images/step07_05.jpg)

![Step 7: Wiring the Connections image 6](images/step07_06.jpg)

Once you have added all of the wires to the circuit it's now time to connect them to the rest of the other bits.

Steps:

1. First add the pot, switch and the 2 sockets to the case. I added all of these parts to the front section of my case

2. Place the circuit into the case and start to solder the connections together. You want to be able to place the top of the case flat and then attach all of the wires. This will let you be able to open the case easily if necessary.

3. Carefully solder the wires to all of the correct connections. Take your time and refer to the schematic to make sure you do them correctly.

4. Once everything is connected, add a battery and check to make sure the amp works as it should. If it doesn't, check your connections and also the solder points on the circuit board so there's no short circuits.

5. If the amp works as it should, close up the case and get ready to be rocked by awesome sound.

NOTE: You may have noticed that here is an extra circuit inside the case. This was a voltage regulator that I was going to add until I noticed that it was causing some interference so I took it out. There isn't really any need for it, I just thought it might help add a filter to the power.


## Step 8: Using You Headphone Amp

![Step 8: Using You Headphone Amp image 1](images/step08_01.jpg)

![Step 8: Using You Headphone Amp image 2](images/step08_02.jpg)

![Step 8: Using You Headphone Amp image 3](images/step08_03.jpg)

![Step 8: Using You Headphone Amp image 4](images/step08_04.jpg)

![Step 8: Using You Headphone Amp image 5](images/step08_05.jpg)

![Step 8: Using You Headphone Amp image 6](images/step08_06.jpg)

![Step 8: Using You Headphone Amp image 7](images/step08_07.jpg)

Steps:

1. Now you have everything inside the case, it’s time to finally add the battery, turn it on and listen to the best sounding music your ears have heard!

2. Also, remember to make sure you don’t have the volume turned up fully on the amp and also your phone when you turn it on – you could damage your ears as it really pumps out the noise.

NOTE:

You may experience some “ticking” sounds sometimes when you have the volume down. This is caused by interference from usually a phone. The best thing to do if you experience this is to turn your phone onto aeroplane mode, which should stop any interference.


---
*44 images archived*
