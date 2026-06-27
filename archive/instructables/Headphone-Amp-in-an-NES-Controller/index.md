# Headphone Amp in an NES Controller!

Source: https://www.instructables.com/Headphone-Amp-in-an-NES-Controller/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)


## Step 1: Parts & Tools

![Step 1: Parts & Tools image 1](images/step02_01.jpg)

![Step 1: Parts & Tools image 2](images/step02_02.jpg)

![Step 1: Parts & Tools image 3](images/step02_03.jpg)

![Step 1: Parts & Tools image 4](images/step02_04.jpg)

Parts:1.    NES Controller – You can buy copies for cheap on eBay2.    10K duel gang Potentiometer – eBay3.    Potentiometer knob - eBay4.    2 X 18K Resistor – eBay5.    4 X 68K resistor – eBay6.    47K resistor - eBay7.     3mm LED – eBay8.     NE5532 IC – eBay (10 IC's for just over a dollar!)9.     8 pin socket holder - eBay10.   SPDT switch - eBay11.   3 X 4.7uf capacitor – eBay12.   2 X 22pf ceramic capacitor – eBay13.   3 X 220uf capacitor – eBay14.    2 X 3.5mm stereo jack socket – eBay15.    Prototype board – eBay16.    3.7 li-po battery – eBay or get one from an old phone17.   3.7v charger and voltage regulator module - eBay18. Micro USB adapter - eBay19.   Wires.  I used thin computer ribbon cable which you can pick-up for free at your local e-waste or buy it on eBayTools1.      Soldering Iron2.       Drill.  It’s also good to have a stepped drill piece to make the holes (only just got myself a set recently and I love them)3.       Wire cutters4.       Dremel (not necessary but always handy5.       Exacto knife6.       Usual screwdrivers, phillips heads etc7.       Epoxy Glue


## Step 2: About the Amp Circuit I Choose to Build

![Step 2: About the Amp Circuit I Choose to Build image 1](images/step03_01.jpg)

![Step 2: About the Amp Circuit I Choose to Build image 2](images/step03_02.jpg)

The amp is built using op amp 5532. The op amp is a low-distortion, low-noise device, which can drive low-impedance loads to a full voltage swing while maintaining low distortion. Furthermore, it is fully output short-circuit proof. I’ve included the datasheet on the op amp in case anyone is interested.The other positives about this op amp is it’s cheap, you only need 1 for the circuit and you don’t have to worry about virtual grounds or trying to separate the input and output grounds. Also, when you first look at the schematic it might seem that there are 2 op amp IC’s. There is actually only one and is done this way so it is easier to design. The end result is a high quality, high performance portable device that is relatively easy to build and will change the way you listen to music from your phone.Make sure you also breadboard the circuit first.  Nothing worse than thinking “you got this”, soldering everything into place then realising you have messed it up!ne5532.pdfDownloadschematic.fzzDownload


## Step 3: Pulling Apart the NES Controller

![Step 3: Pulling Apart the NES Controller image 1](images/step04_01.jpg)

![Step 3: Pulling Apart the NES Controller image 2](images/step04_02.jpg)

![Step 3: Pulling Apart the NES Controller image 3](images/step04_03.jpg)

![Step 3: Pulling Apart the NES Controller image 4](images/step04_04.jpg)

![Step 3: Pulling Apart the NES Controller image 5](images/step04_05.jpg)

![Step 3: Pulling Apart the NES Controller image 6](images/step04_06.jpg)

![Step 3: Pulling Apart the NES Controller image 7](images/step04_07.jpg)

The first step is to pull apart the NES controller.  Steps:1.       Remove the 6 screws on the back of the controller and keep in a safe place2.       Remove the circuit board and cord.   The cord is wound around a couple of pieces of plastic inside the controller so you need to un-wind this3.       Remove the circuit board and all of the buttons.  Keep the buttons with the screws – somewhere safe4.       My controller was pretty dirty so I gave it a good wash in soapy water


## Step 4: Removing the Excess Plastic Inside the Controller

![Step 4: Removing the Excess Plastic Inside the Controller image 1](images/step05_01.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 2](images/step05_02.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 3](images/step05_03.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 4](images/step05_04.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 5](images/step05_05.jpg)

Inside the controller, there are plastic gussets, brackets and other little pieces that you will need to remove.  You have to make as much room as possible inside the controller to enable to fit the electronics inside.  Make sure though that you don’t remove any of the screw mounts or you want be able to close the case!Steps:1.       First, use a pair of flat wire cutters and trim away all of the raised plastic that you see inside the case.2.       You will need to remove the plastic that surrounds the buttons as well.3.       Remove any gussets around the insides of the case4.       You will also need to remove the little bit of excess plastic that supported the cable hole.  I just ran an exacto knife across it and carefully removed the excess plastic5.       The only things that should be standing inside the controller are the screw mounts.6.       Clean-up the plastic sections removed so there isn’t any little bits sticking up – you want the inside of the case as flat as possible


## Step 5: Enlarging the Cord Hole to Fit the Pot Inside

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 1](images/step06_01.jpg)

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 2](images/step06_02.jpg)

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 3](images/step06_03.jpg)

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 4](images/step06_04.jpg)

Steps:1.       The hole that the cord came out of needs to be enlarged.  The best way to do this is to put the controller case back together first.2.       Enlarge the hole with a drill bit3.       Un-do the controller again and place the pot in the section to make sure it fits ok.4.       At this stage I also placed the main components inside the case so I could get a feel on how everything will be laid out inside the case.


## Step 6: Adding the Audio Jack Inputs to the NES Controller

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 1](images/step07_01.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 2](images/step07_02.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 3](images/step07_03.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 4](images/step07_04.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 5](images/step07_05.jpg)

I did think about adding the jack inputs to where the 2 red buttons on the NES controller are.  I realised pretty quickly though that this would be awkward place to locate them as the jacks would be sticking out sideways which would be pretty uncomfortable le in your pocket.Steps:1.       First, bend the legs on the jack inputs as shown in the images.  This will give you a little more room inside the case2.       Next, you need to drill a couple of holes to fit the input jacks.  When drilling the holes into the side of the case make sure of the following:a.       The holes will need to be drilled so the jack inputs can sit flat on the bottom of the case.  To do this the drilled holes will need to be located as high as possible in the bottom case.b.       Make sure that you take into consideration the screw mounts inside the case.  If you drill the holes in the wrong place the mounts will get in the way3.       Secure each of the jack inputs into place.


## Step 7: Adding a Switch to the NES Controller

![Step 7: Adding a Switch to the NES Controller image 1](images/step08_01.jpg)

![Step 7: Adding a Switch to the NES Controller image 2](images/step08_02.jpg)

![Step 7: Adding a Switch to the NES Controller image 3](images/step08_03.jpg)

The switch I used was one that I had lying around.  I would have pulled it out of some dead electronic gizmo.  I decided to locate the switch in the “start” section on the NES controller, which seemed a fitting placeSteps:1.       To secure the switch in place I used a little bit of epoxy glue.  Switches and glue don’t really mix so don’t use much.2.       Once dry, test the switch to make sure no glue got into the switch3.       The “select” hole will have the original black button replaced a little later on


## Step 8: Adding the Micro USB Adapter to the NES Controller

![Step 8: Adding the Micro USB Adapter to the NES Controller image 1](images/step09_01.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 2](images/step09_02.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 3](images/step09_03.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 4](images/step09_04.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 5](images/step09_05.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 6](images/step09_06.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 7](images/step09_07.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 8](images/step09_08.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 9](images/step09_09.jpg)

The charging module is awesome but the only small downfall is the USB outlet is recessed which makes it hard to use in a project like this.  The solution is to add a mini USB adapter.  There are clear solder points on both the module and the adapter so connecting them is a breezeSteps:1.       As I wanted to keep the battery, module and adapter close together (only short lengths of wire needed), I decided to add the adapter close to the potentiometer.2.       Place the adapter inside the case and mark out where the USB input will exit the case3.       To make the small slot for the USB outlet, first drill a couple small holes as shown in the image.  The drill bit should be aprox ¾ the width of the USB outlet4.       Next, cut away the small piece of plastic between the holes5.       Use a small, flat file to start to shape the slot.  Take your time and slowly enlarge it until the USB outlet just fits6.       Lastly, use a small amount of epoxy on the bottom of the outlet and glue into place.  Make sure you don’t get any glue inside the USB outlet


## Step 9: Attaching the Charging Module to the Battery

![Step 9: Attaching the Charging Module to the Battery image 1](images/step10_01.jpg)

![Step 9: Attaching the Charging Module to the Battery image 2](images/step10_02.jpg)

![Step 9: Attaching the Charging Module to the Battery image 3](images/step10_03.jpg)

![Step 9: Attaching the Charging Module to the Battery image 4](images/step10_04.jpg)

![Step 9: Attaching the Charging Module to the Battery image 5](images/step10_05.jpg)

I forgot to take photos but before you add the battery, you’ll need to glue all of the buttons in place.  I added a little epoxy glue to each and glued them into placeSteps:I recently did an Instructable on how to reuse old mobile batteries which can be found here.  This Instructable will take you through how to wire the module up to the battery1.       Add some superglue to the bottom of the module and stick it onto the battery.  Make sure that the “battery” solder points are facing the battery terminals2.       To connect the module to the battery I used some resistor legs.  Add some solder to each of the battery terminals.  Make sure that you add the solder quickly as you don’t want the battery to overheat.3.       Solder a resistor leg to the positive solder point on the module, bend the leg and then solder it to the battery4.       Do the same for the ground.


## Step 10: Wiring the Switch and the USB Adapter

![Step 10: Wiring the Switch and the USB Adapter image 1](images/step11_01.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 2](images/step11_02.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 3](images/step11_03.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 4](images/step11_04.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 5](images/step11_05.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 6](images/step11_06.jpg)

As mentioned in an earlier step, the wire I used is thin ribbon wire.  In a project like this I need to reduce the amount of space where I can and using ribbon wire works a treat.Steps:1.       Solder 2 lengths of wire to the ground and positive solder points on the USB outlet 2.       Work out how long each needs to be, trim and solder to the input solder points on the charging module3.       Next, solder a wire to the positive output solder point on the module.  Measure, trim and solder the other end to one of the end solder points on the switch.  The other wire that will be soldered to the switch will come from the circuit


## Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 1](images/step12_01.jpg)

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 2](images/step12_02.jpg)

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 3](images/step12_03.jpg)

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 4](images/step12_04.jpg)

Adding an LED is a great way to indicate when the amp is on.  It’s a simple addition which is definitely worth including.Steps:1.       Drill a 3mm hole into the NES controller where you want to have the LED.  I placed this on top off the controller near the pot and USB outlet2.       Push the LED into the hole and if necessary, add a little superglue to keep it in place3.       Trim the positive LED leg and solder on a 3.3K resistor.4.       Connect the other leg of the resistor to the middle solder point on the switch5.       The other leg on the LED will be attached to ground on the circuit board


## Step 12: Working Out the Right Size for the Prototype Board

![Step 12: Working Out the Right Size for the Prototype Board image 1](images/step13_01.jpg)

![Step 12: Working Out the Right Size for the Prototype Board image 2](images/step13_02.jpg)

![Step 12: Working Out the Right Size for the Prototype Board image 3](images/step13_03.jpg)

![Step 12: Working Out the Right Size for the Prototype Board image 4](images/step13_04.jpg)

It might seem a little backward to first add all of the parts to the case and then work out the size of the prototype board but it’s a good way to work out exactly what room you have to work with.  I obviously was adding the parts to the NES controller with the circuit board in mind, trying to leave as much space as possible.Steps:1.       Place the prototype board inside the controller.  The board fits very well length ways but will need to be trimmed and cut in half in order for it to fit.2.       You can see why I bent the legs up on the jack inputs.  This gives me a little more room for the circuit board3.       The switch and screw mount was in the way so I just cut out these sections on the prototype board and fitted it around them


## Step 13: Making the Circuit - Part 1

![Step 13: Making the Circuit - Part 1 image 1](images/step14_01.jpg)

![Step 13: Making the Circuit - Part 1 image 2](images/step14_02.jpg)

![Step 13: Making the Circuit - Part 1 image 3](images/step14_03.jpg)

![Step 13: Making the Circuit - Part 1 image 4](images/step14_04.jpg)

So, I decided to solder the IC directly to the circuit board.  I’d suggest you don’t do this and use a IC socket so you can change the IC if something goes wrong.I’ll go through the circuit build step by step so if you are new to this type of build you should be able to follow along easily.Steps:1.       First, solder the IC into place.  You can see in the images that I placed it 4 holes away from the edge.  This gives you some room when adding the capacitors2.       Next, connect pin 4 to the ground bus and pin 8 to the positive bus on the prototype board.  I use resistor legs to do this3.       Grab both the 220 uf caps.  The first one solder the positive leg to pin 7 and the other leg to a spare solder point.  Lay it flat like I did in the images.  If you don’t you won’t be able to fit it into the NES controller4.       The other solder the positive leg to pin 1 and the other leg to a spare solder point


## Step 14: Making the Circuit - Part 2

![Step 14: Making the Circuit - Part 2 image 1](images/step15_01.jpg)

![Step 14: Making the Circuit - Part 2 image 2](images/step15_02.jpg)

![Step 14: Making the Circuit - Part 2 image 3](images/step15_03.jpg)

![Step 14: Making the Circuit - Part 2 image 4](images/step15_04.jpg)

You might have noticed that pin 3 on the IC has a few components soldered to it.  I had to come up with a way to attach all of the parts which I think worked well.  In this step, I will start to expand pin 3 to enable to be able to attach all of the parts neededSteps:1.       Solder a 68K resistor to pins 1 and 2 and also top pins 6 and 72.       Solder a 22pf cap to the same pins3.       Add a jumper wire (just a resister leg) from pin 3 to the spare solder point next to the IC


## Step 15: Making the Circuit - Part 3

![Step 15: Making the Circuit - Part 3 image 1](images/step16_01.jpg)

![Step 15: Making the Circuit - Part 3 image 2](images/step16_02.jpg)

![Step 15: Making the Circuit - Part 3 image 3](images/step16_03.jpg)

You next need to solder the 18K resistors.  You can see in the images that these are going out to the right of the prototype board.  That’s because you will need to add a couple of caps later and will need the spaceSteps:1.       Add an 18K resistor to pin 6 and solder the other leg to a spare spot on the prototype board.2.       Do the same for pin 23.       Time to add one of the first resistors to pin 3.  Place a 68K resistor in the last hole closest to the ground bus strip and solder into place.  Solder the other leg to ground


## Step 16: Making the Circuit - Part 4

![Step 16: Making the Circuit - Part 4 image 1](images/step17_01.jpg)

![Step 16: Making the Circuit - Part 4 image 2](images/step17_02.jpg)

![Step 16: Making the Circuit - Part 4 image 3](images/step17_03.jpg)

![Step 16: Making the Circuit - Part 4 image 4](images/step17_04.jpg)

Now it’s time to add another resistor to pin 3 along with a 4.7 Cap.  You also need to connect pins 3 and 5 together. Steps:1.       Grab a 68K resistor.  This will be connected to the positive bus.  Solder one leg to the jumper wire coming from pin 3.2.       Solder the other leg on the other side of the IC as shown in the image3.       Add another jumper wire and connect it to the positive bus and the resister leg4.       On the other side of the jumper solder a 4.7uf cap (positive leg)5.       The negative leg is to be soldered to the ground bus.  Make sure you  lay the cap down as shown in the images6.       Lastly, you need to solder a 200uf cap from positive bus strip to the ground bus.  Lay this one down as well.That’s it for the components, it’s now time to solder some wires to the circuit board


## Step 17: Soldering the Wires in Place

![Step 17: Soldering the Wires in Place image 1](images/step18_01.jpg)

![Step 17: Soldering the Wires in Place image 2](images/step18_02.jpg)

![Step 17: Soldering the Wires in Place image 3](images/step18_03.jpg)

Now it’s time to add wires so you can connect the pot, jacks, battery and LED up to the circuit board.  The wire I used was thin computer ribbon wire.  You can usually pick this up for free at your local e-waste depo.Steps:1.       Pull strands of wire from the ribbon cable2.       Start to solder these into place on the prototype board.  It helps to use the schematic to make sure you have all the wires connected properly.3.       Don’t forget to add a couple wires for the battery and one extra wire to the negative bus strip for the LED.  The LED isn’t shown on the schematic but it helps to add one so you know when the amp is on.  4.       Solder 2 wires onto the potentiometer as well.  These will be connected to the jack input later on.


## Step 18: Connecting All Those Wires

![Step 18: Connecting All Those Wires image 1](images/step19_01.jpg)

![Step 18: Connecting All Those Wires image 2](images/step19_02.jpg)

![Step 18: Connecting All Those Wires image 3](images/step19_03.jpg)

![Step 18: Connecting All Those Wires image 4](images/step19_04.jpg)

![Step 18: Connecting All Those Wires image 5](images/step19_05.jpg)

Once all of the wires have been added to the prototype board, you’ll next have to connect them to the auxiliary parts.  Wires can take up quite a lot of space so take your time when adding the wires and keep them as short as possible.Steps:1.       Place the circuit board into the NES controller.  It is good practice to be able to get to the bottom of the circuit board in case you need to make any changes, although in this build I kept the wires pretty short2.       Next, start to measure each wire against the component it needs to be connected to and trim to length.3.       Tin the end of the wire and solder into place.4.       Continue to do this until all of the connections have been made5.       For the LED, add a 3.3K resistor to the positive leg and connect this to the switch6.       Solder a wire from the ground bus to the negative leg of the LED7.       The positive wire from the battery needs to be connected to the other solder point on the switch


## Step 19: Finishing Touches

![Step 19: Finishing Touches image 1](images/step20_01.jpg)

![Step 19: Finishing Touches image 2](images/step20_02.jpg)

![Step 19: Finishing Touches image 3](images/step20_03.jpg)

Close now.  Before you close-up the case, give it a test to make sure everything is working as it should.  If not, then check your connections and re-test until you start to hear some sweet tunes coming out of your headphones.  You will hear a slight popping as you turn the amp on through your headphones – don’t worry – this is just the caps charging.Steps:1.       If everything is working as it should be, place the back cover on and make sure that the potentiometer is in the right spot.2.       Carefully screw everything back into place3.       Add the small nut for the potentiometer and secure4.       Add a knob to the top of the potentiometerThat’s it.  You have finished building your own headphone amp


---
*89 images archived*
