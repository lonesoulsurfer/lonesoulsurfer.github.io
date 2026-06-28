# Light Theremin in a NES Controller - 555 Timer

Source: https://www.instructables.com/Slider-Synth-Light-Theremin-555-IC/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

I've been playing around with the 555 IC and never have I managed to get it to do anything until now. When I heard it come to life and start oscillating at me I was pretty damn happy with myself. If I can get it to make a sound, then anyone should be able to!

I won't go into any details about the 555 IC - but if you want to know more you can check it out for yourself [here](https://en.wikipedia.org/wiki/555_timer_IC).

Basically this project uses a photo cell, also known as a CDS photoresister to change the pitch of the oscillating 555 IC. You use an LED to control the pitch, putting it closer to the photo cell shortens the pitch and moving it away lengthens the pitch.

I wish I could claim the circuit but all credit for it goes to [Dean Segovis over at Hack-a-week](http://hackaweek.com/hacks/?attachment_id=1515) who came up with the idea.

It's all my idea though to stick it into a NES controller. Don't really know if it is the smartest one I've ever had but you can be the judge of that. Don't worry, I didn't use an original NES controller, just a cheap knock-off.

[Hackaday](https://hackaday.com/?gclid=CjwKCAiA58fvBRAzEiwAQW-hzTZV1eEwLdO0Vsn_N4EfrDxyIFbPlYwbiKsXVcXBxF25Cwtvi60QjhoCY7cQAvD_BwE) were also nice enough to do a review on this project which can be found [here](https://hackaday.com/tag/cds/)


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

![Step 1: Parts and Tools image 4](images/step01_04.jpg)

![Step 1: Parts and Tools image 5](images/step01_05.jpg)

![Step 1: Parts and Tools image 6](images/step01_06.jpg)

Electrical Components

You will be able to get all of these components at your local electrical hobby store. However I have linked them to eBay as well.

1. 100 Ohm Resistor – [eBay](https://www.ebay.com.au/itm/200Pcs-1-4W-Metal-Film-Resistors-1ohm-47ohm-100ohm-220ohm-470ohm-1K-10K-100K-1M/252706634640?hash=item3ad67d3b90:m:mFG-vc-9lvzKmIrjteHMqzw)

2. Potentiometer 10K - [eBay](https://www.ebay.com.au/itm/6mm-3pin-Knurled-Shaft-Single-Linear-B10K-Ohm-Rotary-Potentiometer-15mm/162933413158?hash=item25ef969526:m:mNP34lIqPW_xXIyb7OMIT4A)

2. 2.2 uf Capacitor – [eBay](https://www.ebay.com.au/itm/2-2-uf-50-V-Electrolytic-capacitor-20-pcs/292465991779?hash=item441854e063:g:JNAAAOSwCY9ZtLEZ)

3. 100 uf Capacitor – [eBay](https://www.ebay.com.au/itm/100-F-35V-High-Temp-Electrolytic-Capacitors-10-20-or-50-pack-100uF-Capacitor/201961792518?hash=item2f05dc6406:m:mBeyhv3yjNTxLr9W8MQ6SMg)

4. Speaker - 8 Ohm 0.5W – [eBay](https://www.ebay.com.au/itm/2-Pcs-8ohm-Loud-Speaker-8-0-5W-Small-Trumpet-36mm-Diameter-AU-NEW/302106509576?epid=22004488711&hash=item4656f38108:g:i84AAOSwZJBYAJFX)

5. 3mm white LED – [eBay](https://www.ebay.com.au/itm/20PCS-LED-3MM-Round-White-LED-Emitting-Red-Llight-Lamp-Super-Bright-SF/191931298476?hash=item2cafff32ac:g:oOAAAOSwIgNXlr8d)

6. Photo Cell – [eBay](https://www.ebay.com.au/itm/20PCS-Photoresistor-LDR-CDS-5mm-Light-Dependent-Resistor-Sensor-GL5516-Arduino/222746709589?epid=22011020945&hash=item33dcbd0e55:g:03YAAOSwKytZL-uQ)

7. LM555 IC – [eBay](https://www.ebay.com.au/itm/10x-555-TIMER-NE555-IC-8-PIN-DIP-Single-Bi-Polar-LM-LM555-NE-NE555P-AUS-STOCK/172142220155?hash=item281479d37b:g:p24AAOSwwpdW8HDA)

8. 2 X CR2032 3v Batteries – [eBay](https://www.ebay.com.au/itm/5Pcs-Lots-3V-Cell-Batteries-CR2032-3-Volt-Coin-Button-Cell-Battery-Bulk/182105983004?epid=1067613200&hash=item2a665cc81c:g:YwMAAOSwtPZXHcYu)

9. CR2032 X 2 Battery Holder – [eBay](https://www.ebay.com.au/itm/Black-CR2032-Button-Coin-Cell-Battery-Holder-Case-Box-W-On-Off-Switch-Lead-GA/182195809053?hash=item2a6bb76b1d:g:GOAAAOSwgY9Xe7nl)

10. Perf Board – [eBay](https://www.ebay.com.au/itm/10pcs-5cm-x-7cm-PCB-Prototyping-Perf-Boards-Breadboard-DIY/183113399570?hash=item2aa268bd12:g:iuwAAOSwqfZab4uO)

11. 1 X tactile switch – [eBay](https://www.ebay.com.au/itm/6-Pin-DPDT-Latching-Tact-Tactile-Push-Button-Pushbutton-Switch-20-Pcs-M9Q6-T0H7/253253294285?epid=24009135255&hash=item3af71298cd:g:tEEAAOSw9hdaBn-z)

12. Thin wire. You can use the wire from the NES controller.

Other Parts

1. NES Controller – [eBay](https://www.ebay.com.au/itm/HOT-USB-Controller-Gaming-Gamer-JoyStick-Joypad-For-NES-Windows-PC-for-MAC-Q4S7/282695225215?epid=560358643&hash=item41d1f2cf7f:g:o74AAOSwjZJZ77Zb)

2. Plastic tubing 1/4" – [eBay](https://www.ebay.com.au/sch/i.html?_odkw=strip+styrene+1%2F4%22&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xtube+styrene+1%2F4%22.TRS0&_nkw=tube+styrene+1%2F4%22&_sacat=0)

3. Plastic tubing 3/16" - [eBay](https://www.ebay.com.au/sch/i.html?_odkw=tube+styrene+1%2F4%22&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR0.TRC0.H0.Xtube+styrene+3%2F16%22.TRS0&_nkw=tube+styrene+3%2F16%22&_sacat=0)

Tools

1. Soldering Iron

2. Pliers

3. Wire cutters

4. Drill

5. Dremel

6. Hot glue

7. [Bread board](https://www.ebay.com.au/itm/Breadboard-830-Point-Solderless-PCB-Bread-Board-MB-102-MB102-Test-Breadboard-TG/263532522395?_trkparms=aid%3D555019%26algo%3DPL.BANDIT%26ao%3D1%26asc%3D20151005190540%26meid%3D014c26d1eb15435e93d09cc9ae84deeb%26pid%3D100505%26rk%3D1%26rkt%3D1%26%26itm%3D263532522395&_trksid=p2045573.c100505.m3226) and j[umper wires](https://www.ebay.com.au/itm/65-Lots-Bread-Board-Solderless-Cord-Jumper-Line-Wire-For-PCB-Breadboard-Connect/162309145554?hash=item25ca6103d2:g:jQIAAOSwo4pYRRAv) - eBay


## Step 2: Schematics

![Step 2: Schematics image 1](images/step02_01.jpg)

![Step 2: Schematics image 2](images/step02_02.jpg)

![Step 2: Schematics image 3](images/step02_03.jpg)

![Step 2: Schematics image 4](images/step02_04.jpg)

![Step 2: Schematics image 5](images/step02_05.gif)

I have included a schematic of the circuit which was created by Dean Segovis. I have also done a schematic which shows the components and how they are attached to one another.

The schematic is really quite simple – just make sure you test it out first on a bread board. Nothing worse than soldering everything up and then realise you have done something wrong. Better to practice on the bread board first.

I have added a link in the parts list if you don’t have one of these along with some jumper wires. They are essential for any electronic projects.

I’ll go through each step in wiring the project up to a perf board and add images to try and make it as fool proof as possible.

Also included an image of a 555 IC and what’s inside of it. For more info on this [visit Wikipedia](https://en.wikipedia.org/wiki/555_timer_IC)


## Step 3: Getting Started - Solder on the 555 IC

![Step 3: Getting Started - Solder on the 555 IC image 1](images/step03_01.jpg)

![Step 3: Getting Started - Solder on the 555 IC image 2](images/step03_02.jpg)

![Step 3: Getting Started - Solder on the 555 IC image 3](images/step03_03.jpg)

I’m going to assume that you have tested this circuit on a breadboard and got it working. Now you know how to wire it up, you next have to solder all of the parts to a perf board (and make it as small as you can!) You will need to stuff this along with batteries, speaker switch and plastic tubing inside a NES controller and believe me there isn’t much room inside of one.

It’s surprising how much room wires take up in a project. That’s why I have used copper wire wherever I can to reduce the space the wires take up.

Steps:

1. Place the 555 IC into the perf board as shown. There is a little dot at the top of the the 555 IC and this helps you orientate it. To follow along on how I soldered it together, make sure the dot is on the left hand side.

2. Slightly bend the legs inwards so it doesn’t fall out

3. Solder each leg into place


## Step 4: Soldering the Speaker Wires and Capacitor

![Step 4: Soldering the Speaker Wires and Capacitor image 1](images/step04_01.jpg)

![Step 4: Soldering the Speaker Wires and Capacitor image 2](images/step04_02.jpg)

![Step 4: Soldering the Speaker Wires and Capacitor image 3](images/step04_03.jpg)

![Step 4: Soldering the Speaker Wires and Capacitor image 4](images/step04_04.jpg)

The speak wires are attached to pins 1 (ground) and 3 of the 555 IC

Steps:

1. solder a wire to leg 8 on the 555 timer. This will attach to the negative terminal on the speaker

2. Next solder the 100 uf capacitor to leg 3 on the 555 timer making sure that it is correctly orientated.

3. Lastly,. solder a wire to the negative leg of the capacitor. This will attach to the positive terminal on the speaker.


## Step 5: Adding the Wires for the Photo Cell

![Step 5: Adding the Wires for the Photo Cell image 1](images/step05_01.jpg)

![Step 5: Adding the Wires for the Photo Cell image 2](images/step05_02.jpg)

The photo cell is attached to pins 7 and 8 on the 555 IC.

Tip: If you want really thin wire, you can always use the wire that comes inside the cord on the NES controller. It's very thin and the black plastic covering comes off easily.

Steps:

1. Solder a wire to leg 7 of the 555

2. Solder another wire to leg 8 of the 555. Don't attach the photo cell yet - you will probably need to trim the wires to remove any excess.


## Step 6: Adding the 2nd Capacitor

![Step 6: Adding the 2nd Capacitor image 1](images/step06_01.jpg)

![Step 6: Adding the 2nd Capacitor image 2](images/step06_02.jpg)

The 2nd capacitor is attached to pin 6 and 1 (ground)

Steps:

1. It's up to you how you want to attach the legs of the capacitor to the IC. As legs 6 and 1 aren't close to one another, you will need to add a jumper wire to be able to attach them. You also want to lay down the capacitors so they will fit into the NES controller (of you are using one as a case)

2. Solder the negative leg of the capacitor to leg 1 (ground)

3. Add a jumper wire to the other capacitor leg and solder this to leg 6


## Step 7: Adding a Jumper Wire From Leg 2 to 6 on the 555 IC

![Step 7: Adding a Jumper Wire From Leg 2 to 6 on the 555 IC image 1](images/step07_01.jpg)

![Step 7: Adding a Jumper Wire From Leg 2 to 6 on the 555 IC image 2](images/step07_02.jpg)

To connect the 2 legs on the 555 IC together, I used a small piece of wire cut from one of the capacitors. You could also just a jumper wire like in the last step as well.

Steps:

1. Add a little solder to one end of the wire

2. Solder to pin 2.

3. Push the wire down and orientate it so it is resting on pin 6.

4. Add some solder to the tip of the soldering iron and attach.


## Step 8: Adding the Wires for the Potentiometer

![Step 8: Adding the Wires for the Potentiometer image 1](images/step08_01.jpg)

![Step 8: Adding the Wires for the Potentiometer image 2](images/step08_02.jpg)

The wires for the pot need to be attached to legs 6 and 7

Steps:

1. Solder wires onto legs 6 and 7 of the 555.

Note: Always make the wires longer than you need - you can always trim later. Don't attach the wires yet to the pot, you need to add all of the components to the NES controller first.

2. This is pretty much it. I didn't show the last little bit of wiring which is attaching the wires for the LED so follow the steps below

3. Solder one leg of the 100 ohm resister to pin 8 of the 55 IC

4. Solder the other leg to the perf board and attach a wire to it. This will go to the switch and then to the positive terminal of the battery

5. Lastly, attach another wire to pin 1. This will go to the negative side of the battery


## Step 9: NES Controller - Pull It Apart

![Step 9: NES Controller - Pull It Apart image 1](images/step09_01.jpg)

![Step 9: NES Controller - Pull It Apart image 2](images/step09_02.jpg)

![Step 9: NES Controller - Pull It Apart image 3](images/step09_03.jpg)

Steps:

1. Un-screw the 6 screws in the back of the case

2. Remove the screw that is holding the circuit board to the case

3. Take-out off of the buttons etc and keep to one side.


## Step 10: Making Some Space

![Step 10: Making Some Space image 1](images/step10_01.jpg)

![Step 10: Making Some Space image 2](images/step10_02.jpg)

![Step 10: Making Some Space image 3](images/step10_03.jpg)

![Step 10: Making Some Space image 4](images/step10_04.jpg)

![Step 10: Making Some Space image 5](images/step10_05.jpg)

You need to remove some of the gussets etc inside the case to make room for the electronics.

Steps:

1. Remove the 2 circle gussets on the back of the ase. I used a pair of pliers to snip away. You can use a dremel with a sanding drum to smooth them out if necessary.

2. Remove the side gussets on the top case. These are so you can add the 1/42 tube later.

3. Remove the bit of plastic that protrudes where the cord come out of.

4. Lastly, remove the plastic leg as shown in the image below.


## Step 11: Adding the Speaker

![Step 11: Adding the Speaker image 1](images/step11_01.jpg)

![Step 11: Adding the Speaker image 2](images/step11_02.jpg)

![Step 11: Adding the Speaker image 3](images/step11_03.jpg)

![Step 11: Adding the Speaker image 4](images/step11_04.jpg)

![Step 11: Adding the Speaker image 5](images/step11_05.jpg)

![Step 11: Adding the Speaker image 6](images/step11_06.jpg)

![Step 11: Adding the Speaker image 7](images/step11_07.jpg)

I had a small speaker cover that I pulled from a small speaker. If you don't have one of these then don't worry, it isn't necessary, just make sure that you make the hole for the speaker a little smaller then then speaker and glue it into place

Steps:

1. Mark where you need to cut.

2. Drill a hole to start the cut-out

3. With a dremel or something similar, enlarge the hole with a sanding drum. Keep on measuring until the speaker grill fits nice and tightly inside

4. Lastly, put the speaker into the cover and hold it in place with the tabs from the cover or with some super glue


## Step 12: Adding the On/Off Switch

![Step 12: Adding the On/Off Switch image 1](images/step12_01.jpg)

![Step 12: Adding the On/Off Switch image 2](images/step12_02.jpg)

Initially I was going to use an tactile on/off switch to activate the synth but decided against it. It was going to be activated by pushing one of the red buttons on the controller.

Steps:

1. Drill a hole into the side of the top cover as shown below

2. Secure the switch into place


## Step 13: Add the Potentiometer

![Step 13: Add the Potentiometer image 1](images/step13_01.jpg)

You could put the pot on the side of the controller but I found that it was easier to use with it on the bottom of the controller near the speaker.

Steps:

1. Drill a hole into the cover

2. Attach the pot. Remember to think about what's underneath the pot when you do to add it to the cover. You need to make sure that there is some empty space as it will take up most of the room in that section of the controller.


## Step 14: Glue Down the Buttons

![Step 14: Glue Down the Buttons image 1](images/step14_01.jpg)

![Step 14: Glue Down the Buttons image 2](images/step14_02.jpg)

As you don't need to used the buttons, you will need to hot glue them into place. If you want to add a audio out, then leave one of the red buttons.

Steps:

1. Put all of the buttons into place

2. add some hot glue to each one and leave to dry. make sure that they are glued strongly as people will try and push them and you don't want them coming loose.


## Step 15: Adding the Photo Cell and 1/4" Tube

![Step 15: Adding the Photo Cell and 1/4" Tube image 1](images/step15_01.jpg)

![Step 15: Adding the Photo Cell and 1/4" Tube image 2](images/step15_02.jpg)

![Step 15: Adding the Photo Cell and 1/4" Tube image 3](images/step15_03.jpg)

![Step 15: Adding the Photo Cell and 1/4" Tube image 4](images/step15_04.jpg)

![Step 15: Adding the Photo Cell and 1/4" Tube image 5](images/step15_05.jpg)

Steps:

1. Drill a hole just large enough for the tube to fit into. The hole should be opposite the switch.

2. Solder on the photo cell to the wires on pins 7 and 8. Add some heat-shrink so the wires don't touch (or hot glue)

3. Push the tube into place. You shouldn't have to glue into place as it's a tight fit. Test that the tube isn't getting squashed by pushing the smaller tube into it. If it moves freely then you are ok. If not, then remove some more of the plastic in the case.

4. Push the photo cell into the end of the tube and add a little hot glue to hold it in place.


## Step 16: Attaching the Speaker and Potentiometer Wires

![Step 16: Attaching the Speaker and Potentiometer Wires image 1](images/step16_01.jpg)

![Step 16: Attaching the Speaker and Potentiometer Wires image 2](images/step16_02.jpg)

![Step 16: Attaching the Speaker and Potentiometer Wires image 3](images/step16_03.jpg)

Steps:

Speaker

1. Attach the wire on pin 1 to the negative terminal on the speaker

2. Next, attach the wire that is connected to the capacitor on pin 3 to the positive terminal on the speaker

Potentiometer

1. Attach the wire from pin 6 to one of the pins on either side of the pot. It doesn't matter which one

2. Next, attach the wire from pin 7 to the other 2 pins on the pot.

.


## Step 17: Adding the LED

![Step 17: Adding the LED image 1](images/step17_01.jpg)

![Step 17: Adding the LED image 2](images/step17_02.jpg)

![Step 17: Adding the LED image 3](images/step17_03.jpg)

![Step 17: Adding the LED image 4](images/step17_04.jpg)

Steps:

1. The wire for the LED (slider section) needs to be long enough for the smaller tube fits into the larger one. The wire that I used was the controller wire which worked excellently. Just trim the

2. Push the smaller tube over the wire and push the wire through the end of the tube.

3. Solder the LED to the ends of the wire, making sure the polarity's are correct and that you use some heat shrink on the exposed wires.

4. Lastly, pull the other end of the wire so the LED is against the end of the tube.


## Step 18: Adding the Battery Holder

![Step 18: Adding the Battery Holder image 1](images/step18_01.jpg)

![Step 18: Adding the Battery Holder image 2](images/step18_02.jpg)

![Step 18: Adding the Battery Holder image 3](images/step18_03.jpg)

![Step 18: Adding the Battery Holder image 4](images/step18_04.jpg)

Steps:

1. Solder the red wire to one of the terminals to the switch.

2. Solder another wire to the middle terminal of the switch and then solder the other end to pin 8 on the 555 IC

3. Solder the negative wire from the battery terminal to pin 1 (ground) on the 555 IC.


## Step 19: Add a Audio Out Jack

![Step 19: Add a Audio Out Jack image 1](images/step19_01.jpg)

![Step 19: Add a Audio Out Jack image 2](images/step19_02.jpg)

![Step 19: Add a Audio Out Jack image 3](images/step19_03.jpg)

![Step 19: Add a Audio Out Jack image 4](images/step19_04.jpg)

![Step 19: Add a Audio Out Jack image 5](images/step19_05.jpg)

![Step 19: Add a Audio Out Jack image 6](images/step19_06.jpg)

![Step 19: Add a Audio Out Jack image 7](images/step19_07.jpg)

![Step 19: Add a Audio Out Jack image 8](images/step19_08.jpg)

![Step 19: Add a Audio Out Jack image 9](images/step19_09.jpg)

Steps:

1. To be able to place the jack flat on the inside of the controller, you need to remove a little bit of plastic that held the red button in place. Just use some wire clippers and a exact knife to remove the area.

2. Next, place the jack through the hole, add a small washer (one you get from a potentiometer works fine) and screw into place with the little, round nut that comes with the jack.

Nearly done. Test and make sure that everything is working as it should before you close up the NES case. If you find that something isn't working, check the solder points and wires.

If everything is working as it should be, close up the case and make some beautiful music.


---
*76 images archived*
