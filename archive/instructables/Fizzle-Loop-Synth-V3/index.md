# Fizzle Loop Synth V3 (555 Timer)

Source: https://www.instructables.com/Fizzle-Loop-Synth-V3/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

This is my 3rd Fizzle Loop Synth circuit and it builds on the previous 2 which can be found [here](https://www.instructables.com/id/Fizzle-Loop-Synth-555-Timer/) and [here](https://www.instructables.com/id/Fizzle-Loop-Synth-II/).

The heart of the synth is 3, 555 Timer IC's which are used to make some really interesting beeps and boops. The difference between this version and the others is; I have reduced the number of IC's down to 3 (version 2 have 4!), the rhythms and sounds you can make from this version are in my opinion are better and lastly, there is a drum sound option which gives some really cool beats.

I also have shrunk this synth into a pocket sized one. By placing some of the capacitors directly onto switches and shrinking the prototype board down, I managed to stuff all of the pots, switches and components into a small flashlight case.

You could probably use something like an altoids tin as a substitute case.

I have also been playing around with designing schematics and have included a circuit diagram which (I hope!) is easy to understand. I've also decided not to do a step by step guide to making the circuit as I don't really think it helps too much. However, if I'm wrong let me know and I'll do it in the future. What I have done instead is described some of the trickier sections and have added explanations where necessary. Such as what a [Vactrol](https://en.wikipedia.org/wiki/Resistive_opto-isolator) is and how to make one.

[Hackaday](https://hackaday.com/?gclid=CjwKCAiA58fvBRAzEiwAQW-hzTZV1eEwLdO0Vsn_N4EfrDxyIFbPlYwbiKsXVcXBxF25Cwtvi60QjhoCY7cQAvD_BwE) were nice enough to do a review of this project which can be found [here](https://hackaday.com/2019/04/05/fizzle-loop-synth-does-it-with-555-timers/)

Finally - I've made a video of the synth in action so check that out to hear how it sounds.


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

![Step 1: Parts image 3](images/step01_03.jpg)

![Step 1: Parts image 4](images/step01_04.jpg)

![Step 1: Parts image 5](images/step01_05.jpg)

![Step 1: Parts image 6](images/step01_06.jpg)

![Step 1: Parts image 7](images/step01_07.jpg)

![Step 1: Parts image 8](images/step01_08.jpg)

Parts:

1. Resistors.

Use metal film ones – they are better quality and cost about the same as other ones. Also, buy them in assorted lots on [eBay](https://www.ebay.com.au/sch/i.html?_osacat=0&_odkw=metal+film+restitor+assorted&_from=R40&_trksid=m570.l1313&_nkw=metal+film+resistors+assorted&_sacat=0)

- 4.7K X 2

- 3.3K X 2

- 7.5K

- 3.6K

- 1.5K

2. Capacitors

You can also buy these in assorted lots on [eBay](https://www.ebay.com.au/sch/i.html?_osacat=0&_odkw=capacitors+resistors+assorted&_from=R40&_trksid=p2334524.m570.l1313.TR1.TRC0.A0.H0.Xcapacitors+assorted.TRS0&_nkw=capacitors+assorted&_sacat=0), which I suggest you do

- 100uf X 2

- 220uf

- 22uf

- 47uf

- 2.2uf

3. Making a vactrol

- 5mm white LED X 2 – [eBay](https://www.ebay.com.au/itm/20pcs-5mm-Superbright-White-Round-LED-20000-MCD-LJ/183559984060?hash=item2abd0713bc:g:vzEAAOSwzpFbJeM-&frcectupt=true)

- LDR (Light Dependent Resistor) X 2 - [eBay](https://www.ebay.com.au/itm/20pcs-5mm-Superbright-White-Round-LED-20000-MCD-LJ/183559984060?hash=item2abd0713bc:g:vzEAAOSwzpFbJeM-&frcectupt=true)

- Heat shrink (needs to be able to fit over the LED so 5 mm should be fine.

4. 10K Potentiometers X 6 – [eBay](https://www.ebay.com.au/itm/3Pcs-6mm-Knurled-Shaft-Single-Linear-B-Type10K-ohm-Rotary-Potentiometer-New/262852339228?epid=1684420726&hash=item3d3338661c:g:Np8AAOSwax5Yos7P)

5. Potentiometer knobs X 6 - [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR11.TRC1.A0.H0.Xpotentiometer+knob.TRS0&_nkw=potentiometer+knob&_sacat=0)

6. 555 Timer X 3 – [eBay](https://www.ebay.com.au/itm/10-20-50-100PCS-NE555P-NE555-DIP-8-SINGLE-BIPOLAR-TIMERS-IC/263770865456?var=&hash=item3d69f7ff30&enc=AQADAAAC4FjVrDbVsZ8oH%2F8PNHtt9VX4%2Fw7FZcmMuqsX8uaFEduVXRDIZzFRvPOpCg5qnj%2BzXXgYqTg2dnBTflL1esofw%2B04Q009pbVc%2BDXNg2FbRZkrkVqbWhMMiHd6nuwtAG1iyvhctqEY%2B6UN57pqqWQmBkJjU4iqrMEQcQO0ica%2F6cnHGoQvpXQcaD1g3cOpHJbxTKO%2BQ17Q6ysXd5PqS6eA4J1F8zjQdPfMpMhGzanNYnb5Q1pCEseISkv7Hw73fOdWMMNrJAZN13iqwPkRy3yTtFS3C96nBBbM7VjmkmeDth%2FseqP4hAPAogQ7SZXi3S0W22extD6hQtejQMAcycNWtcJZJjzsfN3ypNiERLMaR7hu9Dl3nCPIQpjhpWeJz2zYroGLQwmNI%2BObx%2Bg4PaAULxjtTL6QIsVX6FYsEegxLZM1gc3VC9OlUB1KhAZZ3UuFn01Qt8cdIosPzdC6rDDXhZPlgqOhz4jX68gUv66vzpAVFSE%2BbmhNhwMxn%2FSdW4%2BVFKxYcQdfg3QGztLdKBPtE9Gpl%2BnCOK6HLKZMCHrT8oK%2FSQev1YK0EZtUzcLzR5KUagNgdqy6aruXZg4u5vdLePhKrHbKAukE%2FgmlrbxLt5kvDmJSEYHcItLaNv0p%2Bqe25Z8LkVeq43Pa2lBpwXI9%2BY6b4IFljV25FIeEZjAPjUw1z3rr9ciqyuMY3%2FBsqz3zzZ4%2Bao5435yAL7tb6fqVkB1SQeR46X1JkeDmQSIr5sd6DbJyqbUz6jGSaEJbUnS7XqhaWWqTDBDb8yC50vp9C2QIYVefafShPgPjFEC16XA9PIvqHdcFvVj1cx54W0Wv7OPdpi1timsS8jsxxIVsFtXmwrWVuCQTvNwlkARC6HF%2BWNkwR4RU7R9nMD%2FvLjWNRioBQ9A6aUpaiDKd%2FCWJf%2FKWCfMLSH1qYKOTA86b2eA6LV%2BLfoWPjDEPHKt72GvnHI2LJILj01pNFmYGxZ9qA4M%3D&checksum=263770865456bb718d0f7d3547f0a8fed1a112177148&frcectupt=true)

7. 3mm LED X 2 – [eBay](https://www.ebay.com.au/itm/100PCS-3mm-White-LED-Super-Bright-Round-Lighting-Bulbs/322656683959?hash=item4b1fd647b7&enc=AQADAAAC4FjVrDbVsZ8oH%2F8PNHtt9VX4%2Fw7FZcmMuqsX8uaFEduV968OS3LaeFsmQTqp1Xhipkp6ZWfwcDOdYQYkgF9jvImWXbosqk5LVlEk5ACkMhjR0npZxGbwF3lpQfoOuAvqK6JGOjnTRl5JWSvj%2BWPZ1jPIqFPMsWV3jfX0uj1q8tmJ4Q02nlOeeEmDrxnB%2BnpnJKrA9STV9Qb4g%2FjTRBo6ugZtzrbSuosc3Gh8qwZrQ4r%2FnXzkvlrbM8Nk4AudYC5Hufnd4%2F3G1sl4jhUQJsCcW6%2FFuhhWxHENOrDEz9aDkfAKIF2KQDLvSX563m3rMfDIHtt5Q%2F6dOJziqUG3kB2n3u%2BvhVuU9jxmMHI40oMmQ5NtKx7V%2BjrvCQ65Dcc0O1ewsDrnekCq4zAFD7l0fOW8JUe5QZmkF40C1vhA2eEwpR10HMEcJqhhk%2B36ilMov4N6iVminIYLh73LduZY3p6Pn%2FEyUwj6MeFCsrViKpNhjeHsowVBiKrDucfGjXfPVu7b%2FfEAeMumcrUSEXDdpUbg2SmHstA%2BTt5IJUcn82gI5USHKTFlS3TA27yheKIT51qvgu8AA%2FFR4gD%2FSCCOU66fxfvldUROJJSHkAZCcugm70jN1OF%2B9b9asLVVKASnB5ItKi%2FCA7C1nXFMme78Q539VEN6tsWgcsxKccKqL3Ly3N0U8oMfetoQawVao8WKtwGeQ1BYf0lU3EcfJEJ9E3C%2BK%2BSUdPhCbTo1I0hq91Sz8%2BXhQz%2Fb2qcHHa370o5QdbPp2KK4OHeKK7tJBLApfXbOYVT%2BEB0%2FyPE%2BAfGlaTKXXP8oUh6fGmQFc9kDbS%2FEVKqLC85FedZHQXZxp2gObIgutJMr2TWY%2FZb4idZi5pbFCcsWiwDm2tk5xd%2FJonCQfjK%2Bvo1ur1nQZ82%2Bx4PrP7Jw2j144MYNrWL0X8utbkxgHTASwxSTETJqhKpRBgJY8ZVnFQ3wQdypkR%2B17p1cVc%2FwF7Q%3D&checksum=3226566839594a726d95acf1428fbce36cad384d75be&frcectupt=true)

8. SPDT Switches X 2 – [eBay.](https://www.ebay.com.au/itm/1-2-5-10pcs-Mini-ON-ON-MTS-102-3-Pin-SPDT125V-AC-6A-Miniature-Toggle-Switches/282588148734?hash=item41cb90f3fe:m:mLb9w5GnglPqNho7fNbdIEA&frcectupt=true)

9. 0.5W 8ohm speaker – [eBay](https://www.ebay.com.au/itm/2x-20mm-8Ohm-8-0-5W-Audio-Speaker-Stereo-Woofer-Loudspeaker-Trumpet-Horn-New/122266516483?hash=item1c77a6fc03:g:kpQAAOSwfZhXNUCv&frcectupt=true). You can use a larger one if you want to I used a small one as my case was small.

10. 3.5mm output jack socket – [eBay](https://www.ebay.com.au/itm/5Pcs-3-5mm-PCB-Panel-Mount-Stereo-Jack-Female-Socket-Connector-Earphone/173601296623?hash=item286b7190ef:g:4TYAAOSwED5Z2eKX)

11. 9v Battery

12. 9V battery holder – [eBay](https://www.ebay.com.au/itm/10PCS-MN1604-9V-PP3-9volt-Battery-Holder-Clip-Snap-On-Connector-Cable-Lead/282606951665?hash=item41ccafdcf1:g:EYoAAOSwr~dZjXn2)

13. Prototype Board – [eBay](https://www.ebay.com.au/itm/10x-DIY-Prototype-Paper-PCB-Experiment-Board-Bakelite-Circuit-Board-4-8x13-3cm/142759746052?hash=item213d24da04:g:sFUAAOSwcEha0XL3)

14. Momentary Switches X 2 – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_nkw=Momentary+off%2Fon+Push+Button&_sacat=0&_sop=15)

If you also want to add a amp to increase the volume – then you will also need the following parts

14. Small amp module – [eBay](https://www.ebay.com.au/itm/Headphone-150mW-Amplifier-Board-Differential-Balanced-4812-HIFI-Amp-SGM-Module/311736734716?epid=504490827&hash=item4894f513fc:g:3uwAAOSwGhFcb3DT&frcectupt=true)

15. 10K pot (This is one of the 6 that I have included above)

16. Some type of case to add everything into. I used an old torch I had lying around.


## Step 2: About the Circuit

![Step 2: About the Circuit image 1](images/step02_01.jpg)

![Step 2: About the Circuit image 2](images/step02_02.jpg)

![Step 2: About the Circuit image 3](images/step02_03.jpg)

At first glance, the circuit might look a little complicated but it's really pretty simple. The best way to make this synth is in stages which is how I will explain each step in making the circuit. You'll also notice that I have included 2 schmatics, the 2nd one includes a amp module and volume pot. It's not necessary to add this but it will dramatically increase the volume. However, I did add an output socket so you can just plug it into a portable speaker to increase the colume. If you also download Fritzing you can play around with the schematics yourself.

I'll go through what each 555 timer does and will try to explain some of the features and how the synth works.

555 Timer 1 & 2

1. Both 1 & 2 timers are basically a flashing LED circuits. To be able to control the speed of the LED on each 555 IC, there are 2 different capacitor values. These are connected to a SPDT switch which allows you to change the speed of the LED's

2. Also connected to each IC is a 10K pot. This also allows you to control the speed of the LED's.

Vacrol

1. IC timers 1 & 2 are also connected to a vacrol. Inside the vactrol is an LED and a Light dependant resistor (LDR). There is a pot connected to each which controls the brightness of the LED's which changes the pitch and tone

2. Check out the next step on what a vacrol is.

555 Timer 3

1. Lastly, IC 3 generates different sounds depending on the brightness of light. There is also a pot that controls pitch.

2. IC 3 is connected to IC's 1 and 2 via 2 vactrols. When you connect the LED's to the LDR's (which is what a vacrol is) you have a fizzle loop synth!

So to summarise - LED's blink at different rates and brightness's which create rhythms and beats controlled by various pots and switches.


## Step 3: What's a Vacrol?

![Step 3: What's a Vacrol? image 1](images/step03_01.jpg)

![Step 3: What's a Vacrol? image 2](images/step03_02.gif)

A vacrtol is made from 2 common component, an LED and a Light Dependant Resistor (LDR). The parts are incorporated into one package and face each other. I use heat shrink which seems to work well as a casing.

It’s important that the only light that the photo cell can detect is from the LED. If outside light is able to reach the photo cell, then it will interfere with the performance and sound, that’s why you need to add something like heat shrink to protect them.

When wired-up, the Vactrol acts like a potentiometer - applying a voltage to the Vactrol's LED has the same effect as turning up the knob on the potentiometer. Now if you dim the LED or flash it (like in the Fizzle Loop Synth) and hook it up to a 555 timer, then you can generate different tones and rhythms.

Next I'll go through how to easily make your own vacrol. You will need 2 for this project


## Step 4: Making a Vactrol

![Step 4: Making a Vactrol image 1](images/step04_01.jpg)

![Step 4: Making a Vactrol image 2](images/step04_02.jpg)

![Step 4: Making a Vactrol image 3](images/step04_03.jpg)

![Step 4: Making a Vactrol image 4](images/step04_04.jpg)

![Step 4: Making a Vactrol image 5](images/step04_05.jpg)

![Step 4: Making a Vactrol image 6](images/step04_06.jpg)

![Step 4: Making a Vactrol image 7](images/step04_07.jpg)

Steps:

1. Cut a small length of heat shrink tube. The LED and photo cell need to be able to fit inside snuggly. You also want to have a little excess heat shrink so you can pinch it together once heated and ensure no light can enter the vacrol.

2. Place the LED into the heat shrink with the legs facing out and also do the same for the photo cell. Make sure that they are touching inside the heat shrink. Also mark the ground leg on the LED so you know which one is which

3. Heat the heat shrink and start to shrink it. Start with the LED end first and when it has shrink enough, grab some pliers and flatten the end of the heat shrink so it is sealed shut.

4. Do the same for the LDR

5. Make 2 of these

6. That’s it! You have made an important component to the fizzle loop synth


## Step 5: Making the Circuit - IC Timer 1 and 2

![Step 5: Making the Circuit - IC Timer 1 and 2 image 1](images/step05_01.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 2](images/step05_02.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 3](images/step05_03.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 4](images/step05_04.jpg)

![Step 5: Making the Circuit - IC Timer 1 and 2 image 5](images/step05_05.jpg)

As mentioned earlier, I'm not going to go through a step by step process on how to add each component to the circuit. I'm going to assume you have put circuits together and my schematic makes some sense. I will go through a few interesting parts of building this section of the circuit. The first 2 timers are pretty much identical in how they are connected to the board. The only difference is a switch connected to the 2nd IC.

The LED

You may have noticed that there is an LED by itself, connected to pin 3, along with the vactol. This LED acts as a visual when creating tunes and flashes at the same time as the LED inside the vacrol

Wires

You'll need to add wires to the circuit board which will be connected to the pots and switches later on. I use computer ribbon cable wire for this as it's strong, thin and you can pick it up for free at most ewaste recycle places. Add all of the wires to the circuit board first and make sure you give yourself enough length on each as they will need to be connected later on once the circuit is completed.

Adding the Vactrol

1. Solder the legs of the LED's and LDR directly to the prototype board

2. Ensure that the LED legs are facing down and the positive leg is closest to the timer

3. Connect the positive LED leg to pin 3 and the ground to ground on the prototype board

4. Connect one of the legs of the LDR to positive, the other will be connected to pin 6 on 555 timer 3

Check out the next step on how the caps are attached to the SPDT switches


## Step 6: Making the Circuit - IC Timer 3

![Step 6: Making the Circuit - IC Timer 3 image 1](images/step06_01.jpg)

![Step 6: Making the Circuit - IC Timer 3 image 2](images/step06_02.jpg)

![Step 6: Making the Circuit - IC Timer 3 image 3](images/step06_03.jpg)

![Step 6: Making the Circuit - IC Timer 3 image 4](images/step06_04.jpg)

555 IC 3 is the timer that gives you your tunes. It's actually a basic light thermin based on the [slidersynth](http://hackaweek.com/hacks/?attachment_id=1515) by Deno which I have also [built here](https://www.instructables.com/id/Slider-Synth-Light-Theremin-555-IC/). I've taken it a few steps further with the fizzle loop synth but basically it uses the same concepts. I'll go through a few highlights of this section of the build

Steps:

1. There's a 10K pot that is connected to pin 6 and ground. This is used to control the overall pitch of the synth. You could use a 5K pot as well for this section. Just experiment and work out what works best for you.

2. You will also notice that there is a momentary switch connected to the vactol on the 2nd IC and also connected to pin 7 on IC 3. This momentary switch should always be on and is only off when you push it down. It changes the tone when pushed down

3. After experimenting a little I worked out that connecting pins 3 on both both IC 2 and 3 you can get an interesting drum type sound. Adding a switch to this section allows you to change between rythum and drums.

4. Lastly I included a 3.5mm jack socket. This allows you to plug it into an amp for a louder sound. I definitly suggest you add an output socket so you can really pump up the volumne.


## Step 7: Adding Capacitors Directly to the Switches

![Step 7: Adding Capacitors Directly to the Switches image 1](images/step07_01.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 2](images/step07_02.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 3](images/step07_03.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 4](images/step07_04.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 5](images/step07_05.jpg)

![Step 7: Adding Capacitors Directly to the Switches image 6](images/step07_06.jpg)

One of the aims in making the circuit was to try and reduce the size as most as possible. I had to if I wanted it to fit inside a small case such as the flashlight case that I used in this project. Because of this I decided not to solder the capacitors connected to pin 2 to the prototype board but directly to the SPDT switch.

Steps:

1. Solder the positive legs of the 100uf cap to the first pin on the switch, the 220uf to the middle pin and the 330uf cap to the last pin

2. Do the same again for the other caps for 555 timer 2. There are different cap values for this timer - you just need to make sure that they are connected in descending order, 10k 22k and 47k

2. For each switch, connect all of the ground legs of the caps together. These will be connected to pin 2 on 555 timers later on

3. The other pins on each of the switches can also be connected together. These will be connected to ground on the prototype board later.


## Step 8: Making the Case - Adding the Components

![Step 8: Making the Case - Adding the Components image 1](images/step08_01.jpg)

![Step 8: Making the Case - Adding the Components image 2](images/step08_02.jpg)

![Step 8: Making the Case - Adding the Components image 3](images/step08_03.jpg)

![Step 8: Making the Case - Adding the Components image 4](images/step08_04.jpg)

![Step 8: Making the Case - Adding the Components image 5](images/step08_05.jpg)

![Step 8: Making the Case - Adding the Components image 6](images/step08_06.jpg)

![Step 8: Making the Case - Adding the Components image 7](images/step08_07.jpg)

![Step 8: Making the Case - Adding the Components image 8](images/step08_08.jpg)

![Step 8: Making the Case - Adding the Components image 9](images/step08_09.jpg)

![Step 8: Making the Case - Adding the Components image 10](images/step08_10.jpg)

![Step 8: Making the Case - Adding the Components image 11](images/step08_11.jpg)

The case I used is an old flashlight that I had lying around. The lens section was a perfect spot to add a small speaker. The case is a tight fit for all of the electronics but I wanted tpo make a pocket sized flzzle loop synth this time.

Steps:

1. First you need to design the layout of the pots and switches. This is an important part, especially if you are using a small case like I did in thsis build.

2. You'll also need to take into consideration how everything will fit inside the case. Wires, battery and the circuit board will need to be cramed inside so make sure you plan this out too.

3. Once you have planned out the build it's then time to start to add the components. Drill the holes in the case and attach all of the pots, switches and LED's needed for the build.


## Step 9: Wiring-up the Circuit

![Step 9: Wiring-up the Circuit image 1](images/step09_01.jpg)

![Step 9: Wiring-up the Circuit image 2](images/step09_02.jpg)

![Step 9: Wiring-up the Circuit image 3](images/step09_03.jpg)

![Step 9: Wiring-up the Circuit image 4](images/step09_04.jpg)

![Step 9: Wiring-up the Circuit image 5](images/step09_05.jpg)

![Step 9: Wiring-up the Circuit image 6](images/step09_06.jpg)

![Step 9: Wiring-up the Circuit image 7](images/step09_07.jpg)

![Step 9: Wiring-up the Circuit image 8](images/step09_08.jpg)

![Step 9: Wiring-up the Circuit image 9](images/step09_09.jpg)

The case should now have all of the components added to it ready for wiring. Wire for some odd reason takes up a fair amount of space inside a case so you should try to make the wires a short as possible. Also, it's good practice to be able to remove the circuit board out of the case so you can fix any issues with the connections if necessary.

Steps:

1. Place the circuit board inside the case. Also place the battery in the case to make sure you have enough room for everything.

2. Start to connect each of the compents to the wires on the circuit board. Take your time and make sure that each wire is connected correctly.

3. Trim the excess wire before soldering onto each component.

4. If you want to add an audio amp and volume pot - check out the next step.

4. Once all the wires are connected add the battery and test. If nothing happens, you'll have to check over your connections and see if any are incorrect. If it works then congrats, you have made your very own fizzle loop synth. Now to add the knobs and work out how this thing works


## Step 10: Adding an Audio Amp and Volume Pot

![Step 10: Adding an Audio Amp and Volume Pot image 1](images/step10_01.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 2](images/step10_02.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 3](images/step10_03.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 4](images/step10_04.jpg)

![Step 10: Adding an Audio Amp and Volume Pot image 5](images/step10_05.jpg)

Once I had built the synth I decided that adding a small amp and volume pot would allow me to really annoy everyone in the house. It's a easy add-on and definitely worth including in the build. The amp I used can be picked-up on eBay for cheap and I have included a link in the parts section.

Steps:

1. Check out the schematic. I have highlighted the added amp and pot and also where they are connected. In the schematic the symbol for the amp is missing the ground wires for input and output. Check out the other schematic which I did which will also help work out hownto wire this up

2. Connect the ground and positive on the amp to the 9v battery.

3. The input section on the amp should be connected as follows: positive to pin 3 on the 3rd 555 IC and ground to the ground section on the circuit board

4. The output should be connected as follows: positive to the positive solder point on the speaker and the ground to the ground solder point on the speaker

5. To add a volume pot I found that the best place to connect it is to the output socket. If you add it directly to the speaker I found that it caused some interference to the synth and changed the sound. Adding it to the socket isolates it from the speaker and stops the interference.


## Step 11: Adding the Knobs and How to Play the Synth

![Step 11: Adding the Knobs and How to Play the Synth image 1](images/step11_01.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 2](images/step11_02.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 3](images/step11_03.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 4](images/step11_04.jpg)

![Step 11: Adding the Knobs and How to Play the Synth image 5](images/step11_05.jpg)

The final part of the build is to add some knobs to the build. You are now ready to start experimenting and making some awesome sounds.

Check out the image attached which shows what each knob and switch does.

Don’t be afraid to experiment with different capacitor values on the switches or different resistor values on the LED’s. These are a tonne of different options on these parts and you can get many different sounds by changing them. You could also look at changing the potentiometer values as well, which would give you a different range of sounds.

You could even add another flashing LED 555 timer and tie this into the light Theremin 555 timer (timer 3 on the schematic). Maybe add a switch to each 555 timer so you can turn it off or no.

There are a tonne of mods you could do, so make sure you try some different set-ups before you build your own


---
*69 images archived*
