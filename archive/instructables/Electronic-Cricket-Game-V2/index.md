# Electronic Cricket Game V2

Source: https://www.instructables.com/Electronic-Cricket-Game-V2/

---

![Cover](images/cover.jpg)


## Introduction

![Intro 1](images/intro_01.jpg)

![Intro 2](images/intro_02.jpg)

![Intro 3](images/intro_03.jpg)

![Intro 4](images/intro_04.jpg)


## Supplies

![Supplies image 1](images/step02_01.jpg)

![Supplies image 2](images/step02_02.jpg)

![Supplies image 3](images/step02_03.jpg)

![Supplies image 4](images/step02_04.jpg)

![Supplies image 5](images/step02_05.jpg)

![Supplies image 6](images/step02_06.jpg)

![Supplies image 7](images/step02_07.jpg)

I have put together a parts list below. This list can also be found as a spreadsheet in my Google Drive. I have also added the gerber files, schematic and board in there as well. More on those in the next steps.PARTS:PCB - see the next step on how to get your own printed9V battery9V battery holder (one that is made for PCB connection) - eBayTactile momentary switches X 3 - eBaySPDT Sliding switches X 2 - eBayCapacitors1uf - eBay3.3uf- eBay10uf - eBay1nf X 2 - eBayResistors - Buy these in assorted lots - it's cheaper and you get a large variety - eBay12K x 220K10k X 2Trimmer Pot 5K (3362P) - eBay7 Segment display (common cathode) X 2 - eBayIC's555 - eBay4017 - eBay4026 X 2 - eBayIC Sockets8 Pin X 1 - eBay16 Pin X 3 - eBay3mm LED's X 8 (I used 6 yellow and 2 red) - eBay


## Step 1: Getting the PCB Printed

![Step 1: Getting the PCB Printed image 1](images/step03_01.jpg)

![Step 1: Getting the PCB Printed image 2](images/step03_02.jpg)

![Step 1: Getting the PCB Printed image 3](images/step03_03.jpg)

The first thing you will need to do is to get the PCB printed. It's very easy to get the board printed up and cheap as well. I like to use JPLPCB (not affiliated at all) who do a good job at printing the boards. You could also use PCB Way or Osh Park who also provide a quality product. I have decided to include this step as it can be a little daunting if it's the the first time organising a board to be printed.STEPS:1. The first thing you will need to do is to save the zipped gerber file in my GitHub Page Save the file called: Electronic Cricket Game -Gerber file to your computer2. Next, go to the JPLPCB website and click on the 'quote now' button3. Add the saved gerber file (see the first image provided)4. It will take a little bit to download but once it has you'll see the front and back of the board.5. Lastly add to shopping cart and checkout. You'll need to decide on how you want it sent as well. i usually pick the quickest option (air) but it is the most expensive.That's it! Now just sit back and wait for the boards to arrive.


## Step 2: How It All Works

![Step 2: How It All Works image 1](images/step04_01.jpg)

![Step 2: How It All Works image 2](images/step04_02.jpg)

If you take a look at the schematic you'll see that there is in actual fact 2 circuits. The first one which is the scoreboard circuit and the second one is the game circuit.Scoreboard circuitLet's start with the 555 timer IC. This has been wired as a monostable Multivibrator which gives a 'high' pulse and acts like a switch and counts the numbers on the 7 segment display. There is a switch connected to pin 2 which allows you to cycle through the numbers on the 7 segment display.IC 4026 is a seven segment display decade counter which is used to drive a 7 segment display with input clock pulse. The 555 timer gives the clock pulse and is fed into the pin 1 of the first 4026. Two 7 segment displays are stringed together (which is why there are 2 4026 IC's) which allows for the counters to go right up to 99. Also included is a reset button to make the 7 segment display show '00' once the game is overGame CircuitThe game circuit is a well known circuit which uses a 4017 decade counter to drive LED's. There are 2 IC's used so Let's start with the 555 timer again. This time it is wired up as an astable multivibrator and has been configured to allow the LED's to mover fast or slow. This allows you to either play the game so the LED's are moving very fast across the board or at a slower pace (which means you can judge better when an LED will come on).The output from the 555 timer passes into the input of IC2 which is a Johnson Decade counter 4017. It has 10 outputs which 8 outputs are used. Output 9 ( pin9) is tied to the reset pin 15 to repeat the cycle.When the tactile switch connected to pin 6 on the 555 is pressed, the LED's will randomly start to flash. When released one LED will be lit and this what the outcome is. For example, if it lands on boundary, then you scored 4 runs.


## Step 3: Adding Components to the PCB

![Step 3: Adding Components to the PCB image 1](images/step05_01.jpg)

![Step 3: Adding Components to the PCB image 2](images/step05_02.jpg)

![Step 3: Adding Components to the PCB image 3](images/step05_03.jpg)

![Step 3: Adding Components to the PCB image 4](images/step05_04.jpg)

![Step 3: Adding Components to the PCB image 5](images/step05_05.jpg)

![Step 3: Adding Components to the PCB image 6](images/step05_06.jpg)

![Step 3: Adding Components to the PCB image 7](images/step05_07.jpg)

![Step 3: Adding Components to the PCB image 8](images/step05_08.jpg)

Soldering the components on to a PCB is the fun bit. The best advice that I can give you is to firstly, make sure you have a semi decent soldering iron and good quality solder. second, always start with the lowest height components and work up. Usually that means starting with the resistors. The board I designed is 2 sided.  One side has all of the electrical components and the other the controls and scoreboard for playing the game.  You will want to start with the component side firstSTEPSFist, start with the resistors.  There aren't many to add so will be easy to doNext, I like to add the IC sockets.  To ensure that they are soldered in flat, solder into place pin1 and then pin 9 on the IC.  check to make sure it is sitting flat and if so, solder the rest of the legs to the PCBNow you can solder on the rest of the components like the caps etcTo be able to control the brightness of the LED's I have included a 5K trimmer potDON'T solder on the battery holder yet.  Leave this to last as there are LED's that need to be soldered on under the battery holder and you need to do this first


## Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 1](images/step06_01.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 2](images/step06_02.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 3](images/step06_03.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 4](images/step06_04.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 5](images/step06_05.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 6](images/step06_06.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 7](images/step06_07.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 8](images/step06_08.jpg)

![Step 4: Adding the Switches, LED's & 7 Segment Displays to the PCB image 9](images/step06_09.jpg)

Now that you have all of the components connected, you need to flip the board and start to connect all of the parts to the front section.STEPS:First, solder into place the tactile switches - there are 3 to addNext add the LED's. take note of the polarity and ensure that you solder these in correctly. The Ground leg (cathode) needs to be aligned to the right LED hole on the PCB. Use different colours for runs (I used yellow) and wickets (I used red)The 7 segment displays can be added next.Once all the components have been added to the front side, you can go ahead and solder into place the battery holder. I added a little bit of superglue to the feet of the battery holder to keep it in place


## Step 5: How to Play - Electronic Cricket

![Step 5: How to Play - Electronic Cricket image 1](images/step07_01.jpg)

![Step 5: How to Play - Electronic Cricket image 2](images/step07_02.jpg)

![Step 5: How to Play - Electronic Cricket image 3](images/step07_03.jpg)

![Step 5: How to Play - Electronic Cricket image 4](images/step07_04.jpg)

![Step 5: How to Play - Electronic Cricket image 5](images/step07_05.gif)

The game itself is easy to play however, there may be some cricket terms that might seem weird to people new to the game so here's a glossary for each.Losing a wicket - this is when the batsman goes out and a new batsman comes into play. I usually make it 3 wickets and then the game is overBowled - This is when the blower hits the wickets and the batsman is outCaught - This is where the batsman has hit the ball and it has been caught on the full and the batsman is outBoundary - Ball hits the fence around the oval and automatically scores 4 runsSixer - Ball is hit on the full over the fenceNo Ball - Bowler goes over the line with he's foot when bowling, batsman scores 1 runHow to playTurn on the gameDecide whether you want to have the LED's move fast or slow. Slow makes the game easier.Reset the score to 00. You can do this by hitting the reset button. If it doesn't go back to 00, then hold the 'run' button and hit reset againThe LED's will be jumping all around. To play the game, hit the play button. This will freeze the LED's and only one will be on. This is the outcome of the ball being 'bowled'Use the 'run' button to add the score to the scoreboardI set the wickets at 3 - so as soon as I have 3 wickets, then the game is over. Your score is the amount of runs you make over 3 wickets.


---
*38 images archived*
