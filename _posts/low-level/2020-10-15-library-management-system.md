---
layout: post
title: "Design a Library Management System"
author: "Rajat Srivastava"
categories: low-level-designs
tags: [design]
image: library/page.jpg
folder: library
---

A Library Management System is a software built to handle the primary housekeeping functions of a library. Libraries rely on library management systems to manage asset collections as well as relationships with their members. Library management systems help libraries keep track of the books and their checkouts, as well as members’ subscriptions and profiles.

Library management systems also involve maintaining the database for entering new books and recording books that have been borrowed with their respective due dates.

---
## System Requirements
We will focus on the following set of requirements while designing the Library Management System:
1. Any library member should be able to search books by their title, author, subject category as well by the publication date.
2. Each book will have a unique identification number and other details including a rack number which will help to physically locate the book.
3. There could be more than one copy of a book, and library members should be able to check-out and reserve any copy. We will call each copy of a book, a book item.
4. The system should be able to retrieve information like who took a particular book or what are the books checked-out by a specific library member.
5. There should be a maximum limit (5) on how many books a member can check-out.
6. There should be a maximum limit (10) on how many days a member can keep a book.
7. The system should be able to collect fines for books returned after the due date.
8. Members should be able to reserve books that are not currently available.
9. The system should be able to send notifications whenever the reserved books become available, as well as when the book is not returned within the due date.
10. Each book and member card will have a unique barcode. The system will be able to read barcodes from books and members’ library cards.

---
## Use Case Diagrams
We have three main actors in our system:

- **Librarian:** Mainly responsible for adding and modifying books, book items, and users. The Librarian can also issue, reserve, and return book items.
- **Member:** All members can search the catalog, as well as check-out, reserve, renew, and return a book.
- **System:** Mainly responsible for sending notifications for overdue books, canceled reservations, etc.

Here are the top use cases of the Library Management System:

- **Add/Remove/Edit book:** To add, remove or modify a book or book item.
- **Search catalog:** To search books by title, author, subject or publication date.
- **Register new account/cancel membership:** To add a new member or cancel the membership of an existing member.
- **Check-out book:** To borrow a book from the library.
- **Reserve book:** To reserve a book which is not currently available.
- **Renew a book:** To reborrow an already checked-out book.
- **Return a book:** To return a book to the library which was issued to a member.

![Use Case]({{ site.github.url }}/assets/img/{{ page.folder }}/use-case.png)

---
## Class Diagrams
Here are the main classes of our Library Management System:

- **Library:** The central part of the organization for which this software has been designed. It has attributes like ‘Name’ to distinguish it from any other libraries and ‘Address’ to describe its location.
- **Book:** The basic building block of the system. Every book will have ISBN, Title, Subject, Publishers, etc.
- **BookItem:** Any book can have multiple copies, each copy will be considered a book item in our system. Each book item will have a unique barcode.
- **Account:** We will have two types of accounts in the system, one will be a general member, and the other will be a librarian.
- **LibraryCard:** Each library user will be issued a library card, which will be used to identify users while issuing or returning books.
- **BookReservation:** Responsible for managing reservations against book items.
- **BookLending:** Manage the checking-out of book items.
- **Catalog:** Catalogs contain list of books sorted on certain criteria. Our system will support searching through four catalogs: Title, Author, Subject, and Publish-date.
- **Fine:** This class will be responsible for calculating and collecting fines from library members.
- **Author:** This class will encapsulate a book author.
- **Rack:** Books will be placed on racks. Each rack will be identified by a rack number and will have a location identifier to describe the physical location of the rack in the library.
- **Notification:** This class will take care of sending notifications to library members.

![Class Diagram]({{ site.github.url }}/assets/img/{{ page.folder }}/class-diagram.png)

![UML Conventions]({{ site.github.url }}/assets/img/uml.svg)

---
## Activity diagrams

- **Check-out a book:** Any library member or librarian can perform this activity. Here are the set of steps to check-out a book:
![Activity Checkout]({{ site.github.url }}/assets/img/{{ page.folder }}/activity-checkout.svg)

- **Return a book:** Any library member or librarian can perform this activity. The system will collect fines from members if they return books after the due date. Here are the steps for returning a book:
![Activity Return]({{ site.github.url }}/assets/img/{{ page.folder }}/activity-return.png)

- **Renew a book:** While renewing (re-issuing) a book, the system will check for fines and see if any other member has not reserved the same book, in that case the book item cannot be renewed. Here are the different steps for renewing a book:
![Activity Renew]({{ site.github.url }}/assets/img/{{ page.folder }}/activity-renew.svg)

---
## Code
Here is the code for the use cases mentioned above: 1) Check-out a book, 2) Return a book, and 3) Renew a book.

Note: This code only focuses on the design part of the use cases. Since you are not required to write a fully executable code in an interview, you can assume parts of the code to interact with the database, payment system, etc.

- **Enums and Constants:** Here are the required enums, data types, and constants:

{% include codetab.html btnClass="enums" %}

- **Account, Member, and Librarian:** These classes represent various people that interact with our system:

{% include codetab.html btnClass="accounts" %}

- **BookReservation, BookLending, and Fine:** These classes represent a book reservation, lending, and fine collection, respectively.

{% include codetab.html btnClass="reservation" %}

- **BookItem:** Encapsulating a book item, this class will be responsible for processing the reservation, return, and renewal of a book item.

{% include codetab.html btnClass="book" %}

- **Search interface and Catalog:** The Catalog class will implement the Search interface to facilitate searching of books.

{% include codetab.html btnClass="search" %}