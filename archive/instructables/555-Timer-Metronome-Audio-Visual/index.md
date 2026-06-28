# 555 Timer Metronome - Audio & Visual

Source: https://www.instructables.com/555-Timer-Metronome-Audio-Visual/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

My son has recently started to play the ukulele and I thought a metronome would help with his timing. As a maker, I figured I could whip one up myself pretty easily with a 555 timer (what can’t you make with one…) After a little searching on the web I found a nice circuit which included a couple of timing LED’s for a visual reference which I thought was a nice touch.

The tick, ticking of the metronome isn’t very loud so I added a output jack to you an also listen to it through a set of headphones as well. The speed of the metronome is controlled by a potentiometer and has a good range of speeds.

Lastly, I used an old tobacco tin (I always have a bunch of these around to stick projects in) as the case which I think worked out well.

This is a pretty easy 555 project so if you have some basic experience putting circuits together then it should be a cinch. If you want to learn about circuits, then I did an ‘ible on making your first circuit which can be found [here](https://www.instructables.com/id/How-to-Build-Your-1st-Circuit/)


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

Parts:

1. 555 Timer – [eBay](https://www.ebay.com.au/itm/10-20-50-100PCS-NE555P-NE555-DIP-8-SINGLE-BIPOLAR-TIMERS-IC/263770865456?hash=item3d69f7ff30&var&_trkparms=ispr%3D1&enc=AQADAAAC4FjVrDbVsZ8oH%2F8PNHtt9VX4%2Fw7FZcmMuqsX8uaFEduVXRDIZzFRvPOpCg5qnj%2BzXQUZQ3Tm2KCpMCZAlSIM1gucm2aE0Kh1TEbHMCQG4JeMRPhQkmGzHuvsQb1q7GHF2zJy2ygG5sMlJHnciPeFWxWt34WLkcm0jgJ7C9hiUROy1wjVnue4zj9xnJva8ExLoAYCEMWCSv%2BkDFHkeisUx1yhY6OrLelVBuh3HH6lWWObF8kito7YZVhLDAGr4pCDKzAqS1h1PBwzn32zDA5N04SuRKi11RPF8i7CfxfHAX5wsBQ3b%2FoK8eT%2BZECchrqm9QdwSlaY8HGHk90%2FgvSZGx%2BWgR7ENikaFISJ%2FgV96rLi5Bejv%2BSsQTz03zK88K91LwPnWkX1AkTdTAJ%2BK4heD4eohSqlJoXFAbkusvVQGUIcgYvSknIC3eWw5q%2FCridSwNZ%2BoateKcS%2Bjx4%2BmgrIw35Hb%2BdjzN2KtFfhlJ9xrH%2F53Q4wrsTLXalvVdfuROs%2Fx1%2F7gs0J2kwxe1IWttbLjckQK7bp6ufvpJIUa4PdO1X%2BH6cWmXepv%2B0fFGhDkSHrFTKWRjcPPo6Lu1Co4k4RvA5aC3TU%2Fw7L3QS9nXcY47y%2F0yoWRTYWoueKxeJJq6C6PoMGXdKoZN92x1fjd%2FRqo994vgGnbmWjXofVI%2Fm4E9pU7c9s9ptykSquxVWXKFXHckTnFYkS3wp0dkCYIaii2V7P7lL70L3dCf4ayUlhN9Eg%2BQ%2FQmxGcQCQpYaBGPP8bAKtG7avhfN%2BlTtTSgsYEA7HsE771JjzMNzRuhAhGxCT7v6cQ4VwOZhvhvzQMBZoQpSHNglG%2F%2BYaB7EkaYMAs5vdtfLABebYE%2Bm375EEHdCxArDnk2gs8xLmXj5W0yEkVF60wey8anw%2FLAGHGIfNt5zF6Mk8l1QjgnsXVSBaFaitHp%2BuAe0o%2FOTzehs1MkyfjkVmzxDekVMPwEY99qvWQBPo%3D&checksum=263770865456d0916877704543d49d67cd36baa1c2b0&frcectupt=true)

2. 2 X 22uf Capacitors – [eBay](https://www.ebay.com.au/itm/50-100PCS-0-1-22UF-0-1-0-22-0-47-1-4-7-22UF-Electrolytic-capacitor-HOT-AU/323720284201?hash=item4b5f3b8829:m:mOwG6ziQTj2DaHOcniYtsOw) (you can also use 10uf if you want to)

3. 3 X 1K Resistors – [eBay](https://www.ebay.com.au/itm/100PC-1-6W-Metal-Film-Resistor-Tolerance-1-Full-Range-of-Values-0-to-10M/312423918540?hash=item48bdeaabcc:m:mEzu7yilmeDIBUw-KujJ0LQ)

4. 2 X 3/5mm LED’s – [eBay](https://www.ebay.com.au/itm/300pcs-3mm-5mm-LED-Diodes-Emitting-White-Yellow-Red-Green-Blue-Assorted-Kit-DIY/312341507678?hash=item48b9012e5e:g:GOoAAOSwPSxbUvec&frcectupt=true)

5. 1 X Prototype board – [eBay](https://www.ebay.com.au/itm/10x-DIY-Prototype-Paper-PCB-Experiment-Board-Bakelite-Circuit-Board-4-8x13-3cm/142759746052?hash=item213d24da04:g:sFUAAOSwcEha0XL3)

6. 1 X 100K Pot – [eBay](https://www.ebay.com.au/itm/4Pcs-A100K-100K-Ohms-Audio-taper-Potentiometer-Logarithmic-Pot-Split-shaft-New/330819772223?hash=item4d06651f3f:g:bDMAAOSwzRpaNAll) (the schematic has a 250K pot which will also work fine

7. 8 Ohm Speaker – [eBay](https://www.ebay.com.au/itm/Audio-Speaker-1pc-40mm-8Ohm-8-0-5W-Stereo-Woofer-Trumpet-Horn-Loudspeaker-Power/163285175018?hash=item26048e0aea:g:ypQAAOSwuVtbr0Xl)

8. Output audio jack – [eBay](https://www.ebay.com.au/itm/NEW-3-5mm-Female-5pin-Stereo-Headset-Interior-PCB-Mount-Audio-Jack-Socket-10-Pcs/123720223208?epid=18027027146&hash=item1cce4cc9e8:g:BkYAAOSw5VFWIwNt)

9. Switch – [eBay](https://www.ebay.com.au/itm/10-x-On-Off-On-Momentary-Mini-Toggle-Switch-Car-Motor-Dash-Dash-SPDT-3Pin-Sales/201939647988?hash=item2f048a7df4:g:ztcAAOSwIFtaCleh)

10. Old tobacco tin for the case (or something similar)– [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=tobacco+tin&_sacat=0)

11. Thin wire (I use computer ribbon cable which I source from my local e-waste facility for free)

12. 9v battery

13. 9v battery holder – [eBay](https://www.ebay.com.au/itm/Replacement-9V-Battery-Box-Case-Holder-Connector-F9Z4/233231320321?hash=item364dab8501&_trkparms=ispr%3D1&enc=AQADAAAC4FjVrDbVsZ8oH%2F8PNHtt9VX4%2Fw7FZcmMuqsX8uaFEduVlgePuulw4NrWcpFixsPu73lStkRhCdpRLkxincU60gPyu3BPq%2F4UR72Zk5jTf3Hj70PjbnKfPSYrs3ciKbc6LkaodVqx%2F3iB3h2UMDE8JbalOMt%2BUCNWt2JZ5CgvmijhlzH8h3jEZTtwtzIs%2FkL3NxHZTZkTgEf%2BnWEc5qrbPWfWzPttd6m%2BUxInD%2FpRCuTlhwwi352%2FSKibz7N4QiAnQKvfa3%2F1iWTctT8wzifIZlyTz5MLWmPpLP8Z6QX5oJl84exeqCQ%2FdBa3af9U%2F863gz%2FVHimer8MrqcZOOBxgIEM9Nx5WeAm0wwrK6if0bUkwpVq0MQsQgHjJRT8yAAwFwWQls084JwkYDreiCuBH5Yl8NS35ote9QQ5H%2F2JoktNE2sghiJBKhwHXVGBWdUsvsHweJwAjCqI3eLBSPMT1qRPvBStqKxN3FrWlkJMiv3DCN8ShSCXh4K1fP19fhb%2Fu0vL%2FAsPGei0lJu00CZHs3kLIXBpwxGczxrI0GyQiZDLHALppRCepv5vmaP0IfRV4O%2F7D3NL99xbvE7M4ZU%2FUfZStoLUBOrevxFelgUjzJLcu0GC83c3hW8Rg3M%2BaY4vx0uMJratTYGAFQxGQfySgVMAQDpBrt50wWiFMMngiz%2BlAm8F%2BsvgRC5WTfybATico61psqkTzZF0njd6yil8iyb9M1GcuvxryTfUPbumaona8ieMkxwLUd2FcfwxMZanBjqol7g4kQ0Rr%2BTV6cyS7UfVlxf0coTw1kbiGIZn0Pngdc45l7GWD%2B9Yn8dXuvShNLrwLQjW6p%2BvFBiJ2BlUmHDhE7fStemyarwHpfG2hCPRFFS69ZJPMi%2BVGTT39QaQLbV1HBh7r6%2BbbOm1Zl19St%2FwNaEhAztP8FnHlrZ%2FLlFV6Uvo%2BcjIw%2FbT6q92jrLc7FOAtrEJjuNEbHoatny1W6%2Fw%3D&checksum=233231320321f5cacc7630ee49beb3b27a620748c6b0)

Tools:

1. Soldering iron

2. Drill

3. Pliers

4. Hot glue

5. Super glue

6. Wire cutters

7. Double sided tape


## Step 2: Making the Circuit - Bread-boarding

![Step 2: Making the Circuit - Bread-boarding image 1](images/step02_01.jpg)

![Step 2: Making the Circuit - Bread-boarding image 2](images/step02_02.jpg)

Just a heads-up, I did make a couple of mistakes putting this circuit together as I had to do it from memory. they were easy fixes (I usually make at least one mistake when putting a circuit together) so just beware and use the circuit diagram as a guide. I will highlight where I made the mistake so you know where it is in the images.

The first thing to do in any electronic project is to breadboard it. This will help you understand the circuit and will show whether it’s working as it should. The other good thing about bread-boarding is you can make changes to the circuit and customise it.

This isn't a complex circuit but it's still always good practice to breadboard prior to soldering.


## Step 3: Making the Circuit - Part 1

![Step 3: Making the Circuit - Part 1 image 1](images/step03_01.jpg)

![Step 3: Making the Circuit - Part 1 image 2](images/step03_02.jpg)

![Step 3: Making the Circuit - Part 1 image 3](images/step03_03.jpg)

![Step 3: Making the Circuit - Part 1 image 4](images/step03_04.jpg)

![Step 3: Making the Circuit - Part 1 image 5](images/step03_05.jpg)

![Step 3: Making the Circuit - Part 1 image 6](images/step03_06.jpg)

Steps:

1. First, I like to add an IC holder to the prototype board. This way I can easily change the IC if it’s faulty or I burn it out

2. The prototype boards I use are great. You can buy these on eBay in lots of 10 and I used them for most of my prototyping. For this project, I only needed a small piece of board so I just used a pair of wire cutters and cut off a small piece.

3. I then usually make my way around the IC starting with pin 1 and add the connections. I won’t go through step by step how to make each connection as its pretty straight forward.

4. When connecting pins 2 and 6 on a 555 timer, I just use a leg from a resistor and connect these together on the solder side of the prototype board


## Step 4: Making the Circuit - Part 2

![Step 4: Making the Circuit - Part 2 image 1](images/step04_01.jpg)

![Step 4: Making the Circuit - Part 2 image 2](images/step04_02.jpg)

![Step 4: Making the Circuit - Part 2 image 3](images/step04_03.jpg)

![Step 4: Making the Circuit - Part 2 image 4](images/step04_04.jpg)

![Step 4: Making the Circuit - Part 2 image 5](images/step04_05.jpg)

Steps:

1. So here is where I made my mistake. It was with one of the resistors for the LED’s. I was using the breadboard circuit as a reference and messed-up how the LED’s were to be connected to pin 3. It meant that I added a resistor in the wrong spot. I didn’t work this out until I have done all of the wiring and had to move it after everything had been done. Pretty annoying but it worked out ok

2. Once you have all of the parts in place you then have to add wires so you can connect the circuit to all the other parts. I use computer ribbon for this as it’s thin, cheap (I get it for free at my local e-waste) and easy to use

3. The last thing to do is to connect the battery holder to the circuit. The positive wire on the holder will be connected to the switch


## Step 5: Adding a Speaker

![Step 5: Adding a Speaker image 1](images/step05_01.jpg)

![Step 5: Adding a Speaker image 2](images/step05_02.jpg)

![Step 5: Adding a Speaker image 3](images/step05_03.jpg)

![Step 5: Adding a Speaker image 4](images/step05_04.jpg)

![Step 5: Adding a Speaker image 5](images/step05_05.jpg)

![Step 5: Adding a Speaker image 6](images/step05_06.jpg)

![Step 5: Adding a Speaker image 7](images/step05_07.jpg)

I had a small speaker cover on hand so I decided to use this and mount it onto the top of the tobacco lid. If you don’t have one of these you can just drill a few holes directly into the lid and add the speaker to the bottom of it. I’ve done this plenty of times and it works well.

Steps:

1. First, measure where you need to drill any holes and add these to the lid. If you are drilling holes into tin you need to be careful as the tin is thin and can be damaged easily. To help prevent this, Place the lid top down on a piece of wood and drill through the bottom of the lid.

2. Once you have made your holes, you will need to mount the speaker. In my case I had to drill 4 holes for the screw points on the speaker grill and another hole for the wires

3. Secure the speaker into place with some super glue or hot glue. You may have to attach the wires from the circuit to the speaker first like I did before securing into place


## Step 6: The Case - Adding the Auxiliary Parts

![Step 6: The Case - Adding the Auxiliary Parts image 1](images/step06_01.jpg)

![Step 6: The Case - Adding the Auxiliary Parts image 2](images/step06_02.jpg)

![Step 6: The Case - Adding the Auxiliary Parts image 3](images/step06_03.jpg)

![Step 6: The Case - Adding the Auxiliary Parts image 4](images/step06_04.jpg)

![Step 6: The Case - Adding the Auxiliary Parts image 5](images/step06_05.jpg)

![Step 6: The Case - Adding the Auxiliary Parts image 6](images/step06_06.jpg)

The case I went for was an old tobacco tin. You don’t need much room in your case as the circuit is pretty small so you could use something like an altoids tin if you wanted to.

Steps:

1. You need to add the pot, audio output jack and switch to the case. Make sure to add the battery holder and circuit inside the case first and then work out the best places to add the auxiliary parts.

2. Drill 3 holes into the case big enough to fit the auxiliary parts into

3. Secure the parts into place

4. Place the battery and circuit back into the case and make sure everything fits ok

5. Lastly, add some good quality, double sided tape (I use an auto one which works well) and stick down the battery holder. Don’t stick down the circuit yet as you might need to make some changes to it.


## Step 7: Adding the LED's

![Step 7: Adding the LED's image 1](images/step07_01.jpg)

![Step 7: Adding the LED's image 2](images/step07_02.jpg)

![Step 7: Adding the LED's image 3](images/step07_03.jpg)

Next, you will need to add the LED’s somewhere on the case. I found that having a visual cue is also very handy.

Steps:

1. Work out the best place on the case to attached the LED’s.

2. Drill a couple of holes to fit them into the case

3. Use some hot glue or super glue to secure them

4. Don’t trim the legs yet as the different lengths will help you remember which is positive and which is ground


## Step 8: Soldering on All Those Wires.

![Step 8: Soldering on All Those Wires. image 1](images/step08_01.jpg)

![Step 8: Soldering on All Those Wires. image 2](images/step08_02.jpg)

![Step 8: Soldering on All Those Wires. image 3](images/step08_03.jpg)

![Step 8: Soldering on All Those Wires. image 4](images/step08_04.jpg)

![Step 8: Soldering on All Those Wires. image 5](images/step08_05.jpg)

![Step 8: Soldering on All Those Wires. image 6](images/step08_06.jpg)

![Step 8: Soldering on All Those Wires. image 7](images/step08_07.jpg)

It’s now time to solder that lot of spaghetti to the auxiliary parts and LED’s. This is the final step where you get to see whether the circuit will work first go or if you have to go over it and check to see if there are any short circuits or parts in the wrong place. It’s really hard to take images of this step so I really just have a few finished ones to show you want it looks like

Steps:

1. First, solder the switch wires. I usually solder the positive to the switch so connect the positive from the battery and the wire connected to positive from the circuit to the switch

2. Solder the 2 wires to the pot from the circuit.

3. Attach the 2 wires to the audio output jack

4. Solder on the wires for the LED’s. Make sure you get the polarity right by carefully checking the schematic

5. Add the battery and check to make sure the circuit is working. If not, check over your connections to make sure you didn’t forget anything and nothing is short circuited.

6. If everything is working as it should – congrats, you have pretty much finished. The last thing to do is to test to make sure the audio output works. Plug in some headphones and if you can hear the tick tock of the metronome then you’re done

7. You can even add an external speaker if you wanted to which would help increase the volume


---
*42 images archived*
