# Sound Store
Sound Store is an e-commerce website which offers a range of different types of musical instruments and accessories. Users can create an account.

# Design:
## Colours:
The main colours on the site were taken from the Coolors app (https://coolors.co/). 
These are:
1. Dark blue colour = #011627 
2. White colour = #FDFFFC
3. Red Colour = #E71D36
4. Orange colour = #FF9F1C
5. Dark grey colour = #122C34
6. Light blue colour, for :hover/:focus effect = #36597D

# Technologies Used:
## Programming languages and frameworks used:
1. Html, Css, JavaScript and Python
2. The Python framework Django was used to build the site.
3. The bootstrap framework was used  
1. Favicon (https://favicon.io/favicon-generator/) - To get icon for the sites tab.
2. Font Awesome (https://fontawesome.com/v4.7/icons/) - To get icons for social media / shopping cart etc.
3. Google Fonts - (https://fonts.google.com/) - To get letter styling fonts for the site.


# Bugs Encountered
## Webhooks
1. When attempting to send webhook test events, I was receiving a result of "Test webhook error:401". This was fixed by opening up the ports tab in Gitpod and making the 8000 port public.
2. On another occasion while trying to send a test webhook, I was receiving a result of "Test webhook error:404". This was fixed by updating the region code, i.e. "...eu(number)..." in the gitpod workspace url. This number appeared to change somewhat regularly and so needed to be updated in the stripe endpoint url in the stripe dashboard. 
3. Due to the superuser being created at the beginning of development before the profiles app was created, the profiles app did not recognise the superuser name and threw an error 404 screen in response to my attempting to login to admin. This was fixed by commenting out the 'if created:' statement in the profiles.models file... {show picture} ... , logging in with the superuser name and password, and then uncommenting the code. On both the commenting and uncommenting of the 'if' statement, the line inside was indented appropriately in order for the code to work.
## Deployment
1. When trying to load my db.json file to my postgres account I was encountering this result in the console. // Show picture here. To fix this I used a json formatter to make the file easier to read and then with advice from slack I identified where in the file a full country name was used instead of a two letter name which the installed 'CountryField' requires. I opened up my db.json file, found these full country names and changed them to two letter names instead and this fixed the issue.
2. Again when trying to upload this db.json file I received this message // Show picture here. A suggestion seen on Slack suggested to upload the json file without any user information. So I identified, again using the json formatter, where this data was and deleted it. I then uploaded this file to postgres using 'python3 manage.py loaddata db.json' and the products and categories showed up in the site as expected.


# Credits
## Photos:
### Carousel images on index.html
1. Guitar store image taken from https://www.westwoodmusic.com (https://www.westwoodmusic.com/wp-content/uploads/2014/12/sales-floor.jpg) 
2. Other guitar store image taken from https://www.montreal360virtualtour.com/ (https://www.montreal360virtualtour.com/wp-content/uploads/2017/12/Steve_s-Music-Store-15.jpg)
3. Drum store taken from https://www.expressmusic.co.uk (https://www.expressmusic.co.uk/images/store/cov%208_rs.jpg)

### Category Images on index.html
1. Drum set taken from https://www.explorersdrums.com (https://www.explorersdrums.com/assets/images/ACCENTRED.jpg).
2. Guitar taken from https://www.richtonemusic.co.uk (http://images.richtonemusic.co.uk/product/MARTINHD-28-REIMAGINEDb.jpg).
3. Bass guitar taken from https://www.gear4music.com (https://d1aeri3ty3izns.cloudfront.net/media/26/262795/1200/preview.jpg).
4. Trumpet taken from https://www.discoversinging.co.uk (https://i2.wp.com/www.discoversinging.co.uk/wp-content/uploads/2013/08/trumpet.jpg).
5. Viola taken from https://www.victoriabuzz.com (https://www.victoriabuzz.com/wp-content/uploads/2017/12/56386c126c656484fa101f680f7e111e.jpg).
6. Microphone taken from https://www.musicstorelive.com (https://media.musicstorelive.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/a/samsn-r21s_1.jpg)