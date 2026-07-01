# Programmer for ATtiny 85

Source: https://www.instructables.com/Programmer-for-ATtiny-85/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

Make your own ATtiny 85 programmer using an Arduino Nano and a custom made PCB!

I've been building a few projects of late that use a ATtiny 85 microcontrollers and wanted to create a specifically designed programmer to make the job easier.

If you are an old hand with programming ATtiny 85's or a total novice and want to learn, then this bit of kit is essential. Once you have the hardware, programming the ATtiny becomes quite simple. I did do an 'Ible on how to Program a ATtiny with an Arduino which you can find here. Note that I was only really just learing then myself and did the Ible so I wouldn't forget how to do it! However, the programmer I did make was rudimental and I wanted something more permanent.

Along with the build of this project, I'll run through how to program the ATtiny 85 and get the blinking light sketch to work. Once you have conquered that - the sky's the limit!

This build was inspired by [SF94's](https://www.instructables.com/member/SF94/) build on [Instructables](https://www.instructables.com/Compact-Attiny-138584-Programmer-Using-Arduino-Nan/)


## Supplies

![Supplies image 1](images/step01_01.jpg)

![Supplies image 2](images/step01_02.jpg)

![Supplies image 3](images/step01_03.jpg)

![Supplies image 4](images/step01_04.jpg)

Along with the hardware below, you will also need to get one of the custom PCB's printed. I've explained how to do this in the next step.

PARTS:

1. Arduino Nano - [Ali Express](https://www.aliexpress.com/w/wholesale-aduino-nano.html?spm=a2g0o.home.auto_suggest.3.7f2776db9rTDeg)
2. Header Pins Female - (Length - 15 pins) X 2 - [Ali Express](https://www.aliexpress.com/w/wholesale-header-pins-female-15.html?spm=a2g0o.productlist.search.0)
3. Header Pins female - (2X3) - [Ali Express](https://www.aliexpress.com/w/wholesale-header-pins-2-X-6.html?spm=a2g0o.productlist.search.0)
4. Zif 14 ic socket - [Ali Express](https://www.aliexpress.com/w/wholesale-zif-14-ic-.html?spm=a2g0o.productlist.search.0)
5. 330R Resistors X 4 - [Ali Express](https://www.aliexpress.com/w/wholesale-resistor-metal-film.html?spm=a2g0o.productlist.search.0)
6. LED - 3mm (any colours) X 4 -[Ali Express](https://www.aliexpress.com/w/wholesale-led-3mm-assorted.html?spm=a2g0o.productlist.search.0)
7. 10uf Capacitor - [Ali Express](https://www.aliexpress.com/w/wholesale-10uf-electrolytic-capacitor.html?spm=a2g0o.productlist.auto_suggest.2.63c3Xr6wXr6wQK)


## Step 1: Getting the PCB Printed

![Step 1: Getting the PCB Printed image 1](images/step02_01.jpg)

![Step 1: Getting the PCB Printed image 2](images/step02_02.png)

![Step 1: Getting the PCB Printed image 3](images/step02_03.png)

Firstly, you can find all of the files including the gerber files for this build in my [GitHub Page](https://github.com/lonesoulsurfer/ATtiny_85_Programmer)

To get your board printed, You’ll need to send the Gerber files to a PCB manufacturer like [JLCPCB](https://jlcpcb.com/?from=VGBA&gad_source=1&gclid=CjwKCAiAjfyqBhAsEiwA-UdzJCxT2LUX1iS0CvS4HVuZlxetrU2JQNyu0nueQUivgEq7MzfoGlH54RoClQ8QAvD_BwE) (Not affiliated) who will print the boards for you. Jump into my Google Drive link, download the Gerber file to your computer and then send them off to your PCB manufacturer of choice.

If you have no idea how to do this well, I've put together an Instructable on how to get your broads printed which you can find [here](https://www.instructables.com/How-to-Get-a-PCB-Printed-Using-Gerber-Files/).

If you are interested in having a look at the schematic or board files then I have included these as well and you can also find them in my Google Drive. I've also attached the schematic to this step.


## Step 2: Adding Components to the PCB Part 1

![Step 2: Adding Components to the PCB Part 1 image 1](images/step03_01.jpg)

![Step 2: Adding Components to the PCB Part 1 image 2](images/step03_02.jpg)

![Step 2: Adding Components to the PCB Part 1 image 3](images/step03_03.jpg)

![Step 2: Adding Components to the PCB Part 1 image 4](images/step03_04.jpg)

![Step 2: Adding Components to the PCB Part 1 image 5](images/step03_05.jpg)

This is pretty straight forward as there really aren't many components to add to the PCB!

STEPS:

1. Always stsrt with the lowest profile components which in this case is the resistors
2. Solder the 4 LED's into place. 3 of these are indicators when the sketch is uploading, the other is for the blink skech whih we will load upa little laer to the ATtiny. It's a simple way to make sure everything is working as it should be.
3. Next you can add the header pins in for the capacitot. The capcitor is removable as you can sometimes have issues with loading Sketches when it is in place.
4. I've also included a header pin so you can use jumper wires to connect to an ATtiny if it is soldered in place to a PCB. This can also be soldered into place.
5. Now you can add the Arduino to he PCB. Make sure that you add the header pins in first to the Arduino and then solder it intp place to the PCB. It will ensure that the Arduino is lined up right and the header pins go in straight


## Step 3: Adding Components to the PCB Part 2

![Step 3: Adding Components to the PCB Part 2 image 1](images/step04_01.jpg)

![Step 3: Adding Components to the PCB Part 2 image 2](images/step04_02.jpg)

![Step 3: Adding Components to the PCB Part 2 image 3](images/step04_03.jpg)

![Step 3: Adding Components to the PCB Part 2 image 4](images/step04_04.jpg)

![Step 3: Adding Components to the PCB Part 2 image 5](images/step04_05.jpg)

![Step 3: Adding Components to the PCB Part 2 image 6](images/step04_06.jpg)

![Step 3: Adding Components to the PCB Part 2 image 7](images/step04_07.jpg)

Now it's time to add he ZIF socket IC holder. This is an easy way o hold he ATtiny into place whist you are programming it

STEPS:

1. Place the socket holder ino place in he PCB
2. Make sure that the little lock handle is facing down towards the LED's
3. Now you can solder it into place
4. Trim the capacitor legs and place into the 2 header pin. I have indicaed on the board wih a little - symbol which leg of the cap needs to go to ground.
5. Lastly, add a ATtiny to the ZIP socket holder

That's it - you are now ready to sart programming your ATtiny


## Step 4: Programming the ATtiny 85

![Step 4: Programming the ATtiny 85 image 1](images/step05_01.jpg)

![Step 4: Programming the ATtiny 85 image 2](images/step05_02.jpg)

![Step 4: Programming the ATtiny 85 image 3](images/step05_03.gif)

I've actually done an 'Ible now how to program the ATtiny using a Aduino Nano which you can find [here](https://www.instructables.com/How-to-Program-a-ATtiny-With-Arduino/)

However, I've also gone through he process again in the vid that you can find in the intro

STEPS:

1. Once you are ready to upload the blink sketch to the ATtiny (just follow the steps in the vid or the link above), open the 'blink sketch' in my Google Drive
2. Upload the sketch to your ATtiny 85
3. Watch the little LED blink away!

Once you have mastered this basic upload to the ATtiny, you can then move on to more fun things like[these games](https://www.instructables.com/Tiny-Arcade-Game-Attiny85/)that I made, or whatever projects that you can find on line. You might even want to try your hand at coding! baby steps first.

I hope this Instrucable was of some help - if you have any questions, please don't hesitate to add a comment and let me know!

All the best

Lonesoulsurfer


---
*23 images archived*
