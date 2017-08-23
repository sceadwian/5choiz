#V 0.0.1 - zOPClogR_0_0_1.py created from  5choiz version 0.0.13
#V 0.0.2 - 
#V 0.0.3 - 
#V 0.0.4 - 
#V 0.0.5 - 
#V 0.0.6 - 
#V 0.0.7 - 
#V 0.0.8 - 
#V 0.0.9 - 
#V 0.0.10 - 
#V 0.0.11 - 
#V 0.0.12 - 
#V 0.0.13 - 
#V 0.1.1 - 
#V 0.1.2 - 
#V 0.1.3 - 
#V 0.1.4 - 
#V 0.1.5 - 
#V 0.1.6 - 
#V 0.1.7 - 
#V 0.1.8 - 
#V 0.1.9 - 


import time #used for time.sleep(x)
#import pandas as pd
#import numpy as np



def load_data(filename):

		return 0


def MainMenu():
	print ('1. Load dta from csv file') #This selection will be used to open a CSV file
	print ('2. Print Data') #Use the data to print the data from the loaded CSV file
	print ('3. Individual averages') #Use this selection to print individual averages
	print ('4. Quit') 

	while True:
		try:
			selection=int(input('Enter your choice: ')) #Ensures the input is an integer
			if selection==1:
				switch_load_data()
			elif selection==2:
				switch_PrintSomeColumns()
			elif selection==3:
				switch_Aggregators()
			elif selection==4:
				break
			else:
				print('Invalid choice. Enter 1-4')
				MainMenu()
		except ValueError: #Handles the potential of an entry that includes non numerical values
			print('Invalid choice. Enter 1-4')
	exit
	


print ("\n================================================================================")
print ("     LBS OPC logR v0.0.1\n")
print ("================================================================================\n\n")

