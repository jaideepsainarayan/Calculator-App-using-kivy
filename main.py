	 
import kivy 
import math	
from kivy.app import App 
kivy.require('1.9.0') 
from kivy.uix.gridlayout import GridLayout 
# for the size of window 
from kivy.config import Config 

# Setting size to resizable 
Config.set('graphics', 'resizable', 1) 



# Creating Layout class 
class Calc(GridLayout): 

	
	def calculate(self, calculation): 
		if calculation: 
			try: 
				
				self.display.text = str(eval(calculation)) 
			except Exception: 
				self.display.text = "Error"
	def sind(self,a):
		try: 
			self.display.text= str("{0:.9f}".format(math.sin((math.radians(float(a))))))
		except Exception: 
			self.display.text = "Error"
	def cosd(self,a):
		try:
			self.display.text= str("{0:.9f}".format(math.cos((math.radians(float(a))))))
		except Exception: 
			self.display.text = "Error"
	
# Creating App class 
class CalculatorApp(App): 

	def build(self): 
		return Calc() 

# creating object and running it 
calcApp = CalculatorApp() 
calcApp.run() 

