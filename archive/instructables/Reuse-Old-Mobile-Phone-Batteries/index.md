# Reuse Old Mobile Phone Batteries

Source: https://www.instructables.com/Reuse-Old-Mobile-Phone-Batteries/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

![Intro 5](images/intro_05.jpg)

Reuse old mobile phone batteries. I have been using used phone batteries in a bunch of projects recently after discovering an awesome little module on eBay. The module comes with a Li-ion charger and also a voltage regulator, allowing you to increase the voltage of the Li-ion battery from the normal 3.7v’s to up to 30V’s!

The other great thing about using old mobile phone batteries is you can get them for free! There are plenty of places that have mobile phone recycling bins where you can score a few batteries, free of charge. I have one at my work, which I periodically raid for batteries.

The other good news is the modules are very cheap to buy at only around $2 each.

This ible’ shows you how to connect the module along with a micro USB adapter so you can use the battery as a phone charger. It’s a simple project and will show you how to wire-up the module to use in any project of your choice.


## Step 1: Parts & Tools

![Step 1: Parts & Tools image 1](images/step01_01.jpg)

![Step 1: Parts & Tools image 2](images/step01_02.jpg)

![Step 1: Parts & Tools image 3](images/step01_03.jpg)

![Step 1: Parts & Tools image 4](images/step01_04.jpg)

Parts:

1. Li-ion Charger and step-up module - [eBay](https://www.ebay.com.au/itm/3-7V-9V-5V-2A-Adjustable-Step-Up-18650-Lithium-Battery-Charging-Discharge-I-J3Q3/264335034952?epid=23035413437&hash=item3d8b988a48:g:j~wAAOSw4YZc55Ns). The charger will also do Lipo batteries

2. Micro USB Adapter – [eBay](https://www.ebay.com.au/itm/5PCS-CJMCU-5V-Micro-USB-Interface-Power-Adapter-Board-Breakout-Module/264009126118?hash=item3d782b90e6:g:T~8AAOSw7Vtb1DPT&frcectupt=true). The micro USB that comes on the module for charging is slightly recessed which makes it hard to access in a project. I prefer to use a micro USB adapter to do this

3. USB Adapter – [eBay.](https://www.ebay.com.au/itm/10PCS-Type-A-DIP-Female-USB-To-2-54mm-PCB-Board-Adapter-Converter-For-Arduino-AU/362757031057?epid=18024876193&hash=item5476010491:g:2zQAAOSwSrVak60R&frcectupt=true) I used this so I could connect the phone to the module to charge it. If you are using it to power a project then it isn’t necessary – you just wire the project straight up to the module

4. Li-ion Battery. I used discarded ones one you can always buy on pretty cheaply on [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_sacat=0&_nkw=samsung+mobile+phone+battery&_sop=15).

5. Wire. I used resistor legs to connect everything together

The followingbisn't necessary but I decided to add it at the last minute. The voltage meter allows me to check the voltage of the battery easily for this build

1. Voltage meter - [eBay](https://www.ebay.com.au/itm/0-36-DC-4-40V-LED-Digital-Mini-Voltmeter-Gauge-Voltage-Meter-Gauge-Panel-Tester/153584158553?hash=item23c2544759:m:mbaXYKe2LzBwhZzQYgKvViQ)

2. Tactile switch - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR7.TRC0.A0.H0.Xtactile+switch.TRS0&_nkw=tactile+switch&_sacat=0)

Tools

1. Soldering Iron

2. Pliers

3. Wire cutters

4. Good double sided tape


## Step 2: The Charging Module and Li-ion Battery

![Step 2: The Charging Module and Li-ion Battery image 1](images/step02_01.jpg)

![Step 2: The Charging Module and Li-ion Battery image 2](images/step02_02.jpg)

![Step 2: The Charging Module and Li-ion Battery image 3](images/step02_03.jpg)

![Step 2: The Charging Module and Li-ion Battery image 4](images/step02_04.jpg)

![Step 2: The Charging Module and Li-ion Battery image 5](images/step02_05.jpg)

![Step 2: The Charging Module and Li-ion Battery image 6](images/step02_06.jpg)

![Step 2: The Charging Module and Li-ion Battery image 7](images/step02_07.jpg)

First a Little Info on Li-ion batteries

There’s a LOT of facts, do and don’ts etc about mobile phone batteries on the net. Here’s a few facts that most seem to agree on:

1. Mobile phone batteries don’t like to be overheated. I’m sure most of you would have seen the message that comes up on your phone when you have left it in the sun. If you are going to use one in a project, then make sure that it is not in direct sun all of the time

2. Mobile phone batteries can lose roughly 20% of their capacity only after 1000 charges. Mobile phones are power hungry beasts and once the battery starts to lose the ability to charge fully, you start to notice the phone needs more charging. Using an old phone battery will probably mean it won’t hold a full charge but even at 80% capacity the battery will still be able to do most things you want it to.

3. Li-ion batteries are fussy. This can be true. A battery is a massive ongoing chemical reaction sealed away inside a plastic cover. Put simply, Li-Ion batteries are fussy. They hate excess heat, stress, over voltage, under voltage and short circuit. The module has been designed to ensure the battery is charged correctly. I’ve used it to charge over 30 mobile phone batteries and have had no issues.

So where can you find mobile phone batteries for free? You probably have an old phone sitting in a draw somewhere that you can pull apart and get the battery out. Samsung, Google, HTC etc are all great as you can easily remove the backs and get the batteries out. Apple phone take more work because they hate to make things replaceable.

You can also raid the battery-recycling bin, which is what I usually do. There is one at my work I periodically check, which usually yields a few batteries.

Charging Module

The module used in this build ensures that the battery is charged to the right capacity and stops charging once the battery reaches aprox 4.2v. Finding information on this particular module on the net is a little difficult. It seems that every site selling this module just copied each others info! However, the basic information on the module can be found below:

Module Specifications:

Input voltage: 4.5-8V

DC Output voltage: 4.3-27V DC (Continuously adjustable)

Charging voltage: 4.2V DC

Charging current: Max. 1A

Discharging current: Max. 2A


## Step 3: Adding Some Solder to the Battery Terminals

![Step 3: Adding Some Solder to the Battery Terminals image 1](images/step03_01.jpg)

![Step 3: Adding Some Solder to the Battery Terminals image 2](images/step03_02.jpg)

The first thing that needs to be done is to add a little solder to the battery terminals

Steps:

1. First, if you look on the battery you will see that the solder points will be identified as positive and negative.

2. Heat-up the soldering iron so it is quite hot. You want to keep the soldering iron on the terminals for the shortest time possible.

3. Touch the soldering iron tip to the terminal and add a little solder to both the positive and negative terminals

Before I go any further, I like to charge the battery up to make sure it is working ok.


## Step 4: Initial Battery Charge

![Step 4: Initial Battery Charge image 1](images/step04_01.jpg)

![Step 4: Initial Battery Charge image 2](images/step04_02.jpg)

![Step 4: Initial Battery Charge image 3](images/step04_03.jpg)

![Step 4: Initial Battery Charge image 4](images/step04_04.jpg)

![Step 4: Initial Battery Charge image 5](images/step04_05.jpg)

![Step 4: Initial Battery Charge image 6](images/step04_06.jpg)

To ensure that the battery is taking charge I like to do the following:

Steps:

1. Solder a couple of breadboard jumper wires to the positive and ground battery solder points on the module. They should have a female end

2. Add a little solder to each of the battery terminals (see step 3) and solder another couple of breadboard wires, make them both male ends

3. Connect the breadboard wires from the battery to the module and plug in a mini usb cord and connect it to power. A little LED will come on. Wait until the LED changes colour which will indicate when the battery is charged.


## Step 5: Connecting the Module to the Battery

![Step 5: Connecting the Module to the Battery image 1](images/step05_01.jpg)

![Step 5: Connecting the Module to the Battery image 2](images/step05_02.jpg)

![Step 5: Connecting the Module to the Battery image 3](images/step05_03.jpg)

![Step 5: Connecting the Module to the Battery image 4](images/step05_04.jpg)

![Step 5: Connecting the Module to the Battery image 5](images/step05_05.jpg)

![Step 5: Connecting the Module to the Battery image 6](images/step05_06.jpg)

![Step 5: Connecting the Module to the Battery image 7](images/step05_07.jpg)

In this build, I stuck the module on top of the battery with some double-sided mounting tape. It isn’t necessary to do this but in this project I wanted to make it as compact as possible. If you were adding this into a project then you might want to add the module in a difference place

Steps:

1. Add some double-sided mounting tape to the bottom of the module.

2. Stick the module onto the top of the battery. Make sure that the battery “in” solder points are close to the battery terminals. It makes things easier when connecting the battery to the module.

3. To make the connections from the battery to the module I used resistor legs. First, solder the end of a leg to the positive solder point on the module

4. Bend the leg so it sits flat and solder the other end to the positive terminal on the battery

5. Do the same for the ground.


## Step 6: Setting the Voltage

![Step 6: Setting the Voltage image 1](images/step06_01.jpg)

![Step 6: Setting the Voltage image 2](images/step06_02.jpg)

![Step 6: Setting the Voltage image 3](images/step06_03.jpg)

![Step 6: Setting the Voltage image 4](images/step06_04.jpg)

![Step 6: Setting the Voltage image 5](images/step06_05.jpg)

![Step 6: Setting the Voltage image 6](images/step06_06.jpg)

The really great thing about this module is you can set the voltage output from 4.2v to 27v. This is awesome as it allows you to use the battery for a whole heap of different projects. There is a very small pot that you can turned to change the voltage

Steps:

1. First, solder a couple of wires to the output positive and negative on the module. These will allow you to easily attach the module to a multimeter to measure the voltage

2. Connect the multimeter to the module

3. To change the voltage output, grab a small phillips head and turn the pot slowly. You will see the voltage go either down or up. Set the module to your desired voltage. For this project I set the voltage output to 5v as I’m going to use it as a phone charger


## Step 7: Adding a Mirco USB Adapter

![Step 7: Adding a Mirco USB Adapter image 1](images/step07_01.jpg)

![Step 7: Adding a Mirco USB Adapter image 2](images/step07_02.jpg)

![Step 7: Adding a Mirco USB Adapter image 3](images/step07_03.jpg)

![Step 7: Adding a Mirco USB Adapter image 4](images/step07_04.jpg)

![Step 7: Adding a Mirco USB Adapter image 5](images/step07_05.jpg)

![Step 7: Adding a Mirco USB Adapter image 6](images/step07_06.jpg)

This isn’t really necessary if you are just using this as a phone charger. You can probably just connect the cord to the micro USB that is already on the module. I have found though that if you are using this module in a project, it is hard to access the micro USB as it is recessed in the module. I find that using a micro USB adapter enables you to make a small slot in your project and easier access the input on the micro USB for charging.

Steps:

1. Add a little double-sided tape to the bottom of the micro USC adapter. Note that you could just superglue all these parts as well. I choose not to in case I want to ever remove them

2. Stick it down onto the battery, making sure that it is close to the micro USB that comes on the module. There are a couple of solder points that you can use to attach the module and micro USB together

3. Again, I used resister legs to connect the 2 parts together.


## Step 8: Adding a USB Adapter

![Step 8: Adding a USB Adapter image 1](images/step08_01.jpg)

![Step 8: Adding a USB Adapter image 2](images/step08_02.jpg)

![Step 8: Adding a USB Adapter image 3](images/step08_03.jpg)

![Step 8: Adding a USB Adapter image 4](images/step08_04.jpg)

![Step 8: Adding a USB Adapter image 5](images/step08_05.jpg)

![Step 8: Adding a USB Adapter image 6](images/step08_06.jpg)

If you are going to use this battery in a project, then there really isn't any need to add a USB adapter. All you would do is connect ground and positive from your project to the output solder points on the module.

Steps:

1. Stick the USB adapter to the battery using double sided tape

2. Next, you need to connect the USB adapter to the output solder points on the module. Just do the same thing as the micro USB and add a couple resister legs to the solder points.

3. If you haven't already, plug the micro USB into a power adapter and charge up the battery.

At this stage you're ready to plug in a phone and charge it up. If you want to add a voltage display then check out the next step. However, it's not really necessary and the battery will charge your phone.

I kinda realised after I made this that the module might heat-up and as I mentioned at the start of this ible' li-ion batteries don't like to be hot. To counteract this, it would be good to add a heatsink under the module to protect the battery. If yo are using this to power a project then just don't stick the module onto the battery.


## Step 9: Adding a Voltage Meter

![Step 9: Adding a Voltage Meter image 1](images/step09_01.jpg)

![Step 9: Adding a Voltage Meter image 2](images/step09_02.jpg)

![Step 9: Adding a Voltage Meter image 3](images/step09_03.jpg)

![Step 9: Adding a Voltage Meter image 4](images/step09_04.jpg)

![Step 9: Adding a Voltage Meter image 5](images/step09_05.jpg)

![Step 9: Adding a Voltage Meter image 6](images/step09_06.jpg)

![Step 9: Adding a Voltage Meter image 7](images/step09_07.jpg)

So I did this at the last minute just t see what how it would work. It actually turned out ok so here's how I did it

Steps:

1. You will need a voltage meter and a momentary switch which you can find in the parts list.

2. Straighten one side of the legs on a momentary switch and add some solder

3. Add a couple of thin wires to the solder points on the voltage meter. You could use the wires that come on the meter but I found these were quite thick and wanted to use thinner ones

4. solder one leg of the switch to the positive battery solder point on the module. The other leg solder to the positive wire from the voltage meter

5. Solder the ground wire from the meter to the ground solder point on the module.

6. You can add a little super glue to hold the voltage meter in place. You can now monitor the voltage of the battery and work out when to charge


## Step 10: So What Next?

![Step 10: So What Next? image 1](images/step10_01.jpg)

![Step 10: So What Next? image 2](images/step10_02.jpg)

![Step 10: So What Next? image 3](images/step10_03.jpg)

Using the module and phone battery together allows you to use this set-up for many electronic projects. I have been using mobile phone batteries in place of 9v batteries on most of my projects of late. Having a rechargeable battery means firstly, I don't have to keep changing out batteries, and second, if I'm using an enclosure that doesn't allow easy access to the inside, a rechargeable battery means I don't have to worry about opening it everytime the battery goes flat

If you wanted to turn this project into a variable voltage supply you can just connect the voltage meter to the output on the module. The voltage meter will then display the voltage output and can be change by adjusting the mini potentiometer on the module.

Hope this project helps and happy making


---
*59 images archived*
