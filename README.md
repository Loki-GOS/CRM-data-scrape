"# CRM-data-scrape" 
Current Features:
- allows choice of "business" or "consumer" base
- allows choice of where in the reference list you want to start/end
- opens page with selected reference
- pulls as much data as possible and stores to arrays
- if a piece of data isnt found index for that data replaced with "null"
- writes data to appropriate csv file erasing the file beforehand to prevent dupes
- Consumer scrape appears to work

Most Recent update:
- reading csv data to pull rows and use as references
- Selectable Login
- Lots of Validation
- Selectable time waits
- Time Validation and auto pause

Neccessary Features to add:


Potential Features to add:



How to use:

ON FIRST SETUP:  
  - install latest version of python from https://www.python.org/downloads/
  - run the installer
  - press the windows key and "R" simultaniously
  - type cmd
  - type "py --version" (without speech marks) to check if you have Python installed
![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/44eb8e40-4bd3-4326-9607-0f9e5190bfd7)
  - type "py -m pip --version" (without speech marks) to ensure you have Pip installed (if it is not uninstall and reinstall python
![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/a91848c2-cf01-4206-9e14-f22a88b18235)
  - type "py -m pip install requests" (without speech marks)
  - type "py -m pip install BeautifulSoup4" (without speech marks)

  - open Visual Studio Code and select "Clone Git Repository"
![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/92d0b0ba-9465-4173-8fcc-c951c6d9cd45)
  - type in searchbar "https://github.com/Loki-GOS/CRM-data-scrape.git" (without speech marks)
  - this will prompt to save somewhere. save to a memorable location
  - ensure all files from the repository are present (DataScraper.py,README.md,BusinessReferences.csv,ConsumerReferences.csv) DO NOT CREATE SUBFOLDERS
![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/2366e7ff-f021-4df7-a9c8-a38b71f1efbc)

GENERAL USE:
- Open Visual Studio Code
- Select Open Folder
![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/e59d0279-8faf-43fe-80fc-e779e9ec5c14)
- Locate and select the folder labelled "CRM-data-scrape" which you saved earlier when cloning GIT repository
![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/c733b816-b582-4e15-9633-4cec0aa065bf)
- select "yes" to trust authors

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/8bc9ccd2-1a71-4bc7-8f13-171e831d51d2)

- select extensions tab (do next steps if first time running program)

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/5a76ca22-14c2-410d-9d56-9132bbaea75d)

- search py
- locate python debugger, python and pylance
- select install on all

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/2c791dac-6fc7-44a0-8fec-f757bfc9c387)

- (carry on from here once complete previous steps or not first time)
- select explorer tab

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/dde16381-44d4-4bc6-b00b-5ef50de3af75)

- select DataScraper.py

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/e0f47a80-8a3a-4c22-82af-d1d2a164bc48)

- locate and fill username and password fields in format shown below

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/80b608e9-5f50-49b7-994e-e7913389d53f)

- ensure none of the csv files in the folder are open anywhere while running program
- press f5 (dont use alt, ensure fn lock is off)
- if this fails, select run then start debugging

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/403812cf-6664-42ee-8b15-a4fba51ee062)

- if prompted, select to use python debugger
- if prompted select debug currently active python file

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/c28c7395-85e7-40bc-8e36-c744ac59f6d4)

- answer prompted questions to start running the scrape
- if outside of hours program will force pause
- press f5 or continue button

![image](https://github.com/Loki-GOS/CRM-data-scrape/assets/167244472/d053bad7-c64e-4975-90b6-7fccd70dbbac)

- program will force pause if still outside hours
- program will output when the csv with the scraped data has been written
- outputted csv will be located inside same folder as the program








