"# CRM-data-scrape" 
Current Features:
-Randomly selects a login from a list and opens a session to prevent repeat logins (will make user selectable only for testing to lower chance of bieng noticed)
-allows choice of "business" or "consumer" base
-Randomly selects an inputted number of references (within range of business or consumer base references) (for testing to make sure it will work for every record)
-opens page with selected reference
-pulls as much data as possible and stores to arrays
-if a piece of data isnt found index for that data replaced with "null"
-writes data to appropriate csv file erasing the file beforehand to prevent dupes

Neccessary Features to add:
-improve consumer page scrape functionality (different data to be scraped)
    -Account holder & consumer fields
-reading csv data to pull rows and use as references
-selectable login

Potential Features to add:
- fix special requirements doubling



