# PriceAm
## Table of Contents
   - Introduction
   - Features
   - Technologies Used
   - Environment Setup/Installation Guide
   - Contributors
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
cd price_compare_team_27
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



 

