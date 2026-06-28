# Headphone Amp in an NES Controller!

Source: https://www.instructables.com/Headphone-Amp-in-an-NES-Controller/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

I’ve done a few builds now with NES controllers (check them out below). This time round I managed to add a headphone amp inside one – no mean feat when you consider how much space is inside

The trick was to use a li-op battery (from an old phone) with a charging module and voltage regulator in one. This reduced the room needed for these parts and ensured there was enough room for the circuit, pot, LED and switch.

Wire can also take up a lot of space inside a build like this so I used very thin computer cable wire to reduce the amount of space it can take up.

The NES controller I found in a bin with the cord cut. Someone must of thought that the copper inside was worth more than the actual controller! It would have been great to have been able to utilize the buttons on the controller but this just wasn’t possible so I compromised where I had to. The Pot is attached to the side where the cord originally was as there was already a hole for me to use and it seemed like the right spot to add it. I could have used one of the red button holes but the knob would have stuck up and would have been uncomfortable in a pocket.

You might be asking yourself right about now, what the hell is a headphone amp and why do I need one! Your phone doesn’t really have the power to drive a pair of headphones. You can hear this when you listen to music through your phone speakers, the sound sounds flat and has no real range. When you plug your headphones into a separate amp, you’ll be astonished at the level of audible improvement in clarity, detail and dynamics you get out of your speakers.

So without further ado – let’s get cracking

Other headphone Amps I’ve Made

[Make Your Own Headphone Amp V1](https://www.instructables.com/id/Make-Your-Own-Headphone-Amp/)

[Make a Headphone Amp V2](https://www.instructables.com/id/Make-a-Headphone-Amp/)

[Mini Headphone Amp](https://www.instructables.com/id/Mini-Headphone-Amp/)

Projects with NES Controllers

[Variable Power Supply V2](https://www.instructables.com/id/Variable-Power-Supply-Nintendo-Style/)

[Light Theremin in a NES Controller - 555 Timer](https://www.instructables.com/id/Slider-Synth-Light-Theremin-555-IC/)

[NES Controller Night Light V2](https://www.instructables.com/id/NES-Controller-Night-Light-V2/)

[NES Controller Night Light in Resin](https://www.instructables.com/id/NES-Controller-Night-Light-in-Resin/)


## Step 1: Parts & Tools

![Step 1: Parts & Tools image 1](images/step01_01.jpg)

![Step 1: Parts & Tools image 2](images/step01_02.jpg)

![Step 1: Parts & Tools image 3](images/step01_03.jpg)

![Step 1: Parts & Tools image 4](images/step01_04.jpg)

Parts:

1. NES Controller – You can buy copies for cheap on eBay

2. 10K duel gang Potentiometer – [eBay](https://www.ebay.com.au/itm/10K-Ohm-Rotary-Potentiometer-Shaft-6Pin-6MM-Adjustable-Resistance-For-Speaker/392300039085?hash=item5b56e78bad:g:Z1kAAOSwje9c402w&frcectupt=true)

3. Potentiometer knob - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=potentiomener+knob&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=10k+duel+potentiometer)

4. 2 X 18K Resistor – [eBay](https://www.ebay.com.au/itm/100PC-1-6W-Metal-Film-Resistor-Tolerance-1-Full-Range-of-Values-0-to-10M/312423918540?hash=item48bdeaabcc:m:mEzu7yilmeDIBUw-KujJ0LQ&frcectupt=true)

5. 4 X 68K resistor – [eBay](https://www.ebay.com.au/itm/100PC-1-6W-Metal-Film-Resistor-Tolerance-1-Full-Range-of-Values-0-to-10M/312423918540?hash=item48bdeaabcc:m:mEzu7yilmeDIBUw-KujJ0LQ&frcectupt=true)

6. 47K resistor - [eBay](https://www.ebay.com.au/itm/100PC-1-6W-Metal-Film-Resistor-Tolerance-1-Full-Range-of-Values-0-to-10M/312423918540?hash=item48bdeaabcc:m:mEzu7yilmeDIBUw-KujJ0LQ&frcectupt=true)

7. 3mm LED – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2542782.m570.l1313.TR12.TRC2.A0.H0.X3mm+LED.TRS0&_nkw=3mm+LED&_sacat=0)

8. NE5532 IC – [eBay](https://www.ebay.com.au/itm/10PCS-NE5532P-NE5532-DIP-8-Dual-Low-Noise-Op-Amp-TI-IC-NEW/232812686621?hash=item3634b7ad1d:g:9YoAAOSwa69bKgik&frcectupt=true) (10 IC's for just over a dollar!)

9. 8 pin socket holder - [eBay](https://www.ebay.com.au/itm/10-20-50-100PCS-8pin-DIP-IC-Socket-Adaptor-Solder-Type-Socket-Pitch-Dual-Wipe/191981147298?_trkparms=ispr%3D1&hash=item2cb2f7d4a2:m:mTF1xdyk-_4Z3Jjf7SDk92g&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qXFPYrXeKDMVroSgY4vKZ9OiB9JNbZL16SEj4kaiGgCVtYs0e01fDkK7zxQ2TO3YAQq5zwcnwdjui6rmCUmuPhVDmFcQWEO%2FZeCjN90bXJttD8OOWOns3AraqtZm%2B5lL0HQPGms%2BNa3kfpc%2Fe5xum4gvF8I0I4lqlBlAKKzAXvYaa95PRKFJoRXMX%2FPUZ7ZxNfyMaJOF31RkaUBivS8mXHJzPXRhHwG3b7KMSw%2FI2GfBruRyyWX0PGwfs5rOOWB09kerc6mGn%2F%2BNtcNHjYXnP%2FP31AmSSjMAHw7S%2FsuBagcL9XvKLi6Hh88%2F%2BvUyqigcq6hnLIWOnp3bXy8tQtj07xoq2orksL62WvLxVQndpUIk%2B3QMnzNoUY7boa%2BSYcInluH%2BqM29ugMUvmY60mI5IQAD6R9jDk3HgCLPTwMWGCf2qinYCzeGBsSHoOX99zliYZGav81kGZzrf5vAUEoEXp2hNPpyBe0Mpc0byERdW4y%2BhJtTL44geZLdHKqupsHsZgQL3MNsSwAFejCIiXGXIadilIWSdGYg%2BEgQPosVKNWDHTUvAosruiOLQYDp33ebobG7pkUAUoTvn5%2BwZvL1q%2B6k7ZH9NTp8GzucgkxXguj0UfhmNWo2ibc4%2BqAhWUJCq00RObvlxOClEaWkAOjP9yEbGo5T4aT%2FZfzdFDJS5vifJwYqbX%2BdWWJNrQ%2BCikJ3Gje5w%2B05gDgk4osQ4af0h1x1q5YKLDRz5%2BGoQMrD5%2Fhog%3D%3D&checksum=19198114729840f6fb23abb341a780c6bf821bef7321&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qXFPYrXeKDMVroSgY4vKZ9OiB9JNbZL16SEj4kaiGgCVtYs0e01fDkK7zxQ2TO3YAQq5zwcnwdjui6rmCUmuPhVDmFcQWEO%2FZeCjN90bXJttD8OOWOns3AraqtZm%2B5lL0HQPGms%2BNa3kfpc%2Fe5xum4gvF8I0I4lqlBlAKKzAXvYaa95PRKFJoRXMX%2FPUZ7ZxNfyMaJOF31RkaUBivS8mXHJzPXRhHwG3b7KMSw%2FI2GfBruRyyWX0PGwfs5rOOWB09kerc6mGn%2F%2BNtcNHjYXnP%2FP31AmSSjMAHw7S%2FsuBagcL9XvKLi6Hh88%2F%2BvUyqigcq6hnLIWOnp3bXy8tQtj07xoq2orksL62WvLxVQndpUIk%2B3QMnzNoUY7boa%2BSYcInluH%2BqM29ugMUvmY60mI5IQAD6R9jDk3HgCLPTwMWGCf2qinYCzeGBsSHoOX99zliYZGav81kGZzrf5vAUEoEXp2hNPpyBe0Mpc0byERdW4y%2BhJtTL44geZLdHKqupsHsZgQL3MNsSwAFejCIiXGXIadilIWSdGYg%2BEgQPosVKNWDHTUvAosruiOLQYDp33ebobG7pkUAUoTvn5%2BwZvL1q%2B6k7ZH9NTp8GzucgkxXguj0UfhmNWo2ibc4%2BqAhWUJCq00RObvlxOClEaWkAOjP9yEbGo5T4aT%2FZfzdFDJS5vifJwYqbX%2BdWWJNrQ%2BCikJ3Gje5w%2B05gDgk4osQ4af0h1x1q5YKLDRz5%2BGoQMrD5%2Fhog%3D%3D&checksum=19198114729840f6fb23abb341a780c6bf821bef7321)

10. SPDT switch - e[Bay](https://www.ebay.com.au/itm/10x-SPDT-SLIDE-SWITCH-ON-OFF-Mini-PCB-Mount-Metal-Miniature-AUS-STOCK/171687864334?hash=item27f964e80e:g:noQAAOSwqu9U5TB~&frcectupt=true)

11. 3 X 4.7uf capacitor – [eBay](https://www.ebay.com.au/itm/50PCS-50V-4-7uF-High-Frequency-LOW-ESR-Radial-Electrolytic-Capacitors-105-C/223758464007?hash=item34190b3407:g:CTMAAOSwCH9d0PrD&frcectupt=true)

12. 2 X 22pf ceramic capacitor – [eBay](https://www.ebay.com.au/itm/20pcs-pack-50v-10pf-10uf-monolithic-ceramic-capacitors-pitch-5-08mm-32-values/173519085833?hash=item28668b2109:m:m4kJ0kUJqRX--2AOXy7sxOw)

13. 3 X 220uf capacitor – [eBay](https://www.ebay.com.au/itm/10-20-50PCS-16V-220uF-High-Frequency-LOW-ESR-Radial-Electrolytic-Capacitor-105C/392274265663?_trkparms=ispr%3D1&hash=item5b555e463f:m:mad9zAUmoKH9vcMO2PlSWXw&enc=AQAEAAACUBPxNw%2BVj6nta7CKEs3N0qWmoOIRDZuX23GLxRgfy72txxoc%2BpirrRwr8ltGOJAyuMRKHDN8nsUZ48p9ZcebAzZw%2FUAAW2%2FM0AHosQ9%2BDv7Mezp%2F65q7uji%2B54rBJgYqX27NbGufAxc1e1TbzhIaNGpp21z5bOvX2ar9f%2BgHD3DaC0PEvLINxkJndf5YXFtxSFEWKbXmqlBaKzvtSmpOKX3gwm6iCJ7ckcMAsGmI4OGd5iwCTiQSeckxqw9IJ7eEour9qdcjI3VpKl%2BTS6mN79HQ1TaQNGPcZWTrjzG1xlT0NgV3emUUNbWiQSDa%2FvS2tT4mZVFEetHzlOcD6fyZJRPTxitWCCS9TXulEvPf%2B5grdxp2ff51HM04epBQhXWqLoenjB8SlYgQtIucU%2F%2FDE49Vs%2BpFxoicBsZT8crPQ2uhTjugJw%2FcmFZk5sw%2BxXChS4uQkyk6wwidH802I1P6vtrdMkbfF9gOpIwW%2Bt%2BMpmTpq407XKjO%2FT4kRXlfbZmhQ81WAZEjxZOfFpUFj233ajuPZNT%2F%2Fw6gnLws%2BeEbwYrOaioqpHHmjpMmemQBEXa0gVG5R%2BuvF7PSn831mIOZcPO4oQ0%2BXa1TXNETtw9jr7HJYe8FU64jz1LTzyAm%2B2nIr47MRO2us5gpl05fF%2F9ekpdXExBrxHNZQdE84B3ulM3jsnDU79W1r%2BUSHmNjWbKu887zNLipClOcfSI%2FGdZBx5AkXzYgxpL8JJOVvn6WG2EeOcRL6HYvZuHuEnrHE3Va81quVR35JY4eWMpyBTe6JD8%3D&checksum=3922742656632f79e352b08240e394721c56a67e47b1&enc=AQAEAAACUBPxNw%2BVj6nta7CKEs3N0qWmoOIRDZuX23GLxRgfy72txxoc%2BpirrRwr8ltGOJAyuMRKHDN8nsUZ48p9ZcebAzZw%2FUAAW2%2FM0AHosQ9%2BDv7Mezp%2F65q7uji%2B54rBJgYqX27NbGufAxc1e1TbzhIaNGpp21z5bOvX2ar9f%2BgHD3DaC0PEvLINxkJndf5YXFtxSFEWKbXmqlBaKzvtSmpOKX3gwm6iCJ7ckcMAsGmI4OGd5iwCTiQSeckxqw9IJ7eEour9qdcjI3VpKl%2BTS6mN79HQ1TaQNGPcZWTrjzG1xlT0NgV3emUUNbWiQSDa%2FvS2tT4mZVFEetHzlOcD6fyZJRPTxitWCCS9TXulEvPf%2B5grdxp2ff51HM04epBQhXWqLoenjB8SlYgQtIucU%2F%2FDE49Vs%2BpFxoicBsZT8crPQ2uhTjugJw%2FcmFZk5sw%2BxXChS4uQkyk6wwidH802I1P6vtrdMkbfF9gOpIwW%2Bt%2BMpmTpq407XKjO%2FT4kRXlfbZmhQ81WAZEjxZOfFpUFj233ajuPZNT%2F%2Fw6gnLws%2BeEbwYrOaioqpHHmjpMmemQBEXa0gVG5R%2BuvF7PSn831mIOZcPO4oQ0%2BXa1TXNETtw9jr7HJYe8FU64jz1LTzyAm%2B2nIr47MRO2us5gpl05fF%2F9ekpdXExBrxHNZQdE84B3ulM3jsnDU79W1r%2BUSHmNjWbKu887zNLipClOcfSI%2FGdZBx5AkXzYgxpL8JJOVvn6WG2EeOcRL6HYvZuHuEnrHE3Va81quVR35JY4eWMpyBTe6JD8%3D&checksum=3922742656632f79e352b08240e394721c56a67e47b1&frcectupt=true)

14. 2 X 3.5mm stereo jack socket – [eBay](https://www.ebay.com.au/itm/10Pcs-PJ-392-3-Pin-3-5mm-Stereo-Headphone-Audio-Video-Jack-Socket-Plug-Wv/293023325026?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2060353.m2749.l2649)

15. Prototype board – [eBay](https://www.ebay.com.au/itm/10x-DIY-Prototype-Paper-PCB-Experiment-Board-Bakelite-Circuit-Board-4-8x13-3cm/142759746052?hash=item213d24da04:g:sFUAAOSwcEha0XL3)

16. 3.7 li-po battery – [eBay](https://www.ebay.com.au/itm/New-OEM-Battery-Replacement-for-Genuine-Original-Samsung-Galaxy-S2-S3-S4-S5-AU/163190414123?hash=item25fee81b2b:m:mxtq1eCD0Lnt63lj51SyFlA) or get one from an old phone

17. 3.7v charger and voltage regulator module - [eBay](https://www.ebay.com.au/itm/3-7V-9V-5V-2A-Adjustable-Step-Up-18650-Lithium-Battery-Charging-Discharge-I-J3Q3/264335034952?epid=23035413437&hash=item3d8b988a48:g:j~wAAOSw4YZc55Ns)

18. Micro USB adapter - [eBay](https://www.ebay.com.au/itm/5PCS-CJMCU-5V-Micro-USB-Interface-Power-Adapter-Board-Breakout-Module/264009126118?hash=item3d782b90e6:g:T~8AAOSw7Vtb1DPT&frcectupt=true)

19. Wires. I used thin computer ribbon cable which you can pick-up for free at your local e-waste or buy it on [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2542782.m570.l1313.TR2.TRC0.A0.H0.Xribbon+cable.TRS0&_nkw=ribbon+cable&_sacat=0)

Tools

1. Soldering Iron

2. Drill. It’s also good to have a stepped drill piece to make the holes (only just got myself a set recently and I love them)

3. Wire cutters

4. Dremel (not necessary but always handy

5. Exacto knife

6. Usual screwdrivers, phillips heads etc

7. Epoxy Glue


## Step 2: About the Amp Circuit I Choose to Build

![Step 2: About the Amp Circuit I Choose to Build image 1](images/step02_01.jpg)

![Step 2: About the Amp Circuit I Choose to Build image 2](images/step02_02.jpg)

The amp is built using op amp 5532. The op amp is a low-distortion, low-noise device, which can drive low-impedance loads to a full voltage swing while maintaining low distortion. Furthermore, it is fully output short-circuit proof. I’ve included the datasheet on the op amp in case anyone is interested.

The other positives about this op amp is it’s cheap, you only need 1 for the circuit and you don’t have to worry about virtual grounds or trying to separate the input and output grounds.

Also, when you first look at the schematic it might seem that there are 2 op amp IC’s. There is actually only one and is done this way so it is easier to design. The end result is a high quality, high performance portable device that is relatively easy to build and will change the way you listen to music from your phone.

Make sure you also breadboard the circuit first. Nothing worse than thinking “you got this”, soldering everything into place then realising you have messed it up!


- [ne5532](pdfs/ne5532.pdf)

## Step 3: Pulling Apart the NES Controller

![Step 3: Pulling Apart the NES Controller image 1](images/step03_01.jpg)

![Step 3: Pulling Apart the NES Controller image 2](images/step03_02.jpg)

![Step 3: Pulling Apart the NES Controller image 3](images/step03_03.jpg)

![Step 3: Pulling Apart the NES Controller image 4](images/step03_04.jpg)

![Step 3: Pulling Apart the NES Controller image 5](images/step03_05.jpg)

![Step 3: Pulling Apart the NES Controller image 6](images/step03_06.jpg)

![Step 3: Pulling Apart the NES Controller image 7](images/step03_07.jpg)

The first step is to pull apart the NES controller.

Steps:

1. Remove the 6 screws on the back of the controller and keep in a safe place

2. Remove the circuit board and cord. The cord is wound around a couple of pieces of plastic inside the controller so you need to un-wind this

3. Remove the circuit board and all of the buttons. Keep the buttons with the screws – somewhere safe

4. My controller was pretty dirty so I gave it a good wash in soapy water


## Step 4: Removing the Excess Plastic Inside the Controller

![Step 4: Removing the Excess Plastic Inside the Controller image 1](images/step04_01.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 2](images/step04_02.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 3](images/step04_03.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 4](images/step04_04.jpg)

![Step 4: Removing the Excess Plastic Inside the Controller image 5](images/step04_05.jpg)

Inside the controller, there are plastic gussets, brackets and other little pieces that you will need to remove. You have to make as much room as possible inside the controller to enable to fit the electronics inside. Make sure though that you don’t remove any of the screw mounts or you want be able to close the case!

Steps:

1. First, use a pair of flat wire cutters and trim away all of the raised plastic that you see inside the case.

2. You will need to remove the plastic that surrounds the buttons as well.

3. Remove any gussets around the insides of the case

4. You will also need to remove the little bit of excess plastic that supported the cable hole. I just ran an exacto knife across it and carefully removed the excess plastic

5. The only things that should be standing inside the controller are the screw mounts.

6. Clean-up the plastic sections removed so there isn’t any little bits sticking up – you want the inside of the case as flat as possible


## Step 5: Enlarging the Cord Hole to Fit the Pot Inside

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 1](images/step05_01.jpg)

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 2](images/step05_02.jpg)

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 3](images/step05_03.jpg)

![Step 5: Enlarging the Cord Hole to Fit the Pot Inside image 4](images/step05_04.jpg)

Steps:

1. The hole that the cord came out of needs to be enlarged. The best way to do this is to put the controller case back together first.

2. Enlarge the hole with a drill bit

3. Un-do the controller again and place the pot in the section to make sure it fits ok.

4. At this stage I also placed the main components inside the case so I could get a feel on how everything will be laid out inside the case.


## Step 6: Adding the Audio Jack Inputs to the NES Controller

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 1](images/step06_01.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 2](images/step06_02.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 3](images/step06_03.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 4](images/step06_04.jpg)

![Step 6: Adding the Audio Jack Inputs to the NES Controller image 5](images/step06_05.jpg)

I did think about adding the jack inputs to where the 2 red buttons on the NES controller are. I realised pretty quickly though that this would be awkward place to locate them as the jacks would be sticking out sideways which would be pretty uncomfortable le in your pocket.

Steps:

1. First, bend the legs on the jack inputs as shown in the images. This will give you a little more room inside the case

2. Next, you need to drill a couple of holes to fit the input jacks. When drilling the holes into the side of the case make sure of the following:

a. The holes will need to be drilled so the jack inputs can sit flat on the bottom of the case. To do this the drilled holes will need to be located as high as possible in the bottom case.

b. Make sure that you take into consideration the screw mounts inside the case. If you drill the holes in the wrong place the mounts will get in the way

3. Secure each of the jack inputs into place.


## Step 7: Adding a Switch to the NES Controller

![Step 7: Adding a Switch to the NES Controller image 1](images/step07_01.jpg)

![Step 7: Adding a Switch to the NES Controller image 2](images/step07_02.jpg)

![Step 7: Adding a Switch to the NES Controller image 3](images/step07_03.jpg)

The switch I used was one that I had lying around. I would have pulled it out of some dead electronic gizmo. I decided to locate the switch in the “start” section on the NES controller, which seemed a fitting place

Steps:

1. To secure the switch in place I used a little bit of epoxy glue. Switches and glue don’t really mix so don’t use much.

2. Once dry, test the switch to make sure no glue got into the switch

3. The “select” hole will have the original black button replaced a little later on


## Step 8: Adding the Micro USB Adapter to the NES Controller

![Step 8: Adding the Micro USB Adapter to the NES Controller image 1](images/step08_01.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 2](images/step08_02.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 3](images/step08_03.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 4](images/step08_04.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 5](images/step08_05.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 6](images/step08_06.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 7](images/step08_07.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 8](images/step08_08.jpg)

![Step 8: Adding the Micro USB Adapter to the NES Controller image 9](images/step08_09.jpg)

The charging module is awesome but the only small downfall is the USB outlet is recessed which makes it hard to use in a project like this. The solution is to add a mini USB adapter. There are clear solder points on both the module and the adapter so connecting them is a breeze

Steps:

1. As I wanted to keep the battery, module and adapter close together (only short lengths of wire needed), I decided to add the adapter close to the potentiometer.

2. Place the adapter inside the case and mark out where the USB input will exit the case

3. To make the small slot for the USB outlet, first drill a couple small holes as shown in the image. The drill bit should be aprox ¾ the width of the USB outlet

4. Next, cut away the small piece of plastic between the holes

5. Use a small, flat file to start to shape the slot. Take your time and slowly enlarge it until the USB outlet just fits

6. Lastly, use a small amount of epoxy on the bottom of the outlet and glue into place. Make sure you don’t get any glue inside the USB outlet


## Step 9: Attaching the Charging Module to the Battery

![Step 9: Attaching the Charging Module to the Battery image 1](images/step09_01.jpg)

![Step 9: Attaching the Charging Module to the Battery image 2](images/step09_02.jpg)

![Step 9: Attaching the Charging Module to the Battery image 3](images/step09_03.jpg)

![Step 9: Attaching the Charging Module to the Battery image 4](images/step09_04.jpg)

![Step 9: Attaching the Charging Module to the Battery image 5](images/step09_05.jpg)

I forgot to take photos but before you add the battery, you’ll need to glue all of the buttons in place. I added a little epoxy glue to each and glued them into place

Steps:

I recently did an Instructable on how to reuse old mobile batteries which can be [found here](https://www.instructables.com/id/Reuse-Old-Mobile-Phone-Batteries/). This Instructable will take you through how to wire the module up to the battery

1. Add some superglue to the bottom of the module and stick it onto the battery. Make sure that the “battery” solder points are facing the battery terminals

2. To connect the module to the battery I used some resistor legs. Add some solder to each of the battery terminals. Make sure that you add the solder quickly as you don’t want the battery to overheat.

3. Solder a resistor leg to the positive solder point on the module, bend the leg and then solder it to the battery

4. Do the same for the ground.


## Step 10: Wiring the Switch and the USB Adapter

![Step 10: Wiring the Switch and the USB Adapter image 1](images/step10_01.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 2](images/step10_02.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 3](images/step10_03.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 4](images/step10_04.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 5](images/step10_05.jpg)

![Step 10: Wiring the Switch and the USB Adapter image 6](images/step10_06.jpg)

As mentioned in an earlier step, the wire I used is thin ribbon wire. In a project like this I need to reduce the amount of space where I can and using ribbon wire works a treat.

Steps:

1. Solder 2 lengths of wire to the ground and positive solder points on the USB outlet

2. Work out how long each needs to be, trim and solder to the input solder points on the charging module

3. Next, solder a wire to the positive output solder point on the module. Measure, trim and solder the other end to one of the end solder points on the switch. The other wire that will be soldered to the switch will come from the circuit


## Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 1](images/step11_01.jpg)

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 2](images/step11_02.jpg)

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 3](images/step11_03.jpg)

![Step 11: Adding an LED to Indicate When the Headphone Amp Is On/Off image 4](images/step11_04.jpg)

Adding an LED is a great way to indicate when the amp is on. It’s a simple addition which is definitely worth including.

Steps:

1. Drill a 3mm hole into the NES controller where you want to have the LED. I placed this on top off the controller near the pot and USB outlet

2. Push the LED into the hole and if necessary, add a little superglue to keep it in place

3. Trim the positive LED leg and solder on a 3.3K resistor.

4. Connect the other leg of the resistor to the middle solder point on the switch

5. The other leg on the LED will be attached to ground on the circuit board


## Step 12: Working Out the Right Size for the Prototype Board

![Step 12: Working Out the Right Size for the Prototype Board image 1](images/step12_01.jpg)

![Step 12: Working Out the Right Size for the Prototype Board image 2](images/step12_02.jpg)

![Step 12: Working Out the Right Size for the Prototype Board image 3](images/step12_03.jpg)

![Step 12: Working Out the Right Size for the Prototype Board image 4](images/step12_04.jpg)

It might seem a little backward to first add all of the parts to the case and then work out the size of the prototype board but it’s a good way to work out exactly what room you have to work with. I obviously was adding the parts to the NES controller with the circuit board in mind, trying to leave as much space as possible.

Steps:

1. Place the prototype board inside the controller. The board fits very well length ways but will need to be trimmed and cut in half in order for it to fit.

2. You can see why I bent the legs up on the jack inputs. This gives me a little more room for the circuit board

3. The switch and screw mount was in the way so I just cut out these sections on the prototype board and fitted it around them


## Step 13: Making the Circuit - Part 1

![Step 13: Making the Circuit - Part 1 image 1](images/step13_01.jpg)

![Step 13: Making the Circuit - Part 1 image 2](images/step13_02.jpg)

![Step 13: Making the Circuit - Part 1 image 3](images/step13_03.jpg)

![Step 13: Making the Circuit - Part 1 image 4](images/step13_04.jpg)

So, I decided to solder the IC directly to the circuit board. I’d suggest you don’t do this and use a IC socket so you can change the IC if something goes wrong.

I’ll go through the circuit build step by step so if you are new to this type of build you should be able to follow along easily.

Steps:

1. First, solder the IC into place. You can see in the images that I placed it 4 holes away from the edge. This gives you some room when adding the capacitors

2. Next, connect pin 4 to the ground bus and pin 8 to the positive bus on the prototype board. I use resistor legs to do this

3. Grab both the 220 uf caps. The first one solder the positive leg to pin 7 and the other leg to a spare solder point. Lay it flat like I did in the images. If you don’t you won’t be able to fit it into the NES controller

4. The other solder the positive leg to pin 1 and the other leg to a spare solder point


## Step 14: Making the Circuit - Part 2

![Step 14: Making the Circuit - Part 2 image 1](images/step14_01.jpg)

![Step 14: Making the Circuit - Part 2 image 2](images/step14_02.jpg)

![Step 14: Making the Circuit - Part 2 image 3](images/step14_03.jpg)

![Step 14: Making the Circuit - Part 2 image 4](images/step14_04.jpg)

You might have noticed that pin 3 on the IC has a few components soldered to it. I had to come up with a way to attach all of the parts which I think worked well. In this step, I will start to expand pin 3 to enable to be able to attach all of the parts needed

Steps:

1. Solder a 68K resistor to pins 1 and 2 and also top pins 6 and 7

2. Solder a 22pf cap to the same pins

3. Add a jumper wire (just a resister leg) from pin 3 to the spare solder point next to the IC


## Step 15: Making the Circuit - Part 3

![Step 15: Making the Circuit - Part 3 image 1](images/step15_01.jpg)

![Step 15: Making the Circuit - Part 3 image 2](images/step15_02.jpg)

![Step 15: Making the Circuit - Part 3 image 3](images/step15_03.jpg)

You next need to solder the 18K resistors. You can see in the images that these are going out to the right of the prototype board. That’s because you will need to add a couple of caps later and will need the space

Steps:

1. Add an 18K resistor to pin 6 and solder the other leg to a spare spot on the prototype board.

2. Do the same for pin 2

3. Time to add one of the first resistors to pin 3. Place a 68K resistor in the last hole closest to the ground bus strip and solder into place. Solder the other leg to ground


## Step 16: Making the Circuit - Part 4

![Step 16: Making the Circuit - Part 4 image 1](images/step16_01.jpg)

![Step 16: Making the Circuit - Part 4 image 2](images/step16_02.jpg)

![Step 16: Making the Circuit - Part 4 image 3](images/step16_03.jpg)

![Step 16: Making the Circuit - Part 4 image 4](images/step16_04.jpg)

Now it’s time to add another resistor to pin 3 along with a 4.7 Cap. You also need to connect pins 3 and 5 together.

Steps:

1. Grab a 68K resistor. This will be connected to the positive bus. Solder one leg to the jumper wire coming from pin 3.

2. Solder the other leg on the other side of the IC as shown in the image

3. Add another jumper wire and connect it to the positive bus and the resister leg

4. On the other side of the jumper solder a 4.7uf cap (positive leg)

5. The negative leg is to be soldered to the ground bus. Make sure you lay the cap down as shown in the images

6. Lastly, you need to solder a 200uf cap from positive bus strip to the ground bus. Lay this one down as well.

That’s it for the components, it’s now time to solder some wires to the circuit board


## Step 17: Soldering the Wires in Place

![Step 17: Soldering the Wires in Place image 1](images/step17_01.jpg)

![Step 17: Soldering the Wires in Place image 2](images/step17_02.jpg)

![Step 17: Soldering the Wires in Place image 3](images/step17_03.jpg)

Now it’s time to add wires so you can connect the pot, jacks, battery and LED up to the circuit board. The wire I used was thin computer ribbon wire. You can usually pick this up for free at your local e-waste depo.

Steps:

1. Pull strands of wire from the ribbon cable

2. Start to solder these into place on the prototype board. It helps to use the schematic to make sure you have all the wires connected properly.

3. Don’t forget to add a couple wires for the battery and one extra wire to the negative bus strip for the LED. The LED isn’t shown on the schematic but it helps to add one so you know when the amp is on.

4. Solder 2 wires onto the potentiometer as well. These will be connected to the jack input later on.


## Step 18: Connecting All Those Wires

![Step 18: Connecting All Those Wires image 1](images/step18_01.jpg)

![Step 18: Connecting All Those Wires image 2](images/step18_02.jpg)

![Step 18: Connecting All Those Wires image 3](images/step18_03.jpg)

![Step 18: Connecting All Those Wires image 4](images/step18_04.jpg)

![Step 18: Connecting All Those Wires image 5](images/step18_05.jpg)

Once all of the wires have been added to the prototype board, you’ll next have to connect them to the auxiliary parts. Wires can take up quite a lot of space so take your time when adding the wires and keep them as short as possible.

Steps:

1. Place the circuit board into the NES controller. It is good practice to be able to get to the bottom of the circuit board in case you need to make any changes, although in this build I kept the wires pretty short

2. Next, start to measure each wire against the component it needs to be connected to and trim to length.

3. Tin the end of the wire and solder into place.

4. Continue to do this until all of the connections have been made

5. For the LED, add a 3.3K resistor to the positive leg and connect this to the switch

6. Solder a wire from the ground bus to the negative leg of the LED

7. The positive wire from the battery needs to be connected to the other solder point on the switch


## Step 19: Finishing Touches

![Step 19: Finishing Touches image 1](images/step19_01.jpg)

![Step 19: Finishing Touches image 2](images/step19_02.jpg)

![Step 19: Finishing Touches image 3](images/step19_03.jpg)

Close now.

Before you close-up the case, give it a test to make sure everything is working as it should. If not, then check your connections and re-test until you start to hear some sweet tunes coming out of your headphones. You will hear a slight popping as you turn the amp on through your headphones – don’t worry – this is just the caps charging.

Steps:

1. If everything is working as it should be, place the back cover on and make sure that the potentiometer is in the right spot.

2. Carefully screw everything back into place

3. Add the small nut for the potentiometer and secure

4. Add a knob to the top of the potentiometer

That’s it. You have finished building your own headphone amp


## Downloads

- [ne5532](pdfs/ne5532.pdf)

---
*89 images archived*
