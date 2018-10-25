import os,sys
import csv
from collections import defaultdict
import logging



def readInput(input_path):

	'''
	This funtions read the input file and return datastructure D.
	D = {'occupations': {name(key): count}, 'states': {name(key): count}, 'total': totalcertifiedcount}
	'''
	
	# D is Datastrcuture for our problem
	D  = {'occupations': defaultdict(), 'states': defaultdict(), 'total':0}
	
	# dictionary for header and their index value
	header_dict = {}


	# input_file = 'H1B_FY_2014.csv'
	input_file = input_path
	
	try:
		with open(input_file, mode='r',encoding="utf8") as disclosure_file:
			csv_reader = csv.reader(disclosure_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			HEADER = next(csv_reader,None)    



			for i,column in enumerate(HEADER):
		
				if (column=='LCA_CASE_NUMBER' or column=='CASE_NUMBER'):
					header_dict['CASE_NUMBER'] = i
					
				if (column=='STATUS' or column=='CASE_STATUS'):
					header_dict['CASE_STATUS'] = i
					
				if (column=='LCA_CASE_SOC_CODE' or column=='SOC_CODE'):
					header_dict['SOC_CODE'] = i
					
				if (column=='LCA_CASE_SOC_NAME' or column=='SOC_NAME'):
					header_dict['SOC_NAME'] = i
					
				if (column=='LCA_CASE_WORKLOC2_STATE' or column=='WORKSITE_STATE'):
					header_dict['STATE'] = i
	
		
			for row in csv_reader:
				record = []
				
				case_status_idx = header_dict['CASE_STATUS']
				occ_name_idx = header_dict['SOC_NAME']
				state_idx = header_dict['STATE']
				
				if row[case_status_idx] == 'CERTIFIED':
					D['total'] +=1

					
					if row[occ_name_idx] in D['occupations']:
						D['occupations'][row[occ_name_idx]] += 1 
					else:
						D['occupations'][row[occ_name_idx]] = 1 
					
					if row[state_idx] in D['states']:
						D['states'][row[state_idx]] += 1 
					else:
						D['states'][row[state_idx]] = 1 
				
		disclosure_file.close()

			   
	except IOError :
		logging.error("Could not read file %s from input path", disclosure_file)

	return D


def writeTopTen(D,out1,out2):
	'''
	Args :
		D : Data Structure
		out1 : path for occupations.txt
		out2 : path for states.txt
	Returns:		
		Write two output files out1 and out2.
	'''


	topOccupuations = sorted(D['occupations'].items(), key=lambda x:(-x[1],x[0]), reverse=False)[:10]

	outtopOccupuations = ''

	for x  in topOccupuations:
		outtopOccupuations += x[0] +';' + str(x[1]) + ';' + str(round(x[1]*100/float(D['total']),1))+ '%' +"\n"


	headerOccupation ="TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE" 

	with open(out1,'a') as f:
		f.write(headerOccupation + "\n")
		f.write(outtopOccupuations)
	f.close()


	headerStates = 	"TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"

	topStates = sorted(D['states'].items(), key=lambda x:(-x[1],x[0]), reverse=False)[:10]

	outtopStates = ''	

	for x  in topStates:
		outtopStates += x[0] +';' + str(x[1]) + ';' + str(round(x[1]*100/float(D['total']),1))+ '%' +"\n"


	with open(out2,'a') as f:
		f.write(headerStates + "\n")
		f.write(outtopStates)
	f.close()




def main(argv):
   inputfile = sys.argv[1]
   outputfile1 = sys.argv[2]
   outputfile2 = sys.argv[3]

   D = readInput(inputfile)

   writeTopTen(D,outputfile1,outputfile2)



if __name__ == "__main__":
   main(sys.argv[1:])