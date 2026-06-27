# Conways Game of Life - Running on an ATtiny13!

Source: https://www.instructables.com/Conways-Game-of-Life-Running-on-an-ATtiny13/

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

I've created a parts list which can be found in my GitHub page and in the PDF file attached to this step. The PDF includes links and images of each of the parts which will make it easy to order the correct ones for this build.The parts list attached doesn't included the PCB or front panel. You'll need to jump to the next step which goes through how to get yours printed.PARTS:Charging Module X 1 - Ali ExpressUSB C connector X 1 - Ali Express18560 Battery X 1 - Ali Express (or you can scavenge them from old computers)18650 battery holders X 1(PCB through hole) - Ali ExpressJST 2.0 Micro connectors - Ali Express Qty will depend on whether you are planning to locate the switches on the case.On/off switch X 1 - Ali ExpressMomentary Switch X 1 - Ali Express8 pin IC socket X 1 (for the ATiiny) - Ali ExpressATtiny 13A X 1 - Ali Express8 X * LED Matrix X 4 - Ali Express. I went with red but you can also get them in green or blue.Male header pins (single row) - Ali ExpressParts for the Case and Front Panel2mm Opal acrylic (A4 size) - eBay or craft stores. This is used as a diffuser for the LED's. It isn't essential but I really like the effect it adds.Timber molding to make the case - I get mine from the local hardware storeM2 hex bolts and nuts. Buy an assorted pack - Ali ExpressM2 Screws - Ali ExpressM2 Spacers (assorted) - Ali Express


## Step 1: Getting the PCB & Front Panel Printed

![Step 1: Getting the PCB & Front Panel Printed image 1](images/step03_01.png)

![Step 1: Getting the PCB & Front Panel Printed image 2](images/step03_02.png)

![Step 1: Getting the PCB & Front Panel Printed image 3](images/step03_03.png)

![Step 1: Getting the PCB & Front Panel Printed image 4](images/step03_04.jpg)

![Step 1: Getting the PCB & Front Panel Printed image 5](images/step03_05.jpg)

We all have different levels of knowledge, so when it comes to a build like this I want to make sure that I'm providing enough information so anyone with some basic soldering skills can make it. That includes ensuring there are instructions on how to get your own PCB's printed (which is super easy!)So with that said, the first thing you will need to do is to get the front panel and PCB printed. I use JLCPCB (not affiliated) to get this done. The front panel is actually just a PCB without any components included! The front design is done in a program called Inkscape (available free) and the panel including the drilled holes is done in Fusion 360 (also free!)The files that you need to build your own Bleep Drum Synth can be found in my GitHub page. This includes the parts list, Gerber files for the PCB & front panel, schematic, Arduino script etc.  Download the files to your computerSTEPS:Send the Gerber files to a PCB manufacturer like JLCPCB who will print the PCB and front panel for you. Download all of the files from my GitHub page to your computer and send the zipped Gerber files off to the PCB manufacturer of choice.If you have no idea what any of the above means , then check out the Instructable I made on how to get your broads printed which can be found here.NOTE: The manufacture will include an order number on both the PCB and front panel. It doesn't really matter where it is on the PCB but you don't want it on the front on the front panel!Over at JLCPCB you can 'specify a location' once the Gerber files have been loaded so click this for the front panel and specify in the comment section that you want the order number on the back of the panel. The manufacturer will add it to the back where indicated.


## Step 2: Adding Components to the PCB Part 1

![Step 2: Adding Components to the PCB Part 1 image 1](images/step04_01.jpg)

![Step 2: Adding Components to the PCB Part 1 image 2](images/step04_02.jpg)

![Step 2: Adding Components to the PCB Part 1 image 3](images/step04_03.jpg)

![Step 2: Adding Components to the PCB Part 1 image 4](images/step04_04.jpg)

![Step 2: Adding Components to the PCB Part 1 image 5](images/step04_05.jpg)

![Step 2: Adding Components to the PCB Part 1 image 6](images/step04_06.jpg)

![Step 2: Adding Components to the PCB Part 1 image 7](images/step04_07.jpg)

![Step 2: Adding Components to the PCB Part 1 image 8](images/step04_08.jpg)

The PCB is double sided so it's important that you add the components in the right order or you might find that you can't add some components. In version 1 of this PCB I had it powered by a 9V battery that was directly soldered to the PCB. It was only when I started to add components that I realized there was no way to solder the battery holder into place and also solder the 8X8 LED matrix's as well! Lucky for you I fixed the issue! Now it run's off a 18650 li-lo battery and there is less components to solder!STEPS:You need to start adding components to the reverse side of the PCB so let's start there. First, add a header pin to each of the holes in the PCB.  You could also just use resistor legs if you wanted to.  Now place the charging module into place (making sure that the micro USB is facing outwards, and solder into placeNow solder the IC socket into placeNext add the JST connectors. I've included extra connectors for the switches in case you want to mount them into the top of the case. If you are adding the switches to the PCB, then just connect a JST connector to power and the charging connector.Now you can add the switches.Lastly, solder the battery holders into place.


## Step 3: Adding Components to the PCB Part 2

![Step 3: Adding Components to the PCB Part 2 image 1](images/step05_01.jpg)

![Step 3: Adding Components to the PCB Part 2 image 2](images/step05_02.jpg)

![Step 3: Adding Components to the PCB Part 2 image 3](images/step05_03.jpg)

![Step 3: Adding Components to the PCB Part 2 image 4](images/step05_04.jpg)

![Step 3: Adding Components to the PCB Part 2 image 5](images/step05_05.jpg)

![Step 3: Adding Components to the PCB Part 2 image 6](images/step05_06.jpg)

Now you can flip the PCB over and add the 8X8 matrix'sSTEPSYou will need to add male header pins to each of the IN and OUT on the matrix. Remove the LED section from the board and trim the header so there is 5 pins.I find that the easiest way to ensure that the pins are straight in the PCB is to add a little solder to the soldering iron and dab it onto one of the pins. Check that the pins are sitting straight in the PCB and if so, solder the rest into place. Do this for all 4 matrix's.Place the first LED matrix into the top left section of the PCB. IMPORTANT! Make sure you align the 'IN' and 'OUT' pins on the matrix correctly to the PCB. The IN pins on the matrix need to go in the top section of the PCB.Solder the rest of the matrix's onto place.Now you can test the board by adding the battery and turning it on. If everything has been soldered right, a little glider will make it's way across the screen and then explode!If this doesn't happen, check all of the solder joints, especially on the matrix's it doesn't take much to connect a couple of the legs together which will cause you issues.


## Step 4: Adding the Front Panel

![Step 4: Adding the Front Panel image 1](images/step06_01.jpg)

![Step 4: Adding the Front Panel image 2](images/step06_02.jpg)

![Step 4: Adding the Front Panel image 3](images/step06_03.jpg)

![Step 4: Adding the Front Panel image 4](images/step06_04.jpg)

![Step 4: Adding the Front Panel image 5](images/step06_05.jpg)

![Step 4: Adding the Front Panel image 6](images/step06_06.jpg)

![Step 4: Adding the Front Panel image 7](images/step06_07.jpg)

After much toing & throwing I decided to add an acrylic diffuser to the front of the LED Matrix's. The LED's are a little raw without the diffusion. However, the movement of the LED's with the diffusion enhances the illusion that they are alive, moving across the screen with purpose.STEPS:Place the front panel on top of the acrylic.Mark out the area to cut and drill on the acrylic. I'm lucky enough to have a band saw which makes cutting the acrylic simple. If you don't have a band saw, the you could use a fine tooth say to cut through it.To secure the acrylic to the PCB, I used some M2 screws, nuts and spacers (see parts list)I can't recall the length of the screw I used to connect everything together. So, place one into the front panel, then into the acrylic and then the PCB.Place the acrylic against the front panel. Place a screw though the PCB and then the acrylic and add a nut. Do this each of the 4 holes. This will secure the acrylic to the front panel.


## Step 5: Make a Case

![Step 5: Make a Case image 1](images/step07_01.jpg)

![Step 5: Make a Case image 2](images/step07_02.jpg)

![Step 5: Make a Case image 3](images/step07_03.jpg)

![Step 5: Make a Case image 4](images/step07_04.jpg)

The case is made from pieces of wood trim that you can buy from any hardware store. The wood is 8mm wide by 30mm high.  The PCB has been designed to the wood fits perfectly.  You could also use a less width wood as well but no more than 8 mm wide.STEPS:Measure and cut the wood for the sides, top and bottom.  I just used the front panel as a template to make my measurements.Use a nail gun to secure the wood together.  If you don't have one, you can always just glue them togetherPlace the game of life into the wood frame and mark out where to drill the holes to secure the front panelSecure the front panel into place using M2 screws.  You can always use a sander to clean up the sides and edges if it isn't a perfect fit.Add some wax or stain or whatever you have to the wood to give it a nice finish


## Step 6: Adding the USB C Charger Port

![Step 6: Adding the USB C Charger Port image 1](images/step08_01.jpg)

![Step 6: Adding the USB C Charger Port image 2](images/step08_02.jpg)

![Step 6: Adding the USB C Charger Port image 3](images/step08_03.jpg)

![Step 6: Adding the USB C Charger Port image 4](images/step08_04.jpg)

![Step 6: Adding the USB C Charger Port image 5](images/step08_05.jpg)

![Step 6: Adding the USB C Charger Port image 6](images/step08_06.jpg)

You could always just charge the battery up with a 18560 battery charger if you wanted to.  However, It's easy to add the little USC charging port and connect that up to the charging module via a JST connector.STEPS:Mark out where you want to add the USB C port.Drill a few holes and then use a file to clean up the edges etc.Connect a JST wire connector to the JST connector and push the wires out through the slot you made for the USC C port.Trim the wires and solder them to the solder point on the portAdd a couple of M2 screws to secure it into place.  Now you can charge the battery via the port!


---
*48 images archived*
