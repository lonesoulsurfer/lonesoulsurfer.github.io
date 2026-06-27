# Auto Door for Chicken Feeder

Source: https://www.instructables.com/Auto-Door-For-Chicken-Feeder/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)


## Step 1: Parts to Gather

![Step 1: Parts to Gather image 1](images/step02_01.jpg)

![Step 1: Parts to Gather image 2](images/step02_02.jpg)

Parts1.      Large project box2.       Arduino uno – eBay3.       Light sensor – eBay4.       Step down voltage converter – eBay5.       4” Exhaust U Clamp – eBay ( you could probably get away with using a smaller on like 3.5”.6.       Wire connector – eBay7.       Servo – eBay8.       Servo arm – eBay9.       Blank circuit board – eBay10.   10R resister11.   5.5 x 2.1mm barrel  jack – eBay12.   Coat hanger13.   100mm PVC cap14.   90mm PVC pipe15.   90mm 45 degree coupling16.   2 x 90mm screw caps17.  Various nuts and screws and boltsTools1.       Drill2.       Soldering iron3.       Dremel4.       Pliers5.       Drop saw6.       PVC pipe glue


## Step 2: Getting the Servo to Do Your Bidding

![Step 2: Getting the Servo to Do Your Bidding image 1](images/step03_01.jpg)

![Step 2: Getting the Servo to Do Your Bidding image 2](images/step03_02.jpg)

![Step 2: Getting the Servo to Do Your Bidding image 3](images/step03_03.jpg)

The first thing you’ll need to do is to test the servo and light sensor set-up.  If you look on the net for Arduino controlled servo and light sensor you will be able to find a few examples.  I tested most of them and the one that worked best for me was on this website.  The only thing I changed was the resister to a 10R one as the one they recommended was no good for this project.Steps:1.       Watch the video that is loaded on the website.  It’s only short but it will give you an idea of how it’s put together2.       Next check out the image they have of how everything is bread boarded and copy.  I have also included the image below.3.       Test to make sure that the servo moves when the light sensor is covered.  If everything works then it’s time to add the circuit to a circuit board4.       You can also play around with some of the values in the script to either make the servo move less or more.5.  You could also just use the simple code provided in the 'ible by quaddel This will do the job but will mean you can't play around with the variables (or not that I could work out any how!)


## Step 3: Creating the Circuit Board

![Step 3: Creating the Circuit Board image 1](images/step04_01.jpg)

![Step 3: Creating the Circuit Board image 2](images/step04_02.jpg)

![Step 3: Creating the Circuit Board image 3](images/step04_03.jpg)

![Step 3: Creating the Circuit Board image 4](images/step04_04.jpg)

![Step 3: Creating the Circuit Board image 5](images/step04_05.jpg)

![Step 3: Creating the Circuit Board image 6](images/step04_06.jpg)

Once you have found (or created) the script that you are happy with, the next thing to is to make a circuit.Steps:1.  With a small piece of blank circuit board, start to copy what is on the breadboard.  2.  I used the jumper wires to make the connections to the arduino.  3.  Carefully solder the wires into place and add the resister.  I added some extra long wires for the light sensor.4.  Test and make sure everything works


## Step 4: Making the Power Plug

![Step 4: Making the Power Plug image 1](images/step05_01.jpg)

![Step 4: Making the Power Plug image 2](images/step05_02.jpg)

![Step 4: Making the Power Plug image 3](images/step05_03.jpg)

![Step 4: Making the Power Plug image 4](images/step05_04.jpg)

![Step 4: Making the Power Plug image 5](images/step05_05.jpg)

![Step 4: Making the Power Plug image 6](images/step05_06.jpg)

I know that the arduino comes with a voltage regulator, but I wanted to make sure that I didn't blow anything.  I decided to use a step-down board so I could ensure that 5V was being delivered to the arduino.Steps:1.  To power the arduino I used a 5.5 x 2.1mm barrel jack.2.  Next get a spare USB cable and cut off one of the ends.  Find the positive and negative wires and attach these to the barrel jack.  You will have to test to ensure that you have the wires around the right way.  Just plug the jack in and if it doesn't work, then reverse.3.  I tested everything by adding a 9v battery to the voltage regulator, plug in the USB and make sure that everything lights up on the arduino


## Step 5: Adding the Servo to the Project Box

![Step 5: Adding the Servo to the Project Box image 1](images/step06_01.jpg)

![Step 5: Adding the Servo to the Project Box image 2](images/step06_02.jpg)

![Step 5: Adding the Servo to the Project Box image 3](images/step06_03.jpg)

![Step 5: Adding the Servo to the Project Box image 4](images/step06_04.jpg)

Steps:1.  In order to have the servo stick out of the project box, you'll need to cut a hole in it.  2.  Use a dremel and cut through the plastic.  make sure though you mark on the project box exactly how much to cut out.3.  I ran into a problem once I cut through the plastic as there was a plastic section in the way - check out the images below.4.  To fix this I just cut half way through the plastic pillar.  This actually worked in my favour as the servo mounting points now locked into place behind the cut plastic and ii didn't even have to hot glue into place!


## Step 6: Adding the Mounting Bracket (Exhaust Clamp)

![Step 6: Adding the Mounting Bracket (Exhaust Clamp) image 1](images/step07_01.jpg)

![Step 6: Adding the Mounting Bracket (Exhaust Clamp) image 2](images/step07_02.jpg)

![Step 6: Adding the Mounting Bracket (Exhaust Clamp) image 3](images/step07_03.jpg)

![Step 6: Adding the Mounting Bracket (Exhaust Clamp) image 4](images/step07_04.jpg)

![Step 6: Adding the Mounting Bracket (Exhaust Clamp) image 5](images/step07_05.jpg)

I work in the transport industry and have access to truck parts.  I decided to grab a 4" exhaust clamp and use this  to mount to the chicken feeder.Steps:1.  Mark out on the project box where to mount it too the clamp2.  Drill the holes and then mark and drill the clamp.  Now it's ready to mount.  Don't do this yet though as you will need to do a few things to the box first.


## Step 7: Adding the Arduino and Mounting

![Step 7: Adding the Arduino and Mounting image 1](images/step08_01.jpg)

![Step 7: Adding the Arduino and Mounting image 2](images/step08_02.jpg)

![Step 7: Adding the Arduino and Mounting image 3](images/step08_03.jpg)

![Step 7: Adding the Arduino and Mounting image 4](images/step08_04.jpg)

![Step 7: Adding the Arduino and Mounting image 5](images/step08_05.jpg)

![Step 7: Adding the Arduino and Mounting image 6](images/step08_06.jpg)

Steps:1.  Drill a small hole in the top of the box big enough for the light sensor.  2.  Add some velcro to the bottom of the arduino and attach to the bottom of the box.3.  Hot glue into place the light sensor.4.  Find good homes for the circuit board, voltage regulator and tuck away the wires.5.  To be able to connect the arduino to a power source add a couple of wires to the regulator and drill a hole in the side of the box for these to come out of.  Attach a connector to the wires.  You will need to attach the other end of the connector to a length of wire which will be connected to the battery.you shouldn't have any issues fitting everything into the project box.


## Step 8: Adding the Arms (First Try)

![Step 8: Adding the Arms (First Try) image 1](images/step09_01.jpg)

![Step 8: Adding the Arms (First Try) image 2](images/step09_02.jpg)

![Step 8: Adding the Arms (First Try) image 3](images/step09_03.jpg)

First try didn't go so well...1.  Obviously on the servo side you can just add a servo arm.  You can see from the first picture how I first tried to add the wire for the lid to the servo.  This didn't work in the end so I just zip tied and hot glued into place.2,  For the other side I was going to do something similar as you can see but this didn't really work either.  It probably could have though if I used larger terminal sections (those gold bits)


## Step 9: Adding the Arm (The Version That Worked)

![Step 9: Adding the Arm (The Version That Worked) image 1](images/step10_01.jpg)

![Step 9: Adding the Arm (The Version That Worked) image 2](images/step10_02.jpg)

![Step 9: Adding the Arm (The Version That Worked) image 3](images/step10_03.jpg)

![Step 9: Adding the Arm (The Version That Worked) image 4](images/step10_04.jpg)

![Step 9: Adding the Arm (The Version That Worked) image 5](images/step10_05.jpg)

![Step 9: Adding the Arm (The Version That Worked) image 6](images/step10_06.jpg)

Steps:1.  Attach the metal servo arm to the servo.2.  Next I pulled apart an old servo and used the gear and attached a plastic servo arm to the end.  3.  Once this is done, drill a hole in the side of the project box and push through a bolt.  Add a bolt to the end and do this up so it is flush with the box.  This creates the axle for the gear to be attached to.4.  Lastly, with some pressure,  carefully turn the bolt with a screwdriver and force it into the of the gear.5.  Add some hot glue to the bolt and gear to keep everything in place.6.  Next, attach the project box to the actual chicken feeder.  This way you can work out how long the wire arm needs to be for the lid.


## Step 10: Adding the Lid

![Step 10: Adding the Lid image 1](images/step11_01.jpg)

![Step 10: Adding the Lid image 2](images/step11_02.jpg)

![Step 10: Adding the Lid image 3](images/step11_03.jpg)

![Step 10: Adding the Lid image 4](images/step11_04.jpg)

Steps:1.  Cut and straighten out a coat-hanger2.  Bend into place so the wire is touching the top of the lid as shown below.3.  Attach the wire to the servo arms.  This was a little tricky and I would have liked to have come up with a better solution.  In the end I just zip tied and hot glued the wire arm into place.  It did the job but I will take a bit to replace if necessary3.  Mark out on the lid where you have to drill and go for it.4.  Attach the lid with some zip ties.Done...nearly.


## Step 11: Getting It Going

![Step 11: Getting It Going image 1](images/step12_01.jpg)

![Step 11: Getting It Going image 2](images/step12_02.jpg)

So you've finished and it's time to add some juice and get the ting to workSteps:1.  Attach the wire that you added the connector to the battery2,  Next connect the connector from the feeder to the battery connector.3.  Test by putting your hand over the light sensor and make sure that the lid closes over the food section.  remove your hand and the lid should lift up.  If you need to adjust then you can move the project box up or down the feeder.  If the lid doesn't go down far enough, then you will need to do some adjustments to the script.  It's not a big issue, just means you will have to plug the arduino in to the computer and play around.Things I'd do differently next time-   As mentioned previously, I attached the feeder to a battery that I'm using for the auto chicken coop door.  This drained the power faster than the solar panel could charge  so I had to come up with a new solution.-  I would have liked to have figured out a better way to attach the arm to the servo.  my way worked but it was a little messy.-  The script worked ok but I just don't know enough about scripts to make it work really well.  I will probably update the script once I have better knowledge on how they work.


---
*52 images archived*
