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

once all that is done you should be able to run the file ChatRangler.py
follow the cmd prompts to get going

if your controller is not a ps4 or an xbox360
then you will need to create a mapping for the controller to function

mapping a controller:
you can choose to either run the generator tool or code the map yourself inside the StoredMappings.py file
- make sure chatrangler is not running
- plug in the controller you want to map
- run MapGenerator.py
- type the index of the controller from the list of recognized controllers
mapping each button
- press any button to choose how it gets mapped
  - type the xbox controller button you want to map onto
  - type the name of the conversion you wish to use, this allows the programm to convert buttons to axes, axes to buttons, or invert an axis, 
- once you are are done inputing the mappings you need to name the mapping
  - if you type the name of the controller you saw when selecting what controller to map you can put this map into CONTROLLER_AUTO_CONNECTS at the top of ChatRangler.py so that when this controller is connected it gets automatically selected
- you can now choose to either manually copy and paste the map or let the code do it for you
if you have issues with the mapping or wish to delete it go into the StoredMappings.py file and delete the autogenerated mapping and its corisponding dictionary element
you can also manually change the values of the mappings if you feel so brave


