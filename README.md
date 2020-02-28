# Lix
Lix is a script that scans for broken links on the Pybit.es articles!

**Requirements**

See requirements.txt

**Usage**

`python lix.py`

`python lix.py -i 200`

`python lix.py -i 200,201,301`

*Example Output*

```

(venv) E:\Users\Jarvis\PycharmProjects\Lix>python lix.py
[~] Article: How to Write a Guest Article for PyBites
        [OK] https://pybit.es/author/cedric-sambre.html => Seems good!
        [OK] https://pybit.es/category/tools.html => Seems good!
        [OK] https://github.com/pybites/pybites.github.io-src/ => Seems good!
        [OK] https://github.com/pybites/pybites.github.io-src/tree/master/content => Seems good!
        [NOTFOU] https://github.com/pybites/pybites.github.io-src/templates => Not found :(
        [OK] https://github.com/pybites/pybites.github.io-src/tree/master/templates => Seems good!
[*] Exiting because of CTRL+C!

(venv) E:\Users\Jarvis\PycharmProjects\Lix>python lix.py -i 200
[~] Article: How to Write a Guest Article for PyBites
        [NOTFOU] https://github.com/pybites/pybites.github.io-src/templates => Not found :(
[*] Exiting because of CTRL+C!

```
