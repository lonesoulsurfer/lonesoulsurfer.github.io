# Head Phone Amp With Custom PCB

Source: https://www.instructables.com/Head-Phone-Amp-With-Custom-PCB/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

I've been building (and trying to perfect) the headphone amp for some time now. Some of you would have seen my previous 'ible builds. For those that haven't I have linked these below.

On my older builds I have always used prototype board to build the circuit. Nothing wrong with doing it this way mind you but there is more potential to make mistakes and it can be tricky trying to add all of the parts in the smallest space possible using prototype board.

I thought it was time to throw myself in the deep end and start to design my own PCB's! The Instructable crew have put together some training on how to do this which can be [found here](https://www.instructables.com/class/Circuit-Board-Design-Class/). I found the Sparkfun tutorial very helpful and primarily used this one to learn how to create my own PCB's. It's a great resource and easy to follow the step by step instructions.

The software to design the PCB's is eagle and is free to download. Just follow each of the tutorials below from Sparkfun and in no time you'll be designing your own as well.

However, If you just want to use my gerber files (the files you upload to the PCB printing company to make the board), then I've supplied them in this 'ible. All you need to do is to load the zip file up to a manufacturer such as [JLCPCB](https://jlcpcb.com/) and they'll print it up for you.

Sparkfun Tutorials

1st one to do : [Using EAGLE: Schematic](https://learn.sparkfun.com/tutorials/using-eagle-schematic/all)

2nd one to do: [Using EAGLE: Board Layout](https://learn.sparkfun.com/tutorials/using-eagle-board-layout)

You might be asking yourself right about now, what the hell is a headphone amp and why do I need one! Your phone doesn’t really have the power to drive a pair of headphones. You can hear this when you listen to music through your phone speakers, the sound sounds flat and has no real range. When you plug your headphones into a separate amp, you’ll be astonished at the level of audible improvement in clarity, detail and dynamics you get out of your speakers.

So let's get cracking.


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

Circuit

1. PCB. You can find the gerber files [here](https://drive.google.com/drive/folders/1khjtbpl3LDGxoIbwnCDU4SXZjNsY8nSS?usp=sharing). Instructables don't allow you to add zip files so I had to link it to my Google drive

2. 220 uF capacitors X 3 - [eBay](https://www.ebay.com.au/itm/10V-50V-High-Frequency-LOW-ESR-Radial-Electrolytic-Capacitors-105C-1uF-3300uF/264388201105?ssPageName=STRK%3AMEBIDX%3AIT&var=564005352631&_trksid=p2060353.m2749.l2649)

3. 4.7uF Capacitors X 3 - [eBay](https://www.ebay.com.au/itm/50PCS-50V-4-7uF-High-Frequency-LOW-ESR-Radial-Electrolytic-Capacitor-5X11mm/264397802400?hash=item3d8f564ba0:g:tuwAAOSwtKRdHsHs)

4. 22pf Capacitor X 2 - [eBay](https://www.ebay.com.au/itm/20Pcs-Pack-50V-10pF-10uF-Multilayer-Ceramic-Capacitors-Assorted-Kit-Wholesale-5/401563553242?hash=item5d7f0d8dda:g:qd8AAOSwLmlbPulT)

5. 3.5mm Headphone Jack Connector X 2 - [eBay](https://www.ebay.com.au/itm/10pcs-3-5mm-Headphone-Jack-Connector-Female-Stereo-Audio-Socket-5-Pin-PCB-Mount/153301421302?epid=8016332340&hash=item23b17a0cf6:g:vLUAAOSwAFFcEcY3)

6. 5532 IC - [eBay](https://www.ebay.com.au/itm/10PCS-NE5532P-NE5532-DIP-8-Dual-Low-Noise-Op-Amp-TI-IC-NEW/232812686621?hash=item3634b7ad1d:g:9YoAAOSwa69bKgik:rk:1:pf:1&frcectupt=true)

7. IC Dip 8 pin dip socket - [eBay](https://www.ebay.com.au/itm/20-50-100PCS-8pin-DIP-IC-Socket-Adaptor-Solder-Type-Socket-Pitch-Dual-Wipe-NEW/302772458949?hash=item467ea515c5:m:mU03b60t-BPlVH-Taq7boXA:rk:8:pf:0)

8. 18K Resistor X 2 - [eBay](https://www.ebay.com.au/itm/100PCS-1-4W-Metal-Film-Resistor-0-25W-1-Full-Range-of-Values-0-22-to-10M/312406630087?hash=item48bce2dec7:m:mFR91af2geS_bQCs6A2ZfSQ:rk:6:pf:0)

9. 68K Resistor X 4 - [eBay](https://www.ebay.com.au/itm/100PCS-1-4W-Metal-Film-Resistor-0-25W-1-Full-Range-of-Values-0-22-to-10M/312406630087?hash=item48bce2dec7:m:mFR91af2geS_bQCs6A2ZfSQ:rk:6:pf:0)

10. 470K Resistor - [eBay](https://www.ebay.com.au/itm/100PCS-1-4W-Metal-Film-Resistor-0-25W-1-Full-Range-of-Values-0-22-to-10M/312406630087?hash=item48bce2dec7:m:mFR91af2geS_bQCs6A2ZfSQ:rk:6:pf:0)

11. 20K Duel Potentiometer - [eBay](https://www.ebay.com.au/itm/2-Pcs-20K-B20K-Dual-Linear-RK097G-Sealed-Potentiometer-Pot-15mm-Shaft-6pins/162989019220?hash=item25f2e71054:g:CFAAAOSwroZayvhV)

12. Knob - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR7.TRC2.A0.H0.Xpotentiometer+knob.TRS0&_nkw=potentiometer+knob&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=volume+knob)

12. 5mm LED - [eBay](https://www.ebay.com.au/itm/100PCS-3MM-5MM-ASSORTED-COLOR-2-PIN-DIFFUSED-LED-LIGHT-EMITTING-DIODES-PACK-6C4/143275338014?var=442194138299&hash=item215be0291e:g:VRAAAOSweldc8JH8&frcectupt=true)

13. SPDT Switch - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2322090.m570.l1313.TR12.TRC2.A0.H0.Xspdt+switch.TRS0&_nkw=spdt+switch&_sacat=0)

Power

You can use a 9V battery if you want to. I wanted to be able to re-charge the amp so I used the following

1. Voltage regulator - [eBay](https://www.ebay.com.au/itm/3-7V-9V-5V-2A-Adjustable-Step-Up-18650-Lithium-Battery-Charging-Discharge-I-J3Q3/264335034952?epid=23035413437&hash=item3d8b988a48:g:j~wAAOSw4YZc55Ns&frcectupt=true)

2. Mobile Battery - I get most of mine from phone recycle bins but you can also buy them on [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2542782.m570.l1313.TR11.TRC1.A0.H0.Xsamsung+mobile+battery.TRS0&_nkw=samsung+mobile+battery&_sacat=0)

Check out [this Instructable](https://www.instructables.com/id/Reuse-Old-Mobile-Phone-Batteries/) on how to use these

Other Parts

1. Case - I used an old Tobacco tin

3. Wires


## Step 2: Schematic, Board and Gerber Files

![Step 2: Schematic, Board and Gerber Files image 1](images/step02_01.jpg)

![Step 2: Schematic, Board and Gerber Files image 2](images/step02_02.jpg)

In the link below you can find the schematic, board and gerber files. If you already use eagle then you can save the schematic and the board and add them to eagle to play around with.

If you want to just get the board made then save the Headphone Amp Zip file and you can then just send it to someone like [JLCPCB](https://jlcpcb.com/) (not affiliated) who will print it for you. Hit the "quote now" button on the website and then just upload the gerber files. easy.

FYI - I'm not affiliated with JLCPCB in any way - just find them easy to use.

[Link to Gerber files, eagle schematic and PCB - Version 1](https://drive.google.com/drive/folders/1JADVR2uCMUSsN8Ugm_yViibeqSS7GWDv?usp=sharing)

[Link to Gerber files, eagle schematic and PCB - Version 2](https://drive.google.com/drive/folders/1PK22g43kLWdS6ySFPT6xD8JQK1qT_ESt?usp=sharing)

NOTE: I revisited this PCB and made a smaller. The files can be found in version 2 link


- [Headphone Amp 1](pdfs/Headphone Amp 1.pdf)

## Step 3:


## Step 4: Soldering the PCB Together

![Step 4: Soldering the PCB Together image 1](images/step04_01.jpg)

![Step 4: Soldering the PCB Together image 2](images/step04_02.jpg)

![Step 4: Soldering the PCB Together image 3](images/step04_03.jpg)

![Step 4: Soldering the PCB Together image 4](images/step04_04.jpg)

![Step 4: Soldering the PCB Together image 5](images/step04_05.jpg)

![Step 4: Soldering the PCB Together image 6](images/step04_06.jpg)

![Step 4: Soldering the PCB Together image 7](images/step04_07.jpg)

I'm not going to do a step by step on how to do this as it's pretty straight forward. All of the values of the components are on the board and you just need to follow this. However, below are a few tips on the best way to do it.

Steps:

1. The best components to start with in my opinion are the resistors. These are all the same size and you can lay the board on it's back and they will sit flush with the board making them easy to solder into place

2. When adding the audio jacks you might find that one of the 5 legs is slightly off. Just take your time and use a small screwdriver to slightly bend it out so it fits into the hole.

3. Use good quality capacitors. These will help get great sound out of the amp

4. If you know what case you are going to add the amp to, ensure that the capacitors aren't too high for the case. If they are you can always lay them down like I did in order for them to fit. Actually didn't need to do it in the end because I used a difference case.

5. The circuit board will be attached via the audio jacks and volume potentiometer. make sure you take that into consideration when thinking about a case.

6. It's always good to test the board once it has been built and before it's added into a case.


## Step 5: What Case to Use

![Step 5: What Case to Use image 1](images/step05_01.jpg)

![Step 5: What Case to Use image 2](images/step05_02.jpg)

![Step 5: What Case to Use image 3](images/step05_03.jpg)

![Step 5: What Case to Use image 4](images/step05_04.jpg)

You can use whatever case that takes your fancy. I like to add them into old [tobacco tins](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1311.R1.TR12.TRC2.A0.H0.Xtobacco+tin.TRS0&_nkw=tobacco+tins&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=tobaccotin) as they come all ready to use. I've used [NES controllers](https://www.ebay.com.au/itm/Classic-NES-Style-Retro-Game-USB-Controller-Gamepad-Joystick-Joypad-For-PC/122368176185?hash=item1c7db63039:g:n7IAAOSw32lYrg5R&frcectupt=true) before as well which are fun to do but there is a lot less room in one of those.

If you can't find any tobacco tins then you could an [Altoids tin](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.XAltoids+tin.TRS0&_nkw=Altoids+tin&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=tobacco+tins), [projects box](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR12.TRC2.A0.H0.Xproject+box.TRS0&_nkw=project+box&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=Altoids+tin), literally any small container that will fit the parts inside will do.


## Step 6: Adding the Parts to the Case - Circuit Board

![Step 6: Adding the Parts to the Case - Circuit Board image 1](images/step06_01.jpg)

![Step 6: Adding the Parts to the Case - Circuit Board image 2](images/step06_02.jpg)

![Step 6: Adding the Parts to the Case - Circuit Board image 3](images/step06_03.jpg)

![Step 6: Adding the Parts to the Case - Circuit Board image 4](images/step06_04.jpg)

![Step 6: Adding the Parts to the Case - Circuit Board image 5](images/step06_05.jpg)

Steps:

1. First, place all of the parts inside the case and work out how you want everything laid out inside. You need to fit the circuit board, battery and charging module (if you aren't using a 9v battery). Once you know where everything is going, the next thing to is to secure the circuit board

2. Make a small template of the front of the board using a piece of masking tape. Make there the potentiometer and 2 audio jacks are on the tape and then stick this to the case

3. Carefully drill the holes for each of the components. Tobacco tins are quite thin so be careful when drilling.

4. Secure the pot and audio jacks in place with the nuts that come with them


## Step 7: Adding the Parts to the Case - Battery, Switch & LED

![Step 7: Adding the Parts to the Case - Battery, Switch & LED image 1](images/step07_01.jpg)

![Step 7: Adding the Parts to the Case - Battery, Switch & LED image 2](images/step07_02.jpg)

![Step 7: Adding the Parts to the Case - Battery, Switch & LED image 3](images/step07_03.jpg)

![Step 7: Adding the Parts to the Case - Battery, Switch & LED image 4](images/step07_04.jpg)

I went with a rechargeable battery and charging module to power the circuit. If you don't want to do this then just use a 9v battery. I did an Instructable on how to use the module and adding it to a Li-ion battery which you can [find here](https://www.instructables.com/id/Reuse-Old-Mobile-Phone-Batteries/)

Steps:

1. First, secure the charging module to the battery with some good, double sided tape

2. Place the battery inside the case and mark where the micro USB on the module needs to accessed.

3. Make a couple small holes in the case for the micro USB and use some small files to make the hole rectangular.

4. Secure the battery into the case with some more double sided tape and make sure that the USB aligns with the hole in the case

5. For the switch, I initially was going to add this to the side of the case and made a hole for it but decided to add it inside the case. The main reason being, the other ones I have made the amp sometimes turns on in my pocket because of the switch. having it inside the case means this can't happen.

6. I used the hole I made for the switch for the LED. As the hole was rectangle I decided to add a small piece of opal acrylic which is a great diffuser and place the LED behind this.


## Step 8: Using Your Amp

![Step 8: Using Your Amp image 1](images/step08_01.jpg)

![Step 8: Using Your Amp image 2](images/step08_02.jpg)

![Step 8: Using Your Amp image 3](images/step08_03.jpg)

![Step 8: Using Your Amp image 4](images/step08_04.jpg)

Now that the build is done it's time to try out your amp

1. You have an audio input and output jack. The one on the left is output and that's where you plug your headphones into. The other is where you plug your phone or MP3 player into.

2. make sure that the volume is turned down at at least mid-way. you don't want to blow your eardrums if it is too loud!

3. Turn on the amp and start to play music. The sound should be clear, have more bass, and overall have a richer sound then just listening through your headphone.


## Downloads

- [Headphone Amp 1](pdfs/Headphone Amp 1.pdf)

---
*31 images archived*
