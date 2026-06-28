# Push Puppet Automata

Source: https://www.instructables.com/Push-Puppet-Automata/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

As a kid I was always amazed by push puppets. You know the the little (usually wooden) puppets that you push on the bottom and they collapse and dance about. Problem was, I always pulled them apart to see how they worked. Turns out they are very simple. A spring adds tension when the puppet is at rest and when you push on the bottom of the puppet, the spring contracts and the puppet dances. simple!

recently I was thinking how I could make one move and have it sound activated. I initially started to think about an arduino to do the job but couldn't find any good tutorials. I needed to have the microphone convert the sound signal into movement for the servo. I wanted to use a solenoid initially but realized that it probably wouldn't be strong enough to move the spring.

I decided to use some [little bits](http://littlebits.cc/shop) instead. I had some modules from a competition I won sitting in a draw and decided to see what I could do with them. Luckily, I had just the right ones to do what I needed!

The build isn't too complicated, but you will need to find a photo frame that has some depth like the one I used. I purchased the one I used from Kmart (Australia). You could also just make one out of wood if your that way inclined.


## Step 1: Watch the Video

You'll have to excuse my singing - only way I could get the little fella to move about.


## Step 2: Parts and Tools

![Step 2: Parts and Tools image 1](images/step02_01.jpg)

![Step 2: Parts and Tools image 2](images/step02_02.jpg)

![Step 2: Parts and Tools image 3](images/step02_03.jpg)

Parts:

1. Picture Frame. Needs to be one like in the picture. I purchased mine at Kmart (Australia) but I'm sure you will be able to find something similar on-line or at your local shops

2. Little bits: At a minimum, you will need the following:

[Servo](http://littlebits.cc/bits/servo)

[Microphone](http://littlebits.cc/bits/sound-trigger)

[Power](http://littlebits.cc/bits/usb-power)

I also used:

[LED](http://littlebits.cc/bits/long-led)

Get one of these if you don't want to solder

[wire](http://littlebits.cc/bits/wire-bit)

3. 3 x AA battery holder - [ebay](http://www.ebay.com.au/itm/Hard-Plastic-Storage-Holder-Case-Box-For-3-X-AA-Battery-With-Wire-Leads-/380930673781?hash=item58b13ccc75:g:zv8AAOSwcnpTnqQG)

4. Push puppet - [eBay](http://www.ebay.com.au/itm/281748577193?_trksid=p2060353.m1438.l2649&ssPageName=STRK%3AMEBIDX%3AIT)

5. Toggle switch

6. Small screws

Tools:

1. Drill

2. Hot glue

3. Files

4. Soldering iron


## Step 3: Modding the Frame

![Step 3: Modding the Frame image 1](images/step03_01.jpg)

![Step 3: Modding the Frame image 2](images/step03_02.jpg)

![Step 3: Modding the Frame image 3](images/step03_03.jpg)

![Step 3: Modding the Frame image 4](images/step03_04.jpg)

![Step 3: Modding the Frame image 5](images/step03_05.jpg)

![Step 3: Modding the Frame image 6](images/step03_06.jpg)

![Step 3: Modding the Frame image 7](images/step03_07.jpg)

In order to have the servo push against the bottom of the push puppet, you will need to make a large hole in the bottom of the frame.

Steps:

1. Mark on the frame, the best position for the push puppet to sit. Remember that it will need to sit forward a little so the back of the frame can fit correctly

2. I used a 22mm hole drill piece to make the hole. Place the puppet over the hole and make sure that it can be pushed and is not sticking anywhere.


## Step 4: Adding the Servo

![Step 4: Adding the Servo image 1](images/step04_01.jpg)

![Step 4: Adding the Servo image 2](images/step04_02.jpg)

![Step 4: Adding the Servo image 3](images/step04_03.jpg)

![Step 4: Adding the Servo image 4](images/step04_04.jpg)

![Step 4: Adding the Servo image 5](images/step04_05.jpg)

![Step 4: Adding the Servo image 6](images/step04_06.jpg)

![Step 4: Adding the Servo image 7](images/step04_07.jpg)

Steps:

1. Attach the shorter arm top the end of the servo.

2. Have a play and work out the best position for the servo to the attached to the frame. Place the puppet over the hole and hold the servo in place. Activate the servo and make the arm hit the bottom of the puppet. You want the puppet to flop over each time the servo arm hits the bottom.

3. Hot glue the servo into place


## Step 5: Attaching the Push Puppet

![Step 5: Attaching the Push Puppet image 1](images/step05_01.jpg)

![Step 5: Attaching the Push Puppet image 2](images/step05_02.jpg)

![Step 5: Attaching the Push Puppet image 3](images/step05_03.jpg)

![Step 5: Attaching the Push Puppet image 4](images/step05_04.jpg)

Steps:

1. Drill 2 holes into the bottom of the frame. These holes will allow you use a phillips head to screw in the screws.

2. It's probably best to make a paper template of the bottom of the push puppet at this stage. This will help you work out where to best add the screws. I didn't do this and just winged it. Not the smartest ideas but it worked fine.

3. Drill a couple of smaller holes in the frame for the screws to go through. Carefully screw the push puppet to the frame.

4. Lastly, do a test and make sure that the servo arm is making the puppet move. If not, you will need to make some adjustments.


## Step 6: Microphone, Switch and Power

![Step 6: Microphone, Switch and Power image 1](images/step06_01.jpg)

![Step 6: Microphone, Switch and Power image 2](images/step06_02.jpg)

![Step 6: Microphone, Switch and Power image 3](images/step06_03.jpg)

![Step 6: Microphone, Switch and Power image 4](images/step06_04.jpg)

![Step 6: Microphone, Switch and Power image 5](images/step06_05.jpg)

In order for the microphone little bit to be attached to the frame, you need to add some wires.

Steps:

1. Solder 3 wires to the solder points on the microphone little bit. These can be found on the bottom of the little bit.

2 Solder the ends of the wire to the power module little bit. The thing to make sure of is that the wires are correctly orientated and soldered on the right solder point.

3. Test to make sure that the little bits have been wired correctly

4. To power the module, I used the 5v power cord that came with it. Just cut the cord, strip the plastic off the end and keep the red (positive) and black (negative).

5. Solder a couple of sires onto the toggle switch


## Step 7: Wiring the Switch and Power

![Step 7: Wiring the Switch and Power image 1](images/step07_01.jpg)

![Step 7: Wiring the Switch and Power image 2](images/step07_02.jpg)

![Step 7: Wiring the Switch and Power image 3](images/step07_03.jpg)

Steps:

1. Drill a hole into the side of the frame and attach the switch.

2. Solder the negative wire from the battery holder to one of the wires to the switch.

3. Next solder the negative wire from the power cord to the other terminal of the switch

4. lastly, solder the positive wire from the battery holder to the positive on the power cord

5. Once all the wires have been soldered, superglue the power module and microphone little bit togetjer.


## Step 8: Attaching the Microphone to the Frame

![Step 8: Attaching the Microphone to the Frame image 1](images/step08_01.jpg)

![Step 8: Attaching the Microphone to the Frame image 2](images/step08_02.jpg)

![Step 8: Attaching the Microphone to the Frame image 3](images/step08_03.jpg)

Steps:

1. Drill a hole in the frame large enough for the microphone.

2. Drill a smaller hole for the microphone adjuster

3. Hot glue into place.

4. Plug the power cord into the power module.


## Step 9: Add the LED

![Step 9: Add the LED image 1](images/step09_01.jpg)

![Step 9: Add the LED image 2](images/step09_02.jpg)

![Step 9: Add the LED image 3](images/step09_03.jpg)

![Step 9: Add the LED image 4](images/step09_04.jpg)

![Step 9: Add the LED image 5](images/step09_05.jpg)

![Step 9: Add the LED image 6](images/step09_06.jpg)

Steps:

1. Drill a hole in the top of the frame big enough to fit the LED into. Hot glue into place

2. Superglue the LED little bit to the Servo little bit.


## Step 10: Test

![Step 10: Test image 1](images/step10_01.jpg)

![Step 10: Test image 2](images/step10_02.jpg)

![Step 10: Test image 3](images/step10_03.jpg)

Steps:

1. Place the back onto the frame and test the robot.

2. You might have to adjust the sensitivity of the microphone to order for the microphone to pick-up sound.

3. If the puppet is not moving right, try to adjust the arms or legs. You might have to also adjust the servo (hopefully not as it's been hot glued into place!)

4. Lastly, add a sheet of paper to the inside of the frame. This will be the "background"


---
*44 images archived*
