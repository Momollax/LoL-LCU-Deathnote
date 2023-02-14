# LoL-LCU-Deathnote

Hello there !

This is a simple tool that allow you to report a person, only by enter his nickname.
You can report him even if you never play with him.
an account is able to report a person only once per hour.


## How to use it ?
requirements:   - python  (download: https://www.python.org/downloads/)
                - pip     (download: https://pip.pypa.io/en/stable/installation/)

git clone the project:
https://github.com/NoeMoyen/LoL-LCU-Deathnote.git

install library:
pip install lcu_driver

modify the report reason in the script line 26:
"comment": "[reported by DeathNote.py]",
with something like:
"comment": "Player afk, don't whant to play, troll, etc..."

run the script:
python deathnote.py

enter the summoner name you want to report

and voila !


# How it works ?

The script is using the LCU API to connect to your league client.
When you enter a summoner name, i will find the summoner id and the summoner uuid. 
With this, i will find his 21 lasts games, and extract the last game id he played.
with all this information, i will be able to report him.
then i wait 1 hour before being able to report him again.

if you have any question, feel free to ask me :)

Discord: Momolly#7525