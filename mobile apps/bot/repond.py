import random

def handel_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hai'
    if p_message == 'hai':
        return 'hello'
    if p_message == 'roll':
        return str(random.randInt(1,  6))
    if p_message == '!help':
        return 'what is ur problem ?'
    
    