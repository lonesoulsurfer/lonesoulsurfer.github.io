# Breadboard - Variable Power Supply

Source: https://www.instructables.com/Breadboard-Variable-Power-Supply/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

Getting power to your breadboard is one of the most fundamental things you need to do when prototyping and testing circuit. I've been using a 9V battery (my last power supply died a smoky death) and I figured it was time to upgrade.

The voltage supply in this project connects directly to your breadboard so there is no wires getting in the way, it is variable so you can change the voltage from 3.5V to 13V with a potentiometer, and is also rechargeable so no issues with flat batteries.

The build itself is relatively simple and you only need some basic soldering skills to make your own. The module that I have used in this project is one that I have used in many projects. It includes variable voltage and battery charger all in one. I even did an ‘ible on how to wire it up which can be found here. The power supply is powered by an old mobile battery but you could use an 18560 li-ion battery or something similar if you wanted to.

Let’s get building!


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

![Step 1: Parts and Tools image 4](images/step01_04.jpg)

![Step 1: Parts and Tools image 5](images/step01_05.jpg)

PARTS:

1. Voltage regulator & charging module – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=+3.7V+9V+5V+2A+Adjustable+Step+Up+18650+&_sacat=0&LH_TitleDesc=0&_sop=15&_osacat=0&_odkw=voltage+regulator+adjustable+charging)

2. Voltage Meter – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=voltage+meter&_sacat=0&LH_TitleDesc=0&_sop=15&_blrs=recall_filtering)

3. Switch – I used [this one](https://www.ebay.com.au/itm/184761890795?hash=item2b04aab7eb:g:yxUAAOSwk9dZmNIb) from [eBay](https://www.ebay.com.au/itm/274697763470?hash=item3ff5433a8e:g:cQwAAOSwfzZgOHhZ) but you could also use this one

4. Header pins. You will need to get double header pins – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=40+Pin+Header+Pins+Double&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=40P+Pin+Header+Pins+2.54mm+Double)

5. Prototype Board – [eBay](https://www.ebay.com.au/itm/10x-DIY-Prototype-Paper-PCB-Experiment-Board-Bakelite-Circuit-Board-4-8x13-3cm/142759746052?hash=item213d24da04:g:sFUAAOSwcEha0XL3)

6. Battery – I used an old mobile battery but you can use any li-po battery such as [18650](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1311&_nkw=18650+battery&_sacat=0) or buy a mobile battery from [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=mobile+battery&_sacat=0&LH_TitleDesc=0&_sop=15)

7. Wires. I used computer ribbon wire. It’s thin and I get it for free at my local e-waste

8. 100K Potentiometer – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=100k+potentiometer&_sacat=0&LH_TitleDesc=0&_sop=15&_osacat=0&_odkw=mobile+battery)

TOOLS:

1. Soldering Iron

2. Wire Cutters

3. Files

4. Belt Sander (comes in handy but not necessary)

5. Double sided Tape


## Step 2: Cutting the Prototype Board Down to Size

![Step 2: Cutting the Prototype Board Down to Size image 1](images/step02_01.jpg)

![Step 2: Cutting the Prototype Board Down to Size image 2](images/step02_02.jpg)

![Step 2: Cutting the Prototype Board Down to Size image 3](images/step02_03.jpg)

![Step 2: Cutting the Prototype Board Down to Size image 4](images/step02_04.jpg)

![Step 2: Cutting the Prototype Board Down to Size image 5](images/step02_05.jpg)

![Step 2: Cutting the Prototype Board Down to Size image 6](images/step02_06.jpg)

The first thing to do is to work out what size to make the prototype board. You’ll need to cut this down to fit.

Steps:

1. First, cut 2 lots of header pins off with a pair of wire cutters or an exacto knife. You will need a header pin for positive and ground and I used double header pins so they would secure better into the breadboard

2. Place the header pins into the power rails on each side of the breadboard. Place the prototype board into the header pins and work out the size that the prototype board can be

3. You can cut away sections of the prototype board with a pair or wire cutters. Use a sander and/or files to clean up the edges


## Step 3: Soldering the Header Pins Into the Prototype Board

![Step 3: Soldering the Header Pins Into the Prototype Board image 1](images/step03_01.jpg)

![Step 3: Soldering the Header Pins Into the Prototype Board image 2](images/step03_02.jpg)

![Step 3: Soldering the Header Pins Into the Prototype Board image 3](images/step03_03.jpg)

![Step 3: Soldering the Header Pins Into the Prototype Board image 4](images/step03_04.jpg)

You need to make a very small mod on the header pins to be able to solder them into place. The first time I tried to solder the pins into place I did them the wrong way round so make sure you do the mod!

Steps:

1. Grab one set of the header pins and hold them so the short end of the pin is facing down

2. Place the short end on a flat, hard surface and with the tips of your fingers, push the plastic around the pins down until it is at the bottom of the pins

3. Do the same of the other set of pins

4. Next, place a set of the pins into the prototype board so the plastic section is resting onto the back of the board and solder into place

5. Do the same for the other pin. Test to ensure that the pins fit into the power rails on the breadboard


## Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator

![Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator image 1](images/step04_01.jpg)

![Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator image 2](images/step04_02.jpg)

![Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator image 3](images/step04_03.jpg)

![Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator image 4](images/step04_04.jpg)

![Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator image 5](images/step04_05.jpg)

![Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator image 6](images/step04_06.jpg)

![Step 4: Adding Jumper Pins and Potentiometer to the Voltage Regulator image 7](images/step04_07.jpg)

To be able to connect the power regulator to the prototype board, you need to solder some pins to the battery and voltage out solder points.

STEPS:

1. Cut 4 single jumper pins

2. Place 2 of the jumper pins into the 'voltage out' on the voltage regulator and solder them onto place

3. Place another 2 jumper pins into the 'battery' solder points on the voltage regulator and solder them into place

4. Next, place the 100K potentiometer into voltage regulator (there are 3 holes in the voltage regulator to do this) and solder into place

5. The last thing to do is to solder the regulator onto the prototype board. The pins should fit into the holes in the board, however, you might need to slightly bend one of the legs to ensure a good fit. Make sure that the board is soldered to the back of the prototype board. This will help make turning the pot easier


## Step 5: Adding an On/off Switch

![Step 5: Adding an On/off Switch image 1](images/step05_01.jpg)

![Step 5: Adding an On/off Switch image 2](images/step05_02.jpg)

![Step 5: Adding an On/off Switch image 3](images/step05_03.jpg)

![Step 5: Adding an On/off Switch image 4](images/step05_04.jpg)

You'll need to add an on/off switch between the battery and the module. The voltage module draws power even when not in use and adding a switch between the battery and module will ensure the power isn't drained. When you charge the battery you need to make sure that the module is 'on' or it won't charge

STEPS:

1. First find a good spot to locate the switch, remembering you will need to add the voltage meter as well to the prototype board

2. I had to remove one of the legs on the switch to be able to locate it in the spot I did.

3. Once you find the right spot, solder it into place


## Step 6: Wiring

![Step 6: Wiring image 1](images/step06_01.jpg)

![Step 6: Wiring image 2](images/step06_02.jpg)

![Step 6: Wiring image 3](images/step06_03.jpg)

![Step 6: Wiring image 4](images/step06_04.jpg)

![Step 6: Wiring image 5](images/step06_05.jpg)

It's always hard to show how everything is wired via images so I have included a wiring diagram. You could add the wires to the top section of the prototype board but I wanted to have a clean look on the top so decided to wire underneath.

STEPS:

1. The wires need to be kept as flat and neat as possible. You also need to remember that the battery will need to be attached to the bottom of the prototype board so try and make sure that the wires are out of the way and there is room at attach it

2. The main thing to think about is how you want to power to be orientated in the breadboard. If you look at a breadboard buses (the section where power is added) the buses go in the following order; positive and then ground for both the top and bottom. I have always used the first row in the bottom as ground and the top as positive so I wired up the jumper pins is top - positive/ground bottom ground/positive.

4. Don't attach the battery yet though, you need to first add the voltage meter


## Step 7: Adding the Voltage Meter

![Step 7: Adding the Voltage Meter image 1](images/step07_01.jpg)

![Step 7: Adding the Voltage Meter image 2](images/step07_02.jpg)

![Step 7: Adding the Voltage Meter image 3](images/step07_03.jpg)

![Step 7: Adding the Voltage Meter image 4](images/step07_04.jpg)

The easiest way that I could figure out to add the voltage meter was to add a couple of resister legs to the positive and ground solder points on the meter.

STEPS:

1. De-solder the wires on the voltage meter

2. Cut a couple of legs off a resister and solder these to the solder points on the voltage meter

3. Place the resister legs on the voltage meter into the prototype board and solder into place

4. Connect the voltage meter to the 'voltage out' on the voltage regulator

5. You can add the battery once you have completed the wiring. Before you stick the battery down, give the whole thing a test and make sure there is power being provided to the pins and the voltage meter works

6. Add some good quality, double sided tap tot he battery and stick it into place

And that's it! Connect it to your prototype board and start building some circuits.


---
*39 images archived*
