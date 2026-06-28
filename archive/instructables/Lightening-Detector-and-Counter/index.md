# Lightning Detector and Counter

Source: https://www.instructables.com/Lightening-Detector-and-Counter/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

I’ve always wanted to make a lightening detector but found the circuit schematics a little beyond my capabilities. Recently whilst surfing the net, I came across a very cool circuit which counts lightning strikes as they happen! After looking over the circuit schematic I thought – finally, here’s a lightning detector that I can make with my limited skills.

The detector is a simple design and anyone with some basic electronic skills should have no issue making one.

The way it works is the circuit can detect discharge from lightning and counts up to 9 through a 7 segment display. Once you get past 9 it re-sets back to 0.

A big shout-out to [D.Mohankumar](https://dmohankumar.wordpress.com/2015/11/09/lightning-counter-simple-design-14/) who designed the lightning counter and detector.

The main components that make up the detector are an IC (CD 4033) and a 7 segment counter. Both a cheap and easy to find on eBay. Basically, the IC’s number 1 input pin is very sensitive to electric discharges such as lightning. Whenever lightning strikes the earth, it releases thousands of volts which can be detected by the IC. The IC then converts the signal into a numerical output on the 7 segment display.

I have listed all of the parts needed and have also added links to where you can find them. If you have never tackled something like this I really encourage you to give it a go. As I mentioned before, it’s relatively simple to make and a heap of fun.


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

![Step 1: Parts and Tools image 4](images/step01_04.jpg)

![Step 1: Parts and Tools image 5](images/step01_05.jpg)

![Step 1: Parts and Tools image 6](images/step01_06.jpg)

Parts:

1. IC – CD 4033 – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p4712.m570.l1313.TR0.TRC0.H0.XCD4033BE+IC+COUNTR%2FDIVIDR+DECADE+16-DIP.TRS0&_nkw=CD4033BE+IC+COUNTR%2FDIVIDR+DECADE+16-DIP&_sacat=0)

2. 7 Segment display (common cathode) – [eBay](http://www.ebay.com.au/itm/5-pcs-LED-7-Segment-Display-1-Bit-Red-Common-Cathode-0-56-in-5O-/192286104395?epid=566156997&hash=item2cc5251b4b:g:YTQAAOSwMmBVwIAw)

3. 100R Resistor – [eBay](https://www.ebay.com.au/itm/100pcs-1-4W-Watt-0-25W-Metal-Film-Resistor-1-1R-to-1K-Ohm-Accessories-New-/222401836897?var=&hash=item33c82eb761:m:mfTU2Ec6OAWVd95hY9DXomw)

4. 1K Resistor – [eBay](http://www.ebay.com.au/itm/50-x-1-4W-250V-1-5K-ohm-1K5-Axial-Carbon-Film-Resistors-/201899887936?epid=1066822147&hash=item2f022bcd40:g:mrEAAOSwVm5Y-dpK)

5. 9V battery holder – [eBay](http://www.ebay.com.au/itm/Replacement-9V-Battery-Box-Case-Holder-Connector-CS-/202060412901?hash=item2f0bbd37e5:g:pO8AAOSwqd1Zwh7D)

6. 1uF Capacitor – [eBay](https://www.ebay.com.au/itm/30-100pcs-1uF-to-1000uF-25V-35V-50V-Aluminum-Electrolytic-Capacitors-/272776227430?var=&hash=item3f82baea66:m:mJXFbyIQXAnF-D6h8orZ8Aw)

7. Antenna – [eBay](http://www.ebay.com.au/itm/Replacement-25-4cm-10-5-Sections-Telescopic-Antenna-Aerial-for-Radio-TV-L5D9-/282561182107?epid=1153505772&hash=item41c9f5799b:g:EvgAAOSwiA9ZX0gX)

8. Sold core wire (breadboard wire) – [eBay](https://www.ebay.com.au/itm/400pcs-Breadboard-Jumper-Cable-Electronic-Wires-6cm-Kit-Experiment-Test-Tinned/252428303605?_trkparms=aid%3D555019%26algo%3DPL.BANDIT%26ao%3D1%26asc%3D20151005190705%26meid%3Dd59fb3a39e1545b3a3dfd8b3fdd96946%26pid%3D100506%26rk%3D1%26rkt%3D1%26&_trksid=p2045573.c100506.m3226)

9. Blank PCB - [eBay](http://www.ebay.com.au/itm/Electronic-Kit-Circuit-Breadboards-Blank-PCB-Universal-DIY-Phototype-Board-HOT-/122680152992?hash=item1c904e93a0:g:1DUAAOSwsIZZpPvr)

10. 9V Battery

11. Project Box – [eBay](http://www.ebay.com.au/itm/5-Pcs-DIY-100x60x25mm-Plastic-Electronic-Project-Box-Enclosure-Instrument-Case-/131571667714?hash=item1ea2485302:g:72YAAOSw~OdVZWsl)

12. 6pin DIP IC Socket Adapter - [eBay](https://www.ebay.com.au/itm/10PCS-16pin-DIP-IC-Socket-Adaptor-Solder-Type-Socket-Pitch-Dual-Wipe-Contact-/262857158981?hash=item3d3381f145:g:dDgAAOSwdGFYpqGv)

13. Switch - [eBay](https://www.ebay.com.au/itm/5-x-Heavy-Duty-Toggle-Flick-Switch-ON-OFF-Car-Dash-Light-Metal-SPST-Contacts-AU-/263024516128?epid=501119715&hash=item3d3d7b9c20:g:a7cAAOSwPh5ZN6AG)

14. Various small screws etc

Tools:

1. Hot Glue

2. Dremel

3. Soldering iron

4. Bread Board

5. Super glue

6. Pliers

7. Screwdrivers etc


## Step 2: Circuits and Diagrams

![Step 2: Circuits and Diagrams image 1](images/step02_01.jpg)

![Step 2: Circuits and Diagrams image 2](images/step02_02.jpg)

![Step 2: Circuits and Diagrams image 3](images/step02_03.jpg)

![Step 2: Circuits and Diagrams image 4](images/step02_04.jpg)

Familiarise yourself with the circuit diagram. The first 2 images show the original circuit diagram and the other how I slightly modified it. The reason why I added an extra wire from the negative leg on the capacitor to the ground on the battery was because I was getting no reading from the 7 segment display initially. After doing a little investigating I found out what the issue was and added an extra wire which did the trick.

I included both circuit diagrams so you can see the difference. You can also find the original one here.

The next diagram is the pin out for the 7 segment display. Make sure that you take note of how the pins are numbered and laid out.

The last diagram is the pin out for the IC. Again, take note of how the pins are numbered and laid out.

Let’s go back to the main circuit diagram. You can see there are 7 connections to the 7 segment display out of the 10. Another 2 are connected together and are attached to ground via the 100 ohm resistor. That leaves 1 pin left which is pin 5 which is for the decimal point on the display which we won’t be utilising

The other main connections from the IC are either to ground or to positive. Pin 1 is connected to the 1K resistor and also the antenna.

That’s really it. It’s a simple design once you break it down. Now it’s time to get started and breadboard the circuit before doing any soldering


## Step 3: Adding the IC Connections to Ground and Positive

![Step 3: Adding the IC Connections to Ground and Positive image 1](images/step03_01.jpg)

![Step 3: Adding the IC Connections to Ground and Positive image 2](images/step03_02.jpg)

![Step 3: Adding the IC Connections to Ground and Positive image 3](images/step03_03.jpg)

![Step 3: Adding the IC Connections to Ground and Positive image 4](images/step03_04.jpg)

First thing to do is to make the connections on the IC to the ground and positive terminals.

Steps:

Positive Connections

1. Add the IC to the breadboard

2. Attach the 1k resistor to leg 1 on the IC and the other leg to the section on the breadboard that you want to make positive.

3. Next add the negative leg of the capacitor to leg 15 on the IC. Also add a wire from the negative leg to the section on the breadboard that you want to make ground.

4. Add the positive leg to the positive section on the breadboard

5. Add a couple of jumper wires to legs 3 and 16 to the positive section

6. Lastly, add a wire to the antenna and attach this to leg 1 on the IC next to the 1K resistor

Ground Connections

1. Add jumper wires to legs 2, 8 and 14 to the ground section on the breadboard.


## Step 4: Connecting the IC to the 7 Segment Display and the Battery

![Step 4: Connecting the IC to the 7 Segment Display and the Battery image 1](images/step04_01.jpg)

![Step 4: Connecting the IC to the 7 Segment Display and the Battery image 2](images/step04_02.jpg)

Next thing to do is to connect the IC to the 7 segment display

Steps:

1. Push the 7 segment into the breadboard

2. Start to add the wires from the IC to the corresponding leg on the display. Start with the lowest value leg on the IC which happens to be 7 and attach a jumper wire from leg 7 to leg 10 on the display.

3. Keep going until all of the connections have been done from the IC to the display

4. Next, add a couple of jumper wires to legs 3 and 8 on the display. These should then be connected to one of the legs on the 100R resistor and the other leg of the resistor to the Ground section on the breadboard.

5. Next, attach the battery to the ground and positive sections. You should see the LED’s in the display light up and show a ‘0”. If you don’t or have missing segments, check the wires to make sure everything is connected correctly.


## Step 5: Testing Your Circuit.

![Step 5: Testing Your Circuit. image 1](images/step05_01.jpg)

![Step 5: Testing Your Circuit. image 2](images/step05_02.jpg)

The good news is you don’t have to wait for lightning to test your circuit. All you need is a lighter with a clicker (piezo electric) starter in it which you can buy in most places that sell cigarettes. I used something similar to this to test which worked a treat.

Steps:

1. First, extend the antenna

2. Next, turn on the detector. The display should have a zero showing.

3. Place the lighter (or spark generator) close to the antenna and make a spark. This should register on the display as a 1. Try it again and you will see the display count up to 9 and then re-set to zero.

4. If it doesn’t register, try putting the spark closer to the antenna. Make sure you aren’t touching the antenna when making the spark or it won’t register.

5. If you ground the circuit you will find that you get a better reading. Try adding another wire to the ground section and touch the end with your finger. Move the spark generator further away and try it again. You should be able to hold the spark around 150mm away from the antenna before it stops registering. In the final build I kept this wire and added a small piece of copper to help ground the circuit better

6. If you still don’t get anything coming up on the display, try removing the capacitor. Initially I couldn’t get anything coming up but once I removed the capacitor it worked fine. You could leave the capacitor out of the circuit but I found that it would sometimes just jump to 0 if I moved the circuit. I think that it’s because leg 15 which the capacitor is connected to is the reset leg and the capacitor stabilises this. Once I connected the capacitor to the ground wire it worked fine so I replaced it.


## Step 6: Soldering the Circuit Together

![Step 6: Soldering the Circuit Together image 1](images/step06_01.jpg)

![Step 6: Soldering the Circuit Together image 2](images/step06_02.jpg)

![Step 6: Soldering the Circuit Together image 3](images/step06_03.jpg)

![Step 6: Soldering the Circuit Together image 4](images/step06_04.jpg)

![Step 6: Soldering the Circuit Together image 5](images/step06_05.jpg)

![Step 6: Soldering the Circuit Together image 6](images/step06_06.jpg)

![Step 6: Soldering the Circuit Together image 7](images/step06_07.jpg)

![Step 6: Soldering the Circuit Together image 8](images/step06_08.jpg)

![Step 6: Soldering the Circuit Together image 9](images/step06_09.jpg)

![Step 6: Soldering the Circuit Together image 10](images/step06_10.jpg)

![Step 6: Soldering the Circuit Together image 11](images/step06_11.jpg)

If your circuit has been tested and is working fine, next you need to add to a permanent PCB. I won’t go through this step by step as it’s not viable to do this. However, I will give a few tips on how I proceeded. I’m really just a novice myself so I’m sure that there are better ways to get it done.

Steps:

1. First, solder into place the IC pin DIP Connector.

2. Next, start to wire in the wires from the IC to the positive and ground connections. The best way to do this is to make a section on the PCB that all of the ground wires and positive wires can be connected to.

3. Once you have these connections done, add the wires to the IC for the display.

4. How you connect the display is up to you. I just did it “dead bug” style by soldering the wires directly to the legs on the display. You could attach the display to a piece of PCB and solder that way as well.

5. I also decided to add a wire from the ground to a small strip of copper. The copper would be attached to the outside of the case which would ground the circuit when I hold it in my hand. This should help with sensitivity.

6. Don't forget to also add a switch so you can turn the circuit on and off. This can be done by adding a switch on the positive battery wire

6. Once everything is connected, test again to make sure everything works as it should.


## Step 7: Adding to an Enclosure

![Step 7: Adding to an Enclosure image 1](images/step07_01.jpg)

![Step 7: Adding to an Enclosure image 2](images/step07_02.jpg)

![Step 7: Adding to an Enclosure image 3](images/step07_03.jpg)

![Step 7: Adding to an Enclosure image 4](images/step07_04.jpg)

![Step 7: Adding to an Enclosure image 5](images/step07_05.jpg)

![Step 7: Adding to an Enclosure image 6](images/step07_06.jpg)

![Step 7: Adding to an Enclosure image 7](images/step07_07.jpg)

![Step 7: Adding to an Enclosure image 8](images/step07_08.jpg)

![Step 7: Adding to an Enclosure image 9](images/step07_09.jpg)

![Step 7: Adding to an Enclosure image 10](images/step07_10.jpg)

![Step 7: Adding to an Enclosure image 11](images/step07_11.jpg)

It’s up to you what type of enclosure you want to use. You could use an old walkie talkie or even a small cardboard box if that’s all you have around. I used a cheap project box which worked well.

Steps:

1. First, work out where the display is going to go. Use a dremel or something similar to cut out the section and check to make sure the display fits into the hole.

2. Next, attach the battery to the inside of the case

3. Drill holes for the Antenna, switch and the wire for the ground wire

4. Secure the antenna and switch into place.

5. Solder onto the ground wire a small piece of copper or something similar. Glue into place onto the side of the case. It should be in a position where your fingers naturally hold it


## Step 8: Find a Storm

![Step 8: Find a Storm image 1](images/step08_01.jpg)

Ok, so I didn't manage to test this lightening detector in a storm. I'm hoping a storm will come through my area soon so I can test and post a video. I appreciate that a lightening detector ible' should at least show that it actually detects lightening but I got impatient :)

If you do make one and a storm blows past your house, let me know whether your detector counts the lightening strikes.

Nevertheless, it's still a fun project to make and anyone who is keen to learn circuitry will find this project a great place to start.


---
*44 images archived*
