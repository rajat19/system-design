---
layout: post
title: "Design Amazon - Online Shopping System"
author: "Rajat Srivastava"
categories: case_study
tags: [design]
image: shopping/page.png
codeFolder: shopping
---

[Amazon](https://amazon.com) is the world’s largest online retailer. The company was originally a bookseller but has expanded to sell a wide variety of consumer goods and digital media. For the sake of this problem, we will focus on their online retail business where users can sell/buy their products.

---
## System Requirements
We will be designing a system with the following requirements:
1. Users should be able to add new products to sell.
2. Users should be able to search for products by their name or category.
3. Users can search and view all the products, but they will have to become a registered member to buy a product.
4. Users should be able to add/remove/modify product items in their shopping cart.
5. Users can check out and buy items in the shopping cart.
6. Users can rate and add a review for a product.
7. The user should be able to specify a shipping address where their order will be delivered.
8. Users can cancel an order if it has not shipped.
9. Users should get notifications whenever there is a change in the order or shipping status.
10. Users should be able to pay through credit cards or electronic bank transfer.
11. Users should be able to track their shipment to see the current state of their order.

---
## Use Case Diagrams
We have four main Actors in our system:

- **Admin:** Mainly responsible for account management and adding or modifying new product categories.
- **Guest:** All guests can search the catalog, add/remove items to the shopping cart, as well as become registered members.
- **Member:** Members can perform all the activities that guests can, in addition to which, they can place orders and add new products to sell.
- **System:** Mainly responsible for sending notifications for orders and shipping updates.

Here are the top use cases of the Online Shopping System:
1. Add/update products; whenever a product is added or modified, we will update the catalog.
2. Search for products by their name or category.
3. Add/remove product items in the shopping cart.
4. Check-out to buy product items in the shopping cart.
5. Make a payment to place an order.
6. Add a new product category.
7. Send notifications to members with shipment updates.

![Use Case]({{ site.github.url }}/assets/img/shopping/use-case.svg)

---
## Class Diagrams
Here are the descriptions of the different classes of our Online Shopping System:

- **Account:** There are two types of registered accounts in the system: one will be an Admin, who is responsible for adding new product categories and blocking/unblocking members; the other, a Member, who can buy/sell products.
- **Guest:** Guests can search for and view products, and add them in the shopping cart. To place an order they have to become a registered member.
- **Catalog:** Users of our system can search for products by their name or category. This class will keep an index of all products for faster search.
- **ProductCategory:** This will encapsulate the different categories of products, such as books, electronics, etc.
- **Product:** This class will encapsulate the entity that the users of our system will be buying and selling. Each Product will belong to a ProductCategory.
- **ProductReview:** Any registered member can add a review about a product.
- **ShoppingCart:** Users will add product items that they intend to buy to the shopping cart.
- **Item:** This class will encapsulate a product item that the users will be buying or placing in the shopping cart. For example, a pen could be a product and if there are 10 pens in the inventory, each of these 10 pens will be considered a product item.
- **Order:** This will encapsulate a buying order to buy everything in the shopping cart.
- **OrderLog:** Will keep a track of the status of orders, such as unshipped, pending, complete, canceled, etc.
- **ShipmentLog:** Will keep a track of the status of shipments, such as pending, shipped, delivered, etc.
- **Notification:** This class will take care of sending notifications to customers.
- **Payment:** This class will encapsulate the payment for an order. Members can pay through credit card or electronic bank transfer.

![Class Diagram]({{ site.github.url }}/assets/img/shopping/class-diagram.png)

![UML Conventions]({{ site.github.url }}/assets/img/uml.svg)

---
## Activity Diagram
Following is the activity diagram for a user performing online shopping:
![Activity Shopping]({{ site.github.url }}/assets/img/shopping/activity-shopping.svg)

---
## Sequence Diagram
1. Here is the sequence diagram for searching from the catalog:
![Sequence Searching]({{ site.github.url }}/assets/img/shopping/sequence-searching.svg)

2. Here is the sequence diagram for adding an item to the shopping cart:
![Sequence Adding]({{ site.github.url }}/assets/img/shopping/sequence-adding-items.svg)

3. Here is the sequence diagram for checking out to place an order:
![Sequence Checkout]({{ site.github.url }}/assets/img/shopping/sequence-check-out.svg)

---
## Code
Here is the high-level definition for the classes described above.

- **Enums and Constants:** Here are the required enums, data types, and constants:

{% include codetab.html btnClass="enums" %}

- **Account, Customer, Admin, and Guest:** These classes represent different people that interact with our system:

{% include codetab.html btnClass="accounts" %}

- **ProductCategory, Product, and ProductReview:** Here are the classes related to a product:

{% include codetab.html btnClass="product" %}

- **ShoppingCart, Item, Order, and OrderLog:** Users will add items to the shopping cart and place an order to buy all the items in the cart.

{% include codetab.html btnClass="cart" %}

- **Shipment, ShipmentLog, and Notification:** After successfully placing an order, a shipment record will be created:

{% include codetab.html btnClass="shipment" %}

- **Search interface and Catalog:** Catalog will implement Search to facilitate searching of products.

{% include codetab.html btnClass="search" %}