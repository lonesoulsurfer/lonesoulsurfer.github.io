# Build a Ray Gun With Sound Effects

Source: https://www.instructables.com/Build-a-Ray-Gun-With-Sound-Effects/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

![Intro 6](images/intro_06.jpg)


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

The main parts you'll need is the timing light and the sound FX circuit, all the details of the circuit are on the next step. Below are what I used to build the ray gunPARTS:1. Vintage timing light - eBay You can probably also find2. LED's - I used LED filaments - eBay3. Nose Cone - eBay4. There are a few other parts that I used which were pulled from other parts. For example, I used the tops of 2 electric razors for light diffusers. The barrel of the gun was some type of shaft that I pulled out of something. I'll go through all of this in step 5.5. Various small screws, nuts and bolts6. Potentiometer knobs - eBayPower SupplyYou could just use a 9v battery if you wanted to. However, I didn't want to have to open up the whole thing every time i wanted to change a battery so I added a way to recharge it.1. Li-Po battery. I like to use old mobile phone batteries. You can usually get them for free as well from e-waste centres or those mobile phone bins2. Buck booster - you need to increase the voltage from 4.3v to 9v - I used this one from Ali Express3. Micro USB charger module - eBay


## Step 1: The PCB & Getting It Printed

![Step 1: The PCB & Getting It Printed image 1](images/step03_01.jpg)

![Step 1: The PCB & Getting It Printed image 2](images/step03_02.jpg)

![Step 1: The PCB & Getting It Printed image 3](images/step03_03.jpg)

The circuit itself is a low frequency oscillator (LFO) based around a couple of CMOS IC's. The waveform is changed via the added pots and frequency switch. I have also added an LED because all ray guns need LED's! It's a pretty simple circuit as you can see from the attached schematic but you get get some great 'ray gun' sound effects from it.I designed the PCB to be as small as possible and to also have the potentiometers directly attached to the board so less wiring. I have used pin headers to connect everything else like like power, switch etc. You can use JST connectors on the pin headers if you want (which is what I did) to as well which makes it easy to connect to the pin headers on the PCBI have created a folder in my Google drive which can be found in the below link that has the schematic, PCB and Gerber filesGoogle Drive FilesIf you want to get your own board printed, then just save the gerber zip file in the Google Drive Files to your computer and email it to your favourite PCB manufacturer. I use JLCPCB (not affilated) who do a good job of printing the boards and are quick as well. If you are thinking 'what the hell is a gerber file!', then check this 'ible out which is a step by step guide on how to get a PCB printed.I've attached is a list of the components and you can find an excel version in the Google drive link too. I've also listed them below and added links to where you can buy them - you're welcome!PCB Parts ListCapacitor Polarized10uf X 34.7uf220ufnon-polarized100nf X 3Diode 1N4718Zener Diode 3.9vTransistor 2N3904IC's40934046386LED. I used 2 filament LED's but you can use normal 5mm LED's if you want tpFilament5mmSwitch SPDTPotentiometer20K X 250KResistor4.7K X 1470K X 22.2K X 13.3K X 1Header pins MaleJST Connector (Optional) Mini X 4Speaker 1W 8 OhmRay Gun Sound FX - Parts List.pdfDownload


## Step 2: Adding Components to the PCB

![Step 2: Adding Components to the PCB image 1](images/step04_01.jpg)

![Step 2: Adding Components to the PCB image 2](images/step04_02.jpg)

![Step 2: Adding Components to the PCB image 3](images/step04_03.jpg)

![Step 2: Adding Components to the PCB image 4](images/step04_04.jpg)

![Step 2: Adding Components to the PCB image 5](images/step04_05.jpg)

![Step 2: Adding Components to the PCB image 6](images/step04_06.jpg)

![Step 2: Adding Components to the PCB image 7](images/step04_07.jpg)

Now that you have your circuit board, it's time to add the components.  There actually isn't very many components to add , although it's a little tight on the PCBSTEPS:1. Start with the lowest profile parts first.  In this case it's the resistors and the diodes that need to be added first2.  Next I like to add the IC sockets.  They aren't necessary to add, you could just solder the IC's directly to the PCB.  However, you run the risk of potentially having a faulty IC and having to de-solder it3. Then solder on the pin headers and the rest of the components including the 3 potentiometers4. Once you have everything soldered, it's best to give the PCB a test to make sure everything works as it should.  I've made a bunch of these now and they have all worked first go so you shouldn't have any issues unless you have a bad solder joint or IC.5. So what does the PCB actually do?  Well, there is a speed control allowing you to change the speed of the sounds along with 2 tone pots, which allow you to change tones and pitch.  There is also a on/off/on toggle switch which also gives you more control over the sounds produced. Plus, you can add an LED to it and it will turn on when activated.


## Step 3: Vintage Timing Light

![Step 3: Vintage Timing Light image 1](images/step05_01.jpg)

![Step 3: Vintage Timing Light image 2](images/step05_02.jpg)

![Step 3: Vintage Timing Light image 3](images/step05_03.jpg)

One of the key parts to this build is finding yourself a vintage timing light.  These are used to tune your car back in the day (still used today as well but they are a little more modern looking).It's almost like the designers of these timing lights knew that someday someone would want to use them as ray guns.  They are pretty much perfect in the way that they look and feel.The one that I found must of had someone's name engraved in the handle and then someone scratched it out.  No real problem though as I will add some rubber grip to the handle to cover it up and for grip..  It'll also give the ray gun a nice looking handle.you can actually pick these up quiet easily.  Just type into eBay - vintage timing light and you should get a bunch of them.


## Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 1](images/step06_01.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 2](images/step06_02.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 3](images/step06_03.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 4](images/step06_04.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 5](images/step06_05.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 6](images/step06_06.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 7](images/step06_07.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 8](images/step06_08.jpg)

![Step 4: Roughing Out the Design of Your Ray Gun & Making the Nose Cone image 9](images/step06_09.jpg)

Before I start to tear into the ray gun and add parts to it, I first like to rough out the design.  This usually entails going through my parts bins, pulling out parts that I think would work with the ray gun and placing them on the timing light.As I have mentioned earlier, you could just use the timing light as is as and not worry about adding any additional parts except for the electronics.  However, that's a little boring so if you want to add greebles and nose cones and other parts, then you will need to start collecting interesting bit and pieces.  The good news is, the nose cone section you can buy so that wil give you a good start.  There is a link in the parts step.STEPS:1. Rummage through your parts bins and pull out parts that look like would work well on the ray gun, I started with the nose cone and barrel2. To make the barrel, I found an old part that fitted inside the end of the nose cone.  It had a thread at both ends which meant I could add a washer and nut and secure it inside the nose cone.3. To finish off the end, I added a small copper plumbing piece which I managed to screw onto the other end of the barrel section.  I like the idea that the end had to be a different material to the rest.  Maybe because it gets so hot from the laser beam being shot out of the ray gun...


## Step 5: Roughing Out the Design - Adding Some Greebles

![Step 5: Roughing Out the Design - Adding Some Greebles image 1](images/step07_01.jpg)

![Step 5: Roughing Out the Design - Adding Some Greebles image 2](images/step07_02.jpg)

![Step 5: Roughing Out the Design - Adding Some Greebles image 3](images/step07_03.jpg)

![Step 5: Roughing Out the Design - Adding Some Greebles image 4](images/step07_04.jpg)

I decided to go minimalist with the greebles on this build.  The more things I thought about adding, the more the ray gun was looking odd, like the parts didn't belong.  I decided to keep with the silver theme across the parts added as well.  The parts used in this step were from a couple of electric razors and also a large potentiometer.  The blade sections from the razor I used as as diffusers for LED's that were added as well.When deciding where to add the razor parts, I was restricted a little by a screw that is used to hold the body of the ray gun together.  After playing around with different ideas, I decided on the layout you can see in the last image


## Step 6: Adding a Greeble to the Body of the Ray Gun

![Step 6: Adding a Greeble to the Body of the Ray Gun image 1](images/step08_01.jpg)

![Step 6: Adding a Greeble to the Body of the Ray Gun image 2](images/step08_02.jpg)

![Step 6: Adding a Greeble to the Body of the Ray Gun image 3](images/step08_03.jpg)

![Step 6: Adding a Greeble to the Body of the Ray Gun image 4](images/step08_04.jpg)

This little part I believe came from an electric razor.  They are small arms and there was 2 of them which is perfect as it meant I could add one on either side of the ray gun.STEPS:1. First decide where you want to add the part to the ray gun.  In my case I added it near the middle of the ray gun.  I had to take into consideration that I wanted the blade from the electric razor sitting flush against it as well as the screw mount on the ray gun2. Next I drilled a couple of small holes in the ray gun which aligned with the holes in the part I used.  The holes were slightly smaller then the self tapping screws I used3. I then screwed the parts to the body of the ray gun using self tapping screws.  These worked a treat!


## Step 7: Adding the Circuit Board

![Step 7: Adding the Circuit Board image 1](images/step09_01.jpg)

![Step 7: Adding the Circuit Board image 2](images/step09_02.jpg)

![Step 7: Adding the Circuit Board image 3](images/step09_03.jpg)

![Step 7: Adding the Circuit Board image 4](images/step09_04.jpg)

![Step 7: Adding the Circuit Board image 5](images/step09_05.jpg)

![Step 7: Adding the Circuit Board image 6](images/step09_06.jpg)

Initially, I wanted to add the potentiometers so they came out the left side of the ray gun.  However, the pesky screw mount on the ray gun was in the ay again.  The next best place to add them was on the top which worked out really well.  The knobs had to be off-set to the centre but that was ok - it didn't flair up my OCD STEPS:1. The first thing to do is to make a masking tape template of the potentiometers so you can work out where to drill the holes into the ray gun.  Just place some masking take across the tops of the pots, mark the middle of each one on the tape and then place the tape onto the ray gun.2. Next, I drill out the holes and test fitted the PCB and pots.  I had to make the middle hole slightly larger in order for them to fit but that wasn't an issue.3. Once I placed the pots into place, I then secured them to the ray gun with some nuts.4. Lastly, I drilled another hole and added the toggle switch.  The switch allows you to change through different pitches.


## Step 8: Modifying the Momentary Switch

![Step 8: Modifying the Momentary Switch image 1](images/step10_01.jpg)

![Step 8: Modifying the Momentary Switch image 2](images/step10_02.jpg)

![Step 8: Modifying the Momentary Switch image 3](images/step10_03.jpg)

![Step 8: Modifying the Momentary Switch image 4](images/step10_04.jpg)

![Step 8: Modifying the Momentary Switch image 5](images/step10_05.jpg)

![Step 8: Modifying the Momentary Switch image 6](images/step10_06.jpg)

![Step 8: Modifying the Momentary Switch image 7](images/step10_07.jpg)

![Step 8: Modifying the Momentary Switch image 8](images/step10_08.jpg)

![Step 8: Modifying the Momentary Switch image 9](images/step10_09.jpg)

To activate the ray gun sounds, you need to include a momentary switch.  The timing light should already have one included and if you are lucky, with a little modification, you should be able to utilize this switch like I did.STEPS:1. Ok - so you might of noticed that this step includes pulling the inside out of the ray gun.  I guess this should have been the previous step but I reckon it works better here so that's where I'm going to keep it...2. Pull out the insides of the timing light3. Cut off all of the components from the circuit board, just leaving the momentary switch4. Trim down the circuit board so you can utilize any mounting holes in the circuit board.  I was lucky to have 2 mounting holes on either end of the circuit board which allowed e to trim off most of the board.5. Secure the circuit board back into the ray gun and test to make sure it all works ok and the switch is activated when the trigger is pulled.


## Step 9: Adding Some LED's and Diffusers

![Step 9: Adding Some LED's and Diffusers image 1](images/step11_01.jpg)

![Step 9: Adding Some LED's and Diffusers image 2](images/step11_02.jpg)

![Step 9: Adding Some LED's and Diffusers image 3](images/step11_03.jpg)

![Step 9: Adding Some LED's and Diffusers image 4](images/step11_04.jpg)

![Step 9: Adding Some LED's and Diffusers image 5](images/step11_05.jpg)

![Step 9: Adding Some LED's and Diffusers image 6](images/step11_06.jpg)

![Step 9: Adding Some LED's and Diffusers image 7](images/step11_07.jpg)

![Step 9: Adding Some LED's and Diffusers image 8](images/step11_08.jpg)

I decided to add 2 filament LED's, one on each side of the ray gun.  The light would be diffused by the electric razor bladesSTEPS:1. First I soldered wires to each end of the LED's and added some heat shrink to ensure they don't short on the body of the ray gun2. Next, I drilled a couple holes into the ray gun to allow the wires to be threaded through.3. To hold the wires into place I added a couple pieces of fabric tape to the inside.4. As there is only one LED connection point on the ray gun, I had to connect both positives and grounds from the LED's to the one connection.  I also tested the LED's to make sure that they worked before moving onto the next step.  The filaments are quite fragile so be careful with them when putting them into place.5. Lastly, I added some superglue to the bottom sections of the razor blades and carefully glued them over the LED's.  This is the only time I used superglue to attach a part to the ray gun.


## Step 10: Adding Power

![Step 10: Adding Power image 1](images/step12_01.jpg)

![Step 10: Adding Power image 2](images/step12_02.jpg)

![Step 10: Adding Power image 3](images/step12_03.jpg)

![Step 10: Adding Power image 4](images/step12_04.jpg)

![Step 10: Adding Power image 5](images/step12_05.jpg)

![Step 10: Adding Power image 6](images/step12_06.jpg)

![Step 10: Adding Power image 7](images/step12_07.jpg)

![Step 10: Adding Power image 8](images/step12_08.jpg)

You could always just add a 9v battery to power everything if you wanted to.  However, I didn't want to have to open the ray gun up each time I need to change the battery so added a rechargeable battery instead.  I like to re-use mobile phone batteries as they work really well in projects like this.STEPS:1. First, I needed to increase the power from 4.3V to 9V.  To do this I added a small buck booster module to the battery and connected the battery to the positive and ground points on the module.  I added a little bit of superglue and glued it directly onto the battery2. Next I connected the output on the module to the momentary switch connection on the circuit board3. To be able to re-charge the battery I needed to add a charging module.  This is connected to the some solder points on the buck booster as the battery is.  There was even a small cutout on the handle that worked perfectly as a space for the micro USB on the charging module!  I was very lucky with this build as I didn't have to mod the timing light at all!  very rare in a build like this


## Step 11: Adding the Nose Cone

![Step 11: Adding the Nose Cone image 1](images/step13_01.jpg)

![Step 11: Adding the Nose Cone image 2](images/step13_02.jpg)

I was pretty lucky when it came to connecting a lot of the parts to the timing light as most fitted without having to do too much modding.  The nose cone especially was very simple to add to the timing lightSTEPS:Inside the timing light there was a large lens which was held in place via a couple of grooves.  I was able to utilize these to secure the nose cone into placeTo ensure it wouldn't move around, I added a couple of large washers and used these as spacers to clamp the nose cone into place.You can see in the images that I cut one in half which helped secure the nose cone betterand that's all I had to do to secure the nose cone into place!  Simple.


## Step 12: Adding a Speaker, Testing and Closing Up the Ray Gun

![Step 12: Adding a Speaker, Testing and Closing Up the Ray Gun image 1](images/step14_01.jpg)

![Step 12: Adding a Speaker, Testing and Closing Up the Ray Gun image 2](images/step14_02.jpg)

![Step 12: Adding a Speaker, Testing and Closing Up the Ray Gun image 3](images/step14_03.jpg)

![Step 12: Adding a Speaker, Testing and Closing Up the Ray Gun image 4](images/step14_04.jpg)

Finally - getting near the end!  Still need to add some grip to the handle but all of the insides are just about done.STEPS:1. Connect a JST connector wires to the speaker positive and ground.2. Next, attached the connector to the speaker pin header on the circuit board3. Once everything is connected and looks right, give the trigger a pull and see what happens!  The LED's should come on and you should hear the ray gun sound effects kick in.  Try turning the pots and see what happens.  If the tone and or speed changes then you know that the pots work.  Give the switch a go and if that works as well then you are good to close up the ray gun.  If something doesn't work you'll need to do some troubleshooting to identify the problem.NOTE: I found that the speaker was very loud.  To reduce the sound, I added a 20R resister to the positive solder point on the speaker to help reduce the volume.  Up to you if you want to do this or not - you might want it loud and noisy.


## Step 13: Adding the Hand Grip

![Step 13: Adding the Hand Grip image 1](images/step15_01.jpg)

![Step 13: Adding the Hand Grip image 2](images/step15_02.jpg)

![Step 13: Adding the Hand Grip image 3](images/step15_03.jpg)

![Step 13: Adding the Hand Grip image 4](images/step15_04.jpg)

For the handgrips I used some sticky sided rubber grips for steps.  STEPS:First, place the rubber grip, white side up and trace around the handle of the gun.  This will give you a rough template for the handleNext, cut out the rubber grip and place it onto the handle.  If you need to trim then further, mark the area's and trim until they fit onto the handlePeal off the back paper from the rubber grip and stick into place.  Push down hard on the rubber so it is stuck into place


## Step 14: Making a Display Stand

![Step 14: Making a Display Stand image 1](images/step16_01.jpg)

![Step 14: Making a Display Stand image 2](images/step16_02.jpg)

![Step 14: Making a Display Stand image 3](images/step16_03.jpg)

Now that you have made your ray gun, you'll definitely want to put it on display.  It can be a little tricky working out the best way to get the gun to stand, however, most of the timing lights will have a hole in the bottom of the handle where the power cord was so you can utilize this to get your ray gun to standSTEPS:First I used a piece of wood as a stand and rounded off the sides with a routerI then placed the gun on the wood to work out where best to position itTo enable to gun to mount I added a bolt into the bottom of the wood which stick out the top.  The hole in the handle then can be used to mount the ray gun via the bolt in the wood.If it is a bit wobbly, you might need to add a support for the front of the ray gun such as a piece of aluminum tube.    The tube can be secured to the base and cut so the 'barrel' of the ray gun sits on it.


---
*89 images archived*
