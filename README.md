Limeade
=======

Limeade is a webapp that aggregates music videos from some blogs across the web. You can check out the live site [here](http://limeade.co/).

This is a fairly simple project that I started working on to explore a new stack.

The actual Limeade app is in the folder limeade. You will not be able to deploy the app as is. Make sure you enter the folder, create a git repo and push from there.

Its built with the following components:

#### Client-facing web app

* [Tornado](http://www.tornadoweb.org/en/stable/)

* [MongoDB](http://www.mongodb.org/)

* [LESS](http://lesscss.org/)

* [handlebars](http://handlebarsjs.com/)

#### Web crawlers

The web crawlers use a combination of the Requests library and BeautifulSoup to parse the response and extract the relevant data.


