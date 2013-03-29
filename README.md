# FAiler

## It's the FurAffinity Filer or FAiler for short!
FAiler is a pep defying name for FurAffinity parsing tools.
It is designed to help you parse out files and urls from the popular furry service much like the API it doesn't have.
FAiler is not an application, applet, or app anythting. It is a light framework to help you manage files and urls from the site.

## Usage
- Install the failer directory into the path of your stubs or scripts
- Import into your own scripts just like in the examples below
- ???
- Don't profit[^AUP].

[^AUP]: You may not profit from your hard work or even share it cause that's against the [Terms of Service (TOS) | Fur Affinity Help and Support](http://help.furaffinity.net/article/AA-00203/8/Terms-of-Service-TOS.html)

## Classes
### FAile
This file parser class takes the files downloaded from FA, either by name or path to and parses them, returning a workable object you can extend or parse pragmatically.
It is hightly recommended to read the docstrings since it is hightly explanitory and contains usecases.
It is basically an overglorified struct


### FAurl
Ever wonder what is in that link before you click it? FAurl has you.
This class requires [mechanize](http://wwwsearch.sourceforge.net/mechanize/) and [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/). This hypothetically makes it slightly less fragile against site changes than if I had done the entire thing in urllib and re.

Again reading the comments is vital, please note that when you init a new object it does it's internet calls.
