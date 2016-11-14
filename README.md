# URL Checker

Checks what suffixes are reserved for a certain url.
For example if checked url is www.google there would be at least
www.google.com, www.google.fi and www.google.se in the results.
Results are stored in results.txt

Usage:

If you have Python just run src/main.py, use existing command line since the app just closes after it's done.

Example:

User types: 
* www.google

Results include
* www.google.com
* www.google.fi

But exclude:
* www.google.xxx



# Known bugs:
* Response to ping doesn't always mean that the site has some content