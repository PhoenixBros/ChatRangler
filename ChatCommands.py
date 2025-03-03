from InputMapping import xbox_valid_inputs as x_inputs
# store varius chat command lists here

# command dictionary format 'the command chat types': [a list of inputs performed on delays]
    # input format {'input':x_innputs.[the name of the xbox controller input], 'value':[the value to be input on the controller], 'delay': [how much time in seconds till the input is performed]}

# a basic list of xbox controller inputs notably without 'start', 'back', and 'guide'
empty_chat_commands = {}

simple_chat_commands = {
    'a':[{'input':x_inputs.A, 'value':True, 'delay':0},
        {'input':x_inputs.A, 'value':False, 'delay':.1}],
    'b':[{'input':x_inputs.B,  'value':True, 'delay':0},
        {'input':x_inputs.B, 'value':False, 'delay':.1}],
    'x':[{'input':x_inputs.X, 'value':True, 'delay':0},
        {'input':x_inputs.X, 'value':False, 'delay':.1}],
    'y':[{'input':x_inputs.Y, 'value':True, 'delay':0},
        {'input':x_inputs.Y, 'value':False, 'delay':.1}],
    
    'dpad up':[{'input':x_inputs.DPAD_UP, 'value':True, 'delay':0},
               {'input':x_inputs.DPAD_UP, 'value':False, 'delay':.1}],
    'dpad down':[{'input':x_inputs.DPAD_DOWN, 'value':True, 'delay':0},
                 {'input':x_inputs.DPAD_DOWN, 'value':False, 'delay':.1}],
    'dpad left':[{'input':x_inputs.DPAD_LEFT, 'value':True, 'delay':0}, 
                 {'input':x_inputs.DPAD_LEFT, 'value':False, 'delay':.1}],
    'dpad right':[{'input':x_inputs.DPAD_RIGHT, 'value':True, 'delay':0},
                  {'input':x_inputs.DPAD_RIGHT, 'value':False, 'delay':.1}],
    
    'l1':[{'input':x_inputs.BUMPER_LEFT, 'value':True, 'delay':0},
        {'input':x_inputs.BUMPER_LEFT, 'value':False, 'delay':.1}],
    'l2':[{'input':x_inputs.TRIGGER_LEFT, 'value':1.0, 'delay':0},
        {'input':x_inputs.TRIGGER_LEFT, 'value':-1.0, 'delay':.1}],
    'l3':[{'input':x_inputs.THUMB_LEFT, 'value':True, 'delay':0},
        {'input':x_inputs.THUMB_LEFT, 'value':False, 'delay':.1}],
    
    'r1':[{'input':x_inputs.BUMPER_RIGHT, 'value':True, 'delay':0},
        {'input':x_inputs.BUMPER_RIGHT, 'value':False, 'delay':.1}],
    'r2':[{'input':x_inputs.TRIGGER_RIGHT, 'value':1.0, 'delay':0},
        {'input':x_inputs.TRIGGER_RIGHT, 'value':-1.0, 'delay':.1}],
    'r3':[{'input':x_inputs.THUMB_RIGHT, 'value':True, 'delay':0},
        {'input':x_inputs.THUMB_RIGHT, 'value':False, 'delay':.1}],
    
    'up':[{'input':x_inputs.STICK_LEFT_Y, 'value':1.0, 'delay':0},
        {'input':x_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}],
    'down':[{'input':x_inputs.STICK_LEFT_Y, 'value':-1.0, 'delay':0},
        {'input':x_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}],
    'left':[{'input':x_inputs.STICK_LEFT_X, 'value':-1.0, 'delay':0},
        {'input':x_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}],
    'right':[{'input':x_inputs.STICK_LEFT_X, 'value':1.0, 'delay':0},
        {'input':x_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}],
    
    'c up':[{'input':x_inputs.STICK_RIGHT_Y, 'value':1.0, 'delay':0},
        {'input':x_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}],
    'c down':[{'input':x_inputs.STICK_RIGHT_Y, 'value':-1.0, 'delay':0},
        {'input':x_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}],
    'c left':[{'input':x_inputs.STICK_RIGHT_X, 'value':-1.0, 'delay':0},
        {'input':x_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':.5}],
    'c right':[{'input':x_inputs.STICK_RIGHT_X, 'value':1.0, 'delay':0},
        {'input':x_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':5.}],
}


chat_command_profiles = {'none':{},'simple':simple_chat_commands}


def get_command_profile(profile) -> dict:
    if profile.lower() in chat_command_profiles.keys():
        return chat_command_profiles[profile.lower()]
    else:
        return {}
