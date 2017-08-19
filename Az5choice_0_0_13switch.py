#V 0.0.1 - absorb input from csv file
#V 0.0.2 - changed how to open file using csv module
#V 0.0.3 - started using pandas on the "alt" version
#V 0.0.4 - using pandas still
#V 0.0.5 - worked on means and groupby
#V 0.0.6 - added import dateutils + mean by group working
#V 0.0.7 - switch version - can switch on/off parts of the code to print different things
#V 0.0.8 - sig digits changed to 2 + added % correct column
#V 0.0.9 - add function to dataframe + data time + average last 3 days
#V 0.0.10 - tried different approach to average last 3 days
#V 0.0.11 - added text to report
#V 0.0.12 - tried a new moving average function -> havent yet but it looks like the rolling average I'm taking is averaging the averages
#V 0.0.13 - tried to add propper menu (https://www.youtube.com/watch?v=f3D-w6XMTN8)
#V 0.1.1 - 
#V 0.1.2 - 
#V 0.1.3 - 
#V 0.1.4 - 
#V 0.1.5 - 
#V 0.1.6 - 
#V 0.1.7 - 
#V 0.1.8 - 
#V 0.1.9 - 

import random #used for randomly selecting crap
import csv #used to read csv files
import itertools
import time #used for time.sleep(x)
import pandas as pd
import numpy as np
import dateutil #some stuff from http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/


pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 300)
pd.set_option('display.width', 6000)

switch_load_data = 0 # switches on/off (1/0) for loading csv file using load_data function
switch_read_csv = 1 #switches on/off (1/0) for loading csv file using the pandas function
switch_MeanCorrect = 0 #switches on/off (1/0)
switch_PrintSomeColumns = 0 #switches on/off (1/0)
switch_IndAvg = 1 #switches on/off (1/0) averaging of individual animals
switch_Aggregators = 0 #switches aggregators at the end of the program

# setting maximum number of significant digits to 2
pd.set_option('display.precision',2)


def function(fx_input):

	return 0

def fx_PerCorr(fx_Corr):

	return 0

def load_data(filename):

	# CSV file contains ID,Box,Date,Cue Duration,Correct,Incorrect,Correct Rejections,
	# False Alarms,Omissions,Prematures,PSV 1,PSV 2,PSV 3,PSV 4,PSV 5,PSV Total,
	# Correct Latency,Incorrect Latency,Reward Latency
	print ('-> Filename: %s' % (filename))
	print ('\nParsing animal data . . .')
	with open (filename, 'r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')

		L_subID = []
		L_subBOX = []
		L_subDATE = []
		L_subCUEDUR = []
		L_subCOR = []
		L_subINC = []
		L_subCORREJ = []
		L_subFALSEAL = []
		L_subOMIT = []
		L_subPREM = []
		L_subPSVTOT = []
		L_subCORRLAT = []
		L_subINCLAT = []
		L_subREWLAT = []		


		#below this takes elements from the CSV file and places it into a specific lists
		for row in readCSV:
			subID = row[0] #here you are just taking from each line and putting it into a variable
			subBOX = row [1]
			subDATE = row [2]
			subCUEDUR = row [3]
			subCOR = row [4]
			subINC = row [5]
			subCORREJ = row [6]
			subFALSEAL = row [7]
			subOMIT = row [8]
			subPREM = row [9]
			subPSVTOT = row [15]
			subCORRLAT = row [16]
			subINCLAT = row [17]
			subREWLAT = row [18]
			#subX = row []
			#subX = row []
			#subX = row []
			#subX = row []
			#subX = row []
			# print (subID)
			# print (subCOR)
			# print (row)
			# intCor = int(subCOR)
			# if (intCor >= 50):
			# 	print ('*****************************')
			print (row [0] , '...loaded')
			time.sleep(0.02)

			#here that variable is actually placed into its appropriate list
			L_subID.append(subID)
			L_subBOX.append(subBOX)
			L_subDATE.append(subDATE)
			L_subCUEDUR.append(subCUEDUR)
			L_subCOR.append(subCOR)
			L_subINC.append(subINC)
			L_subCORREJ.append(subCORREJ)
			L_subFALSEAL.append(subFALSEAL)
			L_subOMIT.append(subOMIT)
			L_subPREM.append(subPREM)
			L_subPSVTOT.append(subPSVTOT)
			L_subCORRLAT.append(subCORRLAT)
			L_subINCLAT.append(subINCLAT)
			L_subREWLAT.append(subREWLAT)



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
print ("     LBS 5Choiz v0.0.13\n")
print ("================================================================================\n\n")


#filename_input = input('Filename: ')
filename_input = "z5C_input.csv"

if switch_load_data == 1:
	#number_of_groups = input('number of groups (2,3,4,5): ')
	#number_of_groups = int(number_of_groups)
	load_data(filename_input)
	time.sleep(0.25)

if switch_read_csv == 1:
	#headers = ["ID","Box","Date","Cuedur","Cor","Inc","CorRej","FalseAlarms","Omits","Prem","PSVtot","CorrLat","IncLat","RewLat"]
	#data = pd.read_csv("z5C_input.csv", names = headers)
	
	# this could be made into a funciton maybe
	data = pd.read_csv("Bz5C_input_simple.csv") #creating dataframe named data with input from CSV file
	
	#del data['PSV 1','PSV 2','PSV 3','PSV 4','PSV 5']
	del data['PSV 1']
	del data['PSV 2']
	del data['PSV 3']
	del data['PSV 4']
	del data['PSV 5']
	del data['Incorrect Latency']

	#convert date
	data['Date'] = pd.to_datetime(data['Date'])

	#add data
	data['PercCorr'] = data['Correct'] / 0.86




#reorders data based on one primary column then a different column
data.sort_values(by=['ID','Date'], ascending=[True,False], inplace=True) 

data.head()
#print (data.describe(include=[np.number])) #shows some stats of any numerical column
print (data.head(10))
#print (data.tail(12))


if switch_MeanCorrect == 1:
	# https://stackoverflow.com/questions/30328646/python-pandas-group-by-in-group-by-and-average
	# supposed to take the mean of values based on Correct
	dataMeanCorrect = data.groupby(['Correct']).mean() 
	#dataMeanCorrect = dataMeanCorrect[['Correct']]
	print ('\n\nMean Correct')
	#print (dataMeanCorrect)

	#Total Average
	dataTotAvgCorr = data['Correct'].mean()
	print ('Total AVG = ')
	print (dataTotAvgCorr)

if switch_PrintSomeColumns == 1:
	print ("\n\n--> dataIDs :")
	dataIDs = data.loc[:,['ID','Correct', 'Correct Rejections','Correct Latency']] #https://stackoverflow.com/questions/10665889/how-to-take-column-slices-of-dataframe-in-pandas
	print (dataIDs)
	

print ('HERE!!!')

print ('neimuuuuurrrrr')

if switch_IndAvg == 1:

	# to exclude box 5
	#dataIndAvgCorr = data[data['Box'] != 5].groupby('Date')['Correct'].mean()
	# average based on animal ID
	dataIndAvgCorr = data.groupby('ID')['Correct'].mean()
	print ("\n\n--> dataIndAvgCorr :")
	print (dataIndAvgCorr)
	#--> maybe I should add a column with the last 3 days of correct resps? visually easy to see comparison
	#https://stackoverflow.com/questions/36969174/pandas-average-value-for-the-past-n-days
	dataOrganizeByDate = data.groupby('ID').apply(lambda x: x.set_index("Date").resample('1D').first())
	#print (dataOrganizeByDate)
	dataLast3Days = dataOrganizeByDate.groupby(level=0)['Correct'].apply(lambda x: x.shift().rolling(min_periods=1,window=3).mean()).reset_index(name='AVG3Days')
	print ("\n\n--> dataLast3Days :")
	print (dataLast3Days)
	#--> maybe need to take AVG3Days and just take the last day is what i actually want

	data['RollingAvg3'] = data.Correct.rolling(min_periods=1,window=3).mean()
#	data['RollingAvg3_num'] = data['RollingAvg3'].apply(pd.to_numeric) #https://stackoverflow.com/questions/15891038/pandas-change-data-type-of-columns
#	data['Improving'] = data.where(data['RollingAvg3_num']>=65, 'yes', 'no')
	print ('\n\n--> data Rolling Avg')
	dataRA3 = data.loc[:,['ID','Correct', 'RollingAvg3', 'PercCorr', 'Correct Rejections','Correct Latency','Improving']]
	dataRA3Agg = dataRA3.groupby(['ID']).agg({'Correct': 'mean', 'PercCorr': 'mean', 'RollingAvg3': 'mean', 'Correct Latency': 'mean'})
	print (dataRA3Agg)

if switch_Aggregators == 1:
	#trying aggregators as per what you see on this url
	# http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
	#dataIndAggregator = data.groupby(['Date','ID']).agg({'Correct':[min, max, sum]})
	dataIndAggregator = data.groupby(['ID']).agg({'Correct':[min, max, sum], 'Incorrect': 'mean', 'Correct Latency': 'mean', 'Omissions': 'mean'})
	print ("\n\n--> dataIndAggregator :")
	print (dataIndAggregator)


print ('\nshape of data / size of dataframe = ' ,  data.shape)
