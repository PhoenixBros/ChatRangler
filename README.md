Description:
Chat Wrangler is a program that combines the inputs from chat and a lugged in controller.
The result is a fun and chaotic way to play games while streaming.
In my experience, as a small streamer, it leads to a game of fighting off the occasional malicious input.
But i would expect that if your stream has enough viewers the experience will change drastically.
And it would lead to an experience like herding cats.


Backstory:
This program was born from a few of my old projects i made while watching dougdoug.
I combined some twitch plays code with some code that used virtual inputs, and with code that mapped controller inputs.
But at that time it was just 3 different programs screaming at each other.
So i decided to compile a singular program to do only the chat wrangling. 


dependencies:
- pygame - pip install pygame
- vgamepad - pip install vgamepad
- dougdougs twitch connection code - https://github.com/DougDougGithub/TwitchPlays only the connection code is needed, you can substitute the file with any twitch plays file you have but change the imports in chatrangler.py


make sure you download dougdougs twitch connection code to the chatrangler folder. 
you only need the file called: TwitchPlays_Connection.py


settup:
Download the files individually or the repo as a whole.
install the needed libraries: 
  - pip install pygame
  - pip install vgamepad
  - dowload TwitchPlays_Connection.py from https://github.com/DougDougGithub/TwitchPlays
    - pip install requests
Once you have this repo downloaded and the dependencies installed.
Download dougs 
Just run the file named ChatRangler.py in python 3.9 or higher
The cmd line prompts should guide you through from there


if you need to create a new mapping for the controller you are using or make a bizarre one you can write it youself or run the MapGenerator.p file to create one
