# Dub Siren V3 - 555 Project

Source: https://www.instructables.com/Dub-Siren-V3-555-Project/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

![Intro 6](images/intro_06.jpg)

UPDATE - The PCB, Gerber files have all been updated as there was an issue which has been fixed. The files can be found in my Google Drive and are called 'Dub Siren V3.1'. Note also that I have created a different style of PCB which I have also included in a separate folder called 'Dub Siren V4'.

Ok - so this is going to be my last dub siren build (maybe...). This new one is an extension on the others that I have built and is definitely the best and easiest version I have designed.

So what is a dub siren?

Dub sirens originated in Jamaica in the late 60’s, early 70’s where they started to use police or fire engine sirens and analog synths to create sound effects for their music. Later it was emulated to live DJ performances.

This dub siren is based around 2 x 555 timers and a LM741 Op amp. Adding a bunch of pots and buttons allows you to create and control a whole heap of cool sounds from a traditional siren to a long toned note.

They are usually played with a reverb guitar pedal but I decided to add my own reverb circuit (no need to make this one as you can buy them on eBay) to the final build. Adding this circuit gives you some amazing sounds to help you play along to your favourite dub, hip hop, disco house or whatever else you want to play along to.

When I think back to the first one that I built (link here), I can't believe that I actually got it to work! I mean it looks great (in my humble opinion) but used 3 X 9v batteries to power it and was a hot mess of wires and electronics.

In this version, The dub siren and amp are on one, slim PCB and there are JST connectors for easy connection to the echo/reverb module, battery and switches. The potentiometers are also mounted on the PCB which reduces the amount of wires needed.

I have also designed a front panel which incorporates the PCB and turns this build into a very professional looking one. I should learn how to do 3D printing next so I can design some cases! At the moment though I'm using wood which I'm happy to use as it gives the projects a nice retro feel.

I have provided all of the gerber & Eagle files along with the front panel design so you can also easily build your own dub siren.

Hackaday and Hackster have also done a review on this build. I've provided the links if you are interested in checking them out

Hackaday

Hackster

Let's get going


## Step 1: Dub Siren & Echo Reverb Module Parts List

![Step 1: Dub Siren & Echo Reverb Module Parts List image 1](images/step01_01.jpg)

![Step 1: Dub Siren & Echo Reverb Module Parts List image 2](images/step01_02.jpg)

I have included the component parts list in a PDF (attached) and you can also find an excel version in my Google Drive. It might make it easier having a printable parts list when you are shopping for the parts. I have also included links to the parts below:

Dub Siren

- Capacitor Polyester - eBay
47nf X 2
150nf
- 47nf X 2
- 150nf
- Capacitor Polarized - eBay
47uf
220uf
100uf
10uf
- 47uf
- 220uf
- 100uf
- 10uf
- IC
741 - eBay
386 - eBay
555 X 2 - eBay
- 741 - eBay
- 386 - eBay
- 555 X 2 - eBay
- LED 5mm - eBay or LED Filament - eBay
- Potentiometer 50K X 5 - Ali Express
- Switch Momentary - eBay
- Switch SPDT X 2 - eBay
- Resistors - eBay
560R X 3
4.7K10K X 2
10R
68K
2.2K X 2
- 560R X 3
- 4.7K10K X 2
- 10R
- 68K
- 2.2K X 2
- Transistor 2N3904 - eBay
- JST Connector Mini 2.0 X 8 - Ali Express
- Speaker 8 ohm - eBay
- Audio Jack Input - Switched - eBay
- Echo/Reverb Module
- Module - eBay
- Potentiometer 50K X 2 - Ali Express


- [dub Siren - V2 - Parts List](pdfs/dub Siren - V2 - Parts List.pdf)

## Step 2: The Dub Siren PCB

![Step 2: The Dub Siren PCB image 1](images/step02_01.jpg)

![Step 2: The Dub Siren PCB image 2](images/step02_02.jpg)

![Step 2: The Dub Siren PCB image 3](images/step02_03.jpg)

I have provided the gerber & Eagle files in a Google Drive link which can be found here. You'll need to get the PCB printed and you can do this by sending the zipped gerber files to a PCB manufacturer like JLCPCB (not affiliated). It's a very simple process, just save the file on your computer and follow the instructions on the website.

Here is a 'ible I did on what Gerber files are and how to use them to get your PCB printed.

If you know how to use Eagle (like most things, it's easy once you have done it a few times), I have provided the files in the Google Drive link. If you are interested in learning, I recommend sparkfuns tutorials:

Installing Eagle

Creating Schematics

Creating PCB's

Note that the amp (386IC) isn't connrcted to the main schematic. The reson being, the amp needs to drive the echo/reverb board so this is routed through the 'echo-in' 'echo-out' connections on the schematic.


- [Dub Siren V3.1](pdfs/Dub Siren V3.1.pdf)

## Step 3: The Other Parts You'll Need

![Step 3: The Other Parts You'll Need image 1](images/step03_01.jpg)

![Step 3: The Other Parts You'll Need image 2](images/step03_02.jpg)

![Step 3: The Other Parts You'll Need image 3](images/step03_03.jpg)

![Step 3: The Other Parts You'll Need image 4](images/step03_04.jpg)

![Step 3: The Other Parts You'll Need image 5](images/step03_05.jpg)

![Step 3: The Other Parts You'll Need image 6](images/step03_06.jpg)

![Step 3: The Other Parts You'll Need image 7](images/step03_07.jpg)

![Step 3: The Other Parts You'll Need image 8](images/step03_08.jpg)

![Step 3: The Other Parts You'll Need image 9](images/step03_09.jpg)

Parts For The Circuit:

1. Knobs X 7 - eBay

2. Speaker mesh - Ali ExpressAli Express

Parts for Powering:

1. Lo-po or mobile phone battery - eBay. I get all my mobile phone batteries for free! If you have an e-waste centre near you - go and check it out as it's a great source for them. You could also just use a 9v battery and you won't need the rest of the below. I like to have the ability to re-charge my builds so I don't have to worry bout flat batteries

2. Voltage boost Converter - Ali Express

3. Micro USB adapter - eBay

Parts For the Front Panel

1. Opal Acrylic - eBay

2. A4 Transparent Clear Self Adhesive Sticker Paper - eBay

3. Hard wood Edging - Hardware store


## Step 4: Putting the Dub Siren Circuit Together

![Step 4: Putting the Dub Siren Circuit Together image 1](images/step04_01.jpg)

![Step 4: Putting the Dub Siren Circuit Together image 2](images/step04_02.jpg)

![Step 4: Putting the Dub Siren Circuit Together image 3](images/step04_03.jpg)

![Step 4: Putting the Dub Siren Circuit Together image 4](images/step04_04.jpg)

![Step 4: Putting the Dub Siren Circuit Together image 5](images/step04_05.jpg)

I've designed the circuit as simple as possible so you really only need some basic soldering skills to put this circuit together.

STEPS:

1. Always start with the components with the lowest profile - in this case it's the resistors. I like to add all of them into place on the circuit board and solder in one go.

2. Next I soldered the IC sockets into place along with the JST connectors

3. Then it's time to move onto the capacitors and other ad-hoc components like the transistor

4. Once all the parts are soldered into place, add the IC's

5. Now you won't be able to test yet until the Echo/Reverb module is added. The amp on the board isn't directly connected to the dub siren circuit as it needs to be connected to the 'out' on the echo/reverb board. There is a couple of mods you need to do to the echo/reverb board first before you can use it


## Step 5: Modding the Echo/Reverb Board

![Step 5: Modding the Echo/Reverb Board image 1](images/step05_01.jpg)

![Step 5: Modding the Echo/Reverb Board image 2](images/step05_02.jpg)

![Step 5: Modding the Echo/Reverb Board image 3](images/step05_03.jpg)

i've actually done an in depth 'ible on how to do the mod on the reverb board which can be found here. However, I'll go through the steps you need to do below as well.

STEPS:

1. First, you need to remove a resistor on the echo/reverb board. The resister is numbered R27. You can use a small exacto knife to lift it off easily. This allows you to use the Echo function on the board.

2. You'll then need to remove the potentiometer on the board which is for reverb. The reason why is, you won't be able to fit the board into the case as is. I found that the pads on the board aren't the best and de-soldering can lead to the pads coming off. I find that using a pair of wire cutters and just cutting the pot off works best and you won't run the risk of lifting a pad off.

3. Now solder 3 wires to the solder pads where the pot was. There are also pot connections for the echo so solder 3 wires to these as well.

4. Lastly, solder a 50K pot to the ends of each of the 3 wires. One will be for reverb and the other for echo

5. Now you can connect up the board to the dub siren board and test to make sure everything works. Just connect the echo module via the echo in/echo out on the dub siren circuit.


## Step 6: Adding the Front Cover Design to the Acrylic

![Step 6: Adding the Front Cover Design to the Acrylic image 1](images/step06_01.jpg)

![Step 6: Adding the Front Cover Design to the Acrylic image 2](images/step06_02.jpg)

![Step 6: Adding the Front Cover Design to the Acrylic image 3](images/step06_03.jpg)

![Step 6: Adding the Front Cover Design to the Acrylic image 4](images/step06_04.jpg)

![Step 6: Adding the Front Cover Design to the Acrylic image 5](images/step06_05.jpg)

Usually I would use a water decal, print the panel on that and add it to the acrylic. However, I kept on having issues getting it to stick to the acrylic. Instead, I used a transparent label, printed the design directly onto that and just stuck it on the acrylic - easy!

STEPS:

1. The first thing to do is to grab the PDF provided. I have included 2 different types, one with the speaker and one without in case you want to use a different style of speaker. They are also available in my Google Drive. Print the panel design onto some A4 transparent, adhesive. You can this this from eBay and there is a link in step 3

2. Once you have it printed, cut out the front panel, remove the backing paper and carefully place on a piece of acrylic.

3. To ensure the ink won't come off, add a few layers of acrylic spray paint

4. Once the acrylic is dry, you can then start to cut out the holes needed to add the components. I used a step drill piece to do most of the drilling with. I found that the adhesive didn't rip or pull up when I drilled either which was good news!

5. To make the speaker cut-out, I first drilled a couple holes at the top and bottom and then used a dremel with a cutting wheel to cut the straight sections. I used some sandpaper to finish off the edges


- [Dub Siren v3 - No Speaker](pdfs/Dub Siren v3 - No Speaker.pdf)
- [Dub Siren v3](pdfs/Dub Siren v3.pdf)

## Step 7: Making a Groove in the Wood to Fit the Panel

![Step 7: Making a Groove in the Wood to Fit the Panel image 1](images/step07_01.jpg)

![Step 7: Making a Groove in the Wood to Fit the Panel image 2](images/step07_02.jpg)

![Step 7: Making a Groove in the Wood to Fit the Panel image 3](images/step07_03.jpg)

![Step 7: Making a Groove in the Wood to Fit the Panel image 4](images/step07_04.jpg)

![Step 7: Making a Groove in the Wood to Fit the Panel image 5](images/step07_05.jpg)

![Step 7: Making a Groove in the Wood to Fit the Panel image 6](images/step07_06.jpg)

This does require either a router or a dremel with a special attachment. If you don't have any of these then you can just attached the panel directly on top of the wood! The finish won't be the same but it'll be close.

STEPS:

1. The first thing you need to do is to cut a groove along the wood in order to secure the panel into. I use a dremel with a router attachment to do this.

2. Secure the wood with some clamps and run the bit near the top of the wood. Take your time and make sure you keep the dremel nice and straight.

3. Measure and cut the wood to size. The best way to do this is to just slip in the front panel into the groove of the wood and measure where to make the cuts

5. Place the front panel into the grooves of the wood and use some PVC to glue it together. If you find the panel is a little big and the wood doesn't right then just remove a little of the acrylic along the edge with a sander.

6. Clamp and leave to dry for 12 hours.


## Step 8: Sanding and Painting the Case

![Step 8: Sanding and Painting the Case image 1](images/step08_01.jpg)

![Step 8: Sanding and Painting the Case image 2](images/step08_02.jpg)

![Step 8: Sanding and Painting the Case image 3](images/step08_03.jpg)

![Step 8: Sanding and Painting the Case image 4](images/step08_04.jpg)

![Step 8: Sanding and Painting the Case image 5](images/step08_05.jpg)

![Step 8: Sanding and Painting the Case image 6](images/step08_06.jpg)

STEPS:

1. Once the glue is dried you can then start to clean-up the edges of the case. I use a belt sander to do this which is the quick way. You could also just do it by hand as well.

2. Next, you should add the back to the case. I use some thin ply wood, cut it to size and then secure it with some small screws to the case.

3. Sand it again to make sure that the back is flush with the case

4. Remove the back and paint or stain the case. I love to use 'aged teak' stain on my cases as it gives then a great vintage finish.


## Step 9: Adding the Components to the Case

![Step 9: Adding the Components to the Case image 1](images/step09_01.jpg)

![Step 9: Adding the Components to the Case image 2](images/step09_02.jpg)

![Step 9: Adding the Components to the Case image 3](images/step09_03.jpg)

Now that you have the front panel secured into the case, it's time to add the components.

STEPS:

1. Secure the potentiometers to the front panel. Be careful when tightening the nuts as you don't want to damage the front panel graphics.

2. Secure all of the switches including the momentary switch.

3. Lastly, add the speaker to the front panel. This is secured in place with 4 small screws and nuts


## Step 10: Wiring Everything Up!

![Step 10: Wiring Everything Up! image 1](images/step10_01.jpg)

![Step 10: Wiring Everything Up! image 2](images/step10_02.jpg)

![Step 10: Wiring Everything Up! image 3](images/step10_03.jpg)

![Step 10: Wiring Everything Up! image 4](images/step10_04.jpg)

![Step 10: Wiring Everything Up! image 5](images/step10_05.jpg)

![Step 10: Wiring Everything Up! image 6](images/step10_06.jpg)

![Step 10: Wiring Everything Up! image 7](images/step10_07.jpg)

This is a pretty simple process and I have eliminated much of the soldering by including the pots onto the PCB. You will need to add wires to the echo and reverb pots and circuit board and also a couple for the switching input audio socket.

NOTE - 'echo in' and 'echo-out' on the PCB should be swapped around when connected to the echo/reverb board. In the diagram there are connected incorrectly

STEPS:

1. The attached image shows how everything is connected together. It's all pretty straight forward

2. First, I wired-up the echo/reverb board to the potentiometers.

3. Next connect the JST connectors into the dub siren PCB and then solder them to each of the corresponding components.

4. The switching audio socket needs to be connected to the PCB and the speaker. If you are using a 2 channel one like I did you first must connect both left and right together on the audio socket. Check out the 2nd image which shows how to sire on of these types of audio sockets up. Just think of it like a switch (which it is) and it's turned off when the jack is inserted into the socket, which cuts the connection to the in-built speaker.


## Step 11: Adding a Charging Module

![Step 11: Adding a Charging Module image 1](images/step11_01.jpg)

![Step 11: Adding a Charging Module image 2](images/step11_02.jpg)

![Step 11: Adding a Charging Module image 3](images/step11_03.jpg)

![Step 11: Adding a Charging Module image 4](images/step11_04.jpg)

To be able to charge to mobile battery, I added a small micro USB charging module.

STEPS:

1. To be able to access the micro USB, You need to make a small cut out into the case. I made mine in the back of the case using a file

2. Use some superglue to secure the module into place

3. We'll wire it up in the next step


## Step 12: Adding the Battery

![Step 12: Adding the Battery image 1](images/step12_01.jpg)

![Step 12: Adding the Battery image 2](images/step12_02.jpg)

![Step 12: Adding the Battery image 3](images/step12_03.jpg)

![Step 12: Adding the Battery image 4](images/step12_04.jpg)

I think I might have a small obsession collecting old mobile batteries. I use them in all my projects and find that they are very cheap (free) way of powering projects like this. Plus it means I don't have to stock up on 9v batteries

STEPS:

1. To bring the power up from 3.6V to 9V, you need to connect the battery to a boost converter. I found these tiny ones on Ali Express and they work well. Check out the parts list where I have linked them.

2. Glue the boost converter to the battery and connect it to positive and ground on the battery

3. The output on the module needs to be connected to power on the dub siren PCB. Solder on a JST connector to the module and connect it to the PCB

4. Lastly, connect the battery solder points on the charging module to the battery input on the buck converter. Test to make sure the battery charges when connected to mains power. A little light on the module will turn on if working properly


## Step 13: Screwing on the Back and Adding Some Rubber Feet

![Step 13: Screwing on the Back and Adding Some Rubber Feet image 1](images/step13_01.jpg)

![Step 13: Screwing on the Back and Adding Some Rubber Feet image 2](images/step13_02.jpg)

![Step 13: Screwing on the Back and Adding Some Rubber Feet image 3](images/step13_03.jpg)

![Step 13: Screwing on the Back and Adding Some Rubber Feet image 4](images/step13_04.jpg)

Close now.

STEPS:

1. screw on the back of the case

2. Add a small rubber foot in each corner of the base. This will ensure the dub siren doesn't slide around when you are playing it

3. I also added some speaker mesh to the front as well to give it a cleaner finish. I did this after I made the YouTube clip so it is missing there

4. Get some dub reggae on and start playing!


## Downloads

- [dub Siren - V2 - Parts List](pdfs/dub Siren - V2 - Parts List.pdf)
- [Dub Siren V3.1](pdfs/Dub Siren V3.1.pdf)
- [Dub Siren v3 - No Speaker](pdfs/Dub Siren v3 - No Speaker.pdf)
- [Dub Siren v3](pdfs/Dub Siren v3.pdf)

---
*67 images archived*
