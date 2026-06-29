# Box of Beezz - Drone Synth

Source: https://www.instructables.com/Box-of-Beezz-Drone-Synth/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

![Intro 6](images/intro_06.jpg)

This is my 'Box of Beezz' drone synth using transistors as simple oscillators!

This build uses what is known as a relaxation oscillator. A relaxation oscillator is an oscillator that repeats itself over and over again from the charging of a capacitor to some event threshold and then the discharging of the capacitor. So basically the repetitive charging up of the capacitor and discharging of the capacitor creates oscillations via a transistor.

There are 9 in total built into the circuit and by using different capacitor values you can get different oscillations. The recharge and discharge time of the capacitor determines the time period and frequency of the oscillations

The LED connected to each oscillator acts as an output and these flicker on and off depending on the output signal. Plus, every project needs LED's!

Sawtooth oscillations are produced and they actually sound great. When you add 9 of them in total then you really get some interesting sounds generated.

There is also a master tone knob and I've included a control voltage output so you can hock the drone synth up to a sequencer.

The project was inspired by 'Look Mum No Computers' super simple oscillator build which I have linked below

Super Simple Oscillator

Oh and hackaday did a review of this project which you can find here


## Supplies

![Supplies image 1](images/step01_01.jpg)

![Supplies image 2](images/step01_02.jpg)

![Supplies image 3](images/step01_03.jpg)

![Supplies image 4](images/step01_04.jpg)

![Supplies image 5](images/step01_05.jpg)

![Supplies image 6](images/step01_06.jpg)

![Supplies image 7](images/step01_07.jpg)

![Supplies image 8](images/step01_08.jpg)

![Supplies image 9](images/step01_09.jpg)

Components for the circuit board

- PCB - See the next step on how to get your PCB printed
- Tactile 7x7mm switches - Ali Express
- Tactile push button caps - Ali Express
- JST Connector mini
- 2 pins X 6 Ali Express
- 3 pins X 1 Ali Express
- Capacitor Polarized Ali Express
- 2.2uf X 3
- 4.7uf X 3
- 10uf X 4
- Capacitor Poly 100nf X 3 Ali Express
- LED 3mm white X 9 Ali Express
- Resistors - Buy them in assorted lots - Ali Express
- 47K X 18
- 3.3K X 10
- 1K X1
- Transistors 2N4401 X 9 Ali Express
- Potentiometers 9mm Vertical Ali Express
- 10K X 10
- 100K X 3
Other components

- Speaker - eBay
- Speaker Mesh - Ali Express
- Amplifier Module - Ali Express
- Pot knobs - Ali Express
- USB C Charging module - eBay
- Battery - I used an old mobile battery to power everything which worked fine. You can usually find them for free or you can can buy one - eBay
- Voltage step up module - Ali Express
- 3.5mm Headphones Jack Socket X 3 - Ali Express
- SPDT Toggle Switch X 2 - eBay
- Vactrol - 5mm white LED & LDR See this Instructable on how to make one
Case & Front Panel

- Clear, adhesive paper - eBay
- Opal Acrylic - eBay
- Hard wood for the case - I use edging 40mm X 8mm X 1M


## Step 1: The Schematic, PCB & Getting Your PCB Printed

![Step 1: The Schematic, PCB & Getting Your PCB Printed image 1](images/step02_01.png)

![Step 1: The Schematic, PCB & Getting Your PCB Printed image 2](images/step02_02.png)

If you want a deeper insight on how this circuit works, then check out this link

The board is actually 2 sided. On one side are all of the components like capacitor, resistors, transistors etc. On the other side are the potentiometers and switches.

Due to the size limitations on circuit design in Eagle (100mm X 100mm) I had to jam a lot onto a small sized board. However, you can make the board bigger to add screw mounting holes so the actual size is ...

The oscillators are lined-up in 3 rows of 3 for a total of 9. I've also added tone pots for each row and there is also a master tone pot. There is a on/off switch for each row so you can turn each one off when tuning.

If you would like to play around with the schematic and board in Eagle, well I have also provided these in my GitHub Page You can also find a PDF of the schematic in this step.

There are actually 2 versions available of the PCB. Both are available in my Google Drive

Version 1

This is the one I used ion this build. It has a tone pot for each line of drones (3) plus a master one. I don't use the tone pots very often so decided to do a version 2

Version 2

This has the tone pots removed (only has the master one) and an extra drone circuit for a total of 12 drones!

Getting Your Board Printed

To have the board printed, save the gerber zip file in the GitHub Page files to your computer and email it to your favourite PCB manufacturer. I use JLCPCB (not affiliated) who do a good job of printing the boards and are quick as well. If you are thinking 'what the hell is a gerber file!', then check this 'ible out which is a step by step guide on how to get a PCB manufactured.


## Step 2: Adding the Components to the PCB - Part 1

![Step 2: Adding the Components to the PCB - Part 1 image 1](images/step03_01.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 2](images/step03_02.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 3](images/step03_03.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 4](images/step03_04.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 5](images/step03_05.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 6](images/step03_06.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 7](images/step03_07.jpg)

Adding the components is pretty straight forward. However, you should start with adding the components first. Oh and you need to modify the transistors as well slightly!

STEPS:

- As usual, start with the lowest profile parts - in the case it's the resistors
- Next add the JST connectors
- Before you add the transistors, you need to remove the middle leg of each one. I used some wire cutters to snip these away. Once the legs have been removed you can solder them in place
- Now you can add the capacitors


## Step 3: Adding the Components to the PCB - Part 2

![Step 3: Adding the Components to the PCB - Part 2 image 1](images/step04_01.jpg)

![Step 3: Adding the Components to the PCB - Part 2 image 2](images/step04_02.jpg)

![Step 3: Adding the Components to the PCB - Part 2 image 3](images/step04_03.jpg)

![Step 3: Adding the Components to the PCB - Part 2 image 4](images/step04_04.jpg)

![Step 3: Adding the Components to the PCB - Part 2 image 5](images/step04_05.jpg)

- Flip the board over and add the LED's. I used white and but you could use different colours which might even give you different outputs.
- Add the switches next. Note that the switches have an orientation and how you add them to the PCB will either mean they are normally on or normally off. Just make sure that you orientate them the 3 switches the same way on the board.
- Lastly, add the pots to the PCB.
- You should now go ahead and test the board to make sure everything is working. You'll need to put 18V through it and connect to an amp to hear anything.


## Step 4: The Front Panel

![Step 4: The Front Panel image 1](images/step05_01.jpg)

![Step 4: The Front Panel image 2](images/step05_02.jpg)

![Step 4: The Front Panel image 3](images/step05_03.jpg)

![Step 4: The Front Panel image 4](images/step05_04.jpg)

![Step 4: The Front Panel image 5](images/step05_05.jpg)

![Step 4: The Front Panel image 6](images/step05_06.gif)

![Step 4: The Front Panel image 7](images/step05_07.gif)

I use inkscape to design my front panels. You can find the raw files in my GitHub Page in case you want to play around with it. As I have mentioned, I have made 2 versions of the PCB and have also done a panel design for version 2 which is in my Google drive. I've also come up with a neat way to easily create front panels that match up perfectly to a PCB. Check out the YouTube clip if you are interested in learning how.

STEPS:

- Use the attached PDF copy of the front panel design. Pick whether you want to include the one with the cutout for the speaker or not. You may have a different style of speaker than mine
- The front panel needs to be printed on clear, adhesive paper. You can get this from eBay and have added a link to the parts page.
- Cut out the image and carefully place onto the opal acrylic and remove any air bubbles. I peal away the top section and lay this onto the acrylic. I then use something flat like a ruler and carefully run it down the adhesive paper to ensure no creases or air bubbles are introduced.
- Cut the acrylic to size if you haven't already.
- To ensure the colours on the front panel don't get scratched, spray a few coats of clear acrylic onto the front panel. Make sure you give it a good coating each time and leave for an hour to dry before applying the next one. I used a satin finish clear coat on the final design.


## Step 5: Drilling & Making Cut-outs on the Front Panel

![Step 5: Drilling & Making Cut-outs on the Front Panel image 1](images/step06_01.jpg)

![Step 5: Drilling & Making Cut-outs on the Front Panel image 2](images/step06_02.jpg)

![Step 5: Drilling & Making Cut-outs on the Front Panel image 3](images/step06_03.jpg)

![Step 5: Drilling & Making Cut-outs on the Front Panel image 4](images/step06_04.jpg)

Time to drill out the holes for the pots and switches and also cut out the section for the speaker

STEPS:

- I like to use a stepped drill bit to make the holes in the front panel. Carefully drill out each of the holes for the pots and switches
- To cut out the speaker section, use a hole drill piece and drill out the 2 round sections.
- Attach a small cutting wheel to the dremel and carefully cut away the straight sections
- Tidy up the edges of the speaker hole with a file or a sanding drum attached to the Dremel.
- You'll also need to mark out and drill 4 holes in order to mount the speaker
- Place the PCB into the front panel, mark on the acrylic where to drill the 4 mounting holes to mount the PCB and drill away.
- Don't secure the PCB to the front panel yet - first you need to sort out the case


## Step 6: Making the Case

![Step 6: Making the Case image 1](images/step07_01.jpg)

![Step 6: Making the Case image 2](images/step07_02.jpg)

![Step 6: Making the Case image 3](images/step07_03.jpg)

![Step 6: Making the Case image 4](images/step07_04.jpg)

![Step 6: Making the Case image 5](images/step07_05.jpg)

![Step 6: Making the Case image 6](images/step07_06.jpg)

![Step 6: Making the Case image 7](images/step07_07.jpg)

![Step 6: Making the Case image 8](images/step07_08.jpg)

I have made a simple box shaped case for this build. It's similar to the ones I have previously built but gives a great finish to the project. The case does require either a router or a dremel with a special attachment. If you don't have any of these then you can just attached the panel directly on top of the wood! The finish won't be the same but it'll be close.

STEPS:

- The first thing you need to do is to cut a groove along the wood in order to secure the panel into. I use a dremel with a router attachment to do this.
- Secure the wood with some clamps and run the bit near the top of the wood. Take your time and make sure you keep the dremel nice and straight.
- I also used a larger router bit to remove some of the material on the inside of the case. this will allow me to add the switches, audio sockets so they protrude through the wood and I can secure them easily.
- Measure and cut the wood to size. The best way to do this is to just slip in the front panel into the groove of the wood and measure where to make the cuts
- Place the front panel into the grooves of the wood. You can either use some some PVC or a brader nail gun to secure the case together.
- Lastly, you should make a back for the case before you start to sand. I used some thin ply wood and secure it into place with some small screws. If you add the back now, you can sand it to shape in the next step and it makes things a lot easier.
TIP If you find the panel is a little big and the wood doesn't right then just remove a little of the acrylic along the edge with a sander.

Sanding & Painting

- Time to clean up the edges. I use a belt sander to do this which is the quick way. You could also just do it by hand sanding as well.
- You can also round off the edges of the case with the sander as well which I did.
- Paint or stain the case. I used a clear varnish to give it a clean finish
- Leave it to dry for 12 hours (it's hard I know)


## Step 7: Adding the PCB & Speaker

![Step 7: Adding the PCB & Speaker image 1](images/step08_01.jpg)

![Step 7: Adding the PCB & Speaker image 2](images/step08_02.jpg)

![Step 7: Adding the PCB & Speaker image 3](images/step08_03.jpg)

![Step 7: Adding the PCB & Speaker image 4](images/step08_04.jpg)

![Step 7: Adding the PCB & Speaker image 5](images/step08_05.jpg)

![Step 7: Adding the PCB & Speaker image 6](images/step08_06.jpg)

![Step 7: Adding the PCB & Speaker image 7](images/step08_07.jpg)

Now that you have the front panel secured into the case, it's time to add the PCB

STEPS:

- Place the PCB into the front panel. if you haven't already, mark out the PCB mounting holes on the back of the panel and drill.
- Secure them in place with some small screws and nuts
- For the speaker, also mark and drill out the mounting holes if not already done.
- I also added some speaker grill mesh. Just cut it to shape and drill some holes for mounting to the speaker and case
- Put it all together with 4 screws and nuts


## Step 8: Adding the Components to the Case

![Step 8: Adding the Components to the Case image 1](images/step09_01.jpg)

![Step 8: Adding the Components to the Case image 2](images/step09_02.jpg)

![Step 8: Adding the Components to the Case image 3](images/step09_03.jpg)

![Step 8: Adding the Components to the Case image 4](images/step09_04.jpg)

![Step 8: Adding the Components to the Case image 5](images/step09_05.jpg)

![Step 8: Adding the Components to the Case image 6](images/step09_06.jpg)

![Step 8: Adding the Components to the Case image 7](images/step09_07.jpg)

I have included an amp on this build along with a voltage boosting module, USB C charging module, vactrol (for the control voltage) and a couple other components which will all need to be added to the case.

STEPS:

- Let's start with the charging module. Remove the back from the case
- with a file, make a groove in the bottom section of the case big enough for the module to sit in.
- Super glue the module into place
- Next, place the volume potentiometer into the case and secure into place
- Add the switches, audio sockets and secure into place
- Lastly, add the 10K 'master tone' potentiometer into the front panel and secure.
- The vactrol I used is made from an LED and an LDR. You can easily make your own following this Instructable
- Secure the LDR legs to the 'CV' section on the PCB The LED legs need to be connected to the CV out socket. Make sure that you attached the positive leg of the LED to the L and R terminals on the audio socket and the ground of the LED to the ground on the socket


## Step 9: Wiring Everything Up!

![Step 9: Wiring Everything Up! image 1](images/step10_01.png)

![Step 9: Wiring Everything Up! image 2](images/step10_02.jpg)

![Step 9: Wiring Everything Up! image 3](images/step10_03.jpg)

![Step 9: Wiring Everything Up! image 4](images/step10_04.jpg)

![Step 9: Wiring Everything Up! image 5](images/step10_05.jpg)

![Step 9: Wiring Everything Up! image 6](images/step10_06.jpg)

![Step 9: Wiring Everything Up! image 7](images/step10_07.jpg)

I've included a wiring schematic to help you wire everything up. Note that I have slightly revised the PCB and have included a power JST connector for the amp and also a connection to add the vactrol LDR legs too. My goal when I'm designing something like this is to have the least amount of wires possible. Unfortunately, there is quite a bit of wiring due to the fact that I had to remove the volume pot from the amp and there are wires needed to connect the vactrol and amp up to everything.

STEPS:

- First, connect the out 3.5mm audio socket to the out on the PCB
- You will notice that there is a switch to either have the speaker and amp on or to have it play on an outside amp. Connect the wires next for this switch
- Add the vactrol to the other 3.5mm audio socket. You need to add the LED section of the vactrol to the solder points on the socket. Make sure you have the cathode leg (ground) connected to the ground on the audio socket and the anode (positive) to the left and right solder points on the socket
- the LDR section of the vactrol gets connected the the 'vactrol' connection on the PCB
- Next connect the amp up to the speaker and 'amp' connection point on the PCB along with the 'amp power' connection on the PCB.
- There is a spot to connect an on/off switch on the PCB. However, if you just add a switch to this then it won't turn off the amp. What I did was add a solder blob between the two connections on the PCB and then added a on/off switch from the battery. This way you are turning everything off from the battery.
- To be able to charge the battery you need to add a li-po charging module. I just make a small groove in the case, glue it into place and connect the battery.
- To increase the voltage from 3.7v to 18v, I used a step up module. Connect this to the out on the charging module and then connect it to the power connection on the PCB.
- Once you have wired everything together, add the knobs to the potentiometers.
That's it! Now go and make some noise.


---
*69 images archived*
