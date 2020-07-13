# Vegan Minus Gluten
## Code Institute Data Centric Development Milestone Project

![site logo](https://res.cloudinary.com/www-madine-se/image/upload/v1592952530/vegansite/Screenshot_2020-06-24_at_00.47.43_upejzd.png)

[Deployed site](https://git.heroku.com/vegan-gluten.git)

## Table of Contents

- [**About**](#About)
- [**Demo**](#Demo)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Research](#Research)
  - [Wireframes](#Wireframes)
  - [Design](#Design)
  - [Color Scheme](#Color-Scheme)
- [**Features**](#Features)
    - [Functionality](#Functionality)
    - [Existing features](#Existing-features)
    - [Future features](#Future-features)
- [**Information Architecture**](#Information-Architecture)
- [**Technologies used**](#Technologies-used)
- [**Testing**](#Testing)
    - [Manual testing](#Testing)
    - [Errors](#Errors)
- [**Deployment**](#Deployment)
- [**Credits**](#Deployment)
    - [Code](#Code)
    - [Images](#Images)
- [**Acknowledgements**](#Acknowledgements)
- [**Disclaimer**](#Disclaimer)

## About
## Demo
## UX
### User Stories
### Research
### Wireframes
### Design
### Color Scheme

I kept the color pallette very simple and clean because the content of the page are inevitably very colorful.

![Color Palette](https://res.cloudinary.com/www-madine-se/image/upload/v1594581862/vegansite/palette-2_bhhqtr.png)

## Features
### Functionality
### Existing features
### Future features
### Information Architecture
MongoDB Atlas is used for storing data for this web site.

Recipes Collection

```
"recipe":{
    "_id": "ObjectId()"
    "title": "<string>",
    "category_name": "<string>",
    "description": "<string>",
    "image_url": "<string>",
    "prep": "<string>",
    "cooks": "<string>",
    "difficulty": "<string>",
    "instructions": "<string>",
    "tips": "<string>",
    "date_added": "<string>",
}
```
Categories Collection
```
"categories":{
    "_id": "ObjectId()"
    "category_name": "<string>",
}
```
Users Collection
```
"users":{
    "_id": "ObjectId()"
    "user_name": "<string>",
}
```
Subscribers Collection
```
"subscribers":{
    "_id": "ObjectId()"
    "sub_email": "<string>",
}
```
For the needs of this website I did not find the need to use other data types in MongoDB.

## Technologies used

Below are a list of the programming languages, technologies, frameworks and resources used for this website.

* HTML5
* CSS3
* jQuery
* Python 3.8.2
    * Flask
* MongoDB
* Bootstrap
* Visual Studio Code development environment
    * Live Server Extension
    * Color Picker Extension
    * Markdown Preview Extension
* Git & GitHub.com
* Heroku.com pages
* Markdown
* FontAwesome.com
* Google Fonts
* Adobe Fonts
* Google Chrome Developer tools
* Firefox Inspector
* Safari Web Inspector
* Adobe Suite CC
* Cloudinary.com
* Favicon.io
* EZGIF

## Testing
Devices and platforms used for testing:

* Iphone X 
    - Safari
    - Chrome
    - Brave
* Ipad Pro 12.9" 2018
    - Safari 
    - Chrome
* MacBook Pro 13" MacOS Catalina
    - Safari 
    - Chrome
    - Firefox
* MacBook Pro 13" Windows 10
    - Chrome
    - Firefox
    - Microsoft Edge
* OnePlus 5T
    - Firefox
    - Chrome
* Windows 7
    - Chrome
    - Firefox
* Huawei P20 Pro
    - Chrome

Validators and linters

* W3C HTML Validator
* W3C CSS Validator
* CSS Lint
* JSHint
* PEP8

### Manual testing
### Errors
## Deployment

### Local Development

This project can be ran locally by following the following steps:

Visit this [repository link](https://github.com/sabinemm/recipe-site-ms3.git) and click on the Clone or Download button to copy the link provided.

![clone](https://res.cloudinary.com/www-madine-se/image/upload/v1594582454/vegansite/Screenshot_2020-07-12_at_21.33.47_k4rvyg.png)

In your IDE, open a Terminal window and change to the directory where you want to clone this project and type:

Git clone [repository link](https://github.com/sabinemm/recipe-site-ms3.git)

After pressing Enter the project will be created and cloned locally.

(Alternatively you can download the zipped file, decompress it and use your IDE of choice to access it.)

Create a free account on MongoDb and reproduce the 3 collections as described [here](#Information-Architecture).

Make sure to upgrade PIP. 
```
pip install -U pip 
```



Install all dependencies
```
pip3 install -r requirements.txt
```
Create `.env` file with following data
```
MONGO_URI=mongodb+srv://..."
```
add your .env file to .gitignore

Activate virtual environment 
```
source env/bin/activate
```

You will then be able to run the app locally by typing python app.py or   flask run. 

### Heroku

Heroku was chosen as the deployment platform for this project. The steps to deploy the local app to Heroku were as follow:

In Heroku, created an app. The app must have a unique name.

Linked that app to the GitHub repository by going to the "Deploy" tab in the main app menu.


In the Settings tab, added the corresponding Config Variables as present in my local development:

```
MONGO_URI mongodb+srv://...
IP 0.0.0.0
PORT 5000
```

I also created a "Procfile" by typing 
```
echo web: python run.py > Procfile
```


After that process, the app was live and running remotely in Heroku's servers.


## Credits
### Code
[Datetime](https://www.programiz.com/python-programming/datetime/current-datetime)

[Login](https://startbootstrap.com/snippets/login/)

[Flash](https://pythonprogramming.net/flash-flask-tutorial/)

### Images
[Vegetable fritatta](https://www.crowdedkitchen.com/spring-vegetable-frittata-vegan/)

[Thyme](https://www.pexels.com/photo/close-up-photo-of-thyme-leaves-4113901/)

[Almonds](https://www.pexels.com/photo/white-table-with-tasty-scattered-almonds-4033328/)

[Book](https://unsplash.com/photos/CXYPfveiuis)

[Oranges](https://unsplash.com/photos/S3_D7Q9vz0Y)

## Acknowledgements
A thanks to my mentor [Maranatha Ilesanmi](https://github.com/mbilesanmi), Code Institute Tutor support, Slack

## Disclaimer
I had accidentally committed mongodb password but changed it and hid it later. All secure.
This project is for educational purposes only.


[Back to top ↑](#Vegan-Minus-Gluten)