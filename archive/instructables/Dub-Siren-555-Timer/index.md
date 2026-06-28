# Dub Siren Synth - 555 Timers

Source: https://www.instructables.com/Dub-Siren-555-Timer/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

Dub Siren! Man – I didn’t even know that these existed until a DJ friend asked me to make him one.

I had to do some digging (a lot of digging actually – there isn’t much on the net surprisingly) to find out the history of the dub siren and it didn’t disappoint. Seems that it originated in Jamaica in the late 60’s, early 70’s where they started to use sirens and analog synths to create sound effects for their music. Later it was emulated to live DJ performances using something similar to this ‘ible.

So what is a dub siren? I’m glad you asked…

The dub siren is based around 2 x 555 timers and a LM741 Op amp. Adding a bunch of pots and buttons allows you to create and control a whole heap of cool sounds from a traditional siren to a long toned note.

They are usually played with a reverb guitar pedal but I decided to add my own reverb circuit (no need to make this one as you can buy them on eBay) to the final build. Adding this circuit gives you some amazing sounds to help you play along to your favourite dub, hip hop, disco house or whatever else you want to play along to.

The circuit wasn’t too difficult although the schematic look me a little to get my head around. I found that I only had to modify it a little (if you are going to add the revert circuit you will also need to do the modification) to get the sound I wanted. I’ve included the original schematic ([you can also find it here](https://jacoblysgaard.com/2009/08/dyi-dub-siren-%E2%80%93-the-complete-rubdown/)) and also my modified one.

[Hackaday](https://hackaday.com/?gclid=CjwKCAiA58fvBRAzEiwAQW-hzTZV1eEwLdO0Vsn_N4EfrDxyIFbPlYwbiKsXVcXBxF25Cwtvi60QjhoCY7cQAvD_BwE) were nice enough to do a review of this project which can be found [here](https://hackaday.com/2019/11/29/dub-siren-synth-does-it-the-old-school-way/)


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

![Step 1: Parts image 3](images/step01_03.jpg)

![Step 1: Parts image 4](images/step01_04.jpg)

![Step 1: Parts image 5](images/step01_05.jpg)

![Step 1: Parts image 6](images/step01_06.jpg)

Dub Siren

1. LM555n × 2 – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p4712.m570.l1313.TR10.TRC0.A0.H0.X555+timer.TRS0&_nkw=555+timer&_sacat=0)

2. LM741 × 1 operational amplifier – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR1.TRC0.A0.H0.Xlm741.TRS0&_nkw=lm741&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=555+timer)

3. Momentary on/off button – Normally on - [[eBay](https://www.ebay.com.au/itm/Momentary-Switch-SPST-NO-DS-212-Round-Cap-Push-Button-Switch-16-mm-5A-250V/253777528081?hash=item3b1651c511:m:mXsHtZ7aAb0STMkivgRyoIA)](https://www.ebay.com.au/itm/5PCS-Black-Mini-Push-Button-Momentary-N-O-Switch-PBS-110-OFF-ON/232435034133?hash=item361e352815:g:k50AAOSwjTlZg~wM) and off/on - eBay

4. 2 X On/off switch – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR11.TRC1.A0.H0.Xmini+toggle+switch.TRS0&_nkw=mini+toggle+switch&_sacat=0)

5. 1/4” Output Jack – [eBay](https://www.ebay.com.au/itm/2pcs-Mono-1-4inch-Output-Jack-Socket-Plate-for-Fender-Tele-Electric-Guitar/132747175229?hash=item1ee859253d:g:C1oAAOSw1H9bdin2) (optional but I wanted a way that you could plug it into an amp)

6. 3.5mm Output Jack – [eBay](https://www.ebay.com.au/itm/10-Pcs-Panel-PCB-Female-3-5mm-Headphone-Jack-Audio-Connectors-JR/132565480819?hash=item1edd84b573:g:a8UAAOSw~P9avdwj)

7. 5mm LED – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313.TR4.TRC1.A0.H0.X5mm+led.TRS0&_nkw=5mm+led&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=3.5mm+output+Jack+&LH_TitleDesc=0)

8. 3 X 9V battery’s. Yes you need 3 9v Batteries! Each circuit will need it's own power source. There is too much noise if you don't. Smarter people then me will know how to isolate each circuit but I don't...yet.

9. 3 X 9V battery Holders – [eBay](https://www.ebay.com.au/itm/Replacement-9V-Battery-Box-Case-Holder-Connector-A2R6/323144687061?hash=item4b3cec9dd5:g:~BQAAOSwhuxaqn0p)

10. Knobs – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR11.TRC1.A0.H0.Xpotentiometer+knobs.TRS0&_nkw=potentiometer+knobs&_sacat=0)

11. Case – I found mine at the dump. I think it was an old CB radio

12. 50K X 5 pots - [eBay](https://www.ebay.com.au/itm/2-5-10PCS-B500K-50K-1K-Ohm-3-Pins-Shaft-Linear-Rotary-Taper-Potentiometer-WH148/263838249404?hash=item3d6dfc31bc:m:mgx7CZa9H2tiDe7pctMa_2Q)

13. Protoboard – [eBay](https://www.ebay.com.au/itm/10x-DIY-Prototype-Paper-PCB-Experiment-Board-Bakelite-Circuit-Board-4-8x13-3cm/142759746052?hash=item213d24da04:g:sFUAAOSwcEha0XL3)

14. Plenty of wire

Caps – I got mine from [eBay](https://www.ebay.com.au/itm/450pcs-10Value-50V-10pF-100nF-Ceramic-Capacitors-Assortment-Assorted-Kit-Box/163087715384?hash=item25f8c90c38). Best to buy them in assorted lots. Ceramic - eBay Electrolytic - eBay

15. 47μF × 1

16. 47nF × 1

17. 220μF × 1

18. 150nF × 1

19. 10μF × 1

Resistors – Same with the caps – buy them in assorted lots

20. 10K X 2

21. 68K X 2

22. 560R X 4

23. 2.2K X 2

Reverb Module and Amp

1. Module – eBay

2. 50K Pot

3. Amp Module – [eBay](https://www.ebay.com.au/itm/ammoon-High-Sensitivity-Mini-5W-9V-Amp-Amplifier-Speaker-for-Uke-Guitar-I6B3/132512979045?epid=12012787398&hash=item1eda639865:g:xDgAAOSwBOlajSEM)


## Step 2: The Circuit

![Step 2: The Circuit image 1](images/step02_01.jpg)

![Step 2: The Circuit image 2](images/step02_02.jpg)

![Step 2: The Circuit image 3](images/step02_03.jpg)

I have attached the original dub siren circuit along with my slightly modified one. If you want to, you can just build the circuit to the original one. My modified one add's a small amp and a reverb module which gives the siren more depth and and sound options.

A couple things to note:

The switch that is on the far right of the schematic is a momentary switch which is normally on. Most momentary switches you would use are normally off so make sure you get the right one which I have added a link to in the parts section.

The 220uf Cap on the left hand side is also reversed in the schematic. Make sure that the negative leg is connected to ground.


## Step 3: Making the Circuit - First 555 Timer

![Step 3: Making the Circuit - First 555 Timer image 1](images/step03_01.jpg)

![Step 3: Making the Circuit - First 555 Timer image 2](images/step03_02.jpg)

![Step 3: Making the Circuit - First 555 Timer image 3](images/step03_03.jpg)

![Step 3: Making the Circuit - First 555 Timer image 4](images/step03_04.jpg)

Putting the circuit together wasn’t too difficult but I would suggest that if you are only a beginner, you practice and a few 555 timer projects first before tackling this. The actual schematic is a little difficult to read (was for me anyhow) and took some time for me to get my head around. Make sure you breadboard the project beforehand as well. I usually do it twice to make sure I understand what is going on.

Steps:

1. First thing to do is to solder in an 8 pin IC socket for the first 555 timer. Make sure you give yourself plenty of room on the protoboard to allow for all of the resistors and wires etc.

2. Once the IC socket is in place, solder pin 1 to ground and pin 8 to positive

3. Solder pins 2 and 6 together

4. I then made the clock cycle section and started to add the wires needed for the pots and LED


## Step 4: Making the Circuit - First 555 Timer

![Step 4: Making the Circuit - First 555 Timer image 1](images/step04_01.jpg)

![Step 4: Making the Circuit - First 555 Timer image 2](images/step04_02.jpg)

![Step 4: Making the Circuit - First 555 Timer image 3](images/step04_03.jpg)

Next you need to add the rest of the components for the first 555 timer. These control the various pots (there are 3 pots for this section).

Steps:

1. Add the 220uf cap and components from pin 4 to ground. Pin 4 on the first 555 timer also connects to pin 4 on the other 555 timer. Don’t forget to do this later on!

2. Next you need to connect the components connected to pins 6 and 7. I won’t lie, when I first saw this section it did confuse me. However, with a little patience I worked it out. The best advice I can offer on this part is to start with pin 6 and just follow the connections.

3. Lastly, you need to add all of the wires to attach to the pots, LED, switches etc. Give yourself plenty of extra wire – nothing worse than realising you have made them too short!

4. Next you need to wire up the LM741 op amp – a lot easier than the 555!


## Step 5: Making the Circuit - Wiring the Op Amp

![Step 5: Making the Circuit - Wiring the Op Amp image 1](images/step05_01.jpg)

![Step 5: Making the Circuit - Wiring the Op Amp image 2](images/step05_02.jpg)

Steps:

1. Attach pin 4 to ground and pin 7 to positive

2. Attach a wire to pin 3. This will be later soldered to the middle pin on one of the pots

3. Solder pins 2 and 6 together. You need to do this on all 3 of the IC’s

That’s it for the op amp. You will need to connect pin 6 on the op amp to pin 5 on the 555 timer once the next 555 timer is soldered in


## Step 6: Making the Circuit - the Other 555 Timer

![Step 6: Making the Circuit - the Other 555 Timer image 1](images/step06_01.jpg)

![Step 6: Making the Circuit - the Other 555 Timer image 2](images/step06_02.jpg)

![Step 6: Making the Circuit - the Other 555 Timer image 3](images/step06_03.jpg)

![Step 6: Making the Circuit - the Other 555 Timer image 4](images/step06_04.jpg)

Time to wire up the last 555 timer. On the original schematic there is an option to add an LED and a couple of switches to control the sound to the speaker. I didn’t worry about adding this as I wanted the momentary switch to be always available. In my amended schematic I discarded this section.

Steps:

1. First add pin 1 to ground and pin 8 to positive

2. Next, like the rest of the IC’s, connect pins 2 and 6 together.

3. Connect pin 6 from the op amp to pin 5 on the 555 and pins 4 on both 555 timers

4. Add a 150nf cap to pin 6 and ground

5. Between pins 6 and 7 you need to add a 2.2 resistor and connect a 50k pot

6. Add another 2.2k resistor to pin 7 and positive

7. Lastly, you need to connect pin 3 to a 1uf cap (as per my amended schematic) with wires on either side of the legs of the cap. These will be connected to the reverb module later on. Add the rest of the parts including the momentary switch which needs to be one which is normally on.

Now it’s time to make the case...


## Step 7: Modding the Case - Pulling Apart and Cleaning

![Step 7: Modding the Case - Pulling Apart and Cleaning image 1](images/step07_01.jpg)

![Step 7: Modding the Case - Pulling Apart and Cleaning image 2](images/step07_02.jpg)

![Step 7: Modding the Case - Pulling Apart and Cleaning image 3](images/step07_03.jpg)

![Step 7: Modding the Case - Pulling Apart and Cleaning image 4](images/step07_04.jpg)

![Step 7: Modding the Case - Pulling Apart and Cleaning image 5](images/step07_05.jpg)

Now you have wired up your circuit, it’s time to put together the case. I used an old CB radio I found at the dump for the case. I had to do a fair bit or modding to get it to where I was happy but I’m glad I did pick this case for a couple of reasons. One – it has plenty of room inside so makes fitting speaker, batteries circuits etc a pretty straightforward task. Two – It’s got a great retro feel and I think it fits this synth perfectly.

I’m going to go through what I did to mod this particular case. Yours will most def be different but hopefully I can give you a few tips for when you make yours

So let’s get cracking.

Steps:

1. First you need to pull out any old electronics and parts inside the case. Keep anything that might be handy in the build like knobs etc.

2. Next give the case a good wash in soapy, hot, water. This should bring it back to at least a resemblance of its old self.


## Step 8: Designing and Modding the Case

![Step 8: Designing and Modding the Case image 1](images/step08_01.jpg)

![Step 8: Designing and Modding the Case image 2](images/step08_02.jpg)

![Step 8: Designing and Modding the Case image 3](images/step08_03.jpg)

![Step 8: Designing and Modding the Case image 4](images/step08_04.jpg)

![Step 8: Designing and Modding the Case image 5](images/step08_05.jpg)

Now you have a clean, empty case in front of you, it’s now time to work out where you are going to add all of the knobs, switches audio jacks etc. Take your time when doing this part. Once you start to cut and drill there is no going back. On this case mod I decided to cut a big chunk out of the front and replace with wood. I did this so there was plenty of room to add the knobs etc and also because I thought it would give it a nice, retro feel.

Steps

1. Start by placing knobs on the case. You will need 4 for the siren and 2 for the reverb circuit. Move them around until you are happy with the design.

2. Next, I removed a whole lot of plastic on the front as it was just going to be hard to attach the pots etc to the front. Use a dremel with a cutting wheel. Take your time and check your work.

3. Once the plastic was removed, I smoothed it out with a file. Again, checking my work until I was happy with the lines and edges.

4. I also added some plastic to the side of the case as the original owner made a few mods themselves. After, I decided to add the on/off switch to the piece of plastic.

4. So what to fill the hole with…I was going to use some stainless steel sheeting but instead when with some wood. I’ll go into more in the next step


## Step 9: Keep on Designing

![Step 9: Keep on Designing image 1](images/step09_01.jpg)

![Step 9: Keep on Designing image 2](images/step09_02.jpg)

![Step 9: Keep on Designing image 3](images/step09_03.jpg)

The wood I used was just a piece of thin hard wood ply wood sheet. I stained the wood also to give it a more retro feel.

Steps:

1. Once you have stained the wood, you will need to work out how it will fit in the case. As you might have noticed, I left a small lip right around the hole I cut out of the case. This would allow me to place the wood underneath and give it a nice, neat finish.

2. I used a black marker to finish off the edges of the plastic

3. Cut the wood to size and put it into position. I also cut a couple of grooves into the screw pillars which helped hold the wood into place. You will need to come up with your own mods by trial and error (hopefully not much error!) to best work out how to hold the wood into place.

4. Lastly, I added 3 screws into the case and wood to make sure it wouldn’t move. Now your ready to add the knobs, pots and everything else to the case.


## Step 10: Adding the Pots, Switches, Jacks to the Case

![Step 10: Adding the Pots, Switches, Jacks to the Case image 1](images/step10_01.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 2](images/step10_02.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 3](images/step10_03.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 4](images/step10_04.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 5](images/step10_05.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 6](images/step10_06.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 7](images/step10_07.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 8](images/step10_08.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 9](images/step10_09.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 10](images/step10_10.jpg)

![Step 10: Adding the Pots, Switches, Jacks to the Case image 11](images/step10_11.jpg)

Now that you have made enough room on the case, it’s time to add the pots, switches etc to it. Again, take your time when doing this and try to set out first how best to attach the parts.

Steps:

1. You will need 4 pots for the siren. Add these so that they are well spaced from each other. This will make it easier to turn and also find (esp if it is dark!)

2. I also used 2 different sized knobs. It isn’t necessary but I thought it would help locate the knobs if the lights were out or it was dark around the DJ booth.

3. The siren comes with a momentary switch which allows you to turn the siren off and on. The switch you need to use is an always on one which is usually the opposite of what you need in a switch. I decided to add 2 switches, one normally off and one normally on with a on/off SPDT switch to toggle between them. Add the switches in a place that is easy to get to (no knobs in the way)

4. Next add a couple of pots (they are all 50K) for the reverb module and some knobs

5. Add the audio out jacks. I used 2 sizes for more versatility. You will need to add a switch to toggle between the internal speaker and audio out


## Step 11: Time to Wire the Circuits to the Pots Etc..

![Step 11: Time to Wire the Circuits to the Pots Etc.. image 1](images/step11_01.jpg)

![Step 11: Time to Wire the Circuits to the Pots Etc.. image 2](images/step11_02.jpg)

![Step 11: Time to Wire the Circuits to the Pots Etc.. image 3](images/step11_03.jpg)

![Step 11: Time to Wire the Circuits to the Pots Etc.. image 4](images/step11_04.jpg)

Now it’s time to attach all of those wires to the pots, circuits and other bits and pieces. There isn’t any real easy way to go through this step by step so I’ll just give a few tips on the best way to go about it.

Steps:

1. First – trim your circuit board if you can. You’ll probably need as much room as possible inside your case. There will be a lot of wires which seem to take more room than you would expect.

2. Work out in what order you want to be able to control the sounds with the pots. I just used my bread board one and figured out how I wanted to control the sounds

3. Decide where you are going to mount the circuit board inside the case. You can then start to trim and solder the wires to each of the pots etc. Also, make sure that you leave the wires long enough so the bottom of the circuit board is still assessable. You will probably have to do some fixes or additions to your board and easy access to it will help. You can always trim the wires further once you have tested it and everything works as it should.

4. Once you have the main circuit board wired, you will then need to attach the reverb board


## Step 12: Adding the Reverb Circuit

![Step 12: Adding the Reverb Circuit image 1](images/step12_01.jpg)

![Step 12: Adding the Reverb Circuit image 2](images/step12_02.jpg)

![Step 12: Adding the Reverb Circuit image 3](images/step12_03.jpg)

![Step 12: Adding the Reverb Circuit image 4](images/step12_04.jpg)

The reverb board needs a couple of modifications to be able to add the echo. Also, on the first board I tried to remove the pot that comes on the board so I could I wires and extend it out but when I de-soldered it, the solder pads also came off. If you do need to remove this, then be careful when doing so. I just attached the pot to the case and left it on the board on my second attempt.

NOTE - Each Circuit board will need it's own power supply (9V battery)

Steps:

1. First you need to remove resistor R27. The best way I found was to use an exacto knife and just cut it away. You can also de-solder them quite easily but be careful not to connect the 2 solder points together

2. Solder 3 wires to the 3 small solder points on the board next to R27. These need to be soldered to the legs on a 50K pot. Solder the wires to the pot as if you were soldering the pot directly to the board. This will give you the correct orientation.

3. The reverb module won’t work with an amp. I initially tried to build one from a 386 IC but the reverb wouldn't come through so I decided just to buy one and hack it.

4. You'll also need to wire up to an on/off switch


## Step 13: Adding the Amp

![Step 13: Adding the Amp image 1](images/step13_01.jpg)

![Step 13: Adding the Amp image 2](images/step13_02.jpg)

![Step 13: Adding the Amp image 3](images/step13_03.jpg)

![Step 13: Adding the Amp image 4](images/step13_04.jpg)

![Step 13: Adding the Amp image 5](images/step13_05.jpg)

![Step 13: Adding the Amp image 6](images/step13_06.jpg)

![Step 13: Adding the Amp image 7](images/step13_07.jpg)

![Step 13: Adding the Amp image 8](images/step13_08.jpg)

The reverb module needs to be attached to an amp in order for it to be heard. You can either just have an external one like a portable speaker, or you can add one to the reverb module. I choose to add one to the reverb module so the sub siren was a self-contained unit. Audio output plugs were also added so you can play it through an amp.

I used a small amp that I purchased from eBay - link in the parts section

Steps:

1. First – pull the amp apart

2. Remove the circuit board inside the case

3. You will need to test it out and make sure that when it is connected to the reverb module and dub siren that everything works as it should. I removed the large jack input on the main circuit board and attached wires directly to the positive and negative sections. The negative is always the larger copper sections on a circuit board.

4. Once you have everything working and sounding right, you then have to add it into the case.

NOTE – I found that I had to have separate 9v batteries for each circuit because of noise. That means that this beast takes 3 X 9V batteries. I’m sure that there is a way to isolate each circuit from the power (diodes come to mind) but it’s already complicated so I just decided to use 3 batteries.


## Step 14: Testing

![Step 14: Testing image 1](images/step14_01.jpg)

![Step 14: Testing image 2](images/step14_02.jpg)

![Step 14: Testing image 3](images/step14_03.jpg)

![Step 14: Testing image 4](images/step14_04.jpg)

![Step 14: Testing image 5](images/step14_05.jpg)

![Step 14: Testing image 6](images/step14_06.jpg)

Now that you have everything wired-up, it’s time to give it a test run.

Steps:

1. Connect power to the dub siren and reverb board and make sure everything is getting power.

Note – I found that I had to disconnect and re-connect the battery from the reverb circuit after I made the modification to get it to work properly.

2. You may have to wait a few seconds before you start to hear anything.

3. If you don’t any sound then check your connections and polarities to make sure everything is wired right.

4. If the sound is only coming out very softly from the speaker, then it’s probably a connection from either the reverb board to the amp or from the amp to the speaker. Play around with these and see if it helps to increase the volume.

5. If everything is working as it should, you then need to do the final connections to the on/off switch, audio output jacks and batteries


---
*70 images archived*
