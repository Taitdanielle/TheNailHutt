# The Nail Hutt

**The Nail Hutt** is a small Nail Salon litrally in a hutt! The perfect place to get away have a cuppa and a chat while you get your chosen treatments done. 
You can visit The Nail Hutt, Book an appointment or treat yourself to some lovley nail products that will be delivered straight to your door! :nail_care:

## Content
---
* #### UX 
  * Project Goals
  * User Stories
  * Design
  * Wireframes
* #### Features :ferris_wheel:
  * Existing Features
  * Features Left to Impliment
* #### Information Architecture
  * Database Choice
  * Data Modeling
* #### Technologies Used  :computer:
  * Languages
  * Libriaries and Frameworks
  * Tools
  * Databases
* #### Testing
* #### Deployment :rocket:
* Local Deployment
* Heroku Deployment
* ### Credits :credit_card:
* Code
* Content and Media
* Acknowledgments
### Disclamier :loudspeaker:
***
## UX
### Projet Goals
#### Target Audience: :dart:
* People who enjoy lookig after themselves
* People who like to treat themselves
* People who enjoy socialising 
* People who want to purchase various nail care products 

#### Visitor/ User Goals: :clipboard:
* Purchase products/services that are shown on the website in a safe and secrure enviroment.
* Get relevent information on the products and treatments available.
### User Stories: :book:
#### Common user stories(guest, new users and authenticated users)
* As a user, I expect to access the website from any device with ease. So that I can use the website anywhere at anytime.
* As a user, I expect to easily navigate the website, So I can find out what I am looking for. 
* As a user, I want to access the social media liks of the company, so that I can read more information or see more about deals
* As a user, I want to view deals that happen with the treatments.
* As a user, I want to view service details and product details (e.g. image, price, description), so that I can book/buy some of them.
* As a user, I want to search and filter the products easily, so that I can quickly find a specific product I am looking for.
* As a user, I want to view a total price of my purchases and delivery cost, so that I will understand and see how much I will be charged.
* As a user, I want to view and modify my order in the cart before completing it, so that I can make last changes easily before proceeding to payment.
* As a user, I expect to make payments by card in a safe and secure way, so that I won't be concerned about the safety of my card details and won't be charged incorrectly.
* As a user, I want to receive an email confirmation after checkout, so that I can make sure that payment was successfull.
#### New User
* As a new user, I want to create my own account so that I can Save, View and Edit my profile details. Also to view my order history.
#### Returning User
* As a user, I want to be able to change my password, so that I can create the stronger password (e.g.in case I published my old password somewhere) to protect my personal details. 
* As a user, I want to reset my password if I forgot it, so that I can get access to my profile again.
* As a user, I want to easily login anytime, so that I can get access to my saved profile details and make next purchase quicker.
* As a user, I want to be able to change my email or add the second email, so that I can have an easier access to the website's functionality and to gain more flexibility.
#### Admin(website owner)
* As a user, I want to have convenient and secure admin interface available only for website admin, so that I can add, edit and remove products/services.
* As a user, I want to receive emails from the users when they fill out the contact form, so that I can reply on them satisfying users queries.
### Design :art:
#### Framework
* **Bootstrap**, front-end framework is chosen for this project for its modern interface, ease of use and ability to be easily customized. It is used for creating features such as navbar, cards, forms, modals, as well as for the layout.
* **JQuery** is used for initializing some Bootstrap components, as well as for custom functions, DOM manipulation
#### Colour Scheme
I used warm bright colours to go with the company logo.
* You can see the colours [here](https://github.com/Taitdanielle/TheNailHutt/blob/main/wireframes/colour-palet.png)
* You can see the logo [here](https://github.com/Taitdanielle/TheNailHutt/tree/main/wireframes)
#### Typography 
The typefaces I used across the project are:
* [Quicksand](https://fonts.google.com/specimen/Quicksand) I have used for the paragraphs, I really like this font as it goes well with the business logo and it is also easy to read.
* [Amatic SC](https://fonts.google.com/specimen/Amatic+SC?preview.text=Products&preview.text_type=custom) I have used this for the page titles as it works well with the current theme and other typefaces.
I think both typfaces work well with the style and colours of the website. 
#### Icons
Icons are used all over the web, They are good at grabbing a users attention. They help users find content quickly and easily. Another advantage of useing them is breaking language barriers too! They create more user-friendly experience by giving the visual clue of the subject.
* I used [Font Awesome](https://fontawesome.com/) as the main icon library for social media links, forms, cart, user icons in the navigation.
* I also used some iscons that were found in a free icon library called [Flaticon](https://www.flaticon.com/) used in the party and landing pages.
### Wireframes :wrench:
Balsamiq wireframes tool was used to create all wireframes for this project. I really enjoy using this tool.
You can find the wireframes for this website [here](https://github.com/Taitdanielle/TheNailHutt/tree/main/wireframes).
### Features
The Nail Hutt is composed by applications: `Landing`, `Parties`, `Products`, `Events` , `Shopping Cart`, `Checkout` and `Profiles`.
### Existing Features
#### **NavBar**
The navbar is fixed at the top of the page at all times, This allows a user to easisly navigate through the website. The name The Nail Hutt is located at the top lefthand corner on a desktop and in the center on smaller devices. It redirects a user to the home/landing page when clicked. On smalled screens such as tablet and mobile the navbar is collapsed into a burger icon. Menu links appear when the burger icon is clicked and will collapse back when clicked again or off the page. 
Navbar also contains a shopping cart icon, with a grand total displated if there are items in the cart added. It changes colour to blue when there in somthing in the cart to catch the users attention, and remains purple when the cart is empty. Clicking on the cart redirects a user to the shopping cart page.
The Navbar links change if you are a logged in or non logged in users. 
* for non logged in users the nav bar will show login/register links.
* for logged in users the navbar contains the "My Account" nav item which toggles down the following links that re direct the user to the followin pages, My profile, Order history and Logout.
* for admin apart from all the links available for logged in users mentioned aboove, They also havea link to the **Product Management Page**. Where the admin can add new profucts and services. This is **only** available for **Superusers**.
#### **Landing/home page**
The landing page serves to attract new users and customers to the business. to give a clear understanding about that and to attract the users to use the website(book appointmnet and buy products).Smooth annimation on the scroll is applied to all sections of the page.
* Hero image
* products carousel
* events carousel 
* quote section
* party section
#### **Party Page**
This page reprosents the different kind of nail partys that are available within  The Nail Hutt. A short paragraph explaines to the users how the events are organised and how to book them. 
There's also a Find us here section, showing the address, phone number and the link to the Facebook page, that can be checked to see more details about the partys. On the large screen, The animation on scroll is applied to that image and to the main paragraph.
#### **Products Page**
* The "All products" page displays product cards, including the following information: category, name, price. All product cards are clickable and redirect a user to the individual product page with detailed information (by clicking on the image or the "View details" button).
* Clicking on Add to cart button will add the product to the cart with quantity equal to 1, clicking again will simply updates the quantity by 1. This functionality was added to enhance user experiance, to allow users straight away add an item to the cart without viewing products details and giving more flexibility to use the website.
* If the user is admin, there are also 2 buttons displayed in the cards: Edit and Delete. Clicking Edit button redirects admin to the Edit Product page. Delete button toggles the Delete modal. It asks a superuser to confirm if the product is to be deleted. If so, upon clicking "Delete" button, the product will not be removed from the database, but will set as discontinued and will be removed from the user's view. Then the page reloads and the toast-message will inform about the sucessfull deletion. There is also a button "Cancel" that closes the modal when it's clicked. These actions can be done only by superuser, attempts to access them by other users will end up with redirection to the landing page with toast error messages displayed.
#### **Product Detail Page**
* The product details page displays information about product selected: category, name, description, price and product image (or placeholder if no image was added). Clicking the image will open it in the new tab, if the image_url is assigned.
* The item quantity can be assigned filling the quantity form, the validation is in place restricting the quantity to the range of 1-999. The validation errors will be displayed, if the user tries to input the numbers outside of that range.
Product can be added to the cart by clicking Add to cart button, that will be reflected in the cart icon in the navbar (grand total will be increased there). As well as that, the toast success message will be displayed when the product is added to the cart.
* If the user is admin, there are also 2 buttons displayed below the product name: Edit and Delete. Clicking Edit button redirects admin to the Edit Product page. Delete button toggles the Delete modal. It asks a superuser to confirm if the product is to be deleted. If so, upon clicking "Delete" button, the product will not be removed from the database, but will set as discontinued and will be removed from the user's view. Then the page reloads and the toast-message will inform about the sucessfull deletion. There is also a button "Cancel" that closes the modal when it's clicked. These actions can be done only by a superuser, attempts to access them by other users will end up with redirection to the landing page with toast error messages displayed.
#### **Events Page**
* The Services page displays horizontal services cards including the following information: name, description, price and image. No-image placeholder is assigned if no image is provided.
* The Button "Learn more" redirects a user to the individual events page with detailed information.

#### **Shopping Cart**
* Cart page is available for both logged in and non-logged in users, so that it is possible to make purchase being a guest.
The page contains a summary of the user's order: the item's name, image, quantitie/ number of participants, price, sub-total and sku(for products).
* The link at the top of the page Continue shopping" navigates a user back to the products page, if a user wants to add something else to the cart.
* A user can update item's quantity/number of participants and date-time (if it's a service) and remove items from their order completely. To prevent from the accidental clicking the remove button, the modal will be opened on click asking a user to confirm the deletion. If a user tries to enter invalid quantity, error message will be displayed when "Update" button is clicked and will prevent the invalid form submission. The error message will inform about the possible range: 1-999 for product's quantity and 1-100 for service's number of participants fields.
* Toast messages will be displayed when a user updates/removes items in the cart.
* At the bottom of the page the cart subtotal, delivery coast and grand total are displayed.
* There is a Checkout button that takes a user to the checkout page to proceed with the payment.
#### **Checkout Page**
* Order summary includes short information about items in the order (image, name, quantity, subtotal, date-time), the link to Edit cart ( that redirects a user to the Cart page), delivery cost and also Total to pay.
* Checkout form is represented as 3 tabs with the Next and Go back buttons to navigate between the tabs. The form sections are the following: Personal Details, Billing/Shipping info and Payment.
* If a user already has a profile with the shipping information saved, the form will be pre-populated with this information.
* The validation messages will be displayed on click Next button, so a user can move on the next tab only if the current form-section is filled with valid information.
* The save info checkbox allows the form information to be saved to the user's profile for the logged in users.
* If it's a new or non-logged user there are links to register or login pages, in case a user wants to save the information to their profile.
* Before proceeding the payment, user can review and check all the information in the table (Form Summary).
* There's also an optional Comment field for cases if a user has any additional comments to the order.
* A user is informed how much the card will be charged in the paragraph below the Proceed to payment button.
* Since the website is made for educational purposes only and the Stripe functionality is only for testing, only 4242 4242 4242 4242 card number will lead to the successfull payment. A user is asked to provide card number, expiration date (any date in future) and CVC (any numbers).
* A webhook is used to make sure that the order is processed even in the cases when the payment process is interrupted (e.g. if a user accidentally closes the page or browser after clicking "Proceed to payment" button).
* Once the form is submitted and the payment is successfully proceeded, the Checkout sucesss page is loaded and a confirmation email is sent to the user's email. Also, a toast message appears to ensure the user that the order was processed successfully.
#### **Checkout success Page**
* The paragraph with a Thank you message is displayed on the top of the page to inform a user that the payment was processed and the email was sent to the user's email.
* The 3 sections Order info, Shipping details and Order Summary contain all the information about the completed order.
Keep shopping button redirects user to the Products page.
* For logged-in users there's a button View full order history that takes users to the order history page.
#### **Profile Page**
Profle feature is available only for authenticated users.

* Profile page contains Personal info section (username and email displayed). Also it contains 2 buttons Change password and Manage emails (changing the current or adding a new email) that take a user to the corresponding pages (that's a part of Django allauth functionality with a customized templates).
* Shipping details section allows to save the shipping information, so for the next purchase the fields in the checkout form will be pre-filled with this info. User can update this information anytime.
* View order history link will redirect a user to the Order History page.
#### Order history 
Order history feature is available only for authenticated users.

* If a user has not made any purchases, the paragraph will inform that the order history is empty with a link to the Product page.
* If there are completed orders, the table with the following fields: Order Number, Date, Items, Total is in place.
* Clicking the link on the Order number will redirect a user to the checkout success page with all the order information. The Toast info message will tell the user that it's a past confirmation for the order number.
* View My Profile link will redirect a user to the Profile page.

#### **Contact Page**
Contact page consists of 2 sections:

Contact form that's offered to fill out (name, email, message) if a user has any questions or queries. The real email will be sent to the admin of the website (handling by django send_mail() functionality). If an authenticated user opens the contact page, the full name (if provided in user's profile) and email fields are pre-populated.
Contact details section provides company's address, phone number and email, along with a map showing the location of The Nail Hutt. By clicking at the red marker, a user can check the opening hours. Google Map API was used to accomplish that.
### **Admin Product Management**
Product managment feature is available only for a superuser. The Admin page allows an owner of the website to add new products/services by filling out one of the two forms - Add New Product and Add New Service on the Product Management page. If the form is valid, the product/service is added to the database and the user is redirected to the new created product/service details page. The defensive design is implemented to restrict other than admin users to manually enter the url to get access to the page. User will be redirected to the home page with the toast error messages appeared. Edit and Delete product/service functionality allow an admin to make the corresponding manipulations. The Delete functionality was updated during the development, so the product/service is not being completely removed from the database, but set as discontinued and is hidden from the user's view and can be set as active again any time.
### **Django-allauth features**
**Sign Up**
The sign up page allows a user to create a new account. The user is asked to fill the fields "email", "username", "password" and "password (again)". When adding a username, the code compares it against existing email to ensure that it is unique. If user's input does not meet requirements, flash messages will inform a user about the error. When the form is submitted, a verification email is sent to the user's email to verify the email and finish registration process.
There is also a link to the login page for existing users at the bottom of the form.
The Registration page is only available to anonymous users and logged-in users are redirected out automatically.

**Login**
The login page features the form with "username" and "password" fields, allowing registered users to log into their account. If the login was successfull, a user is redirected to the home page and the toast success message appears informing that the log in was successful. Otherwise, flash messages will be displayed about incorrect user's input.
There is also a link to the sign up page for new users at the bottom of the form. As well as that, there's a link to the forgot password functionality, using which a user can reset their password. The login page is only available to anonymous users and logged-in users are redirected out automatically.

**Forgot password**
A user can reset their password to be able to login by entering the email. Then the link for reseting password will be sent to the email provided. The user can create a new password and then login with a new password.

**Logout**
Hitting "logout" button renders logout page, asking to confirm if a user wants to logout. It will end their session and redirects to the homepage with a toast success message appeared.

**404 and 500 error pages**
Custom 404 and 500 pages contain heading, short information about the error and a button "Back Home". As well as that, they display navbar that allows users to come back easily to any page if they got lost.
## Features Left to Impliment: :construction:
* Rating to the project and services
* Reviews section for people to review te experience,
* Adding other ways to log in such as Social Log ins for easy access
* More variety in products
* More services
## Information Architecture:
#### Database Choice
During the development phase I worked with sqlite3 database which is installed with Django.
For deployment(production), a PostgreSQL database is provided by Heroku as an add-on.

The User model used in this project is provided by Django as a part of defaults django.contrib.auth.models. More information about Django’s authentication system can be found here.
#### Data Modeling
##### Profile App
| Name        | Database Key  | Field Type  | Validation |
| ------------- |:-------------:| -----:|------------:|
| User   | user | OneToOneField'User' | on_delete=models.CASCADE
| Full Name | centered      |   $12 |
| Phone number | are neat      |    $1 |
| Address Line 1
| Address Line 2
| Town/City |
| County |
| Postcode |
| Country |

**Products App**

| Name        | Database Key | Field Type | Validation |
| ----------- |:------------:| ----------:| ----------:|
| Category    | category| ForeignKey |on_delete=models.SET_NULL|
| Description | description |TextField| |
| Price       | price | DecimalField| max_digits=6, decimal_places=2|
| Image       | image |ImageField| null=True, blank=True|
| Image URL   | image_url   |      URLField      | max_length=1024, null=True, blank=True|
| SKU         |sku|CharField|max_length=254, null=True, blank=True|

 **Events** 
 | Name         | Dataase Key | Field Type | Validation |
 | ------------ |:------------:| ----------:| ----------:|
 | Weekday|       weekday |models.CharField| max_length=10         |
 | Time  | time |  models.CahrFiels |max_length=80|
 | Description   | description  | models.CharField | max_length=254 
        
**Category** 

| Name | DataBase Key | Field Type | Validation |
|------|:-------------:|-----------:|----------:|
| Programmaric Name | name|CharField|max_length=254|
| Friendly Name |firendly_name|CharField| max_length=254, null=True, blank=True |

**Checkout App** 

**Order**
|          Name |        Database Key |           Field Type |                                                              Validation |
| -------------:| -------------------:| --------------------:| -----------------------------------------------------------------------:|
|  Order Number |	order_number |            CharField |                               max_length=32, null=False, editable=False |
|       Profile |             profile | ForeignKey 'Profile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
|     Full Name |           full_name |            CharField |                                  max_length=70, null=False, blank=False |
|   Email email |          EmailField |                      |                                 max_length=254, null=False, blank=False |
|  Phone number |        phone_number |            CharField |                                  max_length=20, null=False, blank=False |
| Address Line1 |       address_line1 |            CharField |                                  max_length=60, null=False, blank=False |
| Address Line2 |       address_line2 |            CharField |                                  max_length=60, null=False, blank=False |
|     Town/City |        town_or_city |            CharField |                                  max_length=50, null=False, blank=False |
|        County |              county |            CharField |                                    max_length=50, null=True, blank=True |
|      Postcode |            postcode |            CharField |                                     ax_length=20, null=True, blank=True |
|       Country |             country |         CountryField |                         blank_label='Country*', null=False, blank=False |
| Purchase Date |       purchase_date |        DateTimeField |                                                       auto_now_add=True |
| Delivery Cost |       delivery_cost |         DecimalField |                   max_digits=6, decimal_places=2, null=False, default=0 |
|   Order Total |         order_total |       DecimalField	m |                   ax_digits=10, decimal_places=2, null=False, default=0 |
|   Grand Total |         grand_total |         DecimalField |                  max_digits=10, decimal_places=2, null=False, default=0 |
| Original Bag |       original_bag |            TextField |                                     null=False, blank=False, default='' |
|    Stripe Pid |          stripe_pid |            CharField |                     max_length=254, null=False, blank=False, default='' |
|       Comment |             comment |            TextField |                                   max_length=254, null=True, blank=True |

**Order Item Details**
| Name | Database Key | Field Type | Validation |
| ---- | ------------ | ---------- | ---------- |
|Order|order|	ForeignKey 'Order'	|null=False, blank=False, on_delete=models.CASCADE, related_name='orderitems'|
|Product|	product|	ForeignKey 'Product'|	null=False, blank=False, on_delete=models.PROTECT
|Quantity	|quantity|	IntegerField|	null=False, blank=False, default=0
|Item Total	|item_total	|DecimalField	|max_digits=6, decimal_places=2, null=False, blank=False, editable=False|
                                                                      
## Technologies Used: :computer:
### Languages
* HTML
* CSS 
* Java Script
* Python
* Jinga 

### Libriaries and Frameworks
* Django 
* Bootstrap
* Google fonts
* Font Awesome
* JQuery
* Psycopg2
* Stripe
* Django Crispy forms
* Cloudinary
### Tools
* Gitpod 
* Git
* GitHud
* PIP 
* Heroku
* Cloudinary 
* Tiny png
* Balsamiq
* Coolors.co
### Databases
* sqlite3
* PostgreSQL


## Testing:
### Landing page
User story being tested:
As a user, I want to read a summary info about the business, its ideas and benifits, so that I can quickly decide if it satisfies my needs.
* Test:
click all the buttons accross the page
scroll down the page to check the animation on scroll (AOS)
check all the image-carousels and reviews-carousel by clicking on chevrons
verify that the expected text, icons and images are displayed
* Results:
all the buttons redirect to the corresponding pages (About, Parties, Products, Events and Contact)
the hover effect on buttons works as expected (expanding, changing background colour)
animation on scroll works as expected on all sections and across all devices
image and review carousels display correctly when chevrons are clicked
all the text sections, icons and all the images display correctly, changing the position, size when viewed on different screens
Verdict: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Events page
User story being tested:
As a user, I want to view events that happen in the the salon
* Test:
verify that images are displayed correctly
verify that the data from the Events model is displayed correctly in the events table
scroll down the page to check the animation on scroll (on the text and teapot image)
click on the Facebook link
* Results:
all the images and texts are displayed correctly on different screens
animation on scroll works as expected on all sections and across all devices
Facebook link opens in the new tab leading to the main page (since there is no real page exists for the website)
Verdict: Test passed. All the functionality works as for some reason the tablets doesnt display, but due to time constraints I didnyt have time to fix.

### Contact page
User stories being tested:
As a user, I want to see the location of the Tea Club on a map, so that I can find the address easily and come to the advertised events.
As a user, I want to be able to easily contact the owner/manager of the company, so that I can write an additional query or ask a question.
Admin: As a user, I want to receive emails from the users when they fill out the contact form, so that I can reply on them satisfying users queries.
* Test:
check that a graphic image is displayed only on the large screen
try to submit an empty Contact form
try to enter incorrect email address (without @)
try to submit the form with all valid information
check the contact form as authenticated user to see if the full name and email fields are pre-populated
check the map, clicking on the red marker, zoom controllers
* Results:
the image and contact information are displayed correctly on different screens
after attempts to submit invalid form (empty or invalid informations) corresponding validation messages appears to prevent the submission
if the form was valid and "Send" button clicked, a user is redirected to the "Thank you" page, informing that the message was sent
if the form was submitted successfully, an admin of the website received the real message on the email (it is assigned in the environment variables as EMAIL_HOST_USER)
if the user is authenticated, the email field is always pre-populated
if the user is authenticated and has the full name is saved in the Profile information, the full name is pre-populated in the contact form
map on the contact page displays the correct location, the Info Window shows the opening hours, when the red marker is clicked. Zoom controllers also work correctly.
after successfull contact form submission, admin of the store receives the message on their personal email, getting user's email and full name, so an admin can answer the query directly to the user's email
Verdict: Test passed. All the functionality works as expected, no bugs were found during the testing.

### Deployment: :rocket:
The Nail Hutt was developed using the GitPod online IDE and using Git and GitHub for version control. It is hosted on the Heroku platform.
### Local Deployment
To be able to run this project, the following tools have to be installed:

* An IDE of your choice (I used GitPod for creating this project)
* Git
* PIP
* Python3
Apart from that, you also need to create accounts with the following services:

* Stripe
#### Directions
1. You can clone this repository directly into the editor of your choice by pasting the following command into the terminal:
`git clone https://github.com/Taitdanielle/TheNailHutt`
Alternatively, you can save a copy of this repository by clicking the green button Clone or download , then Download Zip button, and after extract the Zip file to your folder.
In the terminal window of your local IDE change the directory (CD) to the correct file location (directory that you have just created).
#### Heroku Deployment
To start Heroku Deployment process, you need to clone the project as described in the Local deployment section above.
To deploy the project to Heroku the following steps need to be completed:
1. Create a requirement.txt file, which contains a list of the dependencies, using the following command in the terminal:
pip3 freeze > requirements.txt
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:
`web: gunicorn thenailhutt.wsgi:application`
3. `git add`, `git commit` and `git push` these files to GitHub repository.
**NOTE**: these **1-3 steps** already done in this project and included in the GitHub repository, but illistrated here as they are required for the successfull deployment to Heroku.
As well as that, other things that are required for the Heroku deployment and have to be **installed**: `gunicorn (WSGI HTTP Server), dj-database-url for database connection and Psycopg (PostgreSQL driver for Python)`. All of the mentioned above are already installed in this project in the requirements.txt file.
4. On the Heroku website you need to create a new app, assigne a name (must be unique),set a region to the closest to you(for my project I set Europe) and click **Create app**.
5. Go to Resources tab in Heroku, then in the Add-ons search bar look for Heorku Postgres(you can type postgres), select Hobby Dev — Free and click Provision button to add it to your project.
6. In Heroku Settings click on Reveal Config Vars.
7. Set the following config variables there:
8. Copy DATABASE_URL's value(Postrgres database URL) from the Convig Vars and temporary paste it into the default database in settings.py. You can temporary comment out the current database settings code and just paste the following in the settings.py:
```
DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
**Important Note: that's just temporary set up, this URL should not be committed and published to GitHub for security reasons, so make sure not to commit your changes to Git while the URL is in the settings.py.**
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py makemigrations`
`python3 manage.py migrate`
10. Load the data fixtures **(categories, products, Parties,events etc)** into the Postgres database using the following command:
`python3 manage.py loaddata <fixture_name>`
11. Create a superuser for the Postgres database by running the following command(you need to follow the instructions and inserting username,email and password):
python3 manage.py createsuperuser
12. You need to **remove** your Postgres URL database from the settings and uncomment the default DATABASE settings code in the settings.py file.
**Note**: *for production you get the environment variable 'DATABASE_URL' from the Heroku Config Vars and use Postgress database, while for development you use the SQLite as a default database.*
13. Add your Heroku app URL to ALLOWED_HOSTS in the settings.py file. 14. You can connect Heroku to GitHub to automatically deploy each time you push to GitHub.
To do so, from the Heroku dashboard follow the steps:

* Deploy section -> Deployment method -> select GitHub
* Link the Heroku app to your GitHub repository for this project
* Click Enable Automatic Deploys in the Automatic Deployment section
* Run `git push` command in the terminal, that would now push your code to both Github and Heroku, and perform the deployment.
Alternatively, in the terminal you can run:

* `heroku login`
* after adding and comitting to Git, run the following command:
`git push heroku master`
15. After successful deployment, you can view your app bu clicking Open App on Heroku platform.
16. You will also need to verify your email address, so you need to login with your superuser credentials and verify your email address in the admin panel. Now you will be able to view the app running!
#### Hosting media files with AWS
The static files and media files (that will be uploaded by superuser - product/service images) are hosted in the AWS S3 Bucket. To host them, you need to create an account in AWS and create your S3 basket with public access. More about setting it up you can read in Amazon S3 documentation and this tutorial. 
## Credits
### Code
* The projects code was developed by following the Code Institute and based on the understanding of the Boutique Ado Django Project, but was customised and enhanced to fir the purpose of mt chosen idea. some comments with the credits to that modle are added to some parts of the code where needed. 
* Stack Overflow was extreamley helpful and useful during the process of building the this project, credits again are given for the certain solutions are given in the comments. 
* I also was always checking and reffering the following documentation durgont he development django and stripe crispy forms

### Content and Media
colours from coloors
pictures from dreamstime
* Images from [Pexels](www.pixels.com)
* Products content and images taken from [here](wwww.nailpolishdirect.co.uk) at Nail Polish Direct
* Logo was created by me in Photoshop before this project
* Nail pictures from my sisters business [TheNailHutt](https://www.facebook.com/thenailhutt)


### Acknowledgements
I would like to thank everyone who helped me with this project. I appreciate you all!
* My mentor Simen Daehlin [best mentor](https://github.com/Eventyret) for his support, tips, advice and also for beleiving in me and making me relise I can actually do it!
* All the Code Institue Tutors who put up with my many many meltdowns! and night hawk antics :joy:
* My fellow students and the Slack Community I don't know where I would have been without the guys on that.
*  A big should out to [Fran](https://github.com/fdeboo) she kept me going most times and helped me **A LOT!** What an awesome person she is.
## Disclaimer
This site is made for **educational purposes** only. :books: 