# Lix
Lix is a script that scans for broken links on the Pybit.es articles!
It's currently in a very premature alpha-form, but will be turned into a tool (patience, young padawans).

*Known Issues*
* False 404 reports for twitter links that have @handles. (Probably encoding)
* Only checks if status != 200.
  * Other statuses can be valid aswell
  * Might wanna follow redirects?
* Very Limited exception handling, while it's pretty important for the purpose.

But it works!

**Requirements**

See requirements.txt

*Example Output*

```
Running article: A Python Orientation - How to Get Started
         ==> No 200 for https://pythonhosted.org/behave/, instead got 404
Running article: How Promotions work in Large Corporations
Running article: Why Python is Great for Test Automation
         ==> No 200 for http://docs.python-requests.org/en/master/, instead got 404
Running article: My Anaconda Workflow: Python environment and package management made easy
         ==> No 200 for https://anaconda.org/, instead got 403
Running article: Watch Me Code - Solving Bite 21. Query a Nested Data Structure
Running article: Why Python is so popular in Devops?
         ==> No 200 for http://docs.python-requests.org/en/master/, instead got 404
```

