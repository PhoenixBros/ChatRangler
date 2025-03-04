# This program uses pygame, vgamepad, and dougdougs twitch connection (https://www.dougdoug.com/twitchplays)
# It combines the inputs from chat and a controller to create a hybrid output 
# if anything breaks its your fualt :)


import pygame as pg
import vgamepad as vg
import TwitchPlays_Connection
import InputMapping
import StoredMappings
import ChatCommands
import threading
import queue
import time
import random
from copy import deepcopy

# Default stuff to prevent the need to set it everytime you run the code
DEFAULT_TWITCH_CHANNEL = "" # the channel that it will automatically attempt to join on start up, leave as "" to start unconnected
CONTROLLER_AUTO_CONNECTS = ["PS4 Controller", "Xbox 360 Controller"] # the kinds of controllers that you want to automatically use as the active controller if no active is already set
DEFAULT_CHAT_COMMANDS = "simple" # the chat commands profile to initilize with

# how the inputs are combined
# note for dicriminatory instances chat should always be first and player second i.e lambda c,p : p only listen to player input
button_combination = lambda c, p : c ^ p # XOR
trigger_combination = lambda c, p : max(c, p) # whoever is bigger
stick_combination = lambda c, p : min(max((c + p)/max(abs(c + p), 1), -1), 1) # weighted avrg with clamp to prevent overflow


# the sentinal
run = True

# initialize pygame
pg.init()

# log all connected joysticks
joysticks = []
joyce = None
joyce_mapping = None
for event in pg.event.get():
    if event.type == pg.JOYDEVICEADDED:
        joy = pg.joystick.Joystick(event.device_index)
        joysticks.append(joy)
        if joyce == None and joy.get_name() in CONTROLLER_AUTO_CONNECTS:
            joyce = joy
            joyce_mapping = InputMapping.get_mapping(joyce.get_name())
            
            

# initializes the virtual controller to be influenced
gamepad = vg.VX360Gamepad()
gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(.01)
gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()

for event in pg.event.get(): pass # workaround to avoid the virtual gamepad getting detected as a joystick
    

# holds the data from both the controller and from the chat so they can be combined in the update
zeroed_con = {
    vg.XUSB_BUTTON.XUSB_GAMEPAD_A : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_B : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_X : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_Y : {'type':"BUTTON", 'chat':False, 'player':False},
    
    vg.XUSB_BUTTON.XUSB_GAMEPAD_START : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE : {'type':"BUTTON", 'chat':False, 'player':False},

    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT : {'type':"BUTTON", 'chat':False, 'player':False},
    
    vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER : {'type':"BUTTON", 'chat':False, 'player':False},
    
    vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB : {'type':"BUTTON", 'chat':False, 'player':False},
    vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB : {'type':"BUTTON", 'chat':False, 'player':False},
    
    "tr left" : {'type':"TRIGGER", 'chat':0.0, 'player':0.0},
    "tr right" : {'type':"TRIGGER", 'chat':0.0, 'player':0.0},
    
    "left x" : {'type':"STICK", 'chat':0.0, 'player':0.0},
    "left y" : {'type':"STICK", 'chat':0.0, 'player':0.0},
    "right x" : {'type':"STICK", 'chat':0.0, 'player':0.0},
    "right y" : {'type':"STICK", 'chat':0.0, 'player':0.0},
}
hybrid_controller = deepcopy(zeroed_con)

# combines the controller with the chat side and sets the output controller 
hybrid_lock = threading.Lock()
def update_controller():
    with hybrid_lock:
        left, right = [0.0, 0.0], [0.0, 0.0]
        for action in hybrid_controller.keys():
            if action == "tr left":
                gamepad.left_trigger_float(trigger_combination(hybrid_controller[action]['chat'], hybrid_controller[action]['player']))
            elif action == "tr right":
                gamepad.right_trigger_float(trigger_combination(hybrid_controller[action]['chat'], hybrid_controller[action]['player']))
                
            elif action == "left x":
                left[0] = stick_combination(hybrid_controller[action]['chat'], hybrid_controller[action]['player'])
            elif action == "left y":
                left[1] = stick_combination(hybrid_controller[action]['chat'], hybrid_controller[action]['player'])
            elif action == "right x":
                right[0] = stick_combination(hybrid_controller[action]['chat'], hybrid_controller[action]['player'])
            elif action == "right y":  
                right[1] = stick_combination(hybrid_controller[action]['chat'], hybrid_controller[action]['player'])
            
            else:
                if button_combination(hybrid_controller[action]['chat'], hybrid_controller[action]['player']):
                    gamepad.press_button(action)
                else:
                    gamepad.release_button(action)
                    
        gamepad.left_joystick_float(left[0], left[1])
        gamepad.right_joystick_float(right[0], right[1])
    
    gamepad.update()

# resets the controller state to neutral
def reset_hybrid():
    global hybrid_controller
    with hybrid_lock:
        hybrid_controller = deepcopy(zeroed_con)
    update_controller()


#--------------------------------
#       twitch handling
#--------------------------------
# twitch socket
Twitch = TwitchPlays_Connection.Twitch()
chat_active = False
active_chat_profile = ChatCommands.get_command_profile(DEFAULT_CHAT_COMMANDS)
def connect_to_channel(channel:str):
    if Twitch.sock:
        Twitch.disconnect()
    try:
        Twitch.twitch_connect(channel)
        Twitch.receive_and_parse_data()
    except:
        print("failed to connect to twitch: check internet connection")

# chat message processing
chat_event = pg.event.custom_type()
event_lock = threading.Lock()
chat_event_queue = queue.Queue()
def chat_processing_event_queue():
    '''
    processes the chat event queue
    '''
    last_time = time.time()
    while run:
        delta_time = time.time() - last_time
        last_time = time.time()
        # check through the chat event queue
        if not chat_event_queue.empty():
            # grap the first item in the event list of acions
            item = chat_event_queue.get()
            # look through the list of actions in items
            for i in item:
                # reduce delay
                i['delay'] -= delta_time
                
                # perform action when delay is < 0
                if i['delay'] <= 0:
                    with event_lock:
                        pg.event.post(pg.event.Event(chat_event, {'action':i}))
                    item.remove(i)
                    
            # if the action list is not empty put it back
            if item != []:
                chat_event_queue.put(item)  
            
chat_processor = threading.Thread(target=chat_processing_event_queue, daemon=True)
chat_processor.start()     


if DEFAULT_TWITCH_CHANNEL != "":
    connect_to_channel(DEFAULT_TWITCH_CHANNEL)
        
        
# chat message recieving
connection_event = pg.event.custom_type()
def twitch_chat_events_listener():
    '''
    Listens for new messages and pass them on for processing
    '''
    active = False
    while run:
        if Twitch.sock:
            # check and report the changed state of the connecetion
            if active == False:
                with event_lock:
                    pg.event.post(pg.event.Event(connection_event, {'state':"chat connected"}))
                active = True
            
            # recieve messages 
            try:
                messages = Twitch.twitch_receive_messages()
            except:
                print("something whent wrong while recieving messages")
                messages = []
                
            # loop through all the messages recieved from chat
            if chat_active:
                for msg in messages:
                    if msg['message'].lower() in active_chat_profile.keys():
                        chat_event_queue.put(deepcopy(active_chat_profile[msg['message'].lower()]))
        else:
            # check and report the changed state of the connecetion
            if active == True:
                with event_lock:
                    pg.event.post(pg.event.Event(connection_event, {'state':"chat disconnected"}))
                active = False
    if Twitch.sock:
        Twitch.disconnect()

twitch_listener = threading.Thread(target=twitch_chat_events_listener, daemon=True)
twitch_listener.start()


#----------------
# random chatter just spams valid messages
rando_active = False
rando_event = pg.event.custom_type()
def rando():
    avalable_commands = list(StoredMappings.active_commands.keys())
    while rando_active:
        if chat_active:
            time.sleep(.1)
            chat_event_queue.put(deepcopy(StoredMappings.active_commands[random.choice(avalable_commands)]))
        
    print("Rando has died D:")

rando_thread = threading.Thread(target=rando, daemon=True)

#------------------------
#   cmd line function
#------------------------
# all command info tips
info_dict = {'con connect':"lets you choose the active controller", 'con mapping':"lets you select a mapping for the active controller", 'con check':"checks the status of all connected controllers", 'mapping check':"checks the active controllers mapping", 
             'chat connect':"lets you connect to a twitch chat by inputing the channel name", 'chat disconnect':"disconnects from the active chat",'chat profile':"allows the change of the chat commands profile", 'chat':f"any command that is legal can be typed in the command line and executed like a normal chat message.\n(note: only works when started)\n here are the current avalable commands\n {list(active_chat_profile.keys())}", 
             'start':"starts the sytsem listening to all chat messages, this includes rando and cmd messages", 'stop':"stop the system from listening to messages",
             'rando start':"starts randomly sending valid chat messages (note: only works when started)", 'rando stop':"",
             'help':"this is what you just typed\n this gives hints about each of the commands", 'quit':"this exits the program gracefully"}
# command line input processor
def debugger_chat():
    global run, joyce, joyce_mapping, chat_active, rando_active, active_chat_profile
    while run:
        msg = input().lower()
        
        if msg == "list":
            print("Avalable commands are:\n#### Controller commands ####\n- con connect\n- con mapping\n- con check\n- mapping check\n#### Twitch chat commands ####\n- chat connect\n- chat disconnect\n- chat profile\n- All valid chat commands (hints:'help chat')\n#### System commands ####\n- start\n- stop\n- help [command]\n- quit")
        
        # ---- controller block ----
        # sets the active controller
        if msg == "con connect":
            con_name_list = [joy.get_name() for joy in joysticks]
            print("connected joysticks", con_name_list)
            
            con = input("type the number or name of the controller you wish to use (type \"none\" disconnect)\n>").lower()
            if con.isdigit():
                index = int(con)
                if index in range(len(joysticks)):
                    joyce = joysticks[index]
                    joyce_mapping = InputMapping.get_mapping(joyce.get_name())
                    print("connected to:", joysticks[index].get_name())
                else:
                    print("no con at index:", index)
            elif con in con_name_list:
                joyce = joysticks[con_name_list.index(con)]
                joyce_mapping = InputMapping.get_mapping(joyce.get_name())
                print("now connected to:", con)
            elif con == "none":
                joyce == None
                joyce_mapping = None
                print("active controller disabled")
            else:
                print("failed to connect to:", con)
        
        # sets the controller mapping in use
        if msg == "con mapping":
            if joyce != None:
                print("avalable controller mappings are:", list(StoredMappings.controller_mappings.keys()))
                map_name = input("what mapping would you like to select\n>")
                if map_name in StoredMappings.controller_mappings.keys():
                    joyce_mapping = StoredMappings.controller_mappings[map_name]
                else:
                    print("sorry that is not the name of a known mapping")
            else:
                print("sorry there is no active controller to set the mapping for")
            
        # the mapping thats currntly active
        if msg == "mapping check":
            print(joyce_mapping)
            
        # checks the status of the controllers
        if msg == "con check":
            print("Checking joysticks status'")
            if joyce != None:
                print(f"active controller:", joyce.get_name())
            else:
                print(f"- active controller: None")
            for joy in joysticks:
                print(f"- - {joy.get_name()} : init = {joy.get_init()}, power = {joy.get_power_level()}, num of buttons = {joy.get_numbuttons()}, num of axes = {joy.get_numaxes()}, num hats = {joy.get_numhats()}")
            
        # ---- chat block ----
        # starts chat
        if msg == "start":
            print("Chat starts in:")
            for i in range(3)[::-1]:
                print(i+1)
                time.sleep(1)
            print("GO!")
            chat_active = True
            
        # stops chat
        if msg == "stop":
            chat_active = False
            with event_lock:
                while not chat_event_queue.empty():
                    chat_event_queue.get()
            reset_hybrid()
            print("chat has stopped")
        
        # runs msg like a chat message
        if msg in active_chat_profile.keys():
            if chat_active:
                chat_event_queue.put(deepcopy(active_chat_profile[msg]))
            else:
                print("until start is typed chat commands do nothing")
            
        # connects to a channel
        if msg == 'chat connect':
            channel = input("please type the channel name you wish to connect to\n>").lower()
            connect_to_channel(channel)
        
        # disconnects twitch socket
        if msg == 'chat disconnect':
            Twitch.disconnect()
            
        # change chat profile
        if msg == 'chat profile':
            print("avalable chat profiles:", list(ChatCommands.chat_command_profiles.keys()))
            prof = input("type the name of the profile you wish to use\n>")
            active_chat_profile = ChatCommands.get_command_profile(prof)
        
        # ---- rando ----
        # start random message spam
        if msg == "rando start":
            if not chat_active:
                print("rando will not do anything until start is run")
            rando_active = True
            rando_thread.start()
            print("Rando has started. run for your lives")
            
        
        # stops rando
        if msg == "rando stop":
            rando_active = False
            print("Killing rando, may god rest his soul")
        
        # ---- system block ----
        # gives unfo on what each command does

        if msg == "reset":
            reset_hybrid()
        
        if msg.startswith("help "):
            if msg[5:] in info_dict:
                print(info_dict[msg[5:]])
            else:
                print("sorry i cant help you with that")
                print("make sure to type 'help [command]'. to see avalable commands type 'list'")
        
        # quits out
        if msg == "quit":
            run = False

chat_debugger = threading.Thread(target=debugger_chat, daemon=True)
chat_debugger.start() 
#----------------


#-----------------------------
#           main loop
#-----------------------------
print("\n\n\n\n\n\n\n\n- - - - - - Welcome to chat rangler - - - - - - \nto list avalable commands type \"list\"")

print("connected controllers:", [joy.get_name() for joy in joysticks])
print("active con = ", None if joyce == None else joyce.get_name())
while run:
    update_controller()
    
    with event_lock:
        event_list = pg.event.get()
    for event in event_list:
        #print(event)
        if event.type == pg.QUIT:
            run = False
           
        # ----------------- 
        # Device Connection
        # Device added
        elif event.type == pg.JOYDEVICEADDED: # adds a new joystick when it connects
            id = event.guid
            joy = pg.joystick.Joystick(event.device_index)
            joysticks.append(joy)
            print("joystick connected:", joy.get_name())
            
            if joyce == None and joy.get_name() in CONTROLLER_AUTO_CONNECTS:
                joyce = joy
                joyce_mapping = InputMapping.get_mapping(joyce.get_name())
                print("new active controller:", joy.get_name())
                
        # Device removed
        elif event.type == pg.JOYDEVICEREMOVED: # removes a joystick when it disconnects
            for joy in joysticks:
                print(joy.get_instance_id(), event.instance_id)
                if joy.get_instance_id() == event.instance_id:
                    joysticks.remove(joy) 
                    print("joystick disconnected:", joy.get_name())
                    
                    if joyce == joy: # removes the joyce if the conntroller was disconnected
                        joyce = None
                        joyce_mapping = None
                        print("active controller disconnected")
                    
                    joy.quit() # deinitilizes
                    break
            
        # -------------------------
        # Controller input handling
        # Butten pressed or released
        elif event.type in [pg.JOYBUTTONDOWN, pg.JOYBUTTONUP]:
            if joyce != None and joyce_mapping != None and event.instance_id == joyce.get_instance_id():
                # map to xbox controller
                action = InputMapping.apply_input_mapping(joyce_mapping, 'BUTTON', event.button)
                value = InputMapping.apply_value_mapping(joyce_mapping, 'BUTTON', event.button, True if event.type == pg.JOYBUTTONDOWN else False)
                
                if action != None and value != None:
                    with hybrid_lock:
                        hybrid_controller[action['id']]['player'] = value
                 
        # Axis changed
        elif event.type == pg.JOYAXISMOTION:
            if joyce != None and joyce_mapping != None and event.instance_id == joyce.get_instance_id():
                action = InputMapping.apply_input_mapping(joyce_mapping, 'AXIS', event.axis)
                value = InputMapping.apply_value_mapping(joyce_mapping, 'AXIS', event.axis, event.value)
                    
                if action != None and value != None:
                    with hybrid_lock:
                        hybrid_controller[action['id']]['player'] = value
            
        # Chat event handling
        elif event.type == chat_event:
            if chat_active:
                event_dict = event.__dict__['action']
                
                action = event_dict['input']
                with hybrid_lock:
                    hybrid_controller[action['id']]['chat'] = event_dict['value']
            
        elif event.type == rando_event:
            if rando_active:
                event_dict = event.__dict__['action']
                
                action = event_dict['input']
                with hybrid_lock:
                    hybrid_controller[action['id']]['chat'] = event_dict['value']
        
        elif event.type == connection_event:
            event_dict = event.__dict__
            if event_dict['state'] == "disconnected":
                Twitch.reconnect()
            
            
if Twitch.sock:
    Twitch.disconnect()
    

print("- - - - - - Exiting Chat Rangler - - - - - - \nThank you for using Chat Rangler\nHave a good day")