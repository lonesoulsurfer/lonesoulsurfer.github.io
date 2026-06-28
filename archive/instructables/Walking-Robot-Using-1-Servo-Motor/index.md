# Walking Robot Using 1 Servo Motor

Source: https://www.instructables.com/Walking-Robot-Using-1-Servo-Motor/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

I've been wanting to build this walker robot even since I saw it on YouTube. After a little searching I found some more information on it and decided to make my own.

The goal I had building this walker was to try and make it as small as I possibly could. I wanted it to fit in the palm of my hand and although I have pretty big palms, the legs just hang over.

The robot itself runs off a micro servo which has been modified to turn continuously. As the servo spins, it moves a couple of linkages which in turn move the back legs up and down and the front legs side to side allowing it to walk.

The build itself isn't very difficult but "tuning" it in so the walking gait is right takes a little time. I did a fair bit of experimenting and have a few tips which hopefully will help you tune it in easier then it was for me.

If you have never built a walking robot before and want to jump in the deep end, then this is the perfect project to start with.

Hackaday did a review of my walker - check it out below:

[Hackaday](https://hackaday.com/2020/09/16/a-walking-robot-with-a-single-servo/)

And with that, let's get started


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

![Step 1: Parts image 3](images/step01_03.jpg)

![Step 1: Parts image 4](images/step01_04.jpg)

Parts:

1. Mirco Servo - [eBay](https://www.ebay.com.au/itm/1pcs-90S-micro-metal-gear-9g-servo-for-RC-plane-helicopter-boat-car-4-8V-fw/363092424197?hash=item5489feb605:g:dXMAAOSwz05cHJS9&frcectupt=true)

2. 16340 lithium battery - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=16340+lithium+battery&_sacat=0&_sop=15)

3. Aluminium Channel 10mm X 10mm - [eBay](https://www.ebay.com.au/itm/Aluminium-Channel-10mm-x-10mm-x-1-6mm-at-1000mm-long/112027271224?hash=item1a15588038:g:7AEAAMXQsmFRb4sa&frcectupt=true) you can also get it at most hardware stores

4. 2 X large paperclips - Newsagent or stationary store will have them. Get them as big as you can

5. Wire Terminal - [eBay](https://www.ebay.com.au/itm/3Pcs-12-Way-3A-Barrier-Screw-Terminal-Block-Wire-Connection-Connector-Strip-AU/333540024628?hash=item4da888e134:g:cRIAAOSwipleZdGi) hardware store will also have them

6. SPDT Switch - [eBay](https://www.ebay.com.au/itm/2-Pcs-AC-SPDT-On-Off-3-Position-Momentary-Toggle-Switch-AC250V-2A-120V-5A-B-AU/254693639157?hash=item3b4cec83f5:g:oQ8AAOSwQFJauzRQ)

7. Battery charging module - [eBay](https://www.ebay.com.au/itm/10pcs-TP4056-5V-1A-Lipo-Battery-Charging-Board-Charger-Module-lithium-USB-18650/253066138178?hash=item3aebead242:g:yBwAAOSwFypZeCZq&frcectupt=true)

8. Wire coat hanger - Cupboard

9. 3 X M4 screws - [eBay.](https://www.ebay.com.au/itm/M4-4mm-A2-Stainless-Steel-Hex-Socket-Button-Head-Allen-Bolts-Screws/322714607245?hash=item4b234a1e8d:g:kXIAAOSw9L1ZqLkc) Will be able to get them at a hardware store as well. I used philips head ones as that was what I had on hand.

10. 6 X M4 Locknuts - [eBay](https://www.ebay.com.au/itm/M3-M20-Hex-Locknut-304-Stainless-Steel-Self-Locking-Hexagon-Screw-Nuts-DIN985/124226975391?hash=item1cec81369f:g:ILUAAOSwdqFdkFv1&frcectupt=true) Will be able to get them at a hardware store as well

11. 2 X Smaller washers. Hardware store

12. 2 X Female banana plugs - [eBay](https://www.ebay.com.au/itm/2-10pcs-Banana-Plug-Jackvideo-Female-Connector-Amplifier-Terminal-audio-4mm/173701891712?hash=item2871708680:g:IcIAAOSwseFcHF22). I used a section inside these to make the pivots for the legs. They fit perfectly over the M4 screws.

Tools:

1. Angle grinder

2. Dremel not mandatory but always come in handy

3. Drill

4. Superglue

5. soldering iron

6. small blow torch. If you don't have one then you could probably get away with just a soldering iron

7. Pliers. Same needle nose and larger flat pair should do the job


## Step 2: Aluminium Chassis - Bending the Ends Up

![Step 2: Aluminium Chassis - Bending the Ends Up image 1](images/step02_01.jpg)

![Step 2: Aluminium Chassis - Bending the Ends Up image 2](images/step02_02.jpg)

![Step 2: Aluminium Chassis - Bending the Ends Up image 3](images/step02_03.jpg)

![Step 2: Aluminium Chassis - Bending the Ends Up image 4](images/step02_04.jpg)

![Step 2: Aluminium Chassis - Bending the Ends Up image 5](images/step02_05.jpg)

![Step 2: Aluminium Chassis - Bending the Ends Up image 6](images/step02_06.jpg)

The first thing to do is to work out how the battery and servo will fit and also how long to make the chassis.

Steps:

1. Place the servo and the battery on top of the aluminium channel. This will give you an idea on the length of the chassis. You'll need some extra space for the switch and screws. The total length of my chassis is 85mm.

2. Next you need to bend the 2 ends up on the aluminium channel. This will allow you add a small screw in one end and also just finishes and cleans-up the final look of the walker

3. To do this, you need to remove the sides of the channel and bend the aluminium up.

4. Measure 20mm in from the end of the channel and make 2 vertical cuts with a angle grinder. Don't cut the bottom of the channel as you will weaken it and it will break when you bend it

5. With a pair of pliers, carefully bend up the end of the channel. To get it as flat as possible, use a hammer and a piece of metal and give it a few taps. The aluminium scars easily so add some cloth to the section you are hitting to protect it.

6. Do the same to the other end

7. Lastly, I rounded off the corners to give it a better finish.


## Step 3: Making a Cut-out for the Servo

![Step 3: Making a Cut-out for the Servo image 1](images/step03_01.jpg)

![Step 3: Making a Cut-out for the Servo image 2](images/step03_02.jpg)

![Step 3: Making a Cut-out for the Servo image 3](images/step03_03.jpg)

![Step 3: Making a Cut-out for the Servo image 4](images/step03_04.jpg)

The servo goes at the front of the walker. In order for it to fit into the channel, you'll need to remove a couple of sections in the channel

Steps:

1. Place the servo on top of the channel and mark out the width of the servo on the channel. You need to make sure that you leave 5mm at the front as a screw needs to go through the front and you need to keep some clearance tor the head of the screw

2. Carefully cut the side walls of the channel to the bottom.

3. If you have a dremel, use a cutting wheel to make the final cut along the edge to remove the side sections. If you don't, you can prob get away with the angle grinder.

4. Next, use a file to clean-up the cut sections. Check and make sure the servo fits. It should be a nice, snug fit.


## Step 4: Making a Cut-out for the Battery

![Step 4: Making a Cut-out for the Battery image 1](images/step04_01.jpg)

![Step 4: Making a Cut-out for the Battery image 2](images/step04_02.jpg)

![Step 4: Making a Cut-out for the Battery image 3](images/step04_03.jpg)

![Step 4: Making a Cut-out for the Battery image 4](images/step04_04.jpg)

![Step 4: Making a Cut-out for the Battery image 5](images/step04_05.jpg)

![Step 4: Making a Cut-out for the Battery image 6](images/step04_06.jpg)

Next step is to make a cut-out for the battery. It's pretty much the same process as the servo. This chassis wasn't actually the final one I used. I did a faux-pas on this one and had to make another which I'm glad I did as it turned out cleaner then the one in the images

Steps:

1. Like the servo, place the battery on the aluminium channel and mark out the section on the channel on where to cut. There needs to be about a 5mm gap between the servo and battery. That's where the toggle switch will go. Plus, you need to give yourself a little room for the wires as well.

2. Make the vertical cuts with the angle grinder and the horizontal ones with the dremel

3. de-burr the cut section with a file and smooth out the edges.

4. You don't want to have the battery a too tight a fit as it will be sitting in aluminum which is conductive and could short the battery if both positive and ground are touching the chassis. You can always add a little electrical tape to one end to ensure the battery doesn't short


## Step 5: Adding the Screws and Switch to the Chassis

![Step 5: Adding the Screws and Switch to the Chassis image 1](images/step05_01.jpg)

![Step 5: Adding the Screws and Switch to the Chassis image 2](images/step05_02.jpg)

![Step 5: Adding the Screws and Switch to the Chassis image 3](images/step05_03.jpg)

![Step 5: Adding the Screws and Switch to the Chassis image 4](images/step05_04.jpg)

![Step 5: Adding the Screws and Switch to the Chassis image 5](images/step05_05.jpg)

![Step 5: Adding the Screws and Switch to the Chassis image 6](images/step05_06.jpg)

![Step 5: Adding the Screws and Switch to the Chassis image 7](images/step05_07.jpg)

To attach the legs to the chassis, you need to add a couple of screws. To make them move, you need to attach another screw as a pivot point to the side of the chassis. I did a diagram on where each of the holes need to be drilled so use this to help you.

Steps:

1. First, hole 1 in what will be the back section of the walker. You can easily identify the back of the walker as that is where the servo will go. The hole needs to be big enough for the screw to fit into. The back legs will be attached to this screw.

2. Hole 2 into the top section of the chassis. This hole needs to go into the top front of the chassis. The front legs will be attached to this screw

5. Hole 3 needs to be drilled into the top section, between the servo and the battery and is for the toggle switch

3. Hole 4 needs to be in the side of the chassis, directly under drill hole 2. This is where the pivot will go.

4. Hole 5 needs to go directly opposite hole 3. This hole is there to allow you to place the screw into place and to use a screwdriver. Without this hole how would you add the screw to the side of the chassis! make sure it is large enough for the screw head to go through.

5. Now all the holes have been drilled, it's time to add the screws. Secure them in place with the lucknuts.

NOTE: the screw in hole 3 needs to be able to turn so make sure you do it up securely but also ensure that the screw can turn in the hole. the other 2 can be done up tightly.


## Step 6: Modifying the Servo to Make It Continuous.

![Step 6: Modifying the Servo to Make It Continuous. image 1](images/step06_01.jpg)

![Step 6: Modifying the Servo to Make It Continuous. image 2](images/step06_02.jpg)

![Step 6: Modifying the Servo to Make It Continuous. image 3](images/step06_03.jpg)

![Step 6: Modifying the Servo to Make It Continuous. image 4](images/step06_04.jpg)

![Step 6: Modifying the Servo to Make It Continuous. image 5](images/step06_05.jpg)

![Step 6: Modifying the Servo to Make It Continuous. image 6](images/step06_06.jpg)

![Step 6: Modifying the Servo to Make It Continuous. image 7](images/step06_07.jpg)

![Step 6: Modifying the Servo to Make It Continuous. image 8](images/step06_08.jpg)

Before you secure the servo into the chassis, you first need to do a little modification to it. This is a very common modification and you can find plenty of tutorials on Google if you need more information. The modification allows the servo to to continuously spin, without the modification, the servo would only rotate 180 degrees.

Steps:

1. First, remove the screws on the bottom of the servo

2. The servo comes apart in 3 sections. Remove the top section first. If you look carefully on the large cog, you'll see a small piece plastic stuck to the bottom of it. This is a limiter and stops it continuously spinning. Grab some wire cutters and just clip it away. Some servos have the limiter inside the top casing so if you don't see any on the cog, check inside the case

3. Place the top section back on and remove the bottom section. snip the wires off the potentiometer. Don't worry if you're not sure what wires to cut, you need to remove them all so just cut away

4. On the bottom of the motor there will be 2 solder points. You will need to solder a couple of wires directly to the motor. Use the thinest wire you have as it will mean it will take up less space on the walker and you will be able to hide it well.

5. Place the motor back into the case and screw everything back together. Give the servo a test by connecting it up to the battery you are using for the walking. If it spins continuously then you have successfully made the mod.


## Step 7: Adding the Servo, Battery and Charger and Wiring Everything Up.

![Step 7: Adding the Servo, Battery and Charger and Wiring Everything Up. image 1](images/step07_01.jpg)

![Step 7: Adding the Servo, Battery and Charger and Wiring Everything Up. image 2](images/step07_02.jpg)

![Step 7: Adding the Servo, Battery and Charger and Wiring Everything Up. image 3](images/step07_03.jpg)

![Step 7: Adding the Servo, Battery and Charger and Wiring Everything Up. image 4](images/step07_04.jpg)

![Step 7: Adding the Servo, Battery and Charger and Wiring Everything Up. image 5](images/step07_05.jpg)

![Step 7: Adding the Servo, Battery and Charger and Wiring Everything Up. image 6](images/step07_06.jpg)

Now it's time to add the main parts to the chassis! I wanted to try and hide the wires as much as possible so it does get a little tight. I actually had a short the first time and melted the wires which was a pain. I had the positive and ground wires too close together!

Steps:

1. First thing to do is to secure the servo into the chassis. The servo arm needs to be as close as possible to the side of the chassis. If you clip off the screw supports on the servo, you will be able to have the side of the servo flush with the chassis. Add a little superglue and secure it in place

2. Next is the battery. Before that it secured in place, you will need to solder and add some wires directly to the battery, The positive end of the battery should be placed at the switch end and the ground at the back.

NOTE: You want the servo to turn in a clockwise direction. Test to make sure you know which wire on the servo to connect to which end of the battery. If you get it wrong then your walker will go backwards!

3. Solder on the ground wire on the servo to the ground on the battery. Also add an extra wire to ground as this will be connected to the charger module later

4. The wires will go under the battery and then come up the front so they remain hidden.

5. Add some superglue and secure the battery into the chassis.

6. You might find that the middle solder point on the switch is very close or touching the middle solder point on the switch. That's good, all you need to do is to add a little solder and connect them together. You will also need to add a wire to positive and connect this to the charging module a little later

7. Solder the other wire from the servo to one of the solder points on the switch. Give it a shot and make sure the servo turns on. It does! good.

8. Lastly, add a little superglue to the bottom of the charging module and connect the positive and ground to the battery solder points


## Step 8: Making the Legs

![Step 8: Making the Legs image 1](images/step08_01.jpg)

![Step 8: Making the Legs image 2](images/step08_02.jpg)

![Step 8: Making the Legs image 3](images/step08_03.jpg)

![Step 8: Making the Legs image 4](images/step08_04.jpg)

![Step 8: Making the Legs image 5](images/step08_05.jpg)

![Step 8: Making the Legs image 6](images/step08_06.jpg)

![Step 8: Making the Legs image 7](images/step08_07.jpg)

![Step 8: Making the Legs image 8](images/step08_08.jpg)

The legs are made from a coat hanger. Most coat hangers have a coating so you'll need to remove this with some sandpaper. Check out the diagrams which should help with the dimensions and bends

Steps:

1. Once the wire has been sanded, cut the long, bottom section away from the coat hanger.

2. First, I go through the front legs. These are pretty straight forward and are bent to make a cup shape. First bend the wire down so you have about a 70mm length. You need to bend it almost to right angles.

3. The total length of the legs across the top section is 70mm. However, you need to make a little "U" bend in the middle. This will allow you to solder it to a hollow metal tube a little later. Use a pair of pliers and make the "U" as small as you possibly can.

4. Bend the other leg down the same as the first one. This gives you the basic shape of the legs. You can play around with them later to improve the shape if necessary

5. Next, the back legs. These have an extra bend or elbow in them. First, bend the wire down so you have a 50mm length. This should be bent to about 70 degrees at right angle.

6. Hold the wire so the first bend is facing you and make a right angle bend at 30mm. This is the first leg.

7. You now have to do the same as the front and make a "U" shape about 35mm in the middle

8. Bend the other side leg the same as the first.


## Step 9: Soldering on Some Pivots to the Legs

![Step 9: Soldering on Some Pivots to the Legs image 1](images/step09_01.jpg)

![Step 9: Soldering on Some Pivots to the Legs image 2](images/step09_02.jpg)

![Step 9: Soldering on Some Pivots to the Legs image 3](images/step09_03.jpg)

![Step 9: Soldering on Some Pivots to the Legs image 4](images/step09_04.jpg)

![Step 9: Soldering on Some Pivots to the Legs image 5](images/step09_05.jpg)

![Step 9: Soldering on Some Pivots to the Legs image 6](images/step09_06.jpg)

![Step 9: Soldering on Some Pivots to the Legs image 7](images/step09_07.jpg)

OK, so I decided to use the inside of a female banana plug for the pivots. These fit perfectly onto the M4 screws and have very little side movement. You could use some copper tubing if you wanted to instead, just make sure it is a good fit on the screws. This step is a little tricky so make sure you secure the leg and pivot well before soldering. I used a screw and a 3rd hand to ensure everything was sitting right before soldering

Steps:

1. First, pull the banana plug apart and remove all of the plastic bits so you are only left with the metal section.

2. Cut off the metal screw section so you are only left with the female end of the banana plug. Give the cut end a file to smooth it out.

3. You now need to solder one of these to each of the legs to the "U" section you made. Before you do, Place the pivot onto the screw and then place the legs on it. This will help you work out how the legs need to sit against the pivot.

4. Add some flux and with a small blow torch, heat-up the metal and solder the pivot and legs together.

5. Test to make sure that the legs are sitting correct on the chassis.

6. Do the exact same for the other leg.

7. Last thing to do is to secure the legs onto the screws with some locknuts. You want to tighten them to a point where the legs still move side to side but with a minimal amount of wiggle as possible.

The legs kinda look a little weird in the images. The 'toe" sections still need to be shaped a little so the front legs are sitting up quite a lot.


## Step 10: Adding a Terminal to the Arm of the Servo

![Step 10: Adding a Terminal to the Arm of the Servo image 1](images/step10_01.jpg)

![Step 10: Adding a Terminal to the Arm of the Servo image 2](images/step10_02.jpg)

![Step 10: Adding a Terminal to the Arm of the Servo image 3](images/step10_03.jpg)

![Step 10: Adding a Terminal to the Arm of the Servo image 4](images/step10_04.jpg)

The terminals used in the build were pulled out of a wire terminal. Using these allows you to secure the arms later on the move the legs and easily adjust them to get your walker walking right. It's a few adjustments (maybe more then a few!) to get your robot walking right.

Steps:

1. First, you need to drill a hole into the servo arm. The hole should be slightly larger than then screw as the terminal needs to be able to turn with the servo.

2. I drilled a hole into the second hole in the servo arm. There isn't much material right at the end of the arm so using the 2nd hole will give you just enough material to drill the hole.

3. Use one of the small screws on the terminal and secure the terminal to the servo arm

4. Lastly, secure the servo arm to the servo


## Step 11: Linkages to Make the Legs Move

![Step 11: Linkages to Make the Legs Move image 1](images/step11_01.jpg)

![Step 11: Linkages to Make the Legs Move image 2](images/step11_02.jpg)

![Step 11: Linkages to Make the Legs Move image 3](images/step11_03.jpg)

![Step 11: Linkages to Make the Legs Move image 4](images/step11_04.jpg)

![Step 11: Linkages to Make the Legs Move image 5](images/step11_05.jpg)

![Step 11: Linkages to Make the Legs Move image 6](images/step11_06.jpg)

![Step 11: Linkages to Make the Legs Move image 7](images/step11_07.jpg)

Getting the linkages right took me a couple of goes. However, I've made some dimensional drawings which should help in getting them right. You don't have to get exactly the same sizes so don't stress on trying to get them the same as mine. As long as they are close.

Steps:

Back Leg Arm

1. First thing to do is to fully straighten the paperclip as best you can.

2. Next, with some needle nose pliers, bend the wire at around 45mm, 180 degrees

3. Bend-up the end so you an elongated oval shape. 5mm wide

4. Solder the paperclip where the 2 pieces of metal touch.

Front Leg Arm

1. Like the back legs arm, fully straighten the paperclip

2. Again, like the other arm, make an elongated oval shape but this time make it 55mm long, it should also be around 5mm wide

3. Solder the bent up end, the same as you did on the other one.

4. On the other end of the piece of wire, you need to make a small loop. One of the screws from the terminal will go through this so make sure it isn't too small and the screw goes in easily.


## Step 12: Adding the Linkages to the Walker

![Step 12: Adding the Linkages to the Walker image 1](images/step12_01.jpg)

![Step 12: Adding the Linkages to the Walker image 2](images/step12_02.jpg)

![Step 12: Adding the Linkages to the Walker image 3](images/step12_03.jpg)

![Step 12: Adding the Linkages to the Walker image 4](images/step12_04.jpg)

![Step 12: Adding the Linkages to the Walker image 5](images/step12_05.jpg)

The linkages are connected to the servo and the pivot via some terminals that you can pull out of a wire terminal.

Steps:

1. First, place the vertical linkage through the front leg.

2. Next, add a small washer to the pivot screw and push the vertical linkage onto the pivot screw

3. Add another washer (you want to sandwich the linkage between the 2 washers) and add a lucknut to the pivot screw.

4. Push the linkage up so the bottom is close to the pivot screw (images 2) and tighten the locknut so the linkage can't move up or down

5. Next thing to do is to add a terminal to the small loop at the bottom of the terminal. You can use one of the small screws in the terminal to do this

6. For the horizontal linkage, first place the loop section through the front leg

7. Next, push the rod section through the terminal on the servo and also through the other terminal joined to the vertical linkage

8. Tighten both screws on the terminals - this will hold the linkages into place, and turn on your walker. 95% of the time he'll just do a back flip and flop about on his back. You will need to tune it in which takes a little learning. It's not hard however and I have provided a couple tips in the next step to do this.


## Step 13: Fine Tuning Your Walker

![Step 13: Fine Tuning Your Walker image 1](images/step13_01.jpg)

![Step 13: Fine Tuning Your Walker image 2](images/step13_02.jpg)

![Step 13: Fine Tuning Your Walker image 3](images/step13_03.jpg)

![Step 13: Fine Tuning Your Walker image 4](images/step13_04.jpg)

![Step 13: Fine Tuning Your Walker image 5](images/step13_05.jpg)

You can change the way your walker walks by changing the height of the vertical linkage and the length of the horizontal one

Steps:

1. Place your walker on the ground and turn the servo arm so it is facing down. The front legs should be relativity straight and one of the back legs should be raised. You can lower or raise the height of the leg by changing the height of the vertical linkage

2. If you move the servo arm so it is pointing up, the other back leg should be raised and the front legs should be relativity straight

3. Check out the first 2 images which shows how the legs should look with the servo arm down and up

4. If one of the back legs is raising higher then the other, you can adjust this by raising or lowering the vertical linkage.

4. Next, move the servo arm so it is pointing to the right in the 3rd image. Now the back legs should be relatively straight and the front should be turned. You can change the amount of turn in the front legs by changing the length of the horizontal linkage

5. If you move the servo to the left, the opposite will happen to the front legs and they will face the other way. Have a look at the last 2 images which shows both left and right positions of the servo.

6. If you find that the front legs are turning more one way then the other, adjust this by changing the length of the horizontal linkage. Another trick is to slightly bend down the section of linkage around the back leg. This can help to even out the gait.

7. Keep fine tuning your walker until you can get both the front legs lifting around the same amount. You won't be able to get them exact but close enough will do.

8. Last thing to do is to let him start to explore his surroundings. Try putting some obstacles in his way and see if he can climb over them. You'll be surprised at what he manages to get over. He can even turn when he hits a wall by using one foot to turn himself.


---
*81 images archived*
