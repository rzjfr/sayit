# Sayit
Pronouncing given word using Oxford Advanced Learner's Dictionary website.  

``` bash
# Ubuntu
sudo apt install libgirepository1.0-dev
pip install -e .
```

run from command line:
``` bash
sayit hello
```
or just copy as `sayit` somewhere in your path and use it with goldendict:
- Edit -> Dictionaries -> Programs.
- choose "Audio" in type field.
- in "Command Line" field copy and paste this command:
``` bash
sayit %GDWORD%
```
- write "sayit" in "Name" field.
