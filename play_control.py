#entorno\scripts\activate - deactivate

from googleapiclient.discovery import build
import os
import time

#vars
List_s=[]
l_report=[]
match=False
miss=[] 



def extract():
	next_p=None

	key='AIzaSyD6YYI-67gvTInOPoFvqJdxXN3D2HSwBWo'
	#key = os.environ['KEY_Y'] # get key of enviroment variable created from CMD

	yt=build('youtube','v3',developerKey=key)

	while 1:
		request=yt.playlistItems().list(part='snippet', 
			pageToken=next_p,
			maxResults=50, 
			playlistId='PLcigMaOVVhLMpU-GGZUGQ8E3lEKs2hIhb')

		res=request.execute()
		#print(res,'\n\n\n ------------------------------------->\n')


		for item in res['items']:
			element=item['snippet']['title'] # it means that "snippet" is just a key from dictionary "item" that contain inside a dictionary too
			#print(element)#<<
			List_s.append(element)

		#print('Lista:',res,'\n\n\n')#<<		
		next_p=res.get('nextPageToken') # This "get" is only a dictionary function, Not have any relationship with api nor request


		if not next_p:
			break



def save():
	with open('save.txt', 'w', encoding='utf-16') as w :
		open_temp=open('temp.txt','r', encoding='utf-16')
		listTemp=open_temp.readlines()
		for l in listTemp:
			w.write(l+'\n')
		w.close()

def temp():
	with open('temp.txt', 'w', encoding='utf-16') as w :
		for l in List_s:
			w.write(l+'\n')
		w.close()


def process():
	c=0
	c2=0
	global match # always when you need update a global variabe inside of a function
	#Comparisson
	with open('save.txt', 'r', encoding='utf-16') as save:
		Temp=open('temp.txt', 'r', encoding='utf-16') # Nota: is not problem to incomplete readlines
		temp=Temp.readlines()

		for item_s in save.readlines(): # iterate list gotten from text aready saved in the pc
			#time.sleep(0.5)
			#print('save--------------------->>>', item_s)#<< The save-loop was not broken 
			for item_t in temp: #iterate list gotten from extract fata from the website, Nota: in this inner loop cannot set "readlines()" because would restart excution of the "readlines()" function and generates problems 
				#print('temp--------------------->>>', item_t)
				#time.sleep(0.5)#<<
				#print('\n\n',item_s.strip(),'|------|',item_t.strip())#<< pending test the matchs !!!!
				#Do comparison
				if item_s.strip() == item_t.strip():
					#print('ENTROOO')#<< Nota: entry once and break completly te loop
					#time.sleep(3)#<<
					#print('\n\n',item_s.strip(),'|------|',item_t.strip())#<< pending test the matchs !!!!
					match = True # if found the theme 
					break
			#Assess the outcome of the comparison of the entire "list_s"(extract form web) for each "item_s"(item from list save in pc)	 	
			if match == True:
				#print('match True:',c)#<<
				#c+=1#<<
				match=False
			else:
				if item_s.strip()!='':
					#print('match false:',c2)#<<
					#c2+=1#<<
					print('inside append..') 
					time.sleep(0.3)
					miss.append(item_s.strip())
				pass

		Temp.close()		
		save.close()


def lost():
	if miss == []:
		print('\n<There is nothing to saving...>\n')  
	else:	
		nameLost=input('Name of file to Lost>> ')
		with open('bajas\\'+nameLost+'.txt', 'w', encoding='utf-16') as wt :
			for i in miss:
				wt.write(i+'\n')
			wt.close() 
		print('end lost --')


input('\n Press enter..\n')
#1
print('EXTRACT DATA:')
extract()

#2
print('TEMP:')
temp()


#3
print('PROCESO:')
process()

print( '\n ---> \n\n\n')
print('LOST: \n\n', miss)

#4


while True:
	print('''Press: 
	[1]:Save Actual List\n 
	[2]:Save Lost\n 
	[3]:Save both\n 
	[Q]:Quit''')

	opt=input('>> ')

	if opt =='1':
		print('SAVING DATA:')
		save()  
	elif opt=='2':
		print('SAVING LOST ')
		lost()
	elif opt== '3':
		print('SAVING BOTH ')
		save()
		lost()
	elif opt== 'q' or 'Q':
		break
	else: print('Fail option, Try again..')



# NOTA:	Test if work the new config with temp file and readlines for of temp	