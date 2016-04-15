# AmritaToday
AmritaToday is an Android based application which connects the people in Amrita in the most essential ways possible. This repository contains the source code of the application's RESTful API.

1. Canteen Menu APIs - A crowdsource based implementation for anyone in Amrita to see and post data about the present items availabe in all 3 canteens.(v1.0 implemented)
2. Clubs@Amrita - Enables everyone to view the upcoming events by various clubs at Amrita. Also provides heads of clubs to create new events.(v1.0 implemented)
3. Buy/Sell@Amrita - Buy/Sell things at Amrita. No money transactions, only details and contact. (Yet to be implemented)

# Tech
AmritaToday's backend is built using the python web framework Flask. It is current hosted on Heroku (free plan). It uses the PostgreSQL for its database.

# API Reference
1. Canteen Menu APIs:
  To get list of items availabe in the canteens, send a GET request to

  >https://amritatoday.herokuapp.com/api/v1.0/menu/main
  
  >https://amritatoday.herokuapp.com/api/v1.0/menu/mba
  
  >https://amritatoday.herokuapp.com/api/v1.0/menu/it
  
2. Club Event APIs:
  To get list of events posted by various clubs at Amrita, send a GET request to

  Retrieves the list of clubs:
  
  >https://amritatoday.herokuapp.com/api/v1.0/clubs

  Retrieves all events:
  
  >https://amritatoday.herokuapp.com/api/v1.0/events
  
  Retrieves events of specific clubs:
  ```
  https://amritatoday.herokuapp.com/api/v1.0/events?club=clubname
  ```
  
  >Eg: https://amritatoday.herokuapp.com/api/v1.0/events?club=Srishti
  
  >Eg: https://amritatoday.herokuapp.com/api/v1.0/events?club=Srishti&club=Sahaya
  
  Create New events:

  To create new events, send a POST request to:
  
  >https://amritatoday.herokuapp.com/api/v1.0/events
  
  with body:

  ```
  {
        "club": "clubname", 
        "event": "eventname",
        "description": "event description",
        "date": "event start date & time",  eg: 2016-04-12 04:00 PM
        "end_date": "event end date & time", eg: 2016-04-12 06:00 PM
        "venue": "AM Hall"
  } 
  ```
  Eg:
  ```
  {
        "club": "Srishti", 
        "event": "Mime",
        "description": "Fun and Frolic!",
        "date": "Tue, 12 Apr 2016 07:00:00 GMT", 
        "end_date": "Fri, 15 Apr 2016 07:00:00 GMT", 
        "venue": "AM Hall"
  } 
  ```



3.  Buy/Sell APIs:

    To buy and sell items - for people at Amrita.
    
    To retrieve list of items put for sale, send a GET request to:
    
    >https://amritatoday.herokuapp.com/api/v1.0/buy
    
    To post for a sale a new item, send a POST request to:
    
    >https://amritatoday.herokuapp.com/api/v1.0/sell
    
    with body:
    
  ```
    {

    "item": "itemname",
    "category": "category",
    "price": price in rs,
    "orig_price": price in rs,
    "description": "Why do you want to sell this?",
    "email": "seller's email id",
    "phone": "sellers phone number"

    }
  ```
    Eg:
    
  ```
    {

    "item": "Shirt",
    "category": "Clothes",
    "price": 500,
    "orig_price": 1000,
    "description": "I got big!",
    "email": "vishaag@gmail.com",
    "phone": "9876543210"

    }
  ```

