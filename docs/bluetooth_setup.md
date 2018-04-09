# Bluetooth Setup
*Note:* This guide is written for MacOS. 

#### Step 1: Turn on Bluetooth on the brick
1. Turn on your `ev3` brick by pressing the center button.
2. On the brick, select `Wireless and Networks → Bluetooth`.
3. Turn on Bluetooth (If the little box is filled in then Bluetooth is already enabled).
4. Turn on Visible.

#### Step 2: Turn on Bluetooth on your computer
1. On your computer, Open up System Preferences and click on Bluetooth.
2. Make sure Bluetooth is *ON* and says `Now discoverable as <Computer Name>`

#### Step 3: Pair your EV3 Brick to your computer
1. On your brick click `start scan`. A list of Bluetooth enabled devices will start to pop up.
2. Scroll down until you find your computer (be careful to check that it is your computer and not somebody else’s)
3. Click on your computer name and press `pair`
	
    **IMPORTANT:** A number will appear on your brick, and on the computer screen. Make sure that you don’t hit accept unless both numbers are identical, otherwise you may be trying to connect to someone else’s computer, or someone else to you. 

4. When you are sure that you are trying to connect to the correct compute hit `accept` on your brick, and `pair` on your computer. After this do not hit connect in the `ev3` menu you are currently in.

5. After pairing, choose `Network Connection` from the menu.
6. Choose `Connect`.
7. Wait until you get a timeout error.

	Towards the top of the tab you will see something that says `state: configuring…`. Wait until it says `state: Connected`. 
