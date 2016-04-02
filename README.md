# AmritaToday
AmritaToday as an Android based application which connects the people in Amrita in the most essential ways possible. This repository contains the source code of the application's RESTful API.

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

  Retrieves the list of clubs
  
  >https://amritatoday.herokuapp.com/api/v1.0/clubs

  Retrieves all events:
  
  >https://amritatoday.herokuapp.com/api/v1.0/events
  
  Retrieves events of specific clubs:
  
  >https://amritatoday.herokuapp.com/api/v1.0/events?club=clubname
  
  >Eg: https://amritatoday.herokuapp.com/api/v1.0/events?club=Srishti
  
  >Eg: https://amritatoday.herokuapp.com/api/v1.0/events?club=Srishti&club=Sahaya
