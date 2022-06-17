# project-awwards

>[David Njagi](https://github.com/poldiee)  
  
# Description  
project which allows users to post their projects for other users to rate according to design, usability and content 
##  Live Link  
 Click [View Site]()  to visit the site

## Screenshots 
###### Home page

<img src="">

 ###### user profile
 <img src=""> 



## User Story  

* user can view posted projects and their details.  
* user can post a project to be rated/reviewed. 
* user can rate/ review other users' projects.  
* search projects.  
* projects overall score.
* user can view their profile page.  



## Setup and Installation  
To get the project .......  

##### Cloning the repository:  
 ```bash 
 https://github.com/poldiee/proj-award.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd proj-award pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations db-name
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  


## Technology used  

* [Python3.8](https://www.python.org/)  
* [Django 4.0.5](https://docs.djangoproject.com/en)  
* [Heroku](https://heroku.com)  


## Known Bugs  
* 

## Contact Information   
If you have any question or contributions, please email me at [nessidave@gmail.com]  

## License 

* MIT License
* Copyright (c) 2022 **poldiee**