# 100 LED Oscilloscope

Source: https://www.instructables.com/100-LED-Oscilloscope/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)


## Supplies

![Supplies image 1](images/step02_01.jpg)

![Supplies image 2](images/step02_02.jpg)

![Supplies image 3](images/step02_03.jpg)

![Supplies image 4](images/step02_04.jpg)

![Supplies image 5](images/step02_05.jpg)

![Supplies image 6](images/step02_06.jpg)

![Supplies image 7](images/step02_07.jpg)

![Supplies image 8](images/step02_08.jpg)

![Supplies image 9](images/step02_09.jpg)

![Supplies image 10](images/step02_10.jpg)

![Supplies image 11](images/step02_11.jpg)

![Supplies image 12](images/step02_12.jpg)

![Supplies image 13](images/step02_13.jpg)

Below are the components need to build this project along with the parts needed to build the caseStep 1 has the information around the PCB.The best way to buy electronics is in bulk and I have added a link to each. I also used 5mm square LED's and they look awesome! You can also use round ones as well but I highly recommend that you just buy the square ones. I got 1000 for $14!Lastly, I have attached a PDF of the parts list and it can also be found on my GitHub PageComponents for the CircuitPotentiometer - 9mm 50K X 1 - Ali ExpressPotentiometer - Vertical - Ali Express500K X 12K X 150K X 15K X 1CapacitorsPolyester - Ali Express10nf X 147nf X 150nf X 1100nf X 2 150nf X 1 Polarized - Ali Express470uf X 2 10uf X 2Resistor Metal Film - Ali Express1K X 3120R X 115K X 110K X 310R X 1100K X 127K X 1IC's555 X 1 - Ali express4017 X 1 - Ali expressLM3914 X 1 - Ali expressLM386 X 1 - Ali expressTransistor - 2N3904 X 1 - Ali ExpressLED 5mm Square X 100 - Ali ExpressMic electret X 1 - Ali ExpressToggle Switch SPDT X 1 - Ali ExpressSwitch 6 Pin - 7mm x 7mm X 3 - Ali Express JST Connectors Micro JST 2.0 PH X 5 - Ali ExpressBNC connector X 1 - Ali ExpressParts for Front Panel and CaseOpal Acrylic A5 - eBayClear, adhesive A4 label - eBayPly woodPowering the PCB.You can use a 9v battery but I like to re-use old mobile batteries.Mobile battery - If you want to find them just visit your local e-waste or check in the top drawer for an old phone! You can always just buy a new one on eBay as well...Power module (this will increase the voltage from 3.7v to 9v - Ali ExpressUSB charging module (so you can charge the battery up) - Ali Express


## Step 1: A Couple of Options in the Design

![Step 1: A Couple of Options in the Design image 1](images/step03_01.jpg)

![Step 1: A Couple of Options in the Design image 2](images/step03_02.jpg)

After putting together the initial PCB, I decided that I wanted a way to fine tune the horizontal.  This creates the waveform structure and having a fine tune allows you to create great looking waveforms.Version 1 (first schematic) has a couple of extra JST connectors, one for a 50K pot and one for a switch to turn off the fine tune.  The reason why I wanted the ability to turn off the fine horizontal is you can get very slow frame rates when it isn't connected and I like the look of them!  When the fine horizontal is on, you can't slow frame rates to happen.  if you didn't want to bother with the switch, you could just connect the 2 solder points on the PCB.  I also wanted to add the fine horizontal pot to the side of the case where it is easy to really fine tune it.  If you don't care about the fine tune then you don't have to connect the pot or switch and it will all still work.Version 2 (second schematic) has the fine horizontal directly connected to the PCB.  However, it doesn't have the ability to turn off the fine horizontal.I have provided 2 PCB's (next step) so you can pick which one you want to get printed.LED Oscilloscope Schematic V1.pdfDownloadLED Oscilloscope Schematic V2.pdfDownload


## Step 2: Printing the PCB

![Step 2: Printing the PCB image 1](images/step04_01.jpg)

![Step 2: Printing the PCB image 2](images/step04_02.jpg)

The board is actually 2 sided. On one side are all of the components like capacitor, resistors, IC's etc. On the other side is the potentiometers and switches.To have the board printed, save the gerber zip file in the GitHub Page files to your computer and email it to your favourite PCB manufacturer. I use JLCPCB (not affiliated) who do a good job of printing the boards and are quick as well. If you are thinking 'what the hell is a gerber file!', then check this 'ible out which is a step by step guide on how to get a PCB manufactured.If you would like to play around with the schematic and board in Eagle, well I have also provided these in my Google Drive. You can also find a PDF of the schematic in the previous stepRemember - there are 2 versions so have a think how you want your board to look.


## Step 3: Adding the LED's to the PCB

![Step 3: Adding the LED's to the PCB image 1](images/step05_01.jpg)

![Step 3: Adding the LED's to the PCB image 2](images/step05_02.jpg)

![Step 3: Adding the LED's to the PCB image 3](images/step05_03.jpg)

![Step 3: Adding the LED's to the PCB image 4](images/step05_04.jpg)

![Step 3: Adding the LED's to the PCB image 5](images/step05_05.jpg)

![Step 3: Adding the LED's to the PCB image 6](images/step05_06.jpg)

![Step 3: Adding the LED's to the PCB image 7](images/step05_07.jpg)

![Step 3: Adding the LED's to the PCB image 8](images/step05_08.jpg)

![Step 3: Adding the LED's to the PCB image 9](images/step05_09.jpg)

![Step 3: Adding the LED's to the PCB image 10](images/step05_10.jpg)

Adding the LED's isn't too hard (just a little time consuming), especially if you use the square ones that I used in the build.  STEPS:To ensure that the LED's are sitting flat when you solder them into place, it's important that you add a couple to the bottom row as well.  So firstly, add 10 LED's to the top row and a couple each side in the bottom row.Next, solder one leg of each LED into place and check that they are straight before you solder the other leg.Keep on adding row after row, checking your work as you go and making sure that the LED's are straight and sitting flat on the PCB.Once you have added all of the LED's - it's time to start adding the components on the reverse side


## Step 4: Adding the Components to the PCB

![Step 4: Adding the Components to the PCB image 1](images/step06_01.jpg)

![Step 4: Adding the Components to the PCB image 2](images/step06_02.jpg)

![Step 4: Adding the Components to the PCB image 3](images/step06_03.jpg)

![Step 4: Adding the Components to the PCB image 4](images/step06_04.jpg)

![Step 4: Adding the Components to the PCB image 5](images/step06_05.jpg)

![Step 4: Adding the Components to the PCB image 6](images/step06_06.jpg)

![Step 4: Adding the Components to the PCB image 7](images/step06_07.jpg)

![Step 4: Adding the Components to the PCB image 8](images/step06_08.jpg)

![Step 4: Adding the Components to the PCB image 9](images/step06_09.jpg)

![Step 4: Adding the Components to the PCB image 10](images/step06_10.jpg)

![Step 4: Adding the Components to the PCB image 11](images/step06_11.jpg)

STEPS:As always, start with the lowest profile parts first - in this case it's the resistorsNext I usually add the IC sockets and then JST connectors Then move onto the capacitors and transistorI had to solder into the the LED driver IC as i didn't have a IC socket big enough for it.  Luckily there wasn't any issues with it.Once all the components have been added, flip the board over and add the pots and switchesFirst, add the switches to the board.  Note that they have an orientation.  If you look at the one that I'm holding, you can see a small indent in the bottom of the switch.  Make sure that the indent is at the top of the switch when you are soldering them into place.  It will mean that you need to push the switch and lock it into place to turn it on.  If you happen to put them in the wrong way - it won't really matter, it will just mean that you have to 'un-latch' the switch to turn it on


## Step 5: Testing the PCB (and a Small Mod I Did!)

![Step 5: Testing the PCB (and a Small Mod I Did!) image 1](images/step07_01.jpg)

![Step 5: Testing the PCB (and a Small Mod I Did!) image 2](images/step07_02.jpg)

![Step 5: Testing the PCB (and a Small Mod I Did!) image 3](images/step07_03.jpg)

![Step 5: Testing the PCB (and a Small Mod I Did!) image 4](images/step07_04.jpg)

![Step 5: Testing the PCB (and a Small Mod I Did!) image 5](images/step07_05.jpg)

![Step 5: Testing the PCB (and a Small Mod I Did!) image 6](images/step07_06.jpg)

![Step 5: Testing the PCB (and a Small Mod I Did!) image 7](images/step07_07.jpg)

Testing the board is relatively easy, all you need to do is to add a mic and a power source and you can test it.  I also decided to do a mod which was adding the 'fine horizontal' pot and switch to turn it off.  You don't have to worry about doing this as I updated the PCB (version 1).  Version 2 has the pot connected directly to the board so less wiring.  However, you can't turn off the 'fine horizontal'STEPS:Connect a mic and power source to the boardYou should see a line of LED's light upPlay around with the knobs (see the last step on how to actually work the thing!) and see if the LED's move aboutPlay some music (making sure that the mic is turned on via the mic/probe switch) and see if you can get some waveforms happening.Remember that the electret mic have a polarity so if you aren't seeing anything, try swapping the wires around connected to the legs and see if that helps.


## Step 6: The Front Panel

![Step 6: The Front Panel image 1](images/step08_01.jpg)

![Step 6: The Front Panel image 2](images/step08_02.jpg)

![Step 6: The Front Panel image 3](images/step08_03.jpg)

![Step 6: The Front Panel image 4](images/step08_04.jpg)

Like my 81 LED Chaser, I decided to keep the front panel pretty simple - there is already enough going on with all those LED's!I use inkscape to design my front panels. You can find the raw files in my Google Drive in case you want to play around with them. NOTE that there are 2 versions that I made of the circuit board.  I only did a panel for version one which has a 'fine horizontal pot' but not on the actuacl PCB.  See step 5 for further detailsSTEPS:Use the attached PDF copy of the front panel design.The front panel needs to be printed on clear, adhesive paper. You can get this from eBay and have added a link to the parts page.Cut out the image and carefully place onto the opal acrylic and remove any air bubbles.Cut the acrylic to size if you haven't alreadyTo ensure the colours on the front panel don't get scratched, spray a few coats of clear acrylic onto the front panel. Make sure you give it a good coating each time and leave for an hour to dry before applying the next one. I used a satin finish clear coat on the final design.LED Oscilloscope V1.pdfDownload


## Step 7: Drilling & Making Cut-outs on the Front Panel

![Step 7: Drilling & Making Cut-outs on the Front Panel image 1](images/step09_01.jpg)

![Step 7: Drilling & Making Cut-outs on the Front Panel image 2](images/step09_02.jpg)

![Step 7: Drilling & Making Cut-outs on the Front Panel image 3](images/step09_03.jpg)

![Step 7: Drilling & Making Cut-outs on the Front Panel image 4](images/step09_04.jpg)

![Step 7: Drilling & Making Cut-outs on the Front Panel image 5](images/step09_05.jpg)

![Step 7: Drilling & Making Cut-outs on the Front Panel image 6](images/step09_06.jpg)

![Step 7: Drilling & Making Cut-outs on the Front Panel image 7](images/step09_07.jpg)

![Step 7: Drilling & Making Cut-outs on the Front Panel image 8](images/step09_08.jpg)

Time to drill out the holes for the pots and switches and also cut out the section for the LED's.STEPS:I like to use a stepped drill bit to make the holes in the front panel. Carefully drill out each of the holes for the pots and switchesNOTE: I highly recommend to use a drmel for the next step. It makes the job relatively easy. You could also use a small saw to remove the sectionAttach a small cutting wheel to the dremel and carefully cut away the square section in the panel for the LED'sTidy up the edges with a file and then see how the LED's fit. Re-work any sections if necessary until the PCB and LED's fits nicely into the front panelNOTE: I was very close to actually not making the cutout for the LED's!  The acrylic i used was 2mm and it diffused them quite nicely.  However, I decided to take the hard road & make the cutout as I liked seeing all those LED'sPlace the PCB into the front panel, mark where to drill the 4 holes to mount it and drill.Secure the PCB to the front panel using some small screws and nuts.  You may need to add some spacers between the front panel and PCB is you find it is bending inwards.


## Step 8: Making the Case

![Step 8: Making the Case image 1](images/step10_01.jpg)

![Step 8: Making the Case image 2](images/step10_02.jpg)

![Step 8: Making the Case image 3](images/step10_03.jpg)

![Step 8: Making the Case image 4](images/step10_04.jpg)

![Step 8: Making the Case image 5](images/step10_05.jpg)

![Step 8: Making the Case image 6](images/step10_06.jpg)

I decided to make the case so the front panel was on a 45 degree angle. It helps give a better viewing angleSTEPS:The first thing you need to do is to cut a groove along the ply wood in order to secure the panel into. I used a dremel with a router attachment to do this.NOTE: If you don't have one then you could always just stick the panel to the top of the case - easy!Secure the wood with some clamps and run the bit near the top of the wood. Take your time and make sure you keep the dremel nice and straight.Measure and cut the wood to size. The best way to do this is to just slip in the front panel into the groove of the wood and measure where to make the cutsTo give the case an angle, I just cut the side pieces of wood close to a triangle shapePlace the front panel into the grooves of the wood and with a small nail gun like a brad nailer, connect the sides to the base. You can also just glue them as well if you want to - I just get impatient waiting for the glue to dry!NOTE: Before you nail everything together - check out Step 5 which shows you how to add the pot. switch etc to the side of the caseThe top section will need to be screwed into place so you can easily get inside the caseTo finish off the wood I added some clear gloss on the body of the frame and base. Leave to dry for a few hours, give it a light sand and add another coatREMEMBER - you can make the shape of your case anyway you want to. This is just how I did it


## Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case

![Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case image 1](images/step11_01.jpg)

![Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case image 2](images/step11_02.jpg)

![Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case image 3](images/step11_03.jpg)

![Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case image 4](images/step11_04.jpg)

![Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case image 5](images/step11_05.jpg)

![Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case image 6](images/step11_06.jpg)

![Step 9: Adding the Switch, Pot, Mic & BNC Connector to the Case image 7](images/step11_07.jpg)

As mentioned earlier, I made a modification to the PCB and added a fine horizontal pot to make it easier to fine tune the waveforms.  There are 2 versions of the PCB's (I used V1), the 2nd version has the 'fine horizonal' attached to the PCB.STEPS:If you are using ply wood to build the case, then you might find that it is too thick to attach the pot, switch etc.  To get past this, I used a small router bit on my dremel and removed some of the wood on the side panels.  If you reduce the thickness to about half then you should be able to attach everything to the side of the case.Connect the switch, 50K pot to one side and the other add the BNC connector.  FYI - The BNC connector is how you connect the oscilloscope probe to the PCB.Lastly, drill a small hole just big enough to fit the mic.  NOTE: These little mic's have a polarity so if you find that it isn't picking up any signal, then try and swap the wires connected to the mic


## Step 10: Adding a Power Source

![Step 10: Adding a Power Source image 1](images/step12_01.jpg)

![Step 10: Adding a Power Source image 2](images/step12_02.jpg)

![Step 10: Adding a Power Source image 3](images/step12_03.jpg)

![Step 10: Adding a Power Source image 4](images/step12_04.jpg)

![Step 10: Adding a Power Source image 5](images/step12_05.jpg)

![Step 10: Adding a Power Source image 6](images/step12_06.jpg)

![Step 10: Adding a Power Source image 7](images/step12_07.jpg)

![Step 10: Adding a Power Source image 8](images/step12_08.jpg)

You could power everything by a 9V battery. I like to use rechargeable batteries for my builds and have decided to use an old mobile battery to power everything.  If you have seen any of my projects over the last couple of years, then you would have seen me do this many times.STEPS:The step up power module (used to change the voltage from 3.7v to 9v) needs to be formatted to output 9v's. To do this you need to connect the top 2 solder pads with some solder. They are tiny so just add a little solder to your soldering iron and dab it on.Add a dab of superglue to the back of the power module and glue it close to the battery terminalsConnect the input of the module to the battery using a couple resister legsTo charge the battery, you'll need to connect a charging module and be able to access it.. The easiest way is to make a small cutout into the side of the case and glue the USB module to it. You can then connect the USB module to the input on the charging module (the same solder points as the power moduleLastly, connect the wires from a mini JST connector to the output on the step up power module.NOTE - Test to make sure that there is 9v's being generated from the step-up module.  Those tiny solder pads can be tricky to connect.


## Step 11: Connecting Everything Together

![Step 11: Connecting Everything Together image 1](images/step13_01.jpg)

![Step 11: Connecting Everything Together image 2](images/step13_02.jpg)

![Step 11: Connecting Everything Together image 3](images/step13_03.jpg)

![Step 11: Connecting Everything Together image 4](images/step13_04.jpg)

![Step 11: Connecting Everything Together image 5](images/step13_05.jpg)

![Step 11: Connecting Everything Together image 6](images/step13_06.jpg)

Now that you have everything added to the case, it's time to connect everything together.  I use mini JST connector to easily connect the wires to the PCB.  See link in suppliesSTEPS:Solder a JST plug onto the BNC plug, mic, power supply and fine horizontal pot and switch (if you are using version 1)connect all of these to the PCBTest to make sure that everything is working.  Unfortunately I can't test the probe yet as I don't have one!  I'm going to try my hand at making one and will do an 'ible if successful.Screw the top section down Add some knob's to the pots.  They are quite close together so I would recommend using small ones.  Or, don't bother at all with adding pots to the PCB!I added the 'fine horizontal' to the side of the case as it makes it very easy to fine tune it.  I also added a larger knob which gives you more control when tuning.


## Step 12: How to Use the LED Oscillator

![Step 12: How to Use the LED Oscillator image 1](images/step14_01.jpg)

![Step 12: How to Use the LED Oscillator image 2](images/step14_02.jpg)

![Step 12: How to Use the LED Oscillator image 3](images/step14_03.jpg)

![Step 12: How to Use the LED Oscillator image 4](images/step14_04.jpg)

![Step 12: How to Use the LED Oscillator image 5](images/step14_05.jpg)

![Step 12: How to Use the LED Oscillator image 6](images/step14_06.jpg)

![Step 12: How to Use the LED Oscillator image 7](images/step14_07.jpg)

![Step 12: How to Use the LED Oscillator image 8](images/step14_08.jpg)

Ok - so now that you have built it - how do you use it!  Actually, it's really quite easy to get great waveforms appearing via an audio source such as music. I find that there are some songs that work better then others. I highly recommend that you try out 'Extra Kings' by the Avalanches - some beautiful waveforms are created when this is played. Actually, a lot of the avalanches songs look pretty good on the oscilloscopeSTEPS:Turn on the oscilloscopeYou can control where the LED's are positioned in the matrix with the vertical control. Use the fine vertical to help you fine tune the LED's so they are only on one lineTurn on some music and see how it all looksIf you are finding that all of the matrix is filling up with blinking LED's, reduce the strengthNext, turn the horizontal pot until you start to see some waveforms. Use the fine horizonal to tune it even furtherI added a switch to turn off the fine tune as I wanted the ability to really slow down the horizontal. Have a play around with this (version 2 doesn't have the switch)Also play around with the speed, see if the waveforms change (for the better) if you speed up or slow down the rate.Lastly - experiment and see what music works best and what types of waveforms are generated.I'll do an update on the probe once I have built one and tested.


---
*97 images archived*
