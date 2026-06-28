# Sound Bending Synth

Source: https://www.instructables.com/Sound-Bending-Synth/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

I’ve built a few sound bending machines before (check out the links below to the ‘ibles). This time I added a reverb and amp module which really gives you a whole new range of sounds to play around with. Plus, the voice recorder module used in the synth is pretty quiet without an amp so now you can really annoy the neighbours properly.

This is a relatively simple build and doesn’t need any circuits to be made as I use 3 off-the-shelf modules and mash them together. There is some soldering that needs to be done but it’s not too difficult. Anyone who is new to circuits and wants to try their hand at this should check out my ‘ible here.

The basis of this synth is a circuit bend sound recording module. You can control the speed of the sound recorded along with pause and re-start giving you the ability to control the sound. Next I added a reverb and echo module. This allows you to further control the sound and gives you more options with the sound effects. Lastly, I added an amp module so you can hear everything and also have volume control.

I stuck it all in a vintage tuner analyser which I found at the local junk shop.

Hackaday were also nice enough to review this 'ible - check it out [here](https://hackaday.com/2020/02/04/nifty-soundbender-built-from-ebay-modules/)

Enjoy


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

![Step 1: Parts image 3](images/step01_03.jpg)

![Step 1: Parts image 4](images/step01_04.jpg)

![Step 1: Parts image 5](images/step01_05.jpg)

Parts

Modules

Sound Module – [eBay](https://www.ebay.com.au/itm/ISD1820-Sound-Recorder-Voice-Recording-Module-With-Micophone-Loudspeaker-New/191993549376?hash=item2cb3b51240:m:m4nwD-DzuPQ4Ogejrvm8M5g:rk:1:pf:0)

Reverb Module – [eBay](https://www.ebay.com.au/itm/PT2399-Microphone-Reverb-Plate-Reverberation-Board-No-Preamplifier-Function/232453344559?hash=item361f4c8d2f:g:D-MAAOSwcgZZlvbt:rk:1:pf:0)

Amp Module– [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=DC+1.8-12V+0.1+W-5+W+TDA2822M+&_sacat=0)

Switches

Momentary on/off X 2 – [eBay](https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=p2047675.m570.l1313.TR12.TRC2.A0.H0.Xmomentary+switch.TRS0&_nkw=momentary+switch&_sacat=0)

On/off X 1 – [eBay](https://www.ebay.com.au/itm/AC-250V-2A-120V-5A-ON-ON-2-Position-SPDT-Mini-Micro-Toggle-Switch-Red-C1Y9/183032785348?epid=1394258673&hash=item2a9d9aa9c4:rk:1:pf:0)

On/off X 1 (3 solder points) - [eBay](https://www.ebay.com.au/itm/2-X-AC120V-5A-250V-2A-3PDT-9-Pin-ON-ON-2-Positions-Latching-Toggle-Switch/122624737551?hash=item1c8d01010f:rk:1:pf:0)

Potentiometers

50K X 1 – [eBay](https://www.ebay.com.au/itm/2PCS-50K-B50K-Ohm-Linear-3-Terminal-Taper-Rotary-Potentiometer-Panel-Pot/232389701062?hash=item361b816dc6:g:FxIAAOSwXXxZU3sL:rk:9:pf:0)

500K X 1 – [eBay](https://www.ebay.com.au/itm/2-5-10PCS-B500K-50K-1K-Ohm-3-Pins-Shaft-Linear-Rotary-Taper-Potentiometer-WH148/263838249404?hash=item3d6dfc31bc:m:mgx7CZa9H2tiDe7pctMa_2Q:rk:10:pf:0)

Batteries

3 X AAA Battery Holder – eBay

AAA Batteries X 3

9V Battery Holder – eBay

9v Battery

Other bits and pieces

Wire

Case to stick it all in. I used a vintage Tune up analyser for a car

Speaker – eBay


## Step 2: Circuit Hacking the Sound Module

![Step 2: Circuit Hacking the Sound Module image 1](images/step02_01.jpg)

![Step 2: Circuit Hacking the Sound Module image 2](images/step02_02.jpg)

![Step 2: Circuit Hacking the Sound Module image 3](images/step02_03.jpg)

![Step 2: Circuit Hacking the Sound Module image 4](images/step02_04.jpg)

![Step 2: Circuit Hacking the Sound Module image 5](images/step02_05.jpg)

So of you might remember my ‘ible on circuit hacking a sound recorder. This uses the same module but leaves out a few of the circuit bends I have updated the image which shows all of the circuit bends that you will need to do.

Steps:

1. Solder a couple of wires to the bottom of the IC solder pads for the Potentiometer. Use the below image to identify them.

2. Next solder 2 more lots of wires to the IC, one lot for the re-start switch and the other for the pause switch.

That’s the wires for the circuit bend added. If you want to you can add the pot and the momentary switches to the wires and test prior to the build.


## Step 3: Adding the Rest of the Wires to the Sound Module

![Step 3: Adding the Rest of the Wires to the Sound Module image 1](images/step03_01.jpg)

![Step 3: Adding the Rest of the Wires to the Sound Module image 2](images/step03_02.jpg)

![Step 3: Adding the Rest of the Wires to the Sound Module image 3](images/step03_03.jpg)

![Step 3: Adding the Rest of the Wires to the Sound Module image 4](images/step03_04.jpg)

![Step 3: Adding the Rest of the Wires to the Sound Module image 5](images/step03_05.jpg)

You need to add a few more wires to the sound module to you can wire it up to the other module and also extend the switches which are on the board. You’ll also need to remove the microphone so you can attach it to the outside of the case.

Steps:

1. Add a couple of wires to the speaker output on the module. These will be connected to the reverb module later on

2. Add wires to the positive and ground sections on the sound module

3. Add a couple of wires to the repeat section indicated on the drawing in the previous step

4. De-solder the mic from the board and add a couple of wires to the solder points. You’ll need to attach the mic onto the wires later

5. Lastly, you will need to add some wires to each of the solder points for play and record. These will be attached to the momentary switches later on.

That’s it for the sound module. Find a good spot in the case and attach it. I usually just use some good double sided tape in case I need to remove it for some reason later.


## Step 4: Modding the Reverb Module

![Step 4: Modding the Reverb Module image 1](images/step04_01.jpg)

![Step 4: Modding the Reverb Module image 2](images/step04_02.jpg)

![Step 4: Modding the Reverb Module image 3](images/step04_03.jpg)

The reverb board needs a couple of modifications to be able to add the echo. I also had to remove the reverb pot on the module so I could place it in a position in the case that made sense. Be careful when removing this pot as the solder pads on the module can come off (I know as it happened to me the first time I tried! That’s why you always buy 2…)

Steps:

1. First you need to remove resistor R27. The best way I found was to use an exacto knife and just cut it away. You can also de-solder them quite easily but be careful not to connect the 2 solder points together

2. Solder 3 wires to the 3 small solder points on the board next to R27. These need to be soldered to the legs on a 50K pot. Solder the wires to the pot as if you were soldering the pot directly to the board. This will give you the correct orientation.

3. The reverb module won’t work with an amp. I initially tried to build one from a 386 IC but the reverb wouldn't come through so I decided just to buy one and hack it.

That’s all the modding you will need to do to the board


## Step 5: Adding the Rest of the Wires to the Reverb Module

![Step 5: Adding the Rest of the Wires to the Reverb Module image 1](images/step05_01.jpg)

![Step 5: Adding the Rest of the Wires to the Reverb Module image 2](images/step05_02.jpg)

![Step 5: Adding the Rest of the Wires to the Reverb Module image 3](images/step05_03.jpg)

Steps:

1. To connect the sound module to the reverb one, all you need to do is to connect the speaker positive and negative points on the sound module to the “in” section on the reverb module. Just solder a couple of wires to join them together

2. There is also a power section on the reverb module so attach a couple of wires to this. You'll also need to wire up to an on/off switch to the module. You can do that later when you are ready to wire everything up in the case.

3. Next, attach a couple of wires to the output section on the module

4. Lastly, attach the module to the inside of the case with some good, double sided tape


## Step 6: How the Modules Are Connected

![Step 6: How the Modules Are Connected image 1](images/step06_01.jpg)

The heart of this synth is the 3 modules. They are connected together as per the image below. It's actually pretty straight forward once you strip back all of the wires, switches, pots etc.

The thing you will need to remember is each module will need it's own power supply. If you used the same power supply for the sound recorder module and the amp, then for some reason it by-passes the reverb module. This means you will need 2 X 9v battery's, plus 3 X AAA batteries. It's a fair bit of power not I couldn't find a way around it.

You can however connect all of them together using 1 switch which has 3 solder points on it. I have added a link in the parts section to this switch.


## Step 7: Modding the Case

![Step 7: Modding the Case image 1](images/step07_01.jpg)

![Step 7: Modding the Case image 2](images/step07_02.jpg)

![Step 7: Modding the Case image 3](images/step07_03.jpg)

![Step 7: Modding the Case image 4](images/step07_04.jpg)

Whatever case you choose, make sure that it has enough room in it to fit all the batteries, modules etc.

I went with a vintage car tuner analyser that I got from the local junk shop. I thought it had a pretty cool 70’s futuristic vibe that would suit this synth well.

I’ll go through some of the mods I did to the case which might give you a few ideas for your one

Steps

1. Un-screw the housing of the case

2. Remove any of the electronic components from inside the case. If there is any interesting electrical parts, then take these off for future projects

3. Next I usually remove any pieces of plastic and gussets that might get in the way when I’m stuffing it with my components.

4. Usually I would give it a god wash but I forgot this step


## Step 8: Designing the Case Front - Part 1

![Step 8: Designing the Case Front - Part 1 image 1](images/step08_01.jpg)

![Step 8: Designing the Case Front - Part 1 image 2](images/step08_02.jpg)

![Step 8: Designing the Case Front - Part 1 image 3](images/step08_03.jpg)

I’ve done a few of these mods now and in my opinion there are a couple ways to go about it. You can either just use the original look of the case and add your parts to it, or you can make it a bit more original. Giving the case an original look and feel isn’t too difficult, although sometimes you need to make a decision that could potentially ruin the case. Luckily I managed not ro wreck this one.

Steps:

1. The front section has a metal cover with some labels on it and I didn’t want to have this showing. Plus it had a plastic protection on it which had been there so long it wouldn’t peel off any longer. I decided to remove this and use the back of it instead.

2. Carefully pry off the cover making sure you don’t bend it at all. Usually the glue is old and brittle so you can get the covers off without much prying.

3. Once it is off, clean off the dried glue. I use goof off for this which worked well.

4. Next I had to bend the bottom section so it would sit on the case. I did this with a vice.

5. Give it a polish with a metal polish and once you are happy with the finish, glue back onto the front of the case


## Step 9: Designing the Case Front - Part 2

![Step 9: Designing the Case Front - Part 2 image 1](images/step09_01.jpg)

![Step 9: Designing the Case Front - Part 2 image 2](images/step09_02.jpg)

![Step 9: Designing the Case Front - Part 2 image 3](images/step09_03.jpg)

Next part that I had to work out was how to mount the speaker into the case. I could have done this a few ways but in the end I went with ply wood. This gives it a great retro “Atari” look.

I had to be careful also of the space inside as it was starting to get tight.

Steps:

1. First, decide where the best place to mount the ply wood is. Initially I was going to add it o the outside of the case but the finish would have been too rough. I decided to mount the wood to the inside and although this took up some precious space, the finish was much better.

2. Cut a piece of thin ply wood to size

3. Add a stain to the wood

4. I didn’t attached the wood to the case until right at the end as I didn’t work it out until then! If I had though, I would have attached it earlier.

5. Next I cut a hole for the speaker in the middle of the ply wood and also drilled a hole for the microphone.

6. Glue into place


## Step 10: Designing the Case Front - Part 3

![Step 10: Designing the Case Front - Part 3 image 1](images/step10_01.jpg)

![Step 10: Designing the Case Front - Part 3 image 2](images/step10_02.jpg)

![Step 10: Designing the Case Front - Part 3 image 3](images/step10_03.jpg)

![Step 10: Designing the Case Front - Part 3 image 4](images/step10_04.jpg)

![Step 10: Designing the Case Front - Part 3 image 5](images/step10_05.jpg)

![Step 10: Designing the Case Front - Part 3 image 6](images/step10_06.jpg)

Last thing to do is to work out where all of the pots and switches are going to go. I like to place the knobs on the case and move them around until I find a design that I’m happy with.

Steps:

1. Once you are happy with the design you will need to drill out the holes for each of the pots and switches.

2. If you have to drill holes into the metal section like I did. Then make sure that the case is resting flat on a piece of wood. This way you will take the pressure off the metal and get better drilled holes

3. Keep on drilling until you have all of the holes you need.

4. Now you can start to add the pots, switches etc. Secure all of the pots and switches into place and add the knobs


## Step 11: Connecting the Pots, Switches Etc

![Step 11: Connecting the Pots, Switches Etc image 1](images/step11_01.jpg)

![Step 11: Connecting the Pots, Switches Etc image 2](images/step11_02.jpg)

![Step 11: Connecting the Pots, Switches Etc image 3](images/step11_03.jpg)

![Step 11: Connecting the Pots, Switches Etc image 4](images/step11_04.jpg)

![Step 11: Connecting the Pots, Switches Etc image 5](images/step11_05.jpg)

![Step 11: Connecting the Pots, Switches Etc image 6](images/step11_06.jpg)

![Step 11: Connecting the Pots, Switches Etc image 7](images/step11_07.jpg)

![Step 11: Connecting the Pots, Switches Etc image 8](images/step11_08.jpg)

![Step 11: Connecting the Pots, Switches Etc image 9](images/step11_09.jpg)

![Step 11: Connecting the Pots, Switches Etc image 10](images/step11_10.jpg)

Steps:

1. Place the 2 parts of the case side by side. This will make it easy to decide how long to cut the wires. Also, you want to be able to lay the top case flat so it is easy to work on and change the batteries in the future

2. You want to try and make the wire connections as short as possible. Wire seems to take up more room than you would expect so reducing the length with give you more room in the case.

3. Start to solder on the wires from the modules to the pots

4. Next solder on the wires to the switches.

5. Once you have all of the wires attached to the pots etc, you then need to wire-up the power to each of the modules.

6. I used a switch with 3 solder points to connect each of the power sources.

7. The last couple of things to do (for me anyhow) is to attach the microphone, speaker and output jacks


## Step 12: Adding the Output Jacks

![Step 12: Adding the Output Jacks image 1](images/step12_01.jpg)

![Step 12: Adding the Output Jacks image 2](images/step12_02.jpg)

![Step 12: Adding the Output Jacks image 3](images/step12_03.jpg)

The output jack jacks aren’t necessary but it’s definitely worth taking the time to add them. One allows you to plug in an external amp to get the sound cranking, the other allows you to record music directly into the sound module

Steps:

External Amp

1. The easiest way to do this is to secure a couple of extra wires to there the speaker wire are connected to the amp. As I had to place by amp up-side-down, I decided to just solder the 2 wires to the solder points on the bottom of the amp module.

2. Next, solder the 2 wires to the solder points on the output jack. The positive usually goes to the top solder point and the negative to the bottom. If you find it doesn’t work, then just swap them around

Record Music Directly

1. This output jack is connected directly to the microphone. I used the solder points on the mic to connect these wires. It means that there will be 2 wires to each solder point on the mic so you need to be careful that they don’t touch or you don’t get any solder on the actual body of the mic or it won’t work.

2. Connect the other ends of the wires to the solder points on the output jack. I’m not sure if it matters about which solder point they connect to – mine worked first go!


## Step 13: Microphone and Speaker

![Step 13: Microphone and Speaker image 1](images/step13_01.jpg)

![Step 13: Microphone and Speaker image 2](images/step13_02.jpg)

![Step 13: Microphone and Speaker image 3](images/step13_03.jpg)

![Step 13: Microphone and Speaker image 4](images/step13_04.jpg)

![Step 13: Microphone and Speaker image 5](images/step13_05.jpg)

![Step 13: Microphone and Speaker image 6](images/step13_06.jpg)

Next thing I had to add was the microphone and speaker.

Steps.

1. I attached the speaker to the front ply wood panel with some glue and soldered the wires from the amp to the speaker

2. I also decided to place the microphone up near the speaker. Up to you where you want to put it but I found this was the best spot for my build

3. Once you have connected everything, it’s time to turn it on and see if it works.


## Step 14: How to Use the Synth

![Step 14: How to Use the Synth image 1](images/step14_01.jpg)

![Step 14: How to Use the Synth image 2](images/step14_02.jpg)

![Step 14: How to Use the Synth image 3](images/step14_03.jpg)

Using the synth is pretty straight forward. There are a couple things you need to remember which I will go through but other than that – it’s up to you how you want to play it

Make sure the repeat if off before recording

If you don’t flick the repeat switch to off then you won’t be able to record into the module. Once you have recorded what you wanted, flick the repeat switch to on and away you go

If you added audio jacks then you can do a couple neat tricks

One audio jack is hooked up to the speakers and you can plug-in an external amp and play the synth through this. If you find that it’s not working, then just swap the wires around soldered onto the jack output plug

The other one is connected to the solder points on the mic. If you plug your phone into this one and hold record on the synth while playing music you can record it directly to the module. This allows you to bend and twist a piece of music of your choice. Only downside is you can’t hear the music as it records so it’s tricky getting the right length etc.

You can also add more controls if you want to.

Check out my [circuit bent sound module ible here](https://www.instructables.com/id/Lo-Fi-Voice-Sampler-Circuit-Bending-/). It has a few more add-ons that you can include to the sound module

I have included an image below with the synth labelled so you know what each pot and button does.

Have fun and if you do make one I’d love to see the finished version.

Let me know if you have any questions as well.


---
*62 images archived*
