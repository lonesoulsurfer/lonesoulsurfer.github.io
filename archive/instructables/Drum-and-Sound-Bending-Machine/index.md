# Drum and Sound Bending Machine

Source: https://www.instructables.com/Drum-and-Sound-Bending-Machine/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

This Instructable mashes together 2 separate Instructables ([The Sound Bending Machine](https://www.instructables.com/id/Lo-Fi-Voice-Sampler-Circuit-Bending-/) and [Pocket Drum Machine](https://www.instructables.com/id/Pocket-Drum-Machine/)) that I’ve made in the past. I got inspired after finding a retro fire alarm enclosure in a 2nd hand store.

The Drum Bending Machine is made from a birthday card that has a small electric drum kit inside (pretty amazing actually) and a small voice recorder module. By circuit bending the voice module you can record the drums (and other sounds if you like) and then speed –up the sound or slow it down. You can also put the recording in a loop so it plays over and over again.

This project isn’t for the faint hearted. There is a lot of fiddly soldering and delicate work that needs to be done. The drum kit is a little fragile so you need to be careful not to have wires come away from the solder points. However, if you do have moderate skills with a soldering iron, most of the hard bits can be worked out easily enough.

I’ve also done a couple of schematics which will help you understand how to circuit bend the sound module and also how to wire-up the Drum Kit Module.

Check out the YouTube clip to see it in action


## Step 1: Parts and Tools

![Step 1: Parts and Tools image 1](images/step01_01.jpg)

![Step 1: Parts and Tools image 2](images/step01_02.jpg)

![Step 1: Parts and Tools image 3](images/step01_03.jpg)

![Step 1: Parts and Tools image 4](images/step01_04.jpg)

![Step 1: Parts and Tools image 5](images/step01_05.jpg)

![Step 1: Parts and Tools image 6](images/step01_06.jpg)

![Step 1: Parts and Tools image 7](images/step01_07.jpg)

![Step 1: Parts and Tools image 8](images/step01_08.jpg)

Parts:

1. Enclosure. Up to you really. Could be anything from an old walkie talkie to a tin box. Just make sure that there is enough room inside to add the electronics, batteries and wires.

2. Drum Kit Sound Card – If you live in Australia Kmart and Big W both stock the card. You can also buy it [from here](https://www.dayspring.com/wowbirthdayadifferentdrummer2interactivesongcards). I suggest that you buy 2 just in case you mess one up.

3. Sound Module – [eBay](http://www.ebay.com.au/itm/ISD1820-Voice-Recording-Playback-Module-Sound-Recorder-Board-With-Loudspeaker-/201524365876?epid=566136379&hash=item2eebc9ca34:g:7B8AAOSwzgRWwo08) (buy 2 as well)

4. Wire

5. Double sided foam tape

6. 2 x 1M Pots – [eBay](http://www.ebay.com.au/itm/10pcs-Potentiometer-Pot-B1M-1M-Linear-shaft-15mm-/262388040927?hash=item3d178bc4df:g:SlIAAOSwKfVXEJdv)

7. 2 x knobs - [eBay](http://www.ebay.com.au/itm/10PCS-Aluminium-Potentiometer-Knobs-Volume-Control-Amplifier-Shaft-6MM-Gift-OZ/132021422263?_trksid=p2045573.c100506.m3226&_trkparms=aid%3D555014%26algo%3DPL.DEFAULT%26ao%3D1%26asc%3D20151005190705%26meid%3Da88eecb26db5465b871be2e2f4a8c1f8%26pid%3D100506%26rk%3D1%26rkt%3D1%26)

8.1 x Toggle switch – [eBay.](http://www.ebay.com.au/itm/10pcs-AC-250V-2A-125V-6A-SPDT-Toggle-Rocker-Switch-ON-OFF-ON-3-Position-BI579-/201828924444?hash=item2efdf0fc1c:g:kPEAAOSw4A5YrYnN) Actually you use 2 on/off switches so if your enclosure doesn’t have one then get 2 toggle switches.

9. 2 X Momentary switches – I used [[this one](http://www.ebay.com.au/itm/10pcs-2-Pin-SPST-OFF-ON-Car-Boat-Momentary-Push-Button-Switch-0-5A-DC-50V-Red/291559068959?_trksid=p2045573.c100505.m3226&_trkparms=aid%3D555014%26algo%3DPL.DEFAULT%26ao%3D1%26asc%3D20151005190540%26meid%3D34dbcda2872947af9583a929d85f6864%26pid%3D100505%26rk%3D1%26rkt%3D1%26)](http://www.ebay.com.au/itm/5-x-Momentary-Push-Button-Horn-Switch-for-Doorbell-Boat-Car-Waterproof-Red/331856419223?_trksid=p2045573.c100506.m3226&_trkparms=aid%3D555014%26algo%3DPL.DEFAULT%26ao%3D1%26asc%3D20151005190705%26meid%3D95d12ab6b4cc4b459a93e4f6efe713d0%26pid%3D100506%26rk%3D1%26rkt%3D1%26) and this one from eBay

Tools

1. Soldering Iron,

2. Pliers

3. Wire snips

4. Dremel

5. Hot glue

6. Super glue

7. Drill


## Step 2: Adding the Pots and Switches

![Step 2: Adding the Pots and Switches image 1](images/step02_01.jpg)

![Step 2: Adding the Pots and Switches image 2](images/step02_02.jpg)

![Step 2: Adding the Pots and Switches image 3](images/step02_03.jpg)

![Step 2: Adding the Pots and Switches image 4](images/step02_04.jpg)

![Step 2: Adding the Pots and Switches image 5](images/step02_05.jpg)

![Step 2: Adding the Pots and Switches image 6](images/step02_06.jpg)

![Step 2: Adding the Pots and Switches image 7](images/step02_07.jpg)

![Step 2: Adding the Pots and Switches image 8](images/step02_08.jpg)

![Step 2: Adding the Pots and Switches image 9](images/step02_09.jpg)

![Step 2: Adding the Pots and Switches image 10](images/step02_10.jpg)

![Step 2: Adding the Pots and Switches image 11](images/step02_11.jpg)

Once you have decided on an enclosure, the first thing you will need to do is to get it open and remove any unwanted electronics. You want to create as much space as possible inside your enclosure. Next you need to decide how you want to set-up your Drum Bending Machine. You will need to have 2 pots, 5 drum pads, and 5 switches.

I've also added the diagram of how the sound module gets wired-up. This will help you understand how many switches you will need etc.

Steps:

1. Work out where you want to attach the pots. Drill a couple of holes and put them into place

2. Next, you will need to attach a switch to turn the drums on and off. My enclosure came with a on/off switch so I just used this.

3. You will also need to add 2 momentary switches, one to use to record the sound and the other to play it. The one to play the sound only plays it once, you need to add a on/off switch for the loop

4. Lastly, you will need to add 1 on/off switch (2 if your enclosure doesn't already have one) for the loop effect.


## Step 3: Adding Wires to the Switches

![Step 3: Adding Wires to the Switches image 1](images/step03_01.jpg)

![Step 3: Adding Wires to the Switches image 2](images/step03_02.jpg)

![Step 3: Adding Wires to the Switches image 3](images/step03_03.jpg)

Steps:

1. Solder a couple of wires to the solder points on the pots. You need to solder one to the middle point and the other to either of the other solder points. The one you solder it to will determine which way you have to turn the pot to speed or slow down the sound.

2. Solder wires to all of the other solder points on the switches etc

3. Now you are ready to start circuit bending


## Step 4: Circuit Bending the Sound Module

![Step 4: Circuit Bending the Sound Module image 1](images/step04_01.jpg)

![Step 4: Circuit Bending the Sound Module image 2](images/step04_02.jpg)

![Step 4: Circuit Bending the Sound Module image 3](images/step04_03.jpg)

![Step 4: Circuit Bending the Sound Module image 4](images/step04_04.jpg)

Time to circuit bend! Initially I started to solder the wire directly to the legs of the IC. This didn't work so I decided to add the wires to the IC solder points. I didn't take step by step images of all of the wires as it was just too hard to do. If you follow the diagram though you won't have any issues.

Steps

1. Have the diagram in front of you and start to solder the wires from the switches and pots to the correct spots.

2. You will also need to remove the mic so de-solder this from the board

3. Solder some wires to the battery solder points and also the mic solder points. Attach the ends of these wires to the appropriate switches

4. Next, solder the wires from the switches to the record and play legs

5. You also need to add a couple of wires to the pins indicated on the drawing so you can loop the sound. Do this and add attach them to one of the toggle switches

6. Ensure that you don't bridge any of the solder points and take your time adding all of the wires.

7. Make sure that you don’t make the wires too long, especially if your enclosure is small, they can take up quite a lot of room


## Step 5: Testing

![Step 5: Testing image 1](images/step05_01.jpg)

![Step 5: Testing image 2](images/step05_02.jpg)

Before you glue anything down, Make sure that you test everything first

Steps:

1. Power-up the board and test that the sound module is recording sound.

2. Next, play around with the pots to ensure that the sound speeds-up and slows down.

3. Try the loop switch to see if this works too.

4. If everything is working and you are happy with how it sounds, glue down the speaker and also the module with some hot glue


## Step 6: Drum Kit - Getting the Electronics Out

![Step 6: Drum Kit - Getting the Electronics Out image 1](images/step06_01.jpg)

![Step 6: Drum Kit - Getting the Electronics Out image 2](images/step06_02.jpg)

![Step 6: Drum Kit - Getting the Electronics Out image 3](images/step06_03.jpg)

![Step 6: Drum Kit - Getting the Electronics Out image 4](images/step06_04.jpg)

Next step is to add the drum kit. I played around quote a bit with this, trying to work out the best way to connect the drums to the sound module. You can connect the drums so the module records directly through the mic on the sound module instead of passively through the mic, but I couldn’t get rid of the distortion. I tried different capacitors in different locations but nothing worked. I’m sure somebody out there will have some other ideas on how to reduce the distortion. In the end I decided to just record the drums passively through the mic.

Steps:

1. Rip the card open to reveal the goodies inside.

2. Carefully remove the tape holding the wires onto the card

3. Pull off the pads from the foam tape and remove the speaker and circuit board


## Step 7: Drum Kit - Removing the Batteries

![Step 7: Drum Kit - Removing the Batteries image 1](images/step07_01.jpg)

![Step 7: Drum Kit - Removing the Batteries image 2](images/step07_02.jpg)

![Step 7: Drum Kit - Removing the Batteries image 3](images/step07_03.jpg)

You don’t want to keep the batteries that the module comes with as they will run out and you won’t be able to replace them.

Steps:

1. The batteries are held onto the circuit board with small rivets, use a drill to remove the rivets

2. The people who make this board were kind enough to add a couple of solder points to add external power to it. Solder a couple of wires to these solder points and test to make sure that the drums still work. You will find that the original switch doesn’t work anymore either. That doesn’t matter as you will add your own later.

3. The batteries will be wired-up later.


## Step 8: Drum Kit - Adding the Pads

![Step 8: Drum Kit - Adding the Pads image 1](images/step08_01.jpg)

![Step 8: Drum Kit - Adding the Pads image 2](images/step08_02.jpg)

![Step 8: Drum Kit - Adding the Pads image 3](images/step08_03.jpg)

![Step 8: Drum Kit - Adding the Pads image 4](images/step08_04.jpg)

![Step 8: Drum Kit - Adding the Pads image 5](images/step08_05.jpg)

![Step 8: Drum Kit - Adding the Pads image 6](images/step08_06.jpg)

![Step 8: Drum Kit - Adding the Pads image 7](images/step08_07.jpg)

![Step 8: Drum Kit - Adding the Pads image 8](images/step08_08.jpg)

![Step 8: Drum Kit - Adding the Pads image 9](images/step08_09.jpg)

Now comes the fiddly part. To add the pads you need to de-solder the wire from the pad and re-solder. The wires are very thin also.

Steps:

1. Pick a pad to de-solder. Take a photo of the wires and how they are soldered to the pad so you don’t get it wrong when you go to re-solder

2. De-solder the pad and add some double sided foam tape to the back

3. Tape the pad into place on the enclosure.

4. Drill some small holes (depending on how many wires were soldered to the pad) next to the solder points

5. Thread the wires through the holes and re-solder the wires onto the solder pads

6. Do the same for the other 4

7. Continuously test

NOTE: Be careful as the wires as fragile and can come away from the solder pads. If this happens, just re-solder the wire to the pad. Worst case scenario is multiple wires come off you have no idea where they should be soldered! If you check regularly then this won’t happen


## Step 9: Drum Kit - Speaker and Switch

![Step 9: Drum Kit - Speaker and Switch image 1](images/step09_01.jpg)

![Step 9: Drum Kit - Speaker and Switch image 2](images/step09_02.jpg)

![Step 9: Drum Kit - Speaker and Switch image 3](images/step09_03.jpg)

Steps:

1. First you need to de-solder the speaker from the drum kit and attach them to the same speaker that the module uses. Make sure that you have the polarities right.

2. To enable you to record the drums directly into the module you will also need to connect the microphone to the speaker and a switch so you can turn this function off. See the diagram to see how to wire this up.

3. To wire the on/off switch, and batteries you just solder one of the battery wires to the switch and then to the batteries. You can use the same batteries that the module uses.


## Step 10: Testing

![Step 10: Testing image 1](images/step10_01.jpg)

![Step 10: Testing image 2](images/step10_02.jpg)

![Step 10: Testing image 3](images/step10_03.jpg)

![Step 10: Testing image 4](images/step10_04.jpg)

So now you’re up to the fun part – playing with the drum bending machine.

Steps:

1. Record some drum beats onto the recorder. You can also record sounds along with the drums if you want to.

2. Hit the loop switch so the sound plays over and over and then start to play with the speed. You will get some really interesting sounds and beats coming from the little machine.

3. Try recording directly into the module and play around with the sound that way too.

I’m really happy with the way that the drum bending machine turned out. The enclosure definitely gives it some style and retro flair!

There are probably a heap more sound effects that could be added so if you do make one and come up with some new ones, let me know in the comments.


---
*54 images archived*
