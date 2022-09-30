# Cyclo Domestique - Bike Shop

## About

I have chosen to create a bike shop storefront as I share a passion of cycling. Maybe one day I will have an opportunity to own my own shop, so why not to create one now. 

This online store was built with a simple and clean look intent and with all the expected features for the bike shop. Shop offers greatest bikes, accessories, maintenance products or maintenance service offerings for the user and message, inventory management options for the store owners.

Website was built using HTML, CSS and JavaScript for the front end and makes use of Python and the Django framework for the backend, which also uses the PostgreSQL relational database.

### Mockup
#

<a href="https://imgur.com/71H9X86"><img src="https://i.imgur.com/71H9X86.jpg" title="source: imgur.com" /></a>

## UXD
#
### Purpose
#
Website is targeting all ages and demographics, cycling does not have any boundaries and is accessible to all as long as a customer want or needs to cycle either for health, commuting or competitive reasons. For more competitive cyclists we offer higher specification bikes and for new starters we offer high quality affordable bikes from adults to children sizes.

With certain design choices and information within website any visitor should instantly recognise the purpose of the site, and to feel comfortable to browse and explore the website.

#
#### User Stories
#

#### **EPICS**

| id  |  Epic | Description
| ------ | ------ | ------ |
|  [#1](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/1) | Site Admin | Manage store products, stock levels, site messages, site orders. |
|  [#2](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/2) | Profile App |Account registration with email verification, reset password, login and log out function. Access and manage user profile information and view order history, |
|  [#3](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/3) | Home App |Create navigation links, home page, site style with confirmation toast messages. Access to social page  via contact links |
|  [#4](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/4) | Products App |Create product list and detailed pages with filters, sort and search functionality. Sort products using different criteria |
|  [#5](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/5) | Basket App | Customer can add or delete products in basket and view total products listed, update product quantity. |
|  [#6](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/6) | Checkout App| Process online orders and payment transaction, generate order confirmation and email confirmation. |
|  [#7](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/7) | About App |Customer can view details about shop. |
|  [#8](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/8) | Contact App |Customer can view shops contact details, can send a contact form with a query or a question. |
|  [#9](https://github.com/EdgarasSp/cyclo-domestique-storefront/milestone/9) | Marketing |Setup social account for marketing purposes and setup site SEO meta. |

[Back to top](#)
#

### **User Stories with associated site sections links satisfying story requirements:**
#

Each story was assigned a classification as per MOSCOW principles of Must-Have, Should-Have, Could-Have or Won't Have.

**EPIC #1: Site Admin**

| Story id  |  Story| Description | Status / Label  |
| ------ | ------ | ------ | ------ |
|  [#1](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/1) | Process orders online | As a shop owner I can process orders online so that I can sell products online | Complete / Must-Have  
|  [#2](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/2) | Admin CRUD | As a shop owner I want to navigate the admin panel so that I can create, read, update and delete data on the site.  | Complete / Must-Have  
|  [#3](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/3) | Admin add, update and delete product | As a shop owner I want to add, update and delete product so that I can update, add new product or delete unavailable product on the site. | Complete / Must-Have  
|  [#4](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/4) | Admin edit product details | As a shop owner I want to edit the product so that I can update the product information.  | Complete / Must-Have  
|  [#5](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/5) | Admin edit product stock  | As a shop owner I want to edit the product so that I can update the product stock levels.  |  Complete / Must-Have 
|  [#6](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/6) | Admin manage reviews | As a shop owner I want to manage the customer review so that I can filter out and approve the reviews that user wants to post on the site. | To Start / Could-Have
|  [#7](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/7) | Admin view edit orders | As a shop owner I want to view site orders and status so that I can confirm order details and update order status.  | Complete / Must-Have
|  [#8](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/8) | Admin view edit messages | As a shop owner I want to view site messages and status so that I can read message details and update message status.  | Complete / Must-Have
|  [#9](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/9) | Admin receive payment | As a shop owner I want to receive payment from customers electronically so that I can streamline my payment processing.  |  Complete / Must-Have
|  [#10](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/10) | Admin send newsletter | As a shop owner I want to send the newsletters out so that I can promote the products to customer with updates for more business.  |  Complete / Should-Have
#

**EPIC #2: Profile App**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#11](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/11) | Login and logout | As a register customer I want to login and logout so that I can access my account and manage my purchase on the site.|  Complete / Must-Have |
|[#12](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/12) | Register an account | As a customer I want to register an account so that I can manage my activities on the site. |  Complete / Must-Have |
|[#13](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/13) | View purchase history  | As a registered customer I want to view my purchase history so that I can see what I have bought in the past.|  Complete / Must-Have  |
|[#14](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/14) | Reset account password | As a registered customer I want to reset my account password so that I can access my account again if I forgot the password. |  Complete / Should-Have |
|[#15](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/15) | Edit and delete account profile | As a registered customer I want to edit account so that I can personalize my account profile details for autofill checkout form. |  Complete / Should-Have  |
|[#16](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/16) | Verify email address | As a customer I want to verify my email address so that I can securely of my account and purchase on the site.|  Complete / Must-Have  |
|[#17](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/17) | Receive site action feedback | As a register customer I want to receive feedback so that I can verify my activities on the site.|  Complete / Should-Have  |
|[#18](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/18) | Subscribe newsletter | As a registered customer I want to register for s newsletters so that I can receive regular updates about the products.|  Complete / Must-Have |
|[#19](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/19) | Add and delete product to Wishlist | As a customer I want to add or remove product from wish list so that I can mark the products to purchase.|  To Start / Could-Have   |
#

**EPIC #3: Home App**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#20](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/21) | Navigate the site | As a customer I want to navigate the site so that I know what products the site sells and is about.|  Complete / Must-Have  |
|[#21](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/22) | Access the site | As a customer I want to access the site easily so that I can view the site on any media screens.|  Complete / Must-Have |
|[#22](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/23) | View recommended products | As a customer I want to view recommended products so I can see what products are currently trending. |  Complete / Should-Have  |
|[#23](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/24) | Access social media pages | As a customer I want to access the shop social media platform so that I can follow the shop and get updates.|  To Start / Should-Have  |
#

**EPIC #4: Product App**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#24](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/24) | View product list | As a customer I want to view the list of products so that I know what product the site sells.|  Complete / Could-Have  |
|[#25](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/25) | View product details  | As a customer I want to view the product details so that I can see information about the individual product. |  Complete / Should-Have  |
|[#26](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/26) | Filter and view search product result | As a customer I want to filter products so that I can find the products I interested in.|  Complete / Should-Have  |
|[#27](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/27) | Sort products by a specific criteria | As a customer I want to sort by price or rated product in a specific category so that I can find a product matching my criteria. |  Complete / Must-Have  |
|[#28](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/28) | Site info messages for actions | As a customer I want to view messages so that I know my activities when updating my shopping basket or make a payment. |  Complete / Must-Have  |
|[#29](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/29) | Post review and rate a product | As a registered customer I want to post, delete review and rate a product so that I can share my opinion about products.|  To Start / Could-Have  |
#

**EPIC #5: Basket App**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#30](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/30) | Add and delete product in the shopping basket | As a customer I want to add or delete products from the shopping basket so that I know what products and the amount of products and cost.|  Complete / Must-Have  |
|[#31](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/31) | View the total product in the shopping basket | As a customer I want to view the products in my shopping basket so that I know what I'm purchasing and the total cost for the products.|  Complete / Must-Have  |
|[#32](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/32) | Update quantity in the shopping basket | As a customer I want to update the product quantity in my shopping basket so that I can easily add or delete the same product in my shopping basket.|  Complete / Must-Have  |
#

**EPIC #6: Checkout App**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#33](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/33) | Process online orders | As a shop owner I want to process orders online so that I can sell products online. | Complete / Must-Have  |
|[#34](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/34) | Receive order confirmation | As a registered customer I want to receive confirmation after paying so that I know whether my purchase is successful or not.|  Complete / Must-Have  |
|[#35](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/35) | Checkout and payment processor | As a registered customer I want to checkout and pay online so that I can complete the purchase. |  Complete / Must-Have  |
#

**EPIC #7: About App**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#36](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/36) | View about shop details | As a customer I want to view shop history so that I can read about the shop history and their activities.|  Complete / Should-Have  |
|[#37](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/37) | View opening times address | As a customer I want to view shop opening times so that I can check opening times and shop address.|  Complete / Must-Have  |
|[#38](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/38) | View shop location map | As a customer I want to view map with shop location times so that I can check shop location on the map.|  Complete / Must-Have  |
#

**EPIC #8: Contact App**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#39](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/39) | Contact form | As a user I can fill out and submit a contact form so that I can send queries or feedback.|  Complete / Should-Have  |
|[#40](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/40) | View opening times address | As a customer I want to *view shop opening times so that I can check opening times and shop address.|  Complete / Must-Have |
|[#41](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/41) | View shop location map | As a customer I want to view map with shop location times so that I can check shop location on the map.|  Complete / Could-Have  |
|[#42](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/42) | Contact site owner | As a customer I want to make contact to the site owner so that I can contact the owner for any questions.|  Complete / Must-Have  |
#

**EPIC #9: Marketing**

| Story id  |  Story| Description |  Status / Label | 
| ------ | ------ | ------ | ------ |
|[#43](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/43) | Setup Social account | As a shop owner I want to have social shop profile so that I can promote, reach an engage with more clients.|  In Progres / Should-Have  |
|[#44](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues/44) | View Social account | As a customer I want to view shops social account so that I can share, view and contact shop.|  In Progress / Should-Have  |

#



### **Project Board and Issues**
[Back to top](#)
#

Github Issues were used to create the EPICS and user stories. The user stories were entered as issues, then assigned to each EPIC via the milestones. A link to the issues can be found [here](https://github.com/EdgarasSp/cyclo-domestique-storefront/issues).

<a href="https://imgur.com/TXhsPAH"><img src="https://i.imgur.com/TXhsPAH.png" title="source: imgur.com" /></a>

I have also, utilised gitpod projects to move user stories based on their implementation status. A link to the project  can be found [here](https://github.com/users/EdgarasSp/projects/1). The image below illustrates how this was working.

<a href="https://imgur.com/Zs7FNFY"><img src="https://i.imgur.com/Zs7FNFY.png" title="source: imgur.com" /></a>

[Back to top](#)

#
### Theme
#
The site has a simple layout, designed with Bootstrap framework.

The navbar always sits at the top of each page, taking the user to all the site sections they can access. Only the pages relevant to the user are displayed e.g. a logged-in customer will not see a any admin links to the inventory or orders pages, and not logged in user won't be able to see their order history.

Pages designed with minimalist approach to not overcrowded with unnecessary details or images. Page links and interactive elements are marked. Buttons have a colour scheme and feedback to users via Django toast messages are provided. 

## Wireframe
#
Below are the wireframes created in advance of starting the project. I used the wireframing software [Balsamiq](https://balsamiq.com/) for this project.

* Desktop Wireframe
  ![Wireframe for Mobile](https://i.imgur.com/eFdXvMN.jpg)

* Tablet Wireframe
  ![Wireframe for Tablet](https://i.imgur.com/4FqVPZa.jpg)

* Mobile Wireframe
  ![Wireframe for Desktop](https://i.imgur.com/FAn9XWT.jpg)

## Database Schema
#

A relational database has been used to deliver the expected functionality. SQLite was used in the development of the site and Postgres provided by the Heroku platform is being used in production. The diagram below shows the database models and the relationships between them.

<a href="https://imgur.com/PaSSGqW"><img src="https://i.imgur.com/PaSSGqW.png" title="source: imgur.com" /></a>

## Database Model

#
### **Models**

## **Contact Form**                                              

Name              |Field Type   |Validation                                             
------------------|-------------|-------------------------------------------------------
subject_type|CharField|max_length=100, null=True, blank=False
first_name|CharField|max_length=50, null=True, blank=True
last_name|CharField|max_length=50, null=True, blank=True
contact_number|CharField|max_length=20, null=True, blank=True
email_address|EmailField|max_length=50, null=True, blank=False
message|TextField|max_length=1000, null=True, blank=True
received_date|DateField|auto_now_add=True
status|IntegerField|choices=STATUS, default=0
#

## **UserProfile**

Name              |Field Type   |Validation                                             
------------------|-------------|-------------------------------------------------------
user|OneToOneField|User, on_delete=models.CASCAD
default_full_name|CharField|max_length=50, null=True, blank=True
default_email|EmailField|ength=254, null=True, blank=True
default_phone_number|CharField|max_length=20, null=True, blank=True
default_street_address1|CharField|max_length=80, null=True, blank=True
default_street_address|CharField|max_length=80, null=True, blank=True
default_town_or_city|CharField|max_length=40, null=True, blank=True
default_county|CharField|max_length=80, null=True, blank=True
default_country|CountryField|blank_label='Country',   null=True, blank=True
default_postcode|CharField|max_length=20, null=True, blank=True
#

## **Order**

Name              |Field Type        |Validation                                             
------------------|------------------|-------------------------------------------------------
order_number | models.CharField | (max_length=32, null=False, editable=False)
user_profile | models.ForeignKey |(UserProfile, on_delete=models.SET_NULL, null=True, blank=True,  related_name='orders')
full_name |models.CharField | (max_length=50, null=False, blank=False)
email | models.EmailField | (max_length=254, null=False, blank=False)
phone_number | models.CharField | (max_length=20, null=False, blank=False)
town_or_city | models.CharField | (max_length=40, null=False, blank=False)
street_address1 | models.CharField |(max_length=80, null=False, blank=False)
street_address2 | models.CharField | (max_length=80, null=True, blank=True)
county |models.CharField | (max_length=80, null=True, blank=True)
country |  CountryField | (blank_label='Country *', null=False, blank=False)
postcode |  models.CharField | (max_length=20, null=True, blank=True)
date | models.DateTimeField | (auto_now_add=True)
delivery_cost |  models.DecimalField | (max_digits=6, decimal_places=2, null=False, default=0)
order_total | models.DecimalField | (max_digits=10, decimal_places=2, null=False, default=0)
grand_total | models.DecimalField | (max_digits=10, decimal_places=2, null=False, default=0)
original_basket | models.TextField | (null=False, blank=False, default='')
stripe_pid | models.CharField | (max_length=254, null=False, blank=False, default='')
status | models.IntegerField | (choices=status, default=0)
#

## **OrderLineItem**

Name              |Field Type      |Validation                                             
------------------|----------------|-------------------------------------------------------
order | models.ForeignKey | (Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
product | models.ForeignKey | (Product, null=False, blank=False, on_delete=models.CASCADE)
sku | models.CharField | (max_length=254, null=True, blank=True)
product_size | models.CharField | (max_length=10, null=True, blank=True)
quantity |  models.IntegerField | (null=False, blank=False, default=0)
lineitem_total | models.DecimalField | (max_digits=10, decimal_places=2, null=False, blank=False, editable=False)
#

## **Division**

Name              |Field Type      |Validation                                             
------------------|----------------|-------------------------------------------------------
name | models.CharField | (max_length=254)
friendly_name | models.CharField | (max_length=254, null=True, blank=True)
#

## **Category**

Name              |Field Type      |Validation                                             
------------------|----------------|-------------------------------------------------------
division | models.ForeignKey | ('Division', null=True, blank=True, on_delete=models.SET_NULL)
name | models.CharField | (max_length=254)
friendly_name | models.CharField | (max_length=254, null=True, blank=True)
#

## **Product**

Name              |Field Type      |Validation                                             
------------------|----------------|-------------------------------------------------------
category | models.ForeignKey | ('Category', null=True, blank=True, on_delete=models.SET_NULL)
sku |  models.CharField | (max_length=254, null=True, blank=True)
brand |  models.CharField | (max_length=254)
name |  models.CharField | (max_length=254)
size |  models.CharField | (max_length=254, null=True, blank=True)
amount |  models.DecimalField | (max_digits=10, decimal_places=0, default=10)
color |  models.CharField | (max_length=30, null=True, blank=True)
description |  models.TextField | (max_length=254, null=True, blank=True)
full_description |  models.TextField | (blank=True, null=True)
key_features |  models.TextField | (blank=True, null=True)
price | models.DecimalField | (max_digits=6, decimal_places=2)
rating |  models.DecimalField | (max_digits=6, decimal_places=1, null=True, blank=True)
image | models.ImageField | (null=True, blank=True)
image_url |  models.URLField | (max_length=1024, null=True, blank=True)

                                                

#
## Features
#

### Home Page
#
Upon entering the home page of the website, the user sees a large hero image carousel, which displays friendly messages encouraging to search for or view products. Sending strong impression of the website purpose.

![#1 Home Page](https://i.imgur.com/4Vkw9LR.png)

This is Nav set for dekstop view.
![#2 desktop nav](https://i.imgur.com/RhjUMhf.png)

At mobile level nav bar colapses for ease of view.

![#3 responsive nav](https://i.imgur.com/DlaqX7Y.png)

Scrolling down takes the user to the 'shortcuts' for some suggested categories with hyperlink buttons which on click would redirect to a prodict view based on selected filter. 

![#4 Shortcuts to some available categories](https://i.imgur.com/DR6id4o.png)

Scrolling down further takes the user to the best selling 'Product' section. The page features 10 promoted products with a brief text description with info for the user. 

![#5 Recomended Products carousel](https://i.imgur.com/B348hZX.png)

Next is a 'service repairs' section which features 3 service cards to choose from, cards contain some information outlining product scope and brief description about shops involvement with local community.

![#6 Maintenance option cards and brief communtiy message](https://i.imgur.com/pLGERLi.png)

The final part of the home page is a footer. Contains links to the social sites, privacy notice and terms of use. In addition, footer contains a subscribe section setup and hosted by mailchip mailing provider.

![#6.1 Footer](https://i.imgur.com/SyRS8vW.png)

#
### About Page
#
The first part of the about page contains contact information about the shop, further down provides opening times and shop address with heplpful map.

![#7 About Sections with maps](https://i.imgur.com/mItUYNQ.png)

#
### Contact Page
#

Page contains key contact information such as address, telephone number and provides a contact form. Once the contact form is submitted. The page will show success pop up confirming to the user that the form has been submitted successfully.

![#8 Contact Form](https://i.imgur.com/nJtderC.png)
![#9 Confirmation toast message](https://i.imgur.com/YpPE9ca.png)

#
### Products Pages
#

Depending on the selected category, product page will display products matching either search results or sorted products. Products are displayed as cards for ease of view, cards displaying key information including if the product is in stock or not.

User can access detailed product view by clicking on the card picture.

![#10 Product Page](https://i.imgur.com/YcJUGct.png)

#
### Products Detailed page
#
This page shows detailed product view, detailed descriptions and product variables. 
Customer can change the quantity should they want to add more than one item to the basket. 

![#11 detailed product page](https://i.imgur.com/a5LQ0mM.png)

Once user clicks add to basket, a confirmation pop up will appear confirming items were successfully added to the basket. Popup can be closed by the customer or will close after 6 seconds. Also Customer can see basket preview by hovering over the basket.

![#12 Basket confirmation](https://i.imgur.com/uw0mawV.png)

If user is an admin, additional buttons will be displayed allowing to edit product, delete product or access product inventory.

![#22.1 if editing from detailed view.](https://i.imgur.com/hiI2k5H.png)

#
### Basket Page
#

Onc euser finnished browsing, they can proceed to the basket by clicking on the basket icon located top right.

Once basket is loeaded, user can adjust basket items and once happy to prced user to click continue to checkout.

![#13 Basket View](https://i.imgur.com/jTnxQ21.png)

#
### Checkout Page
#

At the checkout user would input delivery details, if user has an account and is logged in, fields will be populated automatically. If new user a tick box can be ticked for saving details, which would store details and user could create an account.

![#14 Checkout](https://i.imgur.com/2EGfoEQ.png)

Ince payment details are entered, and user proceeds to the payment page. Stripe will handle payment and  if sucesfull redirect to confirmation page.

![#15 Order Confirmation Page](https://i.imgur.com/bZbLCu1.png)

#
### Register
#

A user can register from the 'register' page. All user registration/login etc is handled by the 'Django-allauth' module.

The layout is simple. The inputs prompt the user to enter and confirm their email address, provide a username, and enter and confirm a password.

If a user enters invalid data (i.e. username already taken/passwords do not match etc) then the form will not submit and the errors will be displayed in the relevant location on the screen.

![#16 Registration Form](https://i.imgur.com/qMdOr8f.png)

#
### Sign In
#

A registered user can sign in from the sign-in page. A user can enter either their username or email along with the password.

![#17 Login Page](https://i.imgur.com/yblWLFj.png)

and can log out once finnshed using the website.

![#18 logout](https://i.imgur.com/ZddHoTH.png)

#
### My Profile
#

Authenticated user can navigate to their profile page, were they can update their default details so that next time they purchase the form is populated with up to date details.

![#19 User Profile](https://i.imgur.com/opPxzwM.png)

#
### My Orders
#

Authenticated user can navigate to their order page, were they view previously placed orders, and they can view order confirmation and current order status.

![#20 User orders](https://i.imgur.com/3Yc3fZP.png)

#
### Inventory
#

As a authenticated admin user you can navigate to inventory page, which allows to view, add and update existing products. Update out off stock products.

![#21 Product Inventory](https://i.imgur.com/1MOd5L3.png)

![#22 Product edit and form ](https://i.imgur.com/8giXY3S.png)

#
### Site Orders
#

As a authenticated admin user you can navigate to Site orders, which allows to view all orders placed on the website, allows to view order details, and updated order status which is then displayed to the customer on their account.

![#23 View all site orders](https://i.imgur.com/KtMyrkG.png)

![# 24 View order details](https://i.imgur.com/bZbLCu1.png)

![#25 Update order status](https://i.imgur.com/EoAdfbg.png)

#
### Site Messages
#

As a authenticated admin user you can navigate Site Messages, which allows to view all messages sent via websites contact form. Allows to read the messages and update message status once message was handled.

![#26 View Site Messages](https://i.imgur.com/r2jOsBe.png)
![#27 read messages](https://i.imgur.com/mSjvgL0.png)
![#28  edit message status](https://i.imgur.com/NzvdvfO.png)

#
### Navigation and Responsiveness
#

The site uses a simple Bootstrap responsive navbar. All sections of the site can be reached from here. Logout for an authenticated user, and register/sign in for an unauthenticated user. The navbar menu items can be found within the standard 'hamburger' menu icon on smaller devices.

#
### Future Features
#

The site can be improved with:

* Adding blog section to help with marketing and sharing information between own website and social networks.

* Implement discount/promo functionality

Additionally it would be grate to create profile page to allow users to:

* Creat, View and mange booked appointments
* Receive loyalty points for future discounts

#
## Device and Browser Testing
#

* Chrome developer tools used throughout development to check usability on different devices/sizes.

* Personal devices used to check usability and appearance after deployment Google Pixel 6

* Friends and family asked to check usability on their Apple mobile, laptop, desktop, and tablet devices, particularly to check usability on Safari browser

* Browsers checked were Chrome, Firefox, Edge and Safari

#
### Bugs
#

### Could not build wheels for backports.zoneinfo

After deploying app to Heroku, it was failing to build. After reviewing the logs found error "Could not build wheels for backports.zoneinfo" After some research on Google found solution on Stack Overflow. Solution noted that Heroku fails to install correction python version, to bypass this error a runtime.tx file was created in root directory containing single line of code defining python version for Heroku to install "python-3.8.10".

After this app deployed successfully.

![sign-in](https://i.imgur.com/xedjxGLh.png)
#

### Code Validation

* [W3C HTML Validator](https://validator.w3.org/) found no HTML errors throughout the site - result for home page shown below for a reference.

  ![html-validation](https://i.imgur.com/UXAbocR.png)

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) found no CSS errors throughout my files - result for all CSS shown below.

  ![css-validation](https://i.imgur.com/Iq97bGz.png)

* [JS Hint](https://jshint.com/) found no serious JavaScript errors throughout my files. There were a couple suggested use of dot notation:

* [PEP8 Online](http://pep8online.com/) found no Python errors throughout my files, except for settings.py. This is a known issue with the built-in Django settings file, but it is acceptable not to force a line break here.
  - line too long (>79 characters) - AUTH_PASSWORD_VALIDATORS = [{}] x4

  ![PEP8](https://i.imgur.com/J7B1kfIh.png)

* [Flake8](https://flake8.pycqa.org/en/latest/) Running flake 8 in terminal now only omits warnings for the django backend code and unused django app files which haven't been coded by me.As per mentors advice these lines haven’t been adjusted.

  ![Flake8](https://i.imgur.com/RWK4PWl.png)

### Chrome Dev Tools Lighthouse

Chrome dev tools lighthouse was used to test the site for performance, accessibility, best practices and SEO.

#### Performance

Performance was consistently good throughout all pages, only being slowed down slightly by images (which were already compressed), external embedded YouTube video, and external JavaScript resources such as JQuery.

#### Best Practises

Scored between 92 - 100 on every page.

#### SEO

The SEO score tended to be around 100. Full meta tags were used and considerations made for the text used through out site. External links were added rel="nofollow" attribute.

#### Screenshot from dev tools

I was getting notification warning about Chrome extensions affecting results, even in incognito mode.

![Imgur](https://i.imgur.com/N7CM3Mr.png)

## Technologies Used

### Languages Used

* HTML5
* CSS3
* JavaScript
* Python 3

### Frameworks, Libraries and Programs Used

* [Bootstrap 5.0.2](https://getbootstrap.com/) - Used for responsive layout, flexbox and several components e.g. cards, navbar, form elements.
* [jQuery](https://jquery.com/) - Used for interactive elements on the DOM and to simplify JavaScript use
* [Fontawesome](https://fontawesome.com/) - This was used for all icons on the page
* [Google Fonts](https://fonts.google.com/) - To get fonts
* [Git](https://git-scm.com/) - Used for version control
* [Gitpod](https://gitpod.io/) - Text editor used to write all code
* [Github](https://github.com/) - GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com/) - Used to deploy website - Heroku PostgreSQL used for relational database in deployed site
* [Balsamiq](https://balsamiq.com/) - Used to create the wireframe
* [Compressjpeg](https://compressjpeg.com/) - Used to compress images
* [Google Maps](https://maps.google.com/) - Used to embed maps
* [tabletomarkdown](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/ ) - Used to convert spreadsheet tables to markdown for use in this readme
* [Cloudinary)](https://cloudinary.com/) - Used to store media files

#### Validation Programs Used

* [W3C HTML Validator](https://validator.w3.org/) - Used to validate HTML file
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate CSS file
* [JS Hint](https://jshint.com/) - Used to validate JavaScript code
* [PEP8 Online](http://pep8online.com/) - used to validate Python code
* [Flake8](https://i.imgur.com/RWK4PWl.png) - used to validate Python code in terminal

#
## **Web Marketing**

### **SEO**

The site has been equipped with a sitemap generated [here](https://www.xml-sitemaps.com/) and robots.txt. 

The site also has a Privacy Policy and terms and conditions generated [here](https://www.privacypolicygenerator.info/), linked via the footer.

[Back to top](#)

## **Keywords**

The meta tags and descriptions have been updated for SEO purposes.  The main site does not contain very much copy, other than in the product descriptions and in the yellow block on the home page. 

In order to create the list of keywords for the site, I researched both long and short tail keywords using [wordtracker](https://www.wordtracker.com/) to check volume and comp. scores.

Related Searches at the bottom of the first page of Google proved quite useful for long tail keywords.

I have also looked for keywords was by using Google autocomplete and used [Soolve](https://soovle.com/) which check keyword suggested in other search engines.

### **Newsletter**

Subscribe to the newsletter has been added to the footer of the pages. A customer does not have to be registered in order to sign up for the newsletter via Mailchimp services.

### **Facebook Business page** 

Social media marketing in the form of Facebook or Instagram is a way to become identifiable to the community you are trying to reach.  For this project I had to set up a Facebook page as part of one of the assessment criteria for the project.

Here is a [link to the Facebook business page ](https://www.facebook.com/people/Cyclo-Domestique/100086407539322/).  As per notes, this page may be removed by Facebook at some point because it is not for a real business. Below included a screenshot of the page at time of writing showing both setup and sample post..

![Imgur](https://i.imgur.com/GktW3v4.png)

[Back to top](#)
  
## **Code Validation**

Please see [testing.md](/TESTING.md).

## **Testing**

Please see [testing.md](/TESTING.md).

## **Project Bugs and Solutions**

Please see [testing.md](/TESTING.md).

[Back to top](#)


## **Deployment and making a clone**

### **Deployment to Heroku**

**In your app** 

1. add the list of requirements by writing in the terminal "pip3 freeze --local > requirements.txt"
2. Git add and git commit the changes made

**Log into heroku**

3. Log into [Heroku](https://dashboard.heroku.com/apps) or create a new account and log in

4. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

5. Write app name - it has to be unique, it cannot be the same as this app
6. Choose Region - I am in Europe
7. Click "Create App"

**The page of your project opens**

8. Go to Resources Tab, Add-ons, search and add Heroku Postgres

9. Choose "settings" from the menu on the top of the page

10. Go to section "Config Vars" and click button "Reveal Config Vars". 

11. Add the below variables to the list

    * Database URL will be added automatically
    * Secret_key - is the djnago secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 

**Go back to your code**

12. Procfile needs to be created in your app
```
web: gunicorn PROJ_NAME.wsgi
```

13. In settings in your app add Heroku to ALLOWED_HOSTS

14. Add and commit the changes in your code and push to github

**Final step - deployment**

15. Next go to "Deploy" in the menu bar on the top 

16. Go to section "deployment method", choose "GitHub"

17. New section will appear "Connect to GitHub" - Search for the repository to connect to

18. type the name of your repository and click "search"

19. once Heroku finds your repository - click "connect"

20. Scroll down to the section "Automatic Deploys"

21. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy

22. Click "Deploy branch"

Once the program runs:
You should see the message "the app was successfully deployed"

23. Click the button "View"

The live link can be found [here](https://cyclo-domestique.herokuapp.com/).

### Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/EdgarasSp/cyclo-domestique-storefront)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/EdgarasSp/cyclo-domestique-storefront)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open commandline interface on your computer
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/EdgarasSp/cyclo-domestique-storefront
```

7. Press Enter. Your local clone will be created.

### Setting up your local environment

1. Create Virtual environment on your computer or use gitpod built in virtual environment feature.

2. Create env.py file. It needs to contain those 5 variables.

* Database URL can be obtained from [heroku](https://dashboard.heroku.com/), add PostgreSQL as an add on when creating an app. 
* Secret_key - is the django secret key can be generated [here](https://miniwebtool.com/django-secret-key-generator/). 
* Cloudinary URL can be obtained from [cloudinary](https://cloudinary.com/) follow the steps on the website to register. 
* Google API key can be obtained [here](https://cloud.google.com/gcp?authuser=1) you will have to register with google and create new app to get the API key. Follow the instructions on the website.

```
DEVELOPMENT
SECRET_KEY
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY 
STRIPE_WH_SECRET
```
PostgreSQL and AWS keys are needed only on Heroku, not in local IDE

3. Run command 
```
pip3 install -r requirements.txt
```
### Getting Stripe keys
Go to developers tab. On side menu you will find API keys. Copy STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY.

Go to Webhooks. Click Add Endpoint button in top right hand corner.
Add endpoint URL (your local or deployed URL)
Add all events 
Than click add endpoint
You should be redirected to this webhook's page. Reveal webhook sign in secret and copy to Settings and to heroku as STRIPE_WH_SECRET variable

### Getting email variables from gmail

- Log into gmail account
- Go to Settings and than See all settings
- Top menu go to Accounts and import
- Find on the list Other google account settings
- Left side menu - Security
- Turn on two step verification: add phone number and follow instructions
- Go back to security
App passwords - Select Mail, Select Device - Other, Django, Copy app password.

In Heroku 
EMAIL_HOST_PASS is the password copied from above.
EMAIL_HOST_USER is the gmail email address

### Setting AWS bucket

1. Go to [Amzon Web Services](https://aws.amazon.com/) page and login or register

2. You should be redirected to AWS Management Console, if not click onto AWS logo in top left corner or click Services icon and choose Console Home

3. Below the header AWS Services click into All Services and find **S3** under Storage

4. Create New Bucket using **Create Bucket** button in top right hand corner

- **Configuration:** type in your chosen name for the bucket (preferably matching your heroku app name) and AWS Region closest to you

- **Object ownership:** ACLs enabled, Bucket owner preferred

- **Block Public Access settings:** Uncheck to allow public access, Acknowledge that the current settings will result that the objects within the bucket will become public

- Click **Create Bucket**

5. You are redirected to Amazon S3 with list of your buckets. Click into the name of the bucket you just created

6. Find the tab **Properties** on the top of the page:
**Static website hosting** at the bottom of the properties page: click to edit, click enable, fill in index document: index.html and error.html for error

7. On the **Permissions** tab:
- Cross-origin resource sharing (**CORS**) Paste in the below code as configuration and save

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```
- **Bucket Policy** within permissions tab: Edit bucket policy
Click AWS Policy Generator (top right corner)

Select type of policy: S3 Bucket policy
Principal: * (allows all)
Actions: Get object
Amazon Resource Name (ARN): paste from the Edit bucket policy page in permissions
Click Add statement Than Click Generate Policy and Copy the policy into bucket policy editor. 
In the policy code find "Resource" key and add "/*" after the name of the bucket to enable all
Save changes

- **Access control list (ACL)** within permissions tab: click Edit

find Everyone (public access) and check List box and save

8. Identity and Access Management (IAM)
Go back to the AWS Management Console and find IAM in AWS Services

- side menu - User Groups and click **Create Group**
name group "manage-your-app-name" and click Create group

- side menu - Policies and click **Create Policy**
Click import managed policy - find AmazonS3FullAccess
Copy ARN again and paste into "Resource" add list containing two elements "[ "arn::..", ""arn::../*]" First element is for bucket itself, second element is for all files and folders in the bucket

Click bottom right Add Tags, than Click bottom right Next: Review
Add name of the policy and description

Click bottom right Create policy

9. Attach policy to the group we created:
- go to User Groups on side menu
- select your group from the list
- go to permissions tab and add permissions drop down and choose **Attach policies**
- find the policy created above and click button in bottom right Add permissions

10. Create User to go in the group
- **Users** in the side menu and click add users

User name: your-app-staticfiles-user
Check option: Access key - Programmatic access
Click button at the bottom right for Next
- Add user group and add user to the group you created earlier
Click Next Tags and Next: review and Create user
- Download .csv file

11. Connect django to AWS S3 bucket
- install boto3
- install django-storages
- freeze to requirements.txt
- add storages to installed apps in settings.py

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

12. Go to heroku to set up enviromental variables

open CSV file downloaded earlier and copy each variable into heroku Settings

AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID from csv
AWS_SECRET_ACCESS_KEY from csv
USE_AWS = True
remove DISABLE_COLLECTSTATIC variable from heroku

13. Create file in root directory custom_storages.py

```
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```

14. Go to settings.py, add the AWS settings

```
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

15. To load the media files to S3 bucket

- Go to your S3 bucket page on AWS. Create new folder "media"
- go to the media folder and click Upload

## Credits

### Code

The project is influenced by the Code Institute Django tutorial series. These were the most efficient and obvious ways to implement the necessary functionality in my project.

### Content and Images

* The  images used for the webpage were all taken from the official [Pexels](https://www.pexels.com/) website. Images I used are stored in my [Pexels collection](https://www.pexels.com/collections/beauty-wkxbc8d/) with appropriately credits.

* Video was also take from [Pexels](https://www.pexels.com/) and found inside [Pexels collection](https://www.pexels.com/collections/beauty-wkxbc8d/). For embedding to the site I have hosted it on YouTube.

* Also would like to credit my sister in law as she is a hair dresser and helped with some text content.

### Acknowledgements

* [W3 Schools](https://www.w3schools.com/)
* [Stackoverflow](https://stackoverflow.com/)
* [Bootsrap](https://getbootstrap.com//)
* [Django Documentation](https://docs.djangoproject.com/en/3.2/)
* [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)