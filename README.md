# The Nail Hutt
**The Nail Hutt** is a small Nail Salon litrally in a hutt! The perfect place to get away have a cuppa and a chat while you get your chosen treatments done. 
You can visit The Nail Hutt, Book an appointment or treat yourself to some lovley nail products that will be delivered straight to your door!

## Content
---
* #### UX 
  * Project Goals
  * User Stories
  * Design
  * Wireframes
* #### Features
  * Existing Features
  * Features Left to Impliment
* #### Information Architecture
  * Database Choice
  * Data Modeling
* #### Technologies Used
  * Languages
  * Libriaries and Frameworks
  * Tools
  * Databases
* #### Testing
* #### Deployment
* Local Deployment
* Heroku Deployment
* ### Credits
* Code
* Content and Media
* Acknowledgments
### Disclamier 
***
## UX
### Projet Goals
#### Target Audience
* People who enjoy lookig after themselves
* People who like to treat themselves
* People who enjoy socialising 
* People who want to purchase various nail care products 

#### Visitor/ User Goals:
* Purchase products/services that are shown on the website in a safe and secrure enviroment.
* Get relevent information on the products and treatments available.
### User Stories
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
### Design 
#### Framework
* **Bootstrap**, front-end framework is chosen for this project for its modern interface, ease of use and ability to be easily customized. It is used for creating features such as navbar, cards, forms, modals, as well as for the layout.
* **JQuery** is used for initializing some Bootstrap components, as well as for custom functions, DOM manipulation
#### Colour Scheme
I used warm bright colours to go with the company logo.You can see the colours [here](https://github.com/Taitdanielle/TheNailHutt/blob/main/wireframes/colour-palet.png)
#### Typography 
The typefaces I used across the project are:
* [Quicksand](https://fonts.google.com/specimen/Quicksand) I have used for the paragraphs, I really like this font as it goes well with the business logo and it is also easy to read.
* [Amatic SC](https://fonts.google.com/specimen/Amatic+SC?preview.text=Products&preview.text_type=custom) I have used this for the page titles as it works well with the current theme and other typefaces.
I think both typfaces work well with the style and colours of the website. 
#### Icons
Icons are used all over the web, They are good at grabbing a users attention. They help users find content quickly and easily. Another advantage of useing them is breaking language barriers too! They create more user-friendly experience by giving the visual clue of the subject.
* I used [Font Awesome](https://fontawesome.com/) as the main icon library for social media links, forms, cart, user icons in the navigation.
* I also used some iscons that were found in a free iscon library called [Flaticon](https://www.flaticon.com/) used in the party and landing pages.
### Wireframes
Balsamiq wireframes tool was used to create all wireframes for this project. I really enjoy using this tool.
You can find the wireframes for this website [here](https://github.com/Taitdanielle/TheNailHutt/tree/main/wireframes).
### Features
The Nail Hutt is composed by applications: `Landing`, `Partys`, `Products`(Products & Services), `Shopping Cart`, `Checkout` and `Profiles`.
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
* services carousel 
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
#### **Services Page**
* The Services page displays horizontal services cards including the following information: name, description, price and image. No-image placeholder is assigned if no image is provided.
* The Button "Learn more" redirects a user to the individual service page with detailed information.
* Similar to products, Edit and Delete are displayed on the cards if the user is admin with the corresponding functionality to render Edit Service page and toggle Delete modal.
#### **Service Details Page**
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
#### Order history** 
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
Sign Up
The sign up page allows a user to create a new account. The user is asked to fill the fields "email", "username", "password" and "password (again)". When adding a username, the code compares it against existing email to ensure that it is unique. If user's input does not meet requirements, flash messages will inform a user about the error. When the form is submitted, a verification email is sent to the user's email to verify the email and finish registration process.
There is also a link to the login page for existing users at the bottom of the form.
The Registration page is only available to anonymous users and logged-in users are redirected out automatically.

Login
The login page features the form with "username" and "password" fields, allowing registered users to log into their account. If the login was successfull, a user is redirected to the home page and the toast success message appears informing that the log in was successful. Otherwise, flash messages will be displayed about incorrect user's input.
There is also a link to the sign up page for new users at the bottom of the form. As well as that, there's a link to the forgot password functionality, using which a user can reset their password. The login page is only available to anonymous users and logged-in users are redirected out automatically.


## Testing
## Bugs
had to change image urls as they were not wokring in large screen size. 
### Deployment
The Nail Hutt was developed usnig the GitPod online IDE and using Git and GitHub for version control. It is hosted on the Heroku platform.
### Local Deployment
#### Heroku Deployment
## Credits
### Code
### Content and Media
colours from coloors
pictures from dreamstime
Top of home page Photo by Artem Beliaikin from Pexels

### Acknowledgements
I would like to thank everyone who helped me with this project. I appreciate you all!
* My mentor Simen Daehlin(best mentor) for his support, tips, advice and also for beliving in me and making me relise I can actually do it!
* All the Code Institue Tutors who put up with my many many meltdowns!
* My fellow students and the Slack Community I don't know where I would have been without the guys on that. 
## Disclaimer
This site is made for **educational purposes** only. 