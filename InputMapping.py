import StoredMappings

def apply_input_mapping(mapping, type, id):
    '''
    Converts the input to an xbox valid input\n
    Returns None if no mapping exist
    '''
    if type in mapping.keys() and id in mapping[type].keys():
        return mapping[type][id]
    else: 
        return None

def apply_value_mapping(action, convert):
    '''
    Converts the input value ising its conversion funtion\n
    Returns None if no conversion exists
    '''
    if action != None:
        return action['convert'](convert)
    else:
        return None


def get_mapping(map_name) -> dict:
    if map_name.lower() in StoredMappings.controller_mappings.keys():
        return StoredMappings.controller_mappings[map_name.lower()]
    else:
        return StoredMappings.emptymap