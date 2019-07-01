# STONE FILES DOWNLOAD
This repo contains some sample code to deploy a simple (but complete) Python application to make a Request and simulating files download from a web service from Stone API. The deployed app counts with the following features:

* Running Python 3.6 🐍
* Access to STONE API 
* Only GET methods to the endpoint: 'https://conciliation.stone.com.br/conciliation-file/v2.2/{YYYYMMDD}?affiliationCode={code?}' and static os directorys

## Steps to access the endpoint

##### 1. Download files or clone the repository 

##### 2. Install the requirements and set up the static directory in list_stones_code() method, because we will search the files to the directory configured

##### 3. Set another file stone-codes.txt with this information in order STONE CODE,NAME FILE(YOU CHOOSE),D-?(THE DAY YOU WANT TO DOWNLOAD AUTOMATICALY LIKE ALWAYS THE LAST DAY WOULD BE 1)

##### 4. Set Params to get token and authorization from API

```bash
	params = {
		'Authorization': 'xxxx',
		'X-Authorization-Raw-Data': 'xxxx',
		'X-Authorization-Encrypted-Data': 'xxxx',
		'Accept': 'application/xml'
	}
```

##### 5. You can use the methods bellow to Test the Application

##### Get files automaticaly just by information configured in the stone-codes.txt
```bash
	python run.py n "file directory" 
	example: python run.py n C:/Users/
```

##### Get a range of dates from all stones codes configured in the stone-codes.txt
```bash
	python run.py rm from: yyyymmdd to: yyyymmdd  "files directory"
	example: python run.py rm 20190622 20190623 C:/Users/
```

##### Get a range of dates from specific stone code configured in the stone-codes.txt
```bash
	python run.py r from: yyyymmdd to: yyyymmdd code "files directory"	
	python run.py r 20190622 20190623 202205694 C:/Users/
```


# Create the virtualenv
$ mkvirtualenv stone-files-download
# Install dependencies
$ pip install -r requirements.txt
# Run the app
$ python run.py
```
