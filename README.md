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
## **NavBar**
The navbar is fixed at the top of the page at all times, This allows a user to easisly navigate through the website. The name The Nail Hutt is located at the top lefthand corner on a desktop and in the center on smaller devices. It redirects a user to the home/landing page when clicked. On smalled screens such as tablet and mobile the navbar is collapsed into a burger icon. Menu links appear when the burger icon is clicked and will collapse back when clicked again or off the page. 
Navbar also contains a shopping cart icon, with a grand total displated if there are items in the cart added. It changes colour to blue when there in somthing in the cart to catch the users attention, and remains purple when the cart is empty. Clicking on the cart redirects a user to the shopping cart page.
The Navbar links change if you are a logged in or non logged in users. 
* for non logged in users the nav bar will show login/register links.
* for logged in users the navbar contains the "My Account" nav item which toggles down the following links that re direct the user to the followin pages, My profile, Order history and Logout.
* for admin apart from all the links available for logged in users mentioned aboove, They also havea link to the **Product Management Page**. Where the admin can add new profucts and services. This is **only** available for **Superusers**.
## **Landing/home page**
The landing page serves to attract new users and customers to the business. to give a clear understanding about that and to attract the users to use the website(book appointmnet and buy products).Smooth annimation on the scroll is applied to all sections of the page.
* Hero image
* products carousel
* services carousel 
* quote section
* party section
## **Party Page**
This page reprosents the different kind of nail partys that are available within  The Nail Hutt. A short paragraph explaines to the users how the events are organised and how to book them. 
There's also a Find us here section, showing the address, phone number and the link to the Facebook page, that can be checked to see more details about the partys. On the large screen, The animation on scroll is applied to that image and to the main paragraph.
## **Products Page**
* The "All products" page displays product cards, including the following information: category, name, price. All product cards are clickable and redirect a user to the individual product page with detailed information (by clicking on the image or the "View details" button).
* Clicking on Add to cart button will add the product to the cart with quantity equal to 1, clicking again will simply updates the quantity by 1. This functionality was added to enhance user experiance, to allow users straight away add an item to the cart without viewing products details and giving more flexibility to use the website.
* If the user is admin, there are also 2 buttons displayed in the cards: Edit and Delete. Clicking Edit button redirects admin to the Edit Product page. Delete button toggles the Delete modal. It asks a superuser to confirm if the product is to be deleted. If so, upon clicking "Delete" button, the product will not be removed from the database, but will set as discontinued and will be removed from the user's view. Then the page reloads and the toast-message will inform about the sucessfull deletion. There is also a button "Cancel" that closes the modal when it's clicked. These actions can be done only by superuser, attempts to access them by other users will end up with redirection to the landing page with toast error messages displayed.
## **Product Detail Page**
* The product details page displays information about product selected: category, name, description, price and product image (or placeholder if no image was added). Clicking the image will open it in the new tab, if the image_url is assigned.
* The item quantity can be assigned filling the quantity form, the validation is in place restricting the quantity to the range of 1-999. The validation errors will be displayed, if the user tries to input the numbers outside of that range.
Product can be added to the cart by clicking Add to cart button, that will be reflected in the cart icon in the navbar (grand total will be increased there). As well as that, the toast success message will be displayed when the product is added to the cart.
* If the user is admin, there are also 2 buttons displayed below the product name: Edit and Delete. Clicking Edit button redirects admin to the Edit Product page. Delete button toggles the Delete modal. It asks a superuser to confirm if the product is to be deleted. If so, upon clicking "Delete" button, the product will not be removed from the database, but will set as discontinued and will be removed from the user's view. Then the page reloads and the toast-message will inform about the sucessfull deletion. There is also a button "Cancel" that closes the modal when it's clicked. These actions can be done only by a superuser, attempts to access them by other users will end up with redirection to the landing page with toast error messages displayed.
## **Services Page**
* The Services page displays horizontal services cards including the following information: name, description, price and image. No-image placeholder is assigned if no image is provided.
* The Button "Learn more" redirects a user to the individual service page with detailed information.
* Similar to products, Edit and Delete are displayed on the cards if the user is admin with the corresponding functionality to render Edit Service page and toggle Delete modal.
## **Service Details Page**
## **Contact Page**
Contact page consists of 2 sections:

Contact form that's offered to fill out (name, email, message) if a user has any questions or queries. The real email will be sent to the admin of the website (handling by django send_mail() functionality). If an authenticated user opens the contact page, the full name (if provided in user's profile) and email fields are pre-populated.
Contact details section provides company's address, phone number and email, along with a map showing the location of The Nail Hutt. By clicking at the red marker, a user can check the opening hours. Google Map API was used to accomplish that.
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