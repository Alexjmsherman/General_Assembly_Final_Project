## Project Question

**What factors correlate with a seller's listed price for online housing listings?**

## Data

I will use craigslist listings as the core data set. Craigslist listings are fairly structured & include the following data:
   
#### Housing Description:
      -Seller's listed price
      -Listing Title
      -Listing Text
#### Housing Attributes:
        {'availability': u'available now',
         'bathroom': u' 1',
         'bedroom': u'1 ',
         'cat': u'cats are OK - purrr',
         'data_available': u'2015-04-15',
         'dog': u'dogs are OK - wooof',
         'housing_type': u'apartment',
         'laundry': u'w/d in unit',
         'parking': u'attached garage',
         'smoking': u'no smoking',
         'square_footage': u'763'}
#### Location Data
        {'address': u'123 Random Street',
         'city': u'Arlington',
         'country': u'US',
         'latitude': u'11.111111',
         'location_data_accuracy': u'10',
         'longitude': u'-22.222222',
         'state': u'VA'}
#### Image data
        -number of images
        -size of each image (e.g. 600X450.jpg)
        -image link

## Notes on the Data
Using the above data, I will model the association between the various inputs and the listed price. My metric of success will be to create a model that can predict the listed sales price with 20%, provided the other data points from a listing.

Craiglist does not provide sales data, so the question is more a metric of user confidence than actual housing value - The listed price may not equal the actual sales amount.  

My initial data set will consist of the craigslist housing attributes in the Washington, DC market; however, I may explore the location and image data as well as expand to other dataset. Some corollary questions of interest include:


* Can i use the latitude and longitude to determine nearby landmarks that may relate to housing value (e.g. metro proximity)?
* Using natural language processing, can I determine important phrases in the listing text and what role sentiment plays in user confidence
* Using image processing, can I discover important attributes of the gallery image (the image listed as a thumbnail before a user clickcs on the listing)
* Expanding the dataset to other markets, how does the importance of attributes differ across the Uniterd States?
* Expanding the dataset to other housing listing websites (e.g. Trulia, apartments.com, padmapper), how do listing prices change across mediumns for similar houses.
    
    
## Why this Topic
I have selected this topic as I am currently searching for a new apartment, and I hope to use this model to optimize my search and get the best value for my money.

Additionally, the topic has potential to expand to many intersting data science topics:

* web scraping
* geolocation analysis
* NLP / sentiment analysis
* Image processing
    

