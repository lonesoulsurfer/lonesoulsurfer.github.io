# Drum Synth (DS-8) With PS2 Drum Pad

Source: https://www.instructables.com/Drum-Synth-DS-8-With-PS2-Drum-Pad/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

I first come across the DS-8 Drum synth whist searching for a drum circuit I could build. There isn't a lot out there and this particular one caught my attention.

It was originally designed by Coron in the 1980’s for drummers and percussionists to add synth capabilities to their sets. My circuit is based on the Synthrotek schematic which has a few added modifications to the original to expand on it's sound.

You can also use it as a awesome dub siren with the momentary switch included on the board.

The below is taken directly from the Synthrotek website and explains exactly why this is such a versatile and fun to play with synth:

- Amazing analog signal generation! – Wobbly lows, screeching sirens, dive bombs, squeals, and everything in-between. On-board pannable white noise generator puts out snare and hi-hat hits!

- Three different ways to play: use a piezo cell to trigger it like a real drum, send a Trigger/Gate pulse (~+5V) from a sequencer/simple timer circuit, or activate the DS-8 Clone with the on-board Manual Trigger momentary switch!

- Multiple controls to tailor your sound! Sensitivity sets your input threshold to adjust how hard you need to hit or the minimum voltage level to trigger the circuit. The length of the trigger pulse can be varied from staccato to a lengthy drop-off with the Decay control. Sweep adjusts the variation of the output frequency. The analog LFO (low frequency oscillator) circuitry is controlled by the Mode and Rate. VCO (voltage controlled oscillator) sets a base level frequency to limit your frequency range. Dirty up your signal with the Pan control, which varies the amount of white noise you’ll need for snare hits or deep tom rumble. Level controls the volume of the final VCA (voltage controlled amplifier) portion of your circuit.

As the board is no longer available to buy so I designed and printed my own and have provided the gerber files. All you need to do is to send them to a PCB manufacturer and get your own printed.

I also decided to start to design my own front panels. To do this I downloaded Inkscape and taught myself how to use it. It's actually a lot easier then I thought it would be and I will share some tips on how you can also do your own. I've also provided the panel image as well so if you can't be bothered, then just use mine.


## Step 1: DS-8 Drum Synth - Parts List

![Step 1: DS-8 Drum Synth - Parts List image 1](images/step01_01.jpg)

I've broken up the parts list so it's a little easier to read. First let's go through what you'll need for the DS-8

You can find the gerber files for the board in my Google drive [here](https://drive.google.com/drive/folders/1_UcQMlpJbc68a_Bw1BfDyM5o3cCno9F7?usp=sharing). I have also provided the schematic in the same folder along with a complete parts list. The schematic, and board were designed in Eagle so knock yourself out and have a play with it.

Parts

1. I have added the parts in the attached PDF. You can also find an excel spreadsheet in the Google drive link above.

2. All resistors are 1%

3. The non-polarized capacitors are either polypropylene film type or polyester type. There is a 22p which is a ceramic

Board

1. The board I initially designed so the pots could be soldered directly onto it. You can still do this if you want to but I decided to wire them all up. It's a bit of a pain but It allowed me to design the front panel the way I wanted it.

2. Next to each Pot section on the board there is a "F" or "B" next to it. That means the pot is either solder to the top of the board of the bottom. I did this to allow more space between the pots.


- [DS-8 Parts List](pdfs/DS-8 Parts List.pdf)

## Step 2: All the Other Parts

![Step 2: All the Other Parts image 1](images/step02_01.jpg)

![Step 2: All the Other Parts image 2](images/step02_02.jpg)

![Step 2: All the Other Parts image 3](images/step02_03.jpg)

![Step 2: All the Other Parts image 4](images/step02_04.jpg)

![Step 2: All the Other Parts image 5](images/step02_05.jpg)

![Step 2: All the Other Parts image 6](images/step02_06.jpg)

![Step 2: All the Other Parts image 7](images/step02_07.jpg)

Parts - Electrical

1. Reverb/Echo Board - eBay

2. Wire. I used jumper wires - [eBay](https://www.ebay.com.au/itm/40-Pcs-Jumper-Wire-M-M-M-F-F-F-Cable-Pi-Pic-Breadboard-For-Arduino-B-zh/383702151622?hash=item59566e31c6:g:ZWAAAOSwFnFV94L0&frcectupt=true)

3. 2 X SPDT switches - [Ali Express](https://www.aliexpress.com/item/4000177976189.html?spm=a2g0s.9042311.0.0.37f24c4dRe7FMz)

4. Momentary Switch - [Ali Express](https://www.aliexpress.com/item/32976478577.html?spm=a2g0o.productlist.0.0.48c22095XdJxLW&algo_pvid=748f0502-749a-4a24-9a02-fdc720055543&algo_expid=748f0502-749a-4a24-9a02-fdc720055543-44&btsid=0bb0623d16040389935037808ebb2e&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_)

5. Battery. I used a mobile phone battery -[eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2060353.m570.l1313&_nkw=mobile+battery+samsung&_sacat=0)

6. Charging and voltage regulator module - [Ali Express](https://www.aliexpress.com/item/32950938641.html?spm=a2g0s.9042311.0.0.27424c4d8pVLHn)

7. Micro USB Module - [eBay](https://www.ebay.com.au/itm/FT-5Pcs-CJMCU-5V-Micro-USB-Board-Interface-Power-Switch-Adapter-Breakout-Module/324108091584?hash=item4b765900c0:g:dH0AAOSwK~tdoXXg)

8. 4 X Audio sockets - [eBay](https://www.ebay.com.au/itm/Lovoski-Black-3-Pin-3-5mm-Female-Audio-Mono-Headphone-Jacks-Socket-10Pcs/183171615145?_trkparms=ispr%3D1&hash=item2aa5e109a9:g:OnEAAOSw2PtazA-5&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickk8Fd9si%252FIbtWQr%252BhnlRwjDXvWNoBDIgZ3ecAzZ3e%252Fck5rX0gYjICre5FLjXCWjdb0B75pm0cRbPwPIac9Zwwt1c5wUs0gxx10MrWOhWOqmdeyzhHG0pAemQriD3gBdeNggHwfVOFHHBXDF3AQ5mj1LE75lVsrAgINTTL%252FPeCrj99lUmXsD1JarMNzQ0TIuJftHykvJwb%252BpaHq8wtnvLz9tLKJw92n9U3W3NavbmyQxInLrGJsVYDBEPQQuiGtjxUZmlhp5GO28TSTtH1OfiWNLPQNKuSEWIXmQuKh4Y8P%252Bi%252B9X2lne%252BEU21HzpfCqlKGOecNJg1Ol2snfzzWoqVmRvnrWT5pGa3WTUYC2ptdzqtZeJ161nzydorXRhpJlPGZx8NUXPLJdEQaUT5w2%252BdthbC%252FpRwoQF0EYL0nTPTK14cb40iUSkGUdz8lAtyTJ1kaYfpuoWZMHJ3kHZHf4OWB5fJkyApWiLoLB94At0ptb04CuGtdPQvC1WuLHZMtKSSDJhLIQos5SqZjFwJwsIr0gRr41M1IDvI0gStuBMlEoBwOlbQ5oKo5axYPB4Ob%252BSsD4CV8QY%252Fizas2IlKg8qeML2Mu5hx3GhHPHiymoH3t19oaiTWyhY3Y01ccAWKr29HvtlEwmOgNJfs8bfUG59TZzu4iGerpgY%252FY6oMV21lwveo%252F3MR8G0iTHS4wNyUhXCln5JQ5qnQJQ3xeG%252BqTJXyH7s37AffwIbQvf0n1fzxIuoF4OVFMce%252FwPShxaX7kdC6aWGGAjDisJyRRXqvdYXstwug%253D%253D%7Ccksum%3A1831716151455d439cd1d0554ebcbba9006435e81490%7Campid%3APL_CLK%7Cclp%3A2334524)

9. Male right angle header pins - [eBay](https://www.ebay.com.au/itm/10pcs-Right-Angle-40-pin-2-54mm-Male-Header-for-Breadboard-1x40-Single-Row/392287448510?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2060353.m2749.l2649)

Other Parts

1. PS2 Drum set. You don't have to use one of these, you could just make your own

2. Hardwood edging 40mm x 8mm - your local hardware store will have this. You'll need about a meter length.

3. Ply wood for base - Hardware store

4. Water Decal - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=water+decal+a4&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=water+decal)

5. Opal Acrylic - [eBay](https://www.ebay.com.au/itm/Coloured-Perspex-Acrylic-Sheets-Cut-Panels-Free-Tracked-Shipping/221974331742?_trkparms=ispr%3D1&hash=item33aeb3815e:g:AGcAAOSwvmNa~SjK&amdata=enc%3AAQAFAAACcBaobrjLl8XobRIiIML1V4Imu%252Fn%252BzU5L90Z278x5ickkgCVySCgrNFPU8Iu85TabMMqb%252FzFiWrwNQbas1nj5sgePqtHbGIEESoeITQLLMNzCetHWJg9rbFSfKJKUxztvLNkzfEBQBfUxWbaXSmzHXZ1Kda9i0ZZDonqVWQ3aEmgM2lFl3vVF7P9FoVN5ofBWjSrYET7lCoGbq0YWgfDsz6ydQSM0ZmzvBWnGYymiP59y72QcD8VTzc4o%252BHDWhAqjvTq2%252FusGlzTCMO7%252FSY0cyfpSYOhTxuC9x7wWAU5m1l7b5%252B1yTxtisqCGEj1QG1LS1kcKt6aZYrUWusIkTqRgIf%252FZarv5lTxIyfvUntZXmEZvaWn%252F2jQQB8d3HJJgvqpaurqIBegIapw664aXhhwVlAzctjqgoQRf1GMl%252FRbXSuAzO%252BuOp1Jw%252BjY5pgO2Ycvjp4GUdboAV%252BfguDK61j2KF2ymdCiG9c6JHotUL9KJ5oZHFQ554Lr1RvKmVzAZQI6UyywqNALIjLaU%252FhFAA%252FedJHBuOTiEZQBScjHLz8Ml%252Ftc52TmqxdY6jdSbOeCFCdD%252FprGKxaYo2Tf%252B0Feylx53AfIzNaQ11qJFzzjHf9LDzqaqHxlbyfztGCZaCPqsPSNyUIr3njnv70E4J7v66jRsf0TsIRF0SU8FbuvdJHtDG45nW%252BFtVdh7vkdBBP691pzPa8yGjp5oAoElwkf%252BOrUMBqGp79yitbeuLVAf%252BeCZG0hZoTGl9u2DVMmuYujYhERsMmMPvqiTNZS86W2V6Hyb3QGt9k4UTr3iCO2IJlY2T9eSxEC0oiIqQlJHRE%252FJ%252Flx62w%253D%253D%7Ccksum%3A2219743317426961b26d0c8e4f60b0f8292504c255ef%7Campid%3APL_CLK%7Cclp%3A2334524&frcectupt=true)

6. Pot knobs - [Ali Express](https://www.aliexpress.com/item/32954107409.html?spm=a2g0s.9042311.0.0.37f24c4dRe7FMz)


## Step 3: Schematic, Board and Gerber Files

![Step 3: Schematic, Board and Gerber Files image 1](images/step03_01.jpg)

![Step 3: Schematic, Board and Gerber Files image 2](images/step03_02.jpg)

Here's the link to my Google drive with all of the files. Included is the parts list, Eagle schematic and board along with the Gerber files. The gerber zip folder can be sent to a PCB manufacturer and they will print the board up for you


- [DS8 - Pots Soldered on Board](pdfs/DS8 - Pots Soldered on Board.pdf)

## Step 4: DS-8 Board - Soldering on the Components

![Step 4: DS-8 Board - Soldering on the Components image 1](images/step04_01.jpg)

![Step 4: DS-8 Board - Soldering on the Components image 2](images/step04_02.jpg)

![Step 4: DS-8 Board - Soldering on the Components image 3](images/step04_03.jpg)

![Step 4: DS-8 Board - Soldering on the Components image 4](images/step04_04.jpg)

![Step 4: DS-8 Board - Soldering on the Components image 5](images/step04_05.jpg)

![Step 4: DS-8 Board - Soldering on the Components image 6](images/step04_06.jpg)

![Step 4: DS-8 Board - Soldering on the Components image 7](images/step04_07.jpg)

There's no two ways about it, you are going to have to do a lot of soldering. I actually find it quite relaxing so grab yourself a drink, get the soldering iron hot and prepare to solder.

I've soldered a few of these together now and I can definitely confirm that the board works. If you build the board and have an issue, then you'll need to troubleshoot to try and find where the issues lies.

Steps:

1. I always start with the resistors. You can put several in at a time and soldered them to the board. It also means that the board will sit flat whist you are soldering which makes things easy. Take your time, check your values and solder joints and make sure you don't miss any.

2. Next I usually start with the IC sockets. They are pretty low as well

3. Then it's just a matter of working through the rest of the parts. I know this is self evident but always double check the polarity of the caps and take your time to ensure you are putting the right parts in the right spot.

4. You'll notice that I also soldering on the pots to the board. Well I had to de-solder these in the end as I wanted to have a different layout then I planned on. You could easily use the board though in a eurorack as a module if you wanted to with the pot design I did.

5. Lastly, I designed the board to fit 9mm pots. However, it seems that it's very hard to get 1M 9mm and impossible to get 2M ones. Just another reason why I also decided not to mount the pots onto the board.

6. Once you have done, give it a test to make sure everything works. It does, good!


## Step 5: PS2 Drum Set - Removing a Drum

![Step 5: PS2 Drum Set - Removing a Drum image 1](images/step05_01.jpg)

![Step 5: PS2 Drum Set - Removing a Drum image 2](images/step05_02.jpg)

![Step 5: PS2 Drum Set - Removing a Drum image 3](images/step05_03.jpg)

![Step 5: PS2 Drum Set - Removing a Drum image 4](images/step05_04.jpg)

![Step 5: PS2 Drum Set - Removing a Drum image 5](images/step05_05.jpg)

The first thing you'll need to do is to remove one of the 4 drums from the PS2 drum set. I'm going to use the other 3 in a mega DS-8 project at some stage so I made sure i didn't damage it when I removed one of the pads

Steps:

1. The 2 end drums are connected by a plastic joiner You'll first need to cut through this with an angle grinder or something similar

2. make sure that you leave more of the plastic joiner section on the drum that you are using for the DS-8. You can use this section later to attach the synth to

3. Once you have made the cut you'll then need to clean it up. I used a file and a exacto knife to do this. I also used a belt sander to straighten up the cuts and make it flush. This will allow me to put the case of the synth against it and connect via a couple of screws.


## Step 6: PS2 Drum Set - Opening It Up

![Step 6: PS2 Drum Set - Opening It Up image 1](images/step06_01.jpg)

![Step 6: PS2 Drum Set - Opening It Up image 2](images/step06_02.jpg)

![Step 6: PS2 Drum Set - Opening It Up image 3](images/step06_03.jpg)

![Step 6: PS2 Drum Set - Opening It Up image 4](images/step06_04.jpg)

wouldn't usually add a whole step on how to pull apart something but the drum isn't easy to pull apart. Correction, it is easy to pull apart, I just couldn't work out how to do it. I did a couple of searches and worked it out but you won't have to because of this step.

Steps:

1. The first thing you need to do is to pull off the drum head. To do this just put your hand under the drum head and lift up.

2. The head is held into place by 4 rubber stoppers. If you add some pressure they will pop out of the brackets they are held in place with. Move your hand around the drum head after each one is released - there are 4 in total.

3. Once they are off, you then need to remove the top plate which is the section with the foam attached. Initially I couldn't work out how until I saw a screw poking it's head out from behind one of the foam pads.

4. Lift up the end of the foam and you'll see a screw. There are 4 in total which need to be removed. Once these are taken out you can remove the top plate. That's all you need to do to take the drums apart and get to the wiring.


## Step 7: PS2 Drum Set - Wiring and Modding

![Step 7: PS2 Drum Set - Wiring and Modding image 1](images/step07_01.jpg)

![Step 7: PS2 Drum Set - Wiring and Modding image 2](images/step07_02.jpg)

![Step 7: PS2 Drum Set - Wiring and Modding image 3](images/step07_03.jpg)

![Step 7: PS2 Drum Set - Wiring and Modding image 4](images/step07_04.jpg)

![Step 7: PS2 Drum Set - Wiring and Modding image 5](images/step07_05.jpg)

![Step 7: PS2 Drum Set - Wiring and Modding image 6](images/step07_06.jpg)

I guess I should have told you why you need to do this! Well the aim is to use the piezo electric speakers inside as a trigger for each of the drum circuits. This will allow you to play the drums with the synth!

Steps:

1. Inside each of the drums is a piezo which is wired up to a small circuit board. Remove the black plastic part that is holding the piezo in place

2. Un-screw the small circuit board which the wires from the piezo are connected to. The board is just a jumper board and you'll be able to connect wires to it easily

3. You should now be able to remove the piezo and board away from the drum set.

4. You now need to extend the wires on the jumper board. These will be connected a little later to an 3.5mm audio sockets. de-solder the old ones and add some new, longer wires to each of them.

5. You can now put these aside and start to add the audio sockets to each of the drums. The sockets will allow you to connect the trigger output from the drum circuit directly to each drum


## Step 8: PS2 Drum Set - Adding an Audio Socket

![Step 8: PS2 Drum Set - Adding an Audio Socket image 1](images/step08_01.jpg)

![Step 8: PS2 Drum Set - Adding an Audio Socket image 2](images/step08_02.jpg)

![Step 8: PS2 Drum Set - Adding an Audio Socket image 3](images/step08_03.jpg)

![Step 8: PS2 Drum Set - Adding an Audio Socket image 4](images/step08_04.jpg)

The last thing you need to do before closing up the drum is to add 3.5mm mono jack sockets to the body of the drums. This will allow you to connect the piezo to the trigger on the drum synth .

Steps:

1. Find a good location on the front of the drum to add the socket.

2. You may have to remove a little of the plastic on the top plate in order to secure the socket into the side of the drum. I used a demel to do this.

3. Next, drill a hole into the side of the drum and secure the socket into place

4. Solder the wires from the piezo to the socket solder points. There is no issues with polarity, just make sure you solder one wire to the tip and the other to the sleeve solder points on the socket

5. Do the same for the other 3 drums and then close everything up 6. That is pretty much it for the drum mod. You will now be able to use the pads with the DS 8 drum synth


## Step 9: Designing the Front Panel

![Step 9: Designing the Front Panel image 1](images/step09_01.jpg)

To design the panels I used [Inkscape](https://inkscape.org/), a vector graphics editor which you can download for free! I've only been playing around with it for a few weeks and found it easy to pick up. There's a lot of information available on how to use it and I would suggest you do a couple of the basic tutorials to familiarize yourself with the different features.

I did a couple video's on how to design knob scales and also make a front panel which I have included above.

There is even an extension that you can download so you can design knob scales easily and simply which you can [download here](https://inkscape.org/~sincoon/%E2%98%85knob-scale-generator)

However, if you don't want to bother learning how to design your own, you can always just use mine which I have attached as a PDF. I have also includes the Inkscape file so you can play around with that as well if you want to.


- [DS1 Drum Synth - Single Drum V3](pdfs/DS1 Drum Synth - Single Drum V3.pdf)

## Step 10: Drilling and Adding the Water Decal

![Step 10: Drilling and Adding the Water Decal image 1](images/step10_01.jpg)

![Step 10: Drilling and Adding the Water Decal image 2](images/step10_02.jpg)

![Step 10: Drilling and Adding the Water Decal image 3](images/step10_03.jpg)

![Step 10: Drilling and Adding the Water Decal image 4](images/step10_04.jpg)

![Step 10: Drilling and Adding the Water Decal image 5](images/step10_05.jpg)

![Step 10: Drilling and Adding the Water Decal image 6](images/step10_06.jpg)

![Step 10: Drilling and Adding the Water Decal image 7](images/step10_07.jpg)

![Step 10: Drilling and Adding the Water Decal image 8](images/step10_08.jpg)

![Step 10: Drilling and Adding the Water Decal image 9](images/step10_09.jpg)

This was my first time using water decals and it's trickier than I thought it would be. The decals are very fragile and it took 3 goes before I ended up with one I could use. As they say - practice makes perfect so I'm sure it'll get easier (famous last words!).

Also, next time I'm not going to pre drill as it's quite hard to line up the decal to the holes.

Steps:

1. Once you have your design you should print a few copies of it on normal A4 paper. This will allow you to use it as a template for drilling the holes

2. Next, print the panel directly onto the decal paper and leave to dry for 30 minutes

3. Spray some clear acrylic onto the decal, leave to dry and repeat

4. Cut the acrylic panel to the right size and tape the design to it. Make sure that it is as straight as possible and give yourself extra acrylic - you can always trim it later

5. Mark all of the sections with a punch that need to be drilled.

6. Drill out the holes to the right size using a stepped drill piece.

7. Remove the protective paper on the acrylic and cut out the decal

8. Place the decal into some warm water and once it start to lift off, carefully slide it onto the acrylic, ensuring everything is lined up right. Sounds easier than it is. I had to do this a few times to get it right.

9. Remove any excess water with a paper towel and leave to dry

10. Lastly, spray it again a couple of times with the acrylic to ensure it is protected


## Step 11: Adding the Components to the Front Panel

![Step 11: Adding the Components to the Front Panel image 1](images/step11_01.jpg)

![Step 11: Adding the Components to the Front Panel image 2](images/step11_02.jpg)

![Step 11: Adding the Components to the Front Panel image 3](images/step11_03.jpg)

![Step 11: Adding the Components to the Front Panel image 4](images/step11_04.jpg)

![Step 11: Adding the Components to the Front Panel image 5](images/step11_05.jpg)

![Step 11: Adding the Components to the Front Panel image 6](images/step11_06.jpg)

Before you add any of the components, you'll need to cut away the decal around the drilled holes

Steps:

1. With an exacto knife, remove any excess decal around the drilled holes

2. probably a good idea to give it another hit with the clear acrylic as well.

3. Start to add the pot's switches, audio jacks etc, being careful not to over tighten and damage the decal

4. I decided top use jumper wires so I could attach them easily to the board via a female jumper. I cut off the male section and soldered these to each of the components


## Step 12: Making the Case

![Step 12: Making the Case image 1](images/step12_01.jpg)

![Step 12: Making the Case image 2](images/step12_02.jpg)

![Step 12: Making the Case image 3](images/step12_03.jpg)

![Step 12: Making the Case image 4](images/step12_04.jpg)

![Step 12: Making the Case image 5](images/step12_05.jpg)

![Step 12: Making the Case image 6](images/step12_06.jpg)

![Step 12: Making the Case image 7](images/step12_07.jpg)

![Step 12: Making the Case image 8](images/step12_08.jpg)

![Step 12: Making the Case image 9](images/step12_09.jpg)

I used some strips of hardwood to make the case. It's used for edging and can be brought at any hardware store.

Steps:

1. The first thing you need to do is to cut a groove along the wood in order to secure the panel into. I use a dremel with a router attachment to do this.

2. Secure the wood with some clamps and run the bit near the top of the wood. Take your time and make sure you keep the dremel straight.

3. Measure and cut the wood to size.

4. Before you secure the front panel into the case, paint the top section and inside. When the panels in place it will make it hard to do and you might get paint on the panel. I used Aged Teak stain to give the wood a nice vintage feel. You could also just use a clear varnish and bring up the nice grain in the wood. The reason why you don't paint it all is you need to sand the wood once the case is complete.

5. Place the panle into the grooves of the wood and use some PVC to glue it together. Clamp and leave to dry for 12 hours


## Step 13: Moding the Echo/Reverb Module

![Step 13: Moding the Echo/Reverb Module image 1](images/step13_01.jpg)

I did an Instructable on how to mod the echo and reverb module which can be found [here](https://www.instructables.com/Echo-Reverb-Box/). It's not really a mod per se, more just now to had the echo pot and what resistor to remove. I won't go through this in much detail here so if you need further instructions, check out the 'ible above.

Steps:

1. First you'll need to remove one of the SMD resistors (R27). I do this with an exacto knife

2. Next you'll need to remove the pot that is soldered to the board. If you have a de-soldering device then use this as the traces have a tendency to lift if you just add a soldering iron to it. If you don't then use a pair of wire cutters and just cut it away

3. Solder wires to the pot solder points. There are also solder points for the echo pot as well so add wires to these too.

4. That's all you need to do for the moment. later on you will need to connect the wires p to the each and reverb pots.


## Step 14: Adding the Circuits and Battery to the Back Panel

![Step 14: Adding the Circuits and Battery to the Back Panel image 1](images/step14_01.jpg)

![Step 14: Adding the Circuits and Battery to the Back Panel image 2](images/step14_02.jpg)

The next thing to do is to add the battery and circuit boards to the back of the panel.

Steps:

1. lay all of the parts onto the back panel and work out the best place to locate them. For example, if you add the micro USB charging module at the top, then make sure that you locate the battery at the top as well.

2. Once you are happy with the layout, use some good, double sided tape and stick everything down. The great thing about using tape is it's easy to pull off the parts from the back of the wood if you need to. You could also screw down the boards later if you wanted to once everything has been tested


## Step 15: Adding the Drum to the Side of the Wood Case and Adding the Micro USB

![Step 15: Adding the Drum to the Side of the Wood Case and Adding the Micro USB image 1](images/step15_01.jpg)

![Step 15: Adding the Drum to the Side of the Wood Case and Adding the Micro USB image 2](images/step15_02.jpg)

![Step 15: Adding the Drum to the Side of the Wood Case and Adding the Micro USB image 3](images/step15_03.jpg)

![Step 15: Adding the Drum to the Side of the Wood Case and Adding the Micro USB image 4](images/step15_04.jpg)

You don't have to this but I wanted to have a complete unit. As there is a trigger socket, you could just plug in the drum and be done with it.

Steps:

1. Drill a couple holes into the side of the drum. There is a perfect spot where it was cut off from the rest of the drums to do this.

2. Place the drum and DS 8 case next to each other on a flat surface. Make sure you also include the base to the bottom of the case so you include the height of it when aligning the drum and case.

3. Mark on the case where the holes in the drum are and drill them.

4. I used a couple on screws and nuts to secure the drum to the case.

5. You'll need to also have a way to charge the battery. I used a micro USB module to do this and just filed a section away from the bottom of the case.

6. To secure in place , add a little superglue. It will later be connect to the charging module


## Step 16: Connecting the Wires Up to the Circuit Boards

![Step 16: Connecting the Wires Up to the Circuit Boards image 1](images/step16_01.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 2](images/step16_02.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 3](images/step16_03.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 4](images/step16_04.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 5](images/step16_05.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 6](images/step16_06.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 7](images/step16_07.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 8](images/step16_08.jpg)

![Step 16: Connecting the Wires Up to the Circuit Boards image 9](images/step16_09.jpg)

Home stretch now.

Steps:

1. Lay the top and bottom sections of the case next to each to each other.

2. First thing you should do is complete an soldering that needs to be done. Solder the wires from the echo/reverb module to the relevant pots on the front panel

3. Next, stick the battery charger and voltage regulator module on top of the battery. If you want more details on how to use this module then I've done an Instructable on this as well which can be found [here](https://www.instructables.com/Reuse-Old-Mobile-Phone-Batteries/). Wire-up the battery to the module and connect to the on/off switch. Also set the voltage to 9V on the module.

4. You'll also need to add a couple wires from the echo/reverb module to the output on the charging module to power it.

5. Solder any wires needed to the switches as well

6. Once all of the soldering is done, you can start to connect the pots up to the DS 8 board. This should be quite simple if you used jumper cables, just plug them into the pin headers.

7. Test to make sure everything is working as it should before closing it up.

TIP - if you find that the echo/reverb isn't working, disconnect it from the battery and connect it again. Sometimes they need resetting before they will work


## Step 17: Time to Play It

![Step 17: Time to Play It image 1](images/step17_01.jpg)

![Step 17: Time to Play It image 2](images/step17_02.jpg)

Ok so hopfully you didnt have any issues and everything worked first go. That never happens to me and esp with a big project like this, something is bound to go wrong somewhere. I had a wrong value cap which was throwing off the rate which I had to replace. My board is version 2 (version 3 is the one that I have linked to) which didn't have the momentary switch so I had to bodge that in as well. Also in version 3 I have included a 5V out so you can connect this to LED's or other components such as the momentary switch I used which had an LED inside.

There isn't any set rules on how to play the DS-8. However, I have grouped the parts on the panel which are related to each other. For example, the pan and noise switch are cose together and so is the mode and rate pots. Play around with different sounds, you should be able to get a sbare sound and bass drum as well as a whole lot inbetween.

Next I want to use the other 3 drums to make a 3 drum pad DS-8 synth! This build was a perfect lead in to the larger build.

If you have any questions, please add them to the comments and I'll help where I can


## Downloads

- [DS-8 Parts List](pdfs/DS-8 Parts List.pdf)
- [DS8 - Pots Soldered on Board](pdfs/DS8 - Pots Soldered on Board.pdf)
- [DS1 Drum Synth - Single Drum V3](pdfs/DS1 Drum Synth - Single Drum V3.pdf)

---
*84 images archived*
