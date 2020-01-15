"""
File:	slotmachine.py
Author:	David

Python Final Project (9/23/19)
Create a Slot Machine GUI-based application
This application should be GUI-based and contain the following features:
- A label that serves as the title of your app
- A command button that will run the application
- Fields and labels for the output as described below
- The application should randomly generate three integers between 0 and 9 (like a slot machine)
- If the player gets all three numbers the same, a JACKPOT is awarded
- If the player gets 2 of the three numbers the same, a TWO OF A KIND is awarded
- Any other combination of numbers is a LOSS
- The random numbers will need to be displayed in the GUI as well as a message describing the game outcome
"""


from breezypythongui import EasyFrame
import random

class SlotMachine(EasyFrame):

	def __init__(self):

		# Adding window and widgets
		EasyFrame.__init__(self, title = "Slot Machine!")
		self.setResizable(False);


		# Create a panel for everything to exist on
		dataPanel = self.addPanel(row = 0, column = 0, columnspan = 3, background = "plum")
		bgPanel = self.addPanel(row = 1, column = 0, columnspan = 3, background = "cornflowerblue")
		bgSlot1 = bgPanel.addPanel(row = 5, column = 0, background = "gold")
		bgSlot2 = bgPanel.addPanel(row = 5, column = 1, background = "gold")
		bgSlot3 = bgPanel.addPanel(row = 5, column = 2, background = "gold")


		# Adding introductory fields
		self.title = dataPanel.addLabel(text = "Lucky Slots!!!", row = 0, column = 0,columnspan = 3, sticky = "NSEW")
		self.title["background"] = "plum"
		self.instruction = dataPanel.addLabel(text = "Each time you lost it will cost 10 points.\nIf you win TWO OF A KIND you will win 30 points.\nIf you win the JACKPOT you will win 50.", row = 1, column = 0, columnspan = 3, sticky = "NSEW")
		self.instruction["background"] = "plum"


		# Adding score keeping fields
		self.bettingPool = bgPanel.addLabel("Points:", row = 2, column = 0, sticky = "NSEW", background = "orange")
		self.points = bgPanel.addIntegerField(value = 100, row = 2, column = 1)
		self.points["background"] = "orange"
		bgPanel.addLabel(" ", row = 2, column = 2, background = "cornflowerblue")


		# Adding fields for the Slots
			# Output Label
		self.output = bgPanel.addTextField(text = "", row = 4, column = 0, columnspan = 3, sticky = "NSEW")

			# Slot Labels
		self.slotLabel1 = bgSlot1.addLabel(text = "Slot 1", row = 5, column = 0, sticky = "NSEW")
		self.slotLabel1["background"] = "gold"

		self.slotLabel2 = bgSlot2.addLabel(text = "Slot 2", row = 5, column = 1, sticky = "NSEW")
		self.slotLabel2["background"] = "gold"

		self.slotLabel3 = bgSlot3.addLabel(text = "Slot 3", row = 5, column = 2, sticky = "NSEW")
		self.slotLabel3["background"] = "gold"

			# Adding IntegerFields for Slots
		self.firstSlot = bgSlot1.addIntegerField(value = 0, row = 6, column = 0, sticky = "NSEW")
		self.firstSlot["background"] = "gold"

		self.secondSlot = bgSlot2.addIntegerField(value = 0, row = 6, column = 1, sticky = "NSEW")
		self.secondSlot["background"] = "gold"

		self.thirdSlot = bgSlot3.addIntegerField(value = 0, row = 6, column = 2, sticky = "NSEW")
		self.thirdSlot["background"] = "gold"


		# Adding Command Buttons
			# Play the slots games
		self.slotsButton = bgPanel.addButton("Play Slots!", row = 7, column = 0, columnspan = 2, command = self.playSlots)
		self.slotsButton["background"] = "limegreen"

			# Reset the Points to play again
		self.resetButton = bgPanel.addButton("Reset", row = 7, column = 1, columnspan = 2, command = self.reset)
		self.resetButton["background"] = "limegreen"


	# Method that sets up all the data for the running of the slots game
	def playSlots(self):
		# Points Pool Variable
		adjPoints = self.points.getNumber()
		
		# Text Output
		messages = ["WINNER!  JACKPOT!!!",
					"WINNER!  TWO OF A KIND!!",
					"Sorry, no matches.  Try again?!",
					"Sorry, no more points to play..."]

		# Randomly Generated Slots
		slot1 = random.randint(0, 9)
		slot2 = random.randint(0, 9)
		slot3 = random.randint(0, 9)

		# Setting Numbers to the slot IntegerFields
		self.firstSlot.setNumber(slot1)
		self.secondSlot.setNumber(slot2)
		self.thirdSlot.setNumber(slot3)

		# If none of the slots match one another then the player loses
		if slot1 != slot2 and slot1 != slot3 and slot2 != slot3:
			adjPoints = adjPoints - 10
			self.points.setNumber(adjPoints)
			self.output.setText(messages[2])
			self.output["background"] = "tomato"
			self.firstSlot["background"] = "white"
			self.secondSlot["background"] = "white"
			self.thirdSlot["background"] = "white"

			# Check to see if the player has anymore points
			if adjPoints == 0:

				# If not then display message and disable the button
				self.output.setText(messages[3])
				self.slotsButton["state"] = "disabled"
		# Else Check all the slots for equality
		else:
			self.checkSlots(slot1, slot2, slot3, adjPoints, messages)
			self.checkSlots(slot1, slot3, slot2, adjPoints, messages)
			self.checkSlots(slot2, slot1, slot3, adjPoints, messages)


	# Method that checks the equality of all the slot numbers
	def checkSlots(self, slot1, slot2, slot3, adjPoints, messages):
		# If the first and second slot are the same
		if slot1 == slot2:

			# And the second and third are the same
			if slot2 == slot3:

				# Then we have a Jackpot!
				adjPoints = adjPoints + 50
				self.points.setNumber(adjPoints)
				self.output.setText(messages[0])
				self.output["background"] = "forestgreen"
				self.firstSlot["background"] = "forestgreen"
				self.secondSlot["background"] = "forestgreen"
				self.thirdSlot["background"] = "forestgreen"

			# Else we have a 2 of a kind
			else:
				adjPoints = adjPoints + 30
				self.points.setNumber(adjPoints)
				self.output.setText(messages[1])
				self.output["background"] = "forestgreen"
				self.firstSlot["background"] = "forestgreen"
				self.secondSlot["background"] = "forestgreen"
				self.thirdSlot["background"] = "forestgreen"


	# Method that reenstates the 'Play Again' button and resets some variables and panels
	def reset(self):
		resetPoints = self.points.getNumber()
		resetPoints = 100
		self.points.setNumber(resetPoints)
		self.output.setText("")
		self.output["background"] = "white"
		self.slotsButton["state"] = "normal"


def main():
	SlotMachine().mainloop()

main()