# Sound Controlled LED's - Pocket Disco

Source: https://www.instructables.com/Sound-Controlled-LEDs-Pocket-Disco/

---


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)

Make your own pocket disco with some music controlled LED’s. All you need is some music or sound and the
LED’s will dance around to the sound.

This is a really run little circuit to build and only needs a few components to make it. The main one being the 4017 IC which is also known as a decade counter. This little integrated circuit can count to 1 to 10 and controls the LED’s. You can use these IC’s to build LED chasers (just like Kit from Knightrider) and this build is similar but for one major difference. It utilises a transistor and microphone which allows it to react to sound!

If you have never built a circuit before or are only a beginner, then I strongly suggest that you check out my ‘ible here and get the basics down first.

The case I used is a cigarette rolling machine which you can pick-up cheaply on eBay.

Check out the YouTube clip to see it in action


## Step 1: Parts

![Step 1: Parts image 1](images/step01_01.jpg)

![Step 1: Parts image 2](images/step01_02.jpg)

![Step 1: Parts image 3](images/step01_03.jpg)

![Step 1: Parts image 4](images/step01_04.jpg)

![Step 1: Parts image 5](images/step01_05.jpg)

![Step 1: Parts image 6](images/step01_06.jpg)

![Step 1: Parts image 7](images/step01_07.jpg)

![Step 1: Parts image 8](images/step01_08.jpg)

![Step 1: Parts image 9](images/step01_09.jpg)

PARTS LIST:

1. 4017 IC – eBay

2. Toggle Switch – eBay

3. LED’s X 11 – Buy an assorted lot from eBay.

4. BC547 Transistor – eBay

5. 1uf Capacitor – Buy them in assorted lots eBay

6. Resistors - buy them in assorted lots - eBay

a. 2 x 470R

b. 2 X 20K

c. 1 X 2M

7. Electret Condenser Microphone - eBay

8. Prototype Board - eBay

9. Cigarette Roller Machine (Case) – eBay

10. Wires

11. 9V Battery

12. 9V Battery holder – eBay


## Step 2: Modding the Case

![Step 2: Modding the Case image 1](images/step02_01.jpg)

![Step 2: Modding the Case image 2](images/step02_02.jpg)

![Step 2: Modding the Case image 3](images/step02_03.jpg)

![Step 2: Modding the Case image 4](images/step02_04.jpg)

First thing you will need to do is to mod the cigarette roller.

Steps:

1. There is a piece of plastic inside the roller that needs to be removed. Push both the metal pins in which is holding the plastic section and remove it.

2. There is also a roller that moves up and down when the lid is closed. Remove this as well by pushing in the pin.

3. Remove the small hinges on each side that the roller was connected to

4. Lastly, I cut away the side sections that held the roller in place just to make more room inside the case.


## Step 3: Adding the Switch Etc.

![Step 3: Adding the Switch Etc. image 1](images/step03_01.jpg)

![Step 3: Adding the Switch Etc. image 2](images/step03_02.jpg)

Steps:

1. Decide where you want to add the toggle switch and secure in place

2. I also drilled the microphone hole as well at this time. You will also need to add a hole somewhere for 1 LED – I added this to the middle of the case


## Step 4: Making the Circuit - Ground and Positive Connections

![Step 4: Making the Circuit - Ground and Positive Connections image 1](images/step04_01.jpg)

![Step 4: Making the Circuit - Ground and Positive Connections image 2](images/step04_02.jpg)

![Step 4: Making the Circuit - Ground and Positive Connections image 3](images/step04_03.jpg)

![Step 4: Making the Circuit - Ground and Positive Connections image 4](images/step04_04.jpg)

First thing I like to do is to make the ground and positive connections on the IC.

Steps:

1. Solder into the prototype board an IC socket. You could solder directly into the board but I find it’s a lot safer adding a IC socket

2. Connect pins 13, 15 and 8 on the IC to ground on the prototype board

3. Connect pin 16 on the IC to positive


## Step 5: Adding the Transistor and Resistors

![Step 5: Adding the Transistor and Resistors image 1](images/step05_01.jpg)

![Step 5: Adding the Transistor and Resistors image 2](images/step05_02.jpg)

![Step 5: Adding the Transistor and Resistors image 3](images/step05_03.jpg)

![Step 5: Adding the Transistor and Resistors image 4](images/step05_04.jpg)

Steps:

1. The single LED needs to have a 470 Resistor attached. Solder one to pin 12 on the IC and then to a bare section on the prototype board. You’ll need to solder a wire to the end of the resistor later.

2. Next, solder the transistor into the prototype board close to the top section of the IC as shown in the images

3. Connect pin 14 on the IC to the first leg on the transistor

4. Add a 20K resistor to the same leg and connect it to positive on the prototype board

5. Connect a 2M resistor to the middle leg and positive


## Step 6: Adding a Cap and More Resistors

![Step 6: Adding a Cap and More Resistors image 1](images/step06_01.jpg)

![Step 6: Adding a Cap and More Resistors image 2](images/step06_02.jpg)

![Step 6: Adding a Cap and More Resistors image 3](images/step06_03.jpg)

Steps:

1. Connect the positive leg on the 1uf cap to the middle leg on the transistor. The negative leg should be soldered on an empty solder point on the board

2. Add a 20K resistor to the negative leg on the cap and then to positive on the prototype board

3. Connect the 3rd leg on the transistor to ground


## Step 7: Wiring-up the Circuit

![Step 7: Wiring-up the Circuit image 1](images/step07_01.jpg)

![Step 7: Wiring-up the Circuit image 2](images/step07_02.jpg)

![Step 7: Wiring-up the Circuit image 3](images/step07_03.jpg)

![Step 7: Wiring-up the Circuit image 4](images/step07_04.jpg)

![Step 7: Wiring-up the Circuit image 5](images/step07_05.jpg)

![Step 7: Wiring-up the Circuit image 6](images/step07_06.jpg)

![Step 7: Wiring-up the Circuit image 7](images/step07_07.jpg)

You next need to add some wires to the circuit in order to be able to attached it to the microphone, LED’s, batteries etc. I like to use computer ribbon wire for this type of thing as it’s thin and comes connected together. I get this for free from places where e-waste is disposed of – i.e. recycling centres, dumps etc.

Steps:

1. First attach a couple of wires for the microphone. One needs to be connected to the negative leg of the capacitor – the other one needs to be soldered to the ground section on the prototype board

2. Next add a couple of wires for the single LED. Solder one wire to the 470R resistor leg that is connected to pin 12 and the other to ground

3. Now it’s time to solder on all of the wires for the LED’s. You will need to solder 10 wires to different pins on the IC. You can see in the images below, I used ribbon wire to make all of the connections to the pins. Use the schematic to work out the order of how the wires are to be connected to the IC

1. Add a couple of wires so you can connect each of the ground and positive strips on the prototype board.


## Step 8: Preparing the Prototype Board for the LED's

![Step 8: Preparing the Prototype Board for the LED's image 1](images/step08_01.jpg)

![Step 8: Preparing the Prototype Board for the LED's image 2](images/step08_02.jpg)

![Step 8: Preparing the Prototype Board for the LED's image 3](images/step08_03.jpg)

![Step 8: Preparing the Prototype Board for the LED's image 4](images/step08_04.jpg)

![Step 8: Preparing the Prototype Board for the LED's image 5](images/step08_05.jpg)

I decided to paint the prototype board silver so it would blend into the cigarette rolling case.

Steps:

1. First cut the board so you have a strip that will fit into the case. It need to fit into the section where the cigarettes come out of.

2. Next add a few coats of silver paint to the front of the prototype board

3. Leave to dry for a few hours

4. As you will be super gluing this to the inside of the case, you'll need to remove some of the paint on each side with a file. You could also just tape it up before painting - something I forgot to do!


## Step 9: Adding the LED's

![Step 9: Adding the LED's image 1](images/step09_01.jpg)

![Step 9: Adding the LED's image 2](images/step09_02.jpg)

![Step 9: Adding the LED's image 3](images/step09_03.jpg)

![Step 9: Adding the LED's image 4](images/step09_04.jpg)

Steps:

1. Work out the best way to add the LED's to the board. I put to together and left a one hole gab between each 2.

2. When adding them I initially soldered each negative leg together in each group of 2. I found that this didn't work and had to solder each positive and negative leg together. I'm not too sure what wrong here but you can easily rectify this by soldering all of the negative legs to one of the long solder strips on the board.


## Step 10: Wiring the LED's to the IC

![Step 10: Wiring the LED's to the IC image 1](images/step10_01.jpg)

![Step 10: Wiring the LED's to the IC image 2](images/step10_02.jpg)

Steps:

1. If you wire all of the negative legs to the same strip on the prototype board then all you need to do is to add a 470 resistor to the same strip and then add a wire and connect to negative on the circuit board.

2. If you connect the LED legs positive to negative like I did, then you need to solder a wire to each of the connected legs and then connect it to the resistor. Don't do it like this as it is just a waste of time.

3. Next you need to attach all of the positive legs on the LED's to the ribbon wire connected to the IC. Take your time and make sure you look at the schematic to ensure you have the right legs connected to the right wires


## Step 11: Adding the Mic and Power

![Step 11: Adding the Mic and Power image 1](images/step11_01.jpg)

![Step 11: Adding the Mic and Power image 2](images/step11_02.jpg)

![Step 11: Adding the Mic and Power image 3](images/step11_03.jpg)

![Step 11: Adding the Mic and Power image 4](images/step11_04.jpg)

![Step 11: Adding the Mic and Power image 5](images/step11_05.jpg)

![Step 11: Adding the Mic and Power image 6](images/step11_06.jpg)

![Step 11: Adding the Mic and Power image 7](images/step11_07.jpg)

![Step 11: Adding the Mic and Power image 8](images/step11_08.jpg)

Steps:

1. Solder the wires from the circuit to the microphone. Mic's seem to have a polarity so make sure you solder the right wire to each solder point. If you find that the LED's don't flash to sound then you might have them connected incorrectly

2. Add the negative wire from the 9v battery terminal to the ground section on the circuit.

3. Add the positive to the switch and then add another wire from the switch to the positive section on the circuit.

4. At this stage if you feel confident, you can stick the circuit board down inside the case. Use some good, double sided tape and make sure that the circuit is insulated from the case.

5. Close-up the case and turn on the switch

6. You should see the LED's come on but not move. Tap the mic - do the LED’s move? If so congrats, you have finished your very own pocket disco. Next, play some music close to the pocket disco – you will find that the closer it is, the more sensitive the LED’s and the more they will flash. Move it away and the LED’s move more rhythmically to the music

If nothing happens, then you will need to check the connections and trouble shoot. I had a lot of issues initially with my circuit and for the life of me couldn’t work out what was wrong. In the end I worked out that I stuck the wrong IC into the circuit!


---
*56 images archived*
