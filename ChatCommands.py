from StoredMappings import xbox_valid_inputs as x_inputs
# store varius chat command lists here

# command dictionary format 'the command chat types': [a list of inputs performed on delays]
    # input format {'input':x_innputs.[the name of the xbox controller input], 'value':[the value to be input on the controller], 'delay': [how much time in seconds till the input is performed]}

demo_commands = {
    'message' : #this is the message that twitch chat needs to type
    [  # this is a list of all the inputs that need to be preformed when chat types their message
        {  # this is one input that will get performed
            'input':x_inputs, # this is the xbox controller input that gets pressed
            'value':any, # this is the value (bool or float) that gets passed
            'delay': 0, # this is how long (in seconds) it will wait to execute the command 
        },
    ]
}

# a basic list of xbox controller inputs notably without 'start', 'back', and 'guide'
empty_chat_commands = {}

simple_chat_commands = { 'a':[{'input':x_inputs.A, 'value':True, 'delay':0}, {'input':x_inputs.A, 'value':False, 'delay':.1}], 'b':[{'input':x_inputs.B,  'value':True, 'delay':0}, {'input':x_inputs.B, 'value':False, 'delay':.1}], 'x':[{'input':x_inputs.X, 'value':True, 'delay':0}, {'input':x_inputs.X, 'value':False, 'delay':.1}], 'y':[{'input':x_inputs.Y, 'value':True, 'delay':0}, {'input':x_inputs.Y, 'value':False, 'delay':.1}], 'dpad up':[{'input':x_inputs.DPAD_UP, 'value':True, 'delay':0}, {'input':x_inputs.DPAD_UP, 'value':False, 'delay':.1}], 'dpad down':[{'input':x_inputs.DPAD_DOWN, 'value':True, 'delay':0}, {'input':x_inputs.DPAD_DOWN, 'value':False, 'delay':.1}], 'dpad left':[{'input':x_inputs.DPAD_LEFT, 'value':True, 'delay':0},  {'input':x_inputs.DPAD_LEFT, 'value':False, 'delay':.1}], 'dpad right':[{'input':x_inputs.DPAD_RIGHT, 'value':True, 'delay':0}, {'input':x_inputs.DPAD_RIGHT, 'value':False, 'delay':.1}], 'l1':[{'input':x_inputs.BUMPER_LEFT, 'value':True, 'delay':0}, {'input':x_inputs.BUMPER_LEFT, 'value':False, 'delay':.1}], 'l2':[{'input':x_inputs.TRIGGER_LEFT, 'value':1.0, 'delay':0}, {'input':x_inputs.TRIGGER_LEFT, 'value':-1.0, 'delay':.1}],'l3':[{'input':x_inputs.THUMB_LEFT, 'value':True, 'delay':0}, {'input':x_inputs.THUMB_LEFT, 'value':False, 'delay':.1}], 'r1':[{'input':x_inputs.BUMPER_RIGHT, 'value':True, 'delay':0}, {'input':x_inputs.BUMPER_RIGHT, 'value':False, 'delay':.1}], 'r2':[{'input':x_inputs.TRIGGER_RIGHT, 'value':1.0, 'delay':0},{'input':x_inputs.TRIGGER_RIGHT, 'value':-1.0, 'delay':.1}],'r3':[{'input':x_inputs.THUMB_RIGHT, 'value':True, 'delay':0},{'input':x_inputs.THUMB_RIGHT, 'value':False, 'delay':.1}], 'up':[{'input':x_inputs.STICK_LEFT_Y, 'value':1.0, 'delay':0}, {'input':x_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}], 'down':[{'input':x_inputs.STICK_LEFT_Y, 'value':-1.0, 'delay':0},{'input':x_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}],'left':[{'input':x_inputs.STICK_LEFT_X, 'value':-1.0, 'delay':0}, {'input':x_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}],'right':[{'input':x_inputs.STICK_LEFT_X, 'value':1.0, 'delay':0},{'input':x_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}],'c up':[{'input':x_inputs.STICK_RIGHT_Y, 'value':1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}],'c down':[{'input':x_inputs.STICK_RIGHT_Y, 'value':-1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}],'c left':[{'input':x_inputs.STICK_RIGHT_X, 'value':-1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':.5}],'c right':[{'input':x_inputs.STICK_RIGHT_X, 'value':1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':5.}],}

full_chat_commands = {'a':[{'input':x_inputs.A, 'value':True, 'delay':0}, {'input':x_inputs.A, 'value':False, 'delay':.1}],'b':[{'input':x_inputs.B,  'value':True, 'delay':0}, {'input':x_inputs.B, 'value':False, 'delay':.1}],'x':[{'input':x_inputs.X, 'value':True, 'delay':0},{'input':x_inputs.X, 'value':False, 'delay':.1}],'y':[{'input':x_inputs.Y, 'value':True, 'delay':0}, {'input':x_inputs.Y, 'value':False, 'delay':.1}],'dpad up':[{'input':x_inputs.DPAD_UP, 'value':True, 'delay':0}, {'input':x_inputs.DPAD_UP, 'value':False, 'delay':.1}],'dpad down':[{'input':x_inputs.DPAD_DOWN, 'value':True, 'delay':0}, {'input':x_inputs.DPAD_DOWN, 'value':False, 'delay':.1}],'dpad left':[{'input':x_inputs.DPAD_LEFT, 'value':True, 'delay':0},  {'input':x_inputs.DPAD_LEFT, 'value':False, 'delay':.1}],'dpad right':[{'input':x_inputs.DPAD_RIGHT, 'value':True, 'delay':0}, {'input':x_inputs.DPAD_RIGHT, 'value':False, 'delay':.1}],'back':[{'input':x_inputs.BACK,  'value':True, 'delay':0},{'input':x_inputs.BACK, 'value':False, 'delay':.1}],'start':[{'input':x_inputs.START, 'value':True, 'delay':0}, {'input':x_inputs.START, 'value':False, 'delay':.1}], 'guide':[{'input':x_inputs.GUIDE, 'value':True, 'delay':0},{'input':x_inputs.GUIDE, 'value':False, 'delay':.1}], 'l1':[{'input':x_inputs.BUMPER_LEFT, 'value':True, 'delay':0}, {'input':x_inputs.BUMPER_LEFT, 'value':False, 'delay':.1}],'l2':[{'input':x_inputs.TRIGGER_LEFT, 'value':1.0, 'delay':0},{'input':x_inputs.TRIGGER_LEFT, 'value':-1.0, 'delay':.1}],'l3':[{'input':x_inputs.THUMB_LEFT, 'value':True, 'delay':0},{'input':x_inputs.THUMB_LEFT, 'value':False, 'delay':.1}],'r1':[{'input':x_inputs.BUMPER_RIGHT, 'value':True, 'delay':0}, {'input':x_inputs.BUMPER_RIGHT, 'value':False, 'delay':.1}], 'r2':[{'input':x_inputs.TRIGGER_RIGHT, 'value':1.0, 'delay':0},{'input':x_inputs.TRIGGER_RIGHT, 'value':-1.0, 'delay':.1}],'r3':[{'input':x_inputs.THUMB_RIGHT, 'value':True, 'delay':0}, {'input':x_inputs.THUMB_RIGHT, 'value':False, 'delay':.1}], 'up':[{'input':x_inputs.STICK_LEFT_Y, 'value':1.0, 'delay':0}, {'input':x_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}], 'down':[{'input':x_inputs.STICK_LEFT_Y, 'value':-1.0, 'delay':0},{'input':x_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}],'left':[{'input':x_inputs.STICK_LEFT_X, 'value':-1.0, 'delay':0},{'input':x_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}],'right':[{'input':x_inputs.STICK_LEFT_X, 'value':1.0, 'delay':0}, {'input':x_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}], 'c up':[{'input':x_inputs.STICK_RIGHT_Y, 'value':1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}],'c down':[{'input':x_inputs.STICK_RIGHT_Y, 'value':-1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}], 'c left':[{'input':x_inputs.STICK_RIGHT_X, 'value':-1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':.5}],'c right':[{'input':x_inputs.STICK_RIGHT_X, 'value':1.0, 'delay':0},{'input':x_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':5.}],}


###############################
# user created command profiles




# holds all the command profiles and lets them be selected form the chat rangler program
chat_command_profiles = {'none':empty_chat_commands,'simple':simple_chat_commands, 'full':full_chat_commands}

# checks if a profile exist and returns it if it does
def get_command_profile(profile) -> dict:
    if profile.lower() in chat_command_profiles.keys():
        return chat_command_profiles[profile.lower()]
    else:
        return {}
