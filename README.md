Limeade
=======

[![Build Status](https://travis-ci.org/tsharman/limeade.png?branch=master)](https://travis-ci.org/tsharman/limeade)

Limeade is a webapp that aggregates music videos from some blogs across the web. You can check out the live site [here](http://limeade.co/).

This is a fairly simple project that I started working on to explore a new stack.

The actual Limeade app is in the folder limeade. 

If you are in the root directory start the virtualenv, install the requirements in requirements.txt and use foreman start to run it.

Limeade is built with the following components:

#### Client-facing web app

* [Tornado](http://www.tornadoweb.org/en/stable/)

* [MongoDB](http://www.mongodb.org/)

* [LESS](http://lesscss.org/)

* [handlebars](http://handlebarsjs.com/)

#### Web crawlers

The web crawlers use a combination of [Requests](http://docs.python-requests.org/en/latest/) and [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) to parse the response and extract the relevant data.


### Roadmap

There are some major things that need to be implemented in Limeade. Here is a high level list of what I have planned.

* <del>Title search. Search through all blog posts by title.</del>
* Artist based search. See all the music videos blogs have posted about an artist.
* Blog based search. See all music videos a blog has posted.
* Keyboard controls.

