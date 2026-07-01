# Negative Voltage Supply

Source: https://www.instructables.com/Negative-Voltage-Supply/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

Most who play around with electronics would have come across an audio circuit that uses a duel rail power supply. The first time I came across this it totally baffled me – how do I get a negative charge out of a power supply? Isn’t one positive and the other ground? For some reason I had never thought that a power source such as a battery has equal negative and positive charge!

Most of the time the negative charge is grounded and not used but in some builds such as audio projects like amps and synths, you need to use the negative charge along with the positive.

[Robin Mitchell](https://www.allaboutcircuits.com/author/robin-mitchell)over at “All About Circuits” has published a very elegant and easy way to create negative charge using only a handful of common parts that most people who play around with circuits will have in their parts bins.

I won’t go into how this works as Robin has explained it excellently in his article which can be [found here](https://www.allaboutcircuits.com/projects/build-your-own-negative-voltage-generator/).

The circuit itself is made up of a 555 timer (is there anything it can’t do!), a few caps and diodes. I wanted to make mine variable voltage controlled and portable to use and test on future projects so I included a buck booster in the design.


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

![Step 1: Parts and Tools image 4](images/step01_04.jpg)

Negative Voltage Circuit Parts

1. 555 Timer – [eBay](https://www.ebay.com.au/itm/10-20-50-100PCS-NE555P-NE555-DIP-8-SINGLE-BIPOLAR-TIMERS-IC/263770865456?hash=item3d69f7ff30:m:mN1oS6xfsjGS9CLz149posg) 100 under $5!

2. 5.6K Resistor. Buy these as assorted on [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR11.TRC1.A0.H0.Xresistors+assorted.TRS0&_nkw=resistors+assorted&_sacat=0)

3. 47K resistor

4. 100nf Cap – Buy these as assorted on [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.Xcapacitor+assorted.TRS0&_nkw=capacitor+assorted&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=resistors+assorted)

5. 10nf Cap

6. Diode 1N194 – [eBay](https://www.ebay.com.au/itm/50PCS-1N914-Small-Signal-Diode-200mA-100V/302107416191?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2060353.m2749.l2649)

7. 10uf Cap – Buy these as assorted on [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=assorted+capacitors&_sacat=0)

8. 100uf Cap

9. Prototype board - e[Bay](https://www.ebay.com.au/itm/10x-DIY-Prototype-Paper-PCB-Experiment-Board-Bakelite-Circuit-Board-4-8x13-3cm/142759746052?hash=item213d24da04:g:sFUAAOSwcEha0XL3)

10. Assorted wires

To make it portable

1. Case – This one would work fine from eBay. Mines an old garage door opener I found somewhere.

2. [Male](https://www.ebay.com.au/itm/Stackable-Banana-Plug-4mm-Male-Solderless-Speaker-Audio-Video-Jack-Connector-DIY/123801999587?hash=item1cd32c98e3:m:mvtxOgLcmuOLChA8qnotBWw) and [Female](https://www.ebay.com.au/itm/10-Pcs-Female-Banana-Plug-4mm-Socket-Connector-Amplifier-Binding-Post-Terminal/222753964134?hash=item33dd2bc066:g:nfAAAOSwO7haL4em) banana plugs – eBay

3. Various wires

4. Switch - [ebay](https://www.ebay.com.au/itm/10-x-On-Off-On-Momentary-Mini-Toggle-Switch-Car-Motor-Dash-Dash-SPDT-3Pin-Sales/201939647988?_trkparms=ispr%3D1&hash=item2f048a7df4:g:ztcAAOSwIFtaCleh&enc=AQAEAAAB4BPxNw%2BVj6nta7CKEs3N0qVG%2FJgWHkbh%2BeQt113BttN3GlwTNS1gv8LBj4QwyDfBsIzARIlfh%2FdG1%2FSyN%2B5%2FiMB4Lp0mWFZue8e%2FYmqnaBWt1Alt%2BeW3siDk%2F9Zq%2BkSOBnlhiiB%2F3DzbOrdQyCxl2PhUs%2BfOoKCWTikNkbf%2FyQA7v5ZvmcMJo5IopmLfs0aaDvQjUwEyelSgXteXEZpWQWQjzEREHkKcGii8hkj6wIesAM1LUQDbN1%2FUeBzbE9akocxrAEq9WyJ5DZ76ybCgbgrQmF0xHEUk6wXxDvUe3UJN5sUoHVQCqIzwS8wxgUwwU7vcrmA%2FnGSaFRqlSe5dCbIq7Q%2B44BICI7cFKNyb1fhgkGFBnedwkr1vQQR8AE2HKQHrlM%2B9UHIwzP%2BhyAYGNCYDpwoEhCOWeX2ai5ftxDy6OSPC%2BY4gYs8rRgLLJ5yjbvWtThf7ft%2FvuVxGv63Iv8hB9tBQ6P0P%2B%2F9XczabFQIfIU4uqwpIAHer1s75%2F4%2FOrh6QVcBWUHCnlUpGqjS9UM10YB4X0ka6tgO3%2FW34cfoD%2FKUQ2r9m0mlYPqbtanDVMIVQWWWQjiZFquKPE0bxSaSLqCQPc%2FoMdHLFvb4C0NNWYD6mcBnuoxb%2FefZgE9upIQ%3D%3D&checksum=201939647988e16b805ef3ff481b9ca8c18c0a88bae5&frcectupt=true)

5. 9V battery

6. 9V battery holder - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR11.TRC1.A0.H0.X9v+battery+holder.TRS0&_nkw=9v+battery+holder&_sacat=0)

7. Voltage regulator – [eBay](https://www.ebay.com.au/itm/Hot-Auto-DC-DC-Booster-Buck-Module-Converter-Solar-Voltage-Regulator-25W-OM/173947307032?hash=item2880114418:g:o2EAAOSw3hFdFeYU&frcectupt=true)

8. Knob for a potentiometer – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2542782.m570.l1313.TR11.TRC1.A0.H0.Xpotentiometer+knob.TRS0&_nkw=potentiometer+knob&_sacat=0)

9. 10K Pot - [eBay](https://www.ebay.com.au/itm/3Pcs-6mm-Knurled-Shaft-Single-Linear-B-Type10K-ohm-Rotary-Potentiometer-New/232484215262?epid=1684420726&hash=item36212399de:g:5FAAAOSwZ~lZtesc)

10. Voltage Meter - [eBay](https://www.ebay.com.au/itm/DC-3-30V-0-36-Wire-LED-Digital-Panel-Volt-Meter-Voltage-Voltmeter-Car-Motor-sH/333271931902?hash=item4d988e1bfe:m:m0NjocAYqCpkThN9z_0lfBA&frcectupt=true)

Tools:

1. Soldering Iron

2. Pliers

3. Wire cutters

4. Hot Glue

5. Drill

6. Cone stepper drill piece (always comes in handy for drilling holes into things)


## Step 2: Breadboard It First

![Step 2: Breadboard It First image 1](images/step02_01.jpg)

![Step 2: Breadboard It First image 2](images/step02_02.jpg)

![Step 2: Breadboard It First image 3](images/step02_03.jpg)

![Step 2: Breadboard It First image 4](images/step02_04.jpg)

I know this this might be self-evident but I highly recommend that you breadboard this circuit (or any that you build) first. It will ensure that the circuit has been tested and works and is like a first run through which helps you get a better understanding of the circuit and how it is put together.

Once you have built it, test with a multi meter and ensure that the voltage being supplied from the circuit is negative.


## Step 3: Making the Circuit - Part 1

![Step 3: Making the Circuit - Part 1 image 1](images/step03_01.jpg)

![Step 3: Making the Circuit - Part 1 image 2](images/step03_02.jpg)

![Step 3: Making the Circuit - Part 1 image 3](images/step03_03.jpg)

![Step 3: Making the Circuit - Part 1 image 4](images/step03_04.jpg)

The circuit is a really interesting one and uses a clever array of diodes and capacitors to achieve negative voltage on a capacitor plate. Check out this link if you want further details. If you haven’t made any circuits before then check out this Instructable which will show you the ropes.

I have included the original circuit schematic along with the modified one which includes the voltage module and a momentary switch connected to the capacitor. This switch can short the cap and discharge the voltage inside. I had to add this as the cap held the voltage supplied from the voltage regulator and if it was high, say 12v's and I reduced the voltage to 6v's, then the negative voltage will stay at 12V and slowly come down. The reset button discharges the cap and brings it in line with the positive voltage.

Steps:

1. First thing to do is to work out how big (or small) you need to make the circuit board. As I was putting mine inside the old garage door opener, I needed to make it as small as possible.

2. Trim the prototype board to size

3. Add a socket IC holder to the board. This will allow you to change out the IC if faulty for any reason.

4. Connect pin 1 to the ground bus strip on the prototype board, pin 4 and 8 to the positive bus strip.

5. Add a 10nf cap to pin 2 and ground

6. Add a 100nf cap to pin 5 and ground


## Step 4: Making the Circuit - Part 2

![Step 4: Making the Circuit - Part 2 image 1](images/step04_01.jpg)

![Step 4: Making the Circuit - Part 2 image 2](images/step04_02.jpg)

![Step 4: Making the Circuit - Part 2 image 3](images/step04_03.jpg)

![Step 4: Making the Circuit - Part 2 image 4](images/step04_04.jpg)

To make the circuit as small as possible, I utilized the bottom of the circuit as well.

Steps:

1. Connect pins 2 and 6 together. I use a resistor leg to do this

2. Connect pins 2 and 7 together with a 47K resistor

3. Add the positive leg of a 10uf cap to pin 3 and the negative leg to a blank spot on the prototype board.

4. Add a diode (making sure it is connected the right way) to the negative leg of the cap and ground

5. Add another diode (checking again that it is correctly connected) to the negative leg of the 10uf cap and the other leg to a blank spot on the prototype board.


## Step 5: Making the Circuit - Part 3

![Step 5: Making the Circuit - Part 3 image 1](images/step05_01.jpg)

![Step 5: Making the Circuit - Part 3 image 2](images/step05_02.jpg)

![Step 5: Making the Circuit - Part 3 image 3](images/step05_03.jpg)

![Step 5: Making the Circuit - Part 3 image 4](images/step05_04.jpg)

![Step 5: Making the Circuit - Part 3 image 5](images/step05_05.jpg)

Steps:

1. Add the negative leg from a 100uf capacitor to the end of the diode

2. Add the positive leg to ground.

3. If you used similar prototype board as me you will need to connect the ground and positive bus strips together. Solder a couple of small wires to connect these

4. At this stage I always like to check and make sure that the circuit will fit inside my case. There wasn’t much room inside the garage door remote I used and the circuit fitted just. I did remove a small amount of the prototype board to make it fit a little better.


## Step 6: Adding Wires to the Circuit

![Step 6: Adding Wires to the Circuit image 1](images/step06_01.jpg)

![Step 6: Adding Wires to the Circuit image 2](images/step06_02.jpg)

![Step 6: Adding Wires to the Circuit image 3](images/step06_03.jpg)

Next thing to do is to add a bunch of wires to the circuit. Once you have added these you can test it to see if it is working

Steps:

1. First add 2 wires (make all wires longer then needed) to the positive bus strip. One will be joined to the positive output on the voltage regulator and the other to a female banana plug

2. Add another 2 wires to the negative bus strip. One will be connected to ground on the voltage regulator and the other to a female banana plug

3. Lastly, add a wire to the negative leg of the 100uf cap. This will be connected to negative voltage banana plug


## Step 7: Adding the Banana Plugs and Switches

![Step 7: Adding the Banana Plugs and Switches image 1](images/step07_01.jpg)

![Step 7: Adding the Banana Plugs and Switches image 2](images/step07_02.jpg)

There wasn’t much room in my case so I had to think carefully where each of the parts were going to go, especially the banana plugs and switch.

Not shown here as it was something I did later was another momentary switch which you will also need to add. This switch will be later connected to each leg on the 100uf cap to discharge any voltage it may be holding.

Steps:

1. First, drill a hole each for the 3 female banana plugs

2. Secure the banana plugs to the case. I went with from left to right, red – negative, black – ground, and red – positive. Seemed like the most logical way to set them up

3. Drill another hole for the SPDT switch and attached this as well.

4. Drill another hole and ad the momentary switch.

5. Lastly, drill a hole in the top of the case for the wire on the voltage meter. Push the wires through and secure the voltage meter to the case with some hot glue. As I didn't have much room I had to stick the meter on the top of the case. The better way is to cut out a section of the case that the meter will fit into. It's a cleaner finish.


## Step 8: Modding the Voltage Regulator

![Step 8: Modding the Voltage Regulator image 1](images/step08_01.jpg)

![Step 8: Modding the Voltage Regulator image 2](images/step08_02.jpg)

![Step 8: Modding the Voltage Regulator image 3](images/step08_03.jpg)

![Step 8: Modding the Voltage Regulator image 4](images/step08_04.jpg)

![Step 8: Modding the Voltage Regulator image 5](images/step08_05.jpg)

I’m not going to go through this in a lot of detail as I have already provided details on how to do it in [this ‘ible](https://www.instructables.com/id/Portable-Variable-Power-Supply-1/). I have also included a diagram which will help you visualise the wiring

Steps:

1. Remove the pot that is on the regulator by carefully de-soldering it

2. Grab your 10k pot and place the legs on the solder points. Re-heat them and push the legs into place.

3. Add a little solder if necessary to the solder points on the circuit board.


## Step 9: Adding the Parts to the Case and Wiring-up

![Step 9: Adding the Parts to the Case and Wiring-up image 1](images/step09_01.jpg)

![Step 9: Adding the Parts to the Case and Wiring-up image 2](images/step09_02.jpg)

![Step 9: Adding the Parts to the Case and Wiring-up image 3](images/step09_03.jpg)

![Step 9: Adding the Parts to the Case and Wiring-up image 4](images/step09_04.jpg)

![Step 9: Adding the Parts to the Case and Wiring-up image 5](images/step09_05.jpg)

![Step 9: Adding the Parts to the Case and Wiring-up image 6](images/step09_06.jpg)

![Step 9: Adding the Parts to the Case and Wiring-up image 7](images/step09_07.jpg)

![Step 9: Adding the Parts to the Case and Wiring-up image 8](images/step09_08.jpg)

You can see in the images below, I really didn’t have much room to play around with!

Steps:

1. First, secure the voltage regulator in place. Make sure that you can get at the solder points easily. If not, then don’t secure into place until you have done all of the soldering

2. Next add the negative voltage circuit to the case

3. Connect ground and positive from the circuit board to the outputs on the voltage regulator

4. Solder the wires from the voltage meter also to the output of the voltage regulator.

5. Solder the positive wire from the battery holder to the switch and another wire from the switch to the input positive solder point on the voltage regulator

6. Solder the ground wire form the battery holder to the ground input solder point on the regulator

7. Now connect the negative wire from the circuit to the negative banana plug. Do the same for ground and positive

8. Now you should be able to add a battery and test whether it is working


## Step 10: Testing and Using

![Step 10: Testing and Using image 1](images/step10_01.jpg)

![Step 10: Testing and Using image 2](images/step10_02.jpg)

![Step 10: Testing and Using image 3](images/step10_03.jpg)

![Step 10: Testing and Using image 4](images/step10_04.jpg)

The first thing that you want to know is whether your voltage regulator is working ok.

Steps:

1. Turn it on and check that the voltage meter is working by adjusting the potentiometer. The voltage should move up or down.

2. Next, test to see if the negative voltage is working by using a multi meter. Please the positive wire from the multi meter into the negative banana plug and the ground into the ground banana plug.

3. Check to see if the multi meter shows a negative voltage. If it doesn’t, check over your circuit and make sure everything is correctly soldered and there are no shorts.

4. Lastly, you should check the capacitor discharge button. Turn up the voltage meter (don’t go too high or you could fry the 555 timer) and then bring the voltage down. Check the negative voltage with the multi-meter. It will show higher then what is being displayed on the voltage meter. This is because the cap is charged to the last voltage that the regulator was at. To discharge, push the momentary button.

5. Check the multi-meter again. It should show close to the voltage meter


---
*47 images archived*
