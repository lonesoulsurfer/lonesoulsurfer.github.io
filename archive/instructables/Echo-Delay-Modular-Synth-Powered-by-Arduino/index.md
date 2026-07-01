# Echo / Delay Modular Synth - Powered by Arduino

Source: https://www.instructables.com/Echo-Delay-Modular-Synth-Powered-by-Arduino/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

Adding delay to any synth can add fantastic depth to the sonic soundscape. In this build I use an Arduino Nano to create a little module that can be used on a modular synths or as a stand along synth. It's an easy build with minimal components needed and the finished module sounds great!

Just a quick note on my modular synth. The one that I have put together is a bit of a cheats version where most of the modules are powered by an Arduino Nano. It means that I don't have to worry about tuning, playing around with 1v/octave controlled voltages etc. Everything is always in tune and simple to use in my cheats modular synth :)

I've built a number of [delay/echo synths](https://www.instructables.com/Dub-Siren-DelayReverb-2-in-1-Synth-Little-Synths-W/) in the past using the awesome [PT2399 IC.](https://www.electrosmash.com/pt2399-analysis) However, I kept on running into issues when trying to use the PT2399 with my modular synth. I found that I had to isolate the ground in my mixer for all of the other synths connected to it which caused a lot of headaches. I even went so far as to add ground isolating switches to each input on my mixer!

I've called the delay module 'Ekoplazm' which is also the name for a [little synth I built a couple years go](https://www.instructables.com/Dub-Siren-DelayReverb-2-in-1-Synth-Little-Synths-W/)! This new module is super simple to use and features a delay with 6 selectable delay times (63 to 300ms), and a reversable action as well.

Let's get cracking.


## Supplies

![Supplies image 1](images/step01_01.jpg)

![Supplies image 2](images/step01_02.jpg)

![Supplies image 3](images/step01_03.jpg)

The following is a list of components needed to build the synth. You can also find attached a PDF of the parts list in case you want to print it off. You can also find all the files in this build on my [GitHub](https://github.com/lonesoulsurfer/Delay_Modular_Synth) page. On the next step you'll find all of the info to have the PCB's printed.

PARTS:

1. Capacitor Polyester - [Ali Express](https://vi.aliexpress.com/w/wholesale-capacitor-100nf.html?spm=a2g0o.productlist.search.0)
2. 33nf X 2
3. 100nf X 4
4. 220nf X 1
5. Electrolyte (ERS) - [Ali Express](https://vi.aliexpress.com/w/wholesale-capacitor-esr.html?spm=a2g0o.productlist.search.0)
6. 2.2uf X 1
7. 100uf X 2
8. Diode - 1N4148 X 1 - [Ali Express](https://vi.aliexpress.com/w/wholesale-1n4148.html?spm=a2g0o.productlist.search.0)
9. Resistor Metal Film - [Ali Express](https://vi.aliexpress.com/w/wholesale-resistor-metal-film.html?spm=a2g0o.productlist.search.0)
10. 10K X 1
11. 100K X 1
12. 4.7K X 2
13. 2.2K X 2
14. 6.8K X 1
15. 100R X 1

Switch Toggle (stitch pin end) X 2- [Ali Express](https://vi.aliexpress.com/item/1005001510219617.html?spm=a2g0o.order_list.order_list_main.126.21ef1802tppsV9&gatewayAdapt=glo2vnm)

Switch momentary PB86-A1 X 1- [Ali Express](https://vi.aliexpress.com/item/32969818198.html?src=google&src=google&albch=shopping&acnt=708-803-3821&slnk=&plac=&mtctp=&albbt=Google_7_shopping&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&albcp=19374198223&albag=&trgt=&crea=en32969818198&netw=x&device=c&albpg=&albpd=en32969818198&gad_source=1&gclid=CjwKCAiA9ourBhAVEiwA3L5RFqxPIcgD8KLtHe2K-5nYnzxF6l2BSeOxHVyCcuQODW7zW8VA1BFBgBoCnpkQAvD_BwE&gclsrc=aw.ds&aff_fcid=fd5ee7b4cf4949878a24567d90bcdf1e-1701048621355-03264-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=fd5ee7b4cf4949878a24567d90bcdf1e-1701048621355-03264-UneMJZVf&terminal_id=ce8ce011cffc41efa37aa35ced5d12db&afSmartRedirect=y&gatewayAdapt=glo2vnm)

Audio Socket PJ301M X 2- [Ali Express](https://vi.aliexpress.com/item/1005005352992401.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.3.79e8oSDKoSDKlL&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=fbbe9b5c-27f0-4bb1-845b-4fd955b2e5f3&_t=gps-id:pcDetailTopMoreOtherSeller,scm-url:1007.40050.354490.0,pvid:fbbe9b5c-27f0-4bb1-845b-4fd955b2e5f3,tpp_buckets:668%232846%238112%231997&pdp_npi=4%40dis%21AUD%2111.21%2110.65%21%21%2153.35%2150.68%21%4021032dcb17247320167598620e5367%2112000032717531978%21rec%21AU%21129764711%21XZ&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A)

Arduino Nano X 1 - [Ali Express](https://vi.aliexpress.com/w/wholesale-arduino-nano.html?spm=a2g0o.detail.search.0)

Socket and wire JST PH 2.00mm X 1 - [Ali Express](https://vi.aliexpress.com/item/1005005939956886.html?spm=a2g0o.productlist.main.7.7e264a70WvNDdM&algo_pvid=b63886e7-4a9b-476c-a3a7-6728c5570c76&aem_p4p_detail=202408262116298398603954887850001041877&algo_exp_id=b63886e7-4a9b-476c-a3a7-6728c5570c76-3&pdp_npi=4%40dis%21AUD%215.18%214.77%21%21%2124.65%2122.68%21%402140d2dc17247321890732393e7a9d%2112000035184099770%21sea%21AU%21129764711%21X&curPageLogUid=ZBXPr2hTlgeC&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202408262116298398603954887850001041877_1)


- [Parts List](pdfs/Parts List.pdf)

## Step 1: PCB and Front Panel

![Step 1: PCB and Front Panel image 1](images/step02_01.jpg)

![Step 1: PCB and Front Panel image 2](images/step02_02.png)

![Step 1: PCB and Front Panel image 3](images/step02_03.png)

![Step 1: PCB and Front Panel image 4](images/step02_04.png)

We all have different levels of knowledge, so when it comes to a build like this I want to make sure that I'm providing enough information so anyone with some basic soldering skills can make it. That includes ensuring there are instructions on how to get your own PCB's printed (which is super easy!)

So with that said, the first thing you will need to do is to get the front panel and PCB printed. I use [JLCPCB](https://jlcpcb.com/?from=VGS&utm_source=google&utm_medium=cpc&utm_campaign=14177189905&gad_source=1&gbraid=0AAAAABS1QqkiD3-WAMC-R-0N6a2KKPawu&gclid=CjwKCAjwwe2_BhBEEiwAM1I7sfAjCecAjlW7BgEzggjBf0WNDCA4-ZMBy2IrNS7NcwcA4naAhj0_2xoCA-4QAvD_BwE) (not affiliated) to get this done. The front panel is actually just a PCB without any components included! The front panel design is done in a program called [Inkscape](https://inkscape.org/) (available free) and the panel including the drilled holes is done in [Fusion 360](https://www.autodesk.com/products/fusion-360/personal) (also free!)

The files that you need to build your own Ekoplasm Synth can be found in my [GitHub](https://github.com/lonesoulsurfer/Delay_Modular_Synth) page. This includes the parts list, Gerber files for the PCB & front panel, schematic, Arduino script etc.

STEPS:

1. Send the Gerber files to a PCB manufacturer like [JLCPCB](https://jlcpcb.com/?from=VGBA&gad_source=1&gclid=CjwKCAiAjfyqBhAsEiwA-UdzJCxT2LUX1iS0CvS4HVuZlxetrU2JQNyu0nueQUivgEq7MzfoGlH54RoClQ8QAvD_BwE) who will print the PCB and front panel for you. Download all of the files from my [GitHub](https://github.com/lonesoulsurfer/Delay_Modular_Synth) page to your computer and send the zipped Gerber files (PCB and front panel) off to the PCB manufacturer of choice.
2. If you have no idea what any of the above means, then check out the Instructable I made on how to get your broads printed which can be found [here](https://www.instructables.com/How-to-Get-a-PCB-Printed-Using-Gerber-Files/).
3. NOTE: The manufacture will include an order number on both the PCB and front panel. It doesn't really matter where it is on the PCB but you don't want it on the front on the front panel!
4. Over at JLCPCB you can 'specify a location' once the Gerber files have been loaded so click this for the front panel and specify in the comment section that you want the order number on the back of the panel. The manufacturer will add it to the back where indicated.


- [Parts List](pdfs/Parts List.pdf)

## Step 2: Adding the Components to the PCB - Part 1

![Step 2: Adding the Components to the PCB - Part 1 image 1](images/step03_01.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 2](images/step03_02.jpg)

![Step 2: Adding the Components to the PCB - Part 1 image 3](images/step03_03.jpg)

As the PCB is 2 sided, the order you add the components does matter. If you get it wrong it's not the end of the world but it might make it a little harder to add some component.

STEPS:

1. As always, start with the lowest profile components, in this case it's the resistors and diode. Its always good practice to check your resistors values before soldering in case you have to troubleshoot later on.
2. I've included a mini JST connector to power the board. Solder the connecter next into place.
3. A quick note on powering the synth. As I only need positive and ground I have used a JST connector to connect it to power. However, I have included space to add a Eurorack 16 pin adapter in case you want to power it using traditional Eurorack power sources
4. You can now add the capacitors, start with the polyester caps and then add the electrolytic caps.
5. I left adding the Arduino in place until I had populated the other side of the board. I found that it was easier to do this as the header pins wouldn't be in the way.


## Step 3: Adding the Components to the PCB - Part 2

![Step 3: Adding the Components to the PCB - Part 2 image 1](images/step04_01.jpg)

![Step 3: Adding the Components to the PCB - Part 2 image 2](images/step04_02.jpg)

Now it's time time to add the components to the front of the PCB.

STEPS:

1. First place the momentary switch into the PCB and solder into place.
2. Now you can add the toggle switches. Note that you should secure the PCB with a helping hand or something similar to keep it steady
3. Now you can solder the 2 audio sockets into place.

That's it for the components on the front of the panel!


## Step 4: Adding the Arduino

![Step 4: Adding the Arduino image 1](images/step05_01.jpg)

![Step 4: Adding the Arduino image 2](images/step05_02.jpg)

![Step 4: Adding the Arduino image 3](images/step05_03.jpg)

![Step 4: Adding the Arduino image 4](images/step05_04.jpg)

Now it's time to add the Arduino. I always include header pins so the Arduino is removable. It helps if you have to replace the Arduino and also allows you to program it when it isn't in the board. Plus, if the Arduino fails for whatever reason, you can easily remove and replace it.

STEPS:

1. Add the header pins to the Arduino and then place them into the PCB and solder into place.
2. If you need to, you can still get under the components under the Arduino by removing it from the header pins.


## Step 5: Loading the Arduino Sketch

![Step 5: Loading the Arduino Sketch image 1](images/step06_01.png)

If you are new to Arduino and want learn how to upload a sketch to Arduino - then check out [this link](https://support.arduino.cc/hc/en-us/articles/4733418441116-Upload-a-sketch-in-Arduino-IDE). It's really straight forward and doesn't need any special tools - just a computer and a USB cord.

STEPS:

1. Open the sketch in the Arduino folder which will take you to Arduino IDE. This can be found in the folder that you downloaded from my [GitHub](https://github.com/lonesoulsurfer/Delay_Modular_Synth) page
2. Connect your Arduino and upload the sketch
3. Once the sketch is loaded to Arduino you can connect it to the PCB for testing.
4. Connect the PCB to a 9V to 12V power source and check that the synth works. Plug a speaker in to the 'out' jack, connect the 'In' jack to another synth or even to your phone and hit the delay button. You should hear the delay kick in.
5. If you're not hearing anything, then you might need to do some troubleshooting.


## Step 6: Adding the Front Panel

![Step 6: Adding the Front Panel image 1](images/step07_01.jpg)

![Step 6: Adding the Front Panel image 2](images/step07_02.jpg)

![Step 6: Adding the Front Panel image 3](images/step07_03.jpg)

![Step 6: Adding the Front Panel image 4](images/step07_04.jpg)

![Step 6: Adding the Front Panel image 5](images/step07_05.jpg)

![Step 6: Adding the Front Panel image 6](images/step07_06.jpg)

STEPS:

1. The front panel has been designed so it fits perfectly onto the PCB. Carefully place the front panel so it aligns with the components and push it into place. I usually start with the toggle switches facing downwards and then just slide the panel into place.
2. The rectangle hole in the front panel for the momentary switch is a bit of a tight fit. If you find that it is sticking, then just file down the edge of the front panel where it is getting caught.
3. As there is nothing to secure the bottom of the front panel to the PCB, I have added a couple holes so you can add some spaces (Size - M2) and ensure that the bottom section is connected.
4. The nuts for the audio jacks and toggle switches will hold the top section of the front panel to the PCB
5. Now that the front panel is in place, you can either make an individual case to house it in or add it to your Eurorack.


## Step 7: How to Play

![Step 7: How to Play image 1](images/step08_01.jpg)

![Step 7: How to Play image 2](images/step08_02.jpg)

This will probably be the quickest 'how to play' that I have written as the synth is super simple to use

STEPS:

1. Connect a 3.5mm cable to the 'out' on a synth and then connect the other end to 'in' on the Ekoplasm synth
2. Connect the 'out' from the Ekoplasm synth to a speaker or mixer.
3. Now turn the synth on and then the Ekoplasm. Note that if you turn on the Ekoplasm first, you'll hear a bunch of feedback looping.
4. Now hit the 'delay' button. There are 6 selectable delay times (63 to 300ms) where the LED will be on. When you get to the reversable action, the LED will be off on the momentary switch.
5. I have also added a 'FX' switch. This just reduces the delay sound effect and makes it more subtler.

That's it! Check out the vid on the front page to see it in action.


## Downloads

- [Parts List](pdfs/Parts List.pdf)
- [Parts List](pdfs/Parts List.pdf)

---
*29 images archived*
