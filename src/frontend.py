# This is a simple test script which does the absolute bare minimum to pass all the test cases

import os  
import sys                                     

print('Welcome!')

validAccountFile = sys.argv[1]
transactionSummaryFile = sys.argv[2]

userInput = input('> ')
if(userInput == 'login'):
	userInput = input('Enter mode (machine/agent): ')
	
	if(userInput == 'machine'):
		
		if(not(os.path.exists(validAccountFile) and os.path.isfile(validAccountFile))):
			print('Error: Valid accounts list file not found')
			exit(1)
		else:
			print('Success: Logged into ATM mode')
			
			userInput = input('> ')
			
			if(userInput == 'logout'):
			
				with open(transactionSummaryFile, 'w') as wf:
					wf.write('EOS')
					
				print('Success: Logged out')