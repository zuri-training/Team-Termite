# PriceAm
## Table of Contents
   - <a href="https://github.com/zuri-training/Team-Termite##Introduction">Introduction</a>
   - <a href="https://github.com/zuri-training/Team-Termite##Features">Features</a>
   - <a href="https://github.com/zuri-training/Team-Termite##Technologies Used">Technologies Used</a>
   - <a href="https://github.com/zuri-training/Team-Termite##Environment Setup/Installation Guide">Environment Setup/Installation Guide</a>
   - <a href="https://github.com/zuri-training/Team-Termite##To Contribute">To Contribute</a>
   - <a href="https://github.com/zuri-training/Team-Termite##Recommended Links">Recommended Links</a>
## Introduction
The internet provides users with the opportunity to carry out tasks without having to leave their homes. Activities like making purchases online become overwhelming due to variation in prices on the same products across different platforms(online stores). Therefore, it is imperative to get a platform which gives users the power to make the best and smart decision in respect to prices on products of choice.

PriceAm is a web application that allows users to compare the price of IT gadgets/accessories across major online shopping stores.This web application creates a window for prospective buyers to an existing online store with a few clicks of the mouse. Hence, it could be likened to window shopping across several stores at the same time—helping users to make quality right decisions on best fit products at best prices.

## Features
### Unauthenticated User
 The user can visit the platform to view products information, pricing and reviews. The user also has access to view available products after interacting with the documentation. The user can browse through available products using the search feature, and also make enquiries about functionality after signing up for a newsletter with an email address. User can only access additional features after registering with their  Name, email address and password or using any other method like  through their Google account, Facebook account, or Twitter account.
### Authenticated User
 This user has full access to the platform after registering. The user can view previously searched products and see similar product recommendations. The user can leave comments under highlighted products and also interact with other users on products/price. The user can also add products to their watchlist on their dashboard giving them quick access to alerts on price changes on products of choice. The user has access to view the product's full information and view available sellers for desired products. The user can share product information on social media and mail.
 
 ## Technologies Used
 ### Product Design
   - Figma
   - Figjam
 ### Frontend Development
   - HTML5
   - CSS
   - JavaScript
   - Bootstrap
### Backend Development
   - Python
   - Django
## Environment Setup/Installation Guide
- Clone the repo
```
git clone https://github.com/zuri-training/Team-Termite.git 
```
- Enter the project directory 
```
cd team-termite
```
- Create a virtual env
```
python -m venv env 
```
- Activate your env(for windows)
```
./env/Scripts/activate 	 
```
- (for linux or mac)
```
source env/bin/activate 
``` 
- Install Project Dependencies
```
pip install -r requirements.txt
```
- Make Migrations
```
python manage.py makemigrations
python manage.py migrate
```
- Create Superuser
```
python manage.py createsuperuser
```
- Run the server
```
python manage.py runserver
```

## To Contribute

- Create a Fork of this repository

- Clone the forked repository
```
git clone https://github.com/zuri-training/Team-Termite.git 
```

- Open your code editor

- Run your terminal

- Add Upstream
```
git remote add upstream https://github.com/zuri-training/Team-Termite.git
```

- Create a branch
```
git branch {branchname}
```

- Switch to the branch
```
git checkout {branchname}
```

- Make your changes.

- After finishing your tasks, Stage and commit to your branch using
```
git add .
git commit -m " My Contribution "
```

- Merge the upstream changes with your current branch to prevent conflict.
``` 
git pull upstream {branchname}
```

- Push to the branch you’re working on
```
git push origin {branchname}
```
    
- Come to Github and Create a new pull request. Add a description of what you have done.

## Recommended Links
- <a href="https://app.quickdatabasediagrams.com/#/d/1smmJO" target="_blank">Database Schema</a>
- <a href="https://docs.google.com/document/d/1n3uDvnyK9Jy0EoOCXK6DvzdXekHqs_2kNNMZQelMB_E/edit?usp=sharing" target="_blank">Design Sketch</a>
- <a href="https://github.com/zuri-training/Team-Termite"  target="_blank">Github Repo link</a>
- <a href="https://docs.google.com/document/d/1uZacACc6Zj4Rh7XlCHc4kKOTLsaEJrI78xFQSa-lH08" target="_blank">Project Documenation</a>



 

