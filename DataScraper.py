import requests
import csv
import re
from bs4 import BeautifulSoup 
import random
import time
from datetime import datetime 
  
#removes all emojis from the parameter string
def remove_emoji(inputString):
	emoji_pattern = re.compile("["
		u"\U0001F600-\U0001F64F" # emoticons
		u"\U0001F300-\U0001F5FF" # symbols & pictographs
		u"\U0001F680-\U0001F6FF" # transport & map symbols
		u"\U0001F1E0-\U0001F1FF" # flags (iOS)
		u"\U00002702-\U000027B0"
		u"\U000024C2-\U0001F251"
		u"\U0001f926-\U0001f937"
		u'\U00010000-\U0010ffff'
		u"\u200d"
		u"\u2640-\u2642"
		u"\u2600-\u2B55"
		u"\u23cf"
		u"\u23e9"
		u"\u231a"
		u"\u3030"
		u"\ufe0f"
		u"\u2069"
		u"\u2066"
		u"\u200c"
		u"\u2068"
		u"\u2067"
	"]+", flags=re.UNICODE)
	return cleanse_unicode(emoji_pattern.sub(r'', inputString))


#match left and right single quotes
single_quote_expr = re.compile(r'[\u2018\u2019]', re.U)
#match all non-basic latin unicode
unicode_chars_expr = re.compile(r'[\u0080-\uffff]', re.U)
def cleanse_unicode(s):
    if not s:
        return ""
    
    temp = single_quote_expr.sub("'", s, re.U)
    temp = unicode_chars_expr.sub("", temp, re.U)
    return temp

#URL used to login
login_url = "https://crm.salescreate.com/login"

#Bool to represent whether a choice is valid
ValidType=False
#init blank list of references
ReferenceList = []

while(ValidType==False):
	#ask for choice, force lowercase and 1 word
	TypeChoice=input("Business or Consumer:").lower().split()[0]
	print("")

	if (TypeChoice=="business"):
		#reset to true to break loop
		ValidType=True
		#set link to use as business
		LinkType="/business/"
		
		#opens relevant csv
		with open("BusinessReferences.csv", 'r') as file:
			#makes csv readable
			csvreader = csv.reader(file)
			#adds all values to list
			for row in csvreader:
				ReferenceList.append(row)

	#ditto but for consumer
	elif (TypeChoice=="consumer"):
		ValidType=True
		LinkType="/consumer/"

		with open("ConsumerReferences.csv", 'r') as file:
			csvreader = csv.reader(file)

			for row in csvreader:
				ReferenceList.append(row)
		
	else: 
		#if anything other than whats needed restart loop with prompt to inform of error
		print("Invalid Input")

	#bool to represent whether the choices are in range
MinInRange=False
MaxInRange=False

while (MinInRange==False):
	StartRef=int(input("Which line of the csv would you like to start on:"))

	if(StartRef>len(ReferenceList) or StartRef==0):
		print("Out Of Range")

	else:
		MinInRange=True

while (MaxInRange==False):
	EndRef=int(input("Which line of the csv would you like to end on:"))

	if(EndRef>len(ReferenceList)or EndRef<StartRef):
		print("Out Of Range")

	else:
		MaxInRange=True
print ("")


#range of usernames/passwords (indexes for linked users/pass need to be identicle, in speech marks and seperated by commas)
usernames = []
passwords = []

if (len(usernames)!=len(passwords)):
	print("Error:Uneven amount of Usernames compared to Passwords")
	quit()

elif (len(usernames)==0):
	print("Error:Username and password fields empty")
	quit()


Found=False
while (Found==False):
	Choice=(input("Which username do you want to use:")).lower().split()[0]
	for p in range(0,len(usernames)):

		if (usernames[p]==Choice):
			LoginIndex=p
			Found=True

	if (Found==False):
		print("Username not found")
print("")

Short=float(input("Shortest time between requests(seconds):"))
Short=Short+0.01
TimeValid=False
while (TimeValid==False):	
	Long=float(input("Longest time between requests (seconds):"))
	Long=Long+0.01
	if (Long<Short):
		print("must be larger than shortest time")
	else:
		TimeValid=True
print("")

username=usernames[LoginIndex]
password=passwords[LoginIndex]
#informs the user of which login used to identify incase of auth errors
print("Username:",username)

#instantiating arrays to be transcribed to csv
Reference=[]
Connected=[]
Business_Name=[]
Mpn=[]
Account_Holder=[]
Email=[]
Dob=[]
Landline=[]
Billing_Address=[]
Delivery_Address=[]
Box_Value=[]
Agent=[]
Special_Requirements=[]
Notes=[]
ConsumerHeader=["Reference","Connected","Account Holder","MPN","Email","DOB","Landline","Billing Address","Delivery Address","Box Value","Agent","Special Requirements","Notes"]
BusinessHeader=["Reference","Connected","Business Name","MPN","Account Holder","Email","DOB","Landline","Billing Address","Delivery Address","Box Value","Agent","Special Requirements","Notes"]
data=[]

#creates single session to require only 1 login
with requests.session() as s:
	req = s.get(login_url).text
	#loads login page HTML and Parses
	html = BeautifulSoup(req,"html.parser") 
	#finds current Authentication token
	token = html.find("input", {"name": "_token"}). attrs["value"] 
	
    #generates payload to be sent to page
	payload = { 
		"_token": token, 
		"username": username, 
		"password": password, 
    }
	#posts authentication to page
	res = s.post(login_url, data=payload)

	#tests if authentication was successful
	if (res.url=="https://crm.salescreate.com"):
		print("Auth Successful")

	else:
		print("Auth error")
		quit()
	count=0

	for i in range(StartRef-1,EndRef):
		InHours=False

		while (InHours==False):
			now = datetime.now()
			current_time = int(now.strftime("%H"))
			if (current_time>=18):
				print("It is past 6pm")
				breakpoint()

			elif (current_time<9):
				print("It is before 9am")
				breakpoint()
			else:
				InHours=True

		WaitTime=random.uniform(Short,Long)


		time.sleep(float(WaitTime))

		salepageURL="https://crm.salescreate.com"+LinkType+"upgrades/"+str(ReferenceList[i]) [2:-2]
		r=s.get(salepageURL)
		soup=BeautifulSoup(r.content,"html.parser")

		SpecFound=False
    
		RefText=soup.find(class_="page-header")
		if (RefText!=None):
			Reference.append(RefText.text.strip().split()[2])
			SpecFound=False
	
		UpDate=soup.find(class_="alert alert-success")
		if(UpDate==None):
			UpDate=soup.find(class_="alert alert-info")
			if (UpDate==None):
				UpDate=soup.find(class_="alert alert-danger")
				if (UpDate==None):
					UpDate=soup.find(class_="alert alert-warning")
					if (UpDate!=None):
						Connected.append((UpDate.text.strip().split()[4])[:-1])
				else:
					Connected.append((UpDate.text.strip().split()[4])[:-1])
			else:
				Connected.append(RefText.text.strip().split()[3])
		else:
			if (((UpDate.text.strip().split()[4]))=="exported"):
				Connected.append(RefText.text.strip().split()[3])
			else:
				Connected.append((UpDate.text.strip().split()[4])[:-1])

		BusName=soup.find(class_="col-lg-6")
		if (BusName!=None):
			Business_Name.append(" ".join(BusName.text.strip().split()))

		MobileNum=soup.find(class_="h2 text-right")
		if (MobileNum!=None):
			Mpn.append(MobileNum.text)
	
		AccInf=soup.find_all(class_="col-lg-6")
		if (AccInf!=None):

			HolderFound=False
			EmailFound=False
			DOBFound=False
			LLFound=False
			BoxFound=False
			AgentFound=False

			for Field in AccInf:
				Panel=Field.find_all(class_="panel panel-default")

				if (Panel!=None):
					GroupItem=Field.find_all(class_="col-sm-6")
					
					if (GroupItem!=None):

						for TextFields in Panel:

							if ("Delivery Address" in TextFields.text):
								Delivery_Address.append(" ".join(TextFields.text.strip().split())[17:])

							elif ("Billing Address" in TextFields.text):
								Billing_Address.append(" ".join(TextFields.text.strip().split())[16:])

						for data in GroupItem:

							if(len(data.text.strip().split())==0):
								HolderFound=False
								EmailFound=False
								DOBFound=False
								LLFound=False
								BoxFound=False
								AgentFound=False

							if(HolderFound):
								Account_Holder.append(" ".join(data.text.strip().split()))
								HolderFound=False

							elif(EmailFound):
								Email.append(data.text.strip().split()[0])
								EmailFound=False
				
							elif(DOBFound):
								if(len(data.text.strip().split())!=0):
									Dob.append(data.text.strip().split()[0])
									DOBFound=False
				
							elif(LLFound):
								Landline.append(data.text.strip())
								LLFound=False
				
							elif(BoxFound):
								Box_Value.append(data.text.strip().split()[0])
								BoxFound=False
				
							elif(AgentFound):
								AgentText=(data.text.strip().split())
								Agent.append(AgentText[0]+" "+AgentText[1])
								AgentFound=False
				
							elif (data.text.strip()=="Account Holder"):
								HolderFound=True
				
							elif (data.text.strip()=="Email Address"):
								EmailFound=True
				
							elif (data.text.strip()=="Date of Birth"):
								DOBFound=True
				
							elif (data.text.strip()=="Landline Number"):
								LLFound=True
				
							elif (data.text.strip()=="Box Value"):
								BoxFound=True
				
							elif (data.text.strip()=="Agent Name"):
								AgentFound=True

		LrgTextboxes=soup.find_all(class_="col-lg-12")

		if (LrgTextboxes!=None):

			for Contents in LrgTextboxes:
				Details=Contents.find_all(class_="panel panel-default")

				for TextDetails in Details:

					if (("Special Requirements" in TextDetails.text.strip()) and (not "See Special Requirements"in TextDetails.text.strip())and SpecFound==False):
						SpecReqText=(TextDetails.text.strip().split("Special Requirements"))[1]
						Special_Requirements.append(remove_emoji(" ".join(SpecReqText.split())))
						SpecFound=True

					if ("Notes"in TextDetails.text.strip()):
						OverallNoteText=(TextDetails.text.strip().split("Notes"))[1]
						Notes.append(remove_emoji(" ".join((OverallNoteText.split("Add a Note")[0]).split())))

		if((len(Reference)-1)!=count):
			Reference.append("Null")

		if((len(Connected)-1)!=count):
			Connected.append("Null")

		if((len(Business_Name)-1)!=count):
			Business_Name.append("Null")

		if((len(Mpn)-1)!=count):
			Mpn.append("Null")

		if((len(Account_Holder)-1)!=count):
			Account_Holder.append("Null")

		if((len(Email)-1)!=count):
			Email.append("Null")

		if((len(Dob)-1)!=count):
			Dob.append("Null")

		if((len(Landline)-1)!=count):
			Landline.append("Null")

		if((len(Billing_Address)-1)!=count):
			Billing_Address.append("Null")

		if((len(Delivery_Address)-1)!=count):
			Delivery_Address.append("Null")

		if((len(Box_Value)-1)!=count):
			Box_Value.append("Null")

		if((len(Agent)-1)!=count):
			Agent.append("Null")

		if((len(Special_Requirements)-1)!=count):
			Special_Requirements.append("Null")

		if((len(Notes)-1)!=count):
			Notes.append("Null")

		print(count+1)
		print("ref",(str(ReferenceList[i]) [2:-2]))
		count=count+1

if (TypeChoice=="business"):
	with open('CRMBusinessData.csv','w+', newline='')as BusinessCsvfile:
		BusinessWriter=csv.writer(BusinessCsvfile)
		BusinessWriter.writerow(BusinessHeader)
		for x in range(0,count):
			data=[Reference[x],Connected[x],Business_Name[x],Mpn[x],Account_Holder[x],Email[x],Dob[x],Landline[x],Billing_Address[x],Delivery_Address[x],Box_Value[x],Agent[x],Special_Requirements[x],Notes[x]]
			BusinessWriter.writerow(data)
		print("Business CSV written")

if (TypeChoice=="consumer"):
	with open ("CRMConsumerData.csv","w+",newline="")as ConsumerCsvfile:
		ConsumerWriter=csv.writer(ConsumerCsvfile)
		print("Writing CSV")
		ConsumerWriter.writerow(ConsumerHeader)
		for z in range(0,count):
			data=[Reference[z],Connected[z],Business_Name[z],Mpn[z],Email[z],Dob[z],Landline[z],Billing_Address[z],Delivery_Address[z],Box_Value[z],Agent[z],Special_Requirements[z],Notes[z]]
			ConsumerWriter.writerow(data)
		print("Consumer CSV written")

	
	
				
	
			
	
	
	
			
			
			
	
	
	

