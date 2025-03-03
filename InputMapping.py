from vgamepad import XUSB_BUTTON

class xbox_valid_inputs:
    '''
    all the valid inputs for an xbox controller
    '''   
    #empty = None
    
    A = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_A}
    B = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_B}
    X = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_X}
    Y = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_Y}
    
    START = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_START}
    BACK = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_BACK}
    GUIDE = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_GUIDE}
    
    DPAD_UP = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP}
    DPAD_DOWN = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN}
    DPAD_LEFT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT}
    DPAD_RIGHT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT}
    
    BUMPER_LEFT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER}
    BUMPER_RIGHT = {'type':"BUTTON", 'id': XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER}
    
    THUMB_LEFT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB}
    THUMB_RIGHT = {'type':"BUTTON", 'id':XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB}
    
    TRIGGER_LEFT = {'type':"TRIGGER", 'id':"tr left"}
    TRIGGER_RIGHT = {'type':"TRIGGER", 'id':"tr right"}
    
    STICK_LEFT_X = {'type':"STICK", 'id':"left x"}
    STICK_LEFT_Y = {'type':"STICK", 'id':"left y"}
    STICK_RIGHT_X = {'type':"STICK", 'id':"right x"}
    STICK_RIGHT_Y = {'type':"STICK", 'id':"right y"}



def apply_input_mapping(mapping, type, id) -> xbox_valid_inputs:
    '''
    Converts the input to an xbox valid input\n
    Returns None if no mapping exist
    '''
    if type in mapping and id in mapping[type]:
        return mapping[type][id]['input']
    else: 
        return None

def apply_value_mapping(mapping, type, id, value):
    '''
    Converts the input value ising its conversion funtion\n
    Returns None if no conversion exists
    '''
    if type in mapping and id in mapping[type]:
        return mapping[type][id]['value'](value)
    else:
        return None

conversions = {
    "pass": lambda x : x,
    "button to +axis": lambda x : 1.0 if x else 0.0,
    "button to -axis": lambda x : -1.0 if x else 0.0,
    "axis to button": lambda x : True if x > .5 else False,
    "axis flip": lambda x : -x,
}


# --------------------------------------------------------------
#                    controller mapping
# --------------------------------------------------------------
# mappings have 3 types "BUTTON"s, "AXIS"s, and "HAt"s
# each mapping coresponds to a valid input id on the controller in use and a convertion to a valid xbox controller input
# thay can be blank if we dont want to map an input
# one input cannot be mapped to two outputs
# each input that gets mapped also gets its value converted
# conversions can go between types (i.e. converting dpad buttons to joystick motion)


# this mapping is the defualt and wont do anything
emptymap = {'BUTTON':{},'AXiS':{},'HAT':(),}

# defualt mapping for ps4 controller
ps4Map = {
    'BUTTON': {
        0: {'input': xbox_valid_inputs.A, "value":conversions['pass']},
        1: {'input': xbox_valid_inputs.B, "value":conversions['pass']},
        2: {'input': xbox_valid_inputs.X, "value":conversions['pass']},
        3: {'input': xbox_valid_inputs.Y, "value":conversions['pass']},
            
        6: {'input': xbox_valid_inputs.START, "value":conversions['pass']},
        5: {'input': xbox_valid_inputs.GUIDE, "value":conversions['pass']},
        4: {'input': xbox_valid_inputs.BACK, "value":conversions['pass']},
            
        11: {'input': xbox_valid_inputs.DPAD_UP, "value":conversions['pass']},
        12: {'input': xbox_valid_inputs.DPAD_DOWN, "value":conversions['pass']},
        13: {'input': xbox_valid_inputs.DPAD_LEFT, "value":conversions['pass']},
        14: {'input': xbox_valid_inputs.DPAD_RIGHT, "value":conversions['pass']},
            
        15: {'input': xbox_valid_inputs.BACK, "value":conversions['pass']},
            
        9: {'input': xbox_valid_inputs.BUMPER_LEFT, "value":conversions['pass']},
        10: {'input': xbox_valid_inputs.BUMPER_RIGHT, "value":conversions['pass']},
            
        7: {'input': xbox_valid_inputs.THUMB_LEFT, "value":conversions['pass']},
        8: {'input': xbox_valid_inputs.THUMB_RIGHT, "value":conversions['pass']}
    },
    
    'AXIS': {
        0: {'input': xbox_valid_inputs.STICK_LEFT_X, "value":conversions['pass']},
        1: {'input': xbox_valid_inputs.STICK_LEFT_Y, "value":conversions['axis flip']},
        2: {'input': xbox_valid_inputs.STICK_RIGHT_X, "value":conversions['pass']},
        3: {'input': xbox_valid_inputs.STICK_RIGHT_Y, "value":conversions['axis flip']},
            
        4: {'input': xbox_valid_inputs.TRIGGER_LEFT, "value":conversions['pass']},
        5: {'input': xbox_valid_inputs.TRIGGER_RIGHT, "value":conversions['pass']}
    },

    'HAT': {}
}



# make sure to keep all map names lowercase
controller_mappings = {"none":emptymap, "ps4 controller":ps4Map}

def get_mapping(map_name) -> dict:
    if map_name.lower() in controller_mappings.keys():
        return controller_mappings[map_name.lower()]
    else:
        return emptymap



# the commands twitch chat actually writes
simple_chat_commands = {
    'a':[{'input':xbox_valid_inputs.A, 'value':True, 'delay':0},
        {'input':xbox_valid_inputs.A, 'value':False, 'delay':.1}],
    'b':[{'input':xbox_valid_inputs.B,  'value':True, 'delay':0},
        {'input':xbox_valid_inputs.B, 'value':False, 'delay':.1}],
    'x':[{'input':xbox_valid_inputs.X, 'value':True, 'delay':0},
        {'input':xbox_valid_inputs.X, 'value':False, 'delay':.1}],
    'y':[{'input':xbox_valid_inputs.Y, 'value':True, 'delay':0},
        {'input':xbox_valid_inputs.Y, 'value':False, 'delay':.1}],
    
    'dpad up':[{'input':xbox_valid_inputs.DPAD_UP, 'value':True, 'delay':0},
               {'input':xbox_valid_inputs.DPAD_UP, 'value':False, 'delay':.1}],
    'dpad down':[{'input':xbox_valid_inputs.DPAD_DOWN, 'value':True, 'delay':0},
                 {'input':xbox_valid_inputs.DPAD_DOWN, 'value':False, 'delay':.1}],
    'dpad left':[{'input':xbox_valid_inputs.DPAD_LEFT, 'value':True, 'delay':0}, 
                 {'input':xbox_valid_inputs.DPAD_LEFT, 'value':False, 'delay':.1}],
    'dpad right':[{'input':xbox_valid_inputs.DPAD_RIGHT, 'value':True, 'delay':0},
                  {'input':xbox_valid_inputs.DPAD_RIGHT, 'value':False, 'delay':.1}],
    
    'l1':[{'input':xbox_valid_inputs.BUMPER_LEFT, 'value':True, 'delay':0},
        {'input':xbox_valid_inputs.BUMPER_LEFT, 'value':False, 'delay':.1}],
    'l2':[{'input':xbox_valid_inputs.TRIGGER_LEFT, 'value':1.0, 'delay':0},
        {'input':xbox_valid_inputs.TRIGGER_LEFT, 'value':-1.0, 'delay':.1}],
    'l3':[{'input':xbox_valid_inputs.THUMB_LEFT, 'value':True, 'delay':0},
        {'input':xbox_valid_inputs.THUMB_LEFT, 'value':False, 'delay':.1}],
    
    'r1':[{'input':xbox_valid_inputs.BUMPER_RIGHT, 'value':True, 'delay':0},
        {'input':xbox_valid_inputs.BUMPER_RIGHT, 'value':False, 'delay':.1}],
    'r2':[{'input':xbox_valid_inputs.TRIGGER_RIGHT, 'value':1.0, 'delay':0},
        {'input':xbox_valid_inputs.TRIGGER_RIGHT, 'value':-1.0, 'delay':.1}],
    'r3':[{'input':xbox_valid_inputs.THUMB_RIGHT, 'value':True, 'delay':0},
        {'input':xbox_valid_inputs.THUMB_RIGHT, 'value':False, 'delay':.1}],
    
    'up':[{'input':xbox_valid_inputs.STICK_LEFT_Y, 'value':1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}],
    'down':[{'input':xbox_valid_inputs.STICK_LEFT_Y, 'value':-1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_LEFT_Y, 'value':0.0, 'delay':.5}],
    'left':[{'input':xbox_valid_inputs.STICK_LEFT_X, 'value':-1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}],
    'right':[{'input':xbox_valid_inputs.STICK_LEFT_X, 'value':1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_LEFT_X, 'value':0.0, 'delay':.5}],
    
    'c up':[{'input':xbox_valid_inputs.STICK_RIGHT_Y, 'value':1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}],
    'c down':[{'input':xbox_valid_inputs.STICK_RIGHT_Y, 'value':-1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_RIGHT_Y, 'value':0.0, 'delay':.5}],
    'c left':[{'input':xbox_valid_inputs.STICK_RIGHT_X, 'value':-1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':.5}],
    'c right':[{'input':xbox_valid_inputs.STICK_RIGHT_X, 'value':1.0, 'delay':0},
        {'input':xbox_valid_inputs.STICK_RIGHT_X, 'value':0.0, 'delay':5.}],
}


active_commands = simple_chat_commands