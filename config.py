
import functions as fn

# kinds of delay
wait = 0.8
long_wait = 1.5

# Log the capcha warnings
capchaLog = True

# get you access token here - https://vkhost.github.io/
auth_token = '' # str

# owner id is required
owner_id = 0    # int

emoji = {                             # Base emojis
    'expoint'   :   '&#10071;' ,      # Exclamation point
    'smile'     :   '&#128522;',      # Smile emoji
    'wink'      :   '&#128521;',      # Winking emoji
    'sad'       :   '&#128546;',      # Sad emoji
    'crying'    :   '&#128557;',      # Crying emoji
    'normal'    :   '&#128528;',      # Normal emoji
    'bigeyes'   :   '&#128563;',      # Emoji with big eyes
    'cat_sad'   :   '&#128575;',      # Sad cat
    'cat_fun'   :   '&#128569;',      # Funny cat
    'cat_love'  :   '&#128571;',      # Cat with hearts
    'cat_wow'   :   '&#128576;',      # Cat with white eyes
}

# do NOT use names "test", "stop" and "help" in key feild of dict
{               # Example of algorithms types
    'sayhi': {                                           # Example of standart algorithm
        'discription'        :   'it func says "hi"',    # Just discriotion
        'type'               :   'standart',             # Standart (json algorithm) or custom (custom function)
        'func'               :   None,                   # Function for cunstom algorithms (func form functions.py or None)
        'algorithm'          :   {                       # Algorithm for standart function (dict as from example of None)
            'cmd': [                                     # List of messages
                'Wow...' + emoji['cat_wow'],
                'Hi!'   + emoji['smile'],
            ],
            'repeatTimes'    :   3,                      # Times to repeat (times)
            'delayMsgs'      :   0.5,                    # Delay between messages (seconds)
            'delayCycle'     :   0.5,                    # Delay between cycles of messages editting (seconds)
            'deleteAfter'    :   False,                  # Whether to delete message after end of algorithm (True or False)
        },
    }
}

{        # Empty base
    'empty': {
        'discription'        :   'empty',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [],
            'repeatTimes'    :   1,
            'delayMsgs'      :   0,
            'delayCycle'     :   0,
            'deleteAfter'    :   False,
        },
    }
}













commands = {    
    'catwow': {
        'discription'        :   'Cat says "WOW" and becomes lovely',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [
                emoji['cat_wow'],
                emoji['cat_love'],
            ],
            'repeatTimes'    :   3,
            'delayMsgs'      :   1,
            'delayCycle'     :   0,
            'deleteAfter'    :   False,
        },
    },
    
    'catty': {
        'discription'        :   'Cat becomes sad, fun and lovely',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [
                emoji['cat_sad'],
                emoji['cat_fun'],
                emoji['cat_love'],
            ],
            'repeatTimes'    :   3,
            'delayMsgs'      :   1,
            'delayCycle'     :   0,
            'deleteAfter'    :   False,
        },
    },

    'bigeyes': {
        'discription'        :   'Emoji with big eyes',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [
                emoji['normal'],
                emoji['bigeyes'],
            ],
            'repeatTimes'    :   3,
            'delayMsgs'      :   1,
            'delayCycle'     :   0,
            'deleteAfter'    :   False,
        },
    },

    'rain': {
        'discription'        :   'Crying emoji',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [
                emoji['sad'],
                emoji['crying'],
            ],
            'repeatTimes'    :   3,
            'delayMsgs'      :   1,
            'delayCycle'     :   0,
            'deleteAfter'    :   False,
        },
    },

    'wink': {
        'discription'        :   'Winking emoji',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [
                emoji['smile'],
                emoji['wink'],
            ],
            'repeatTimes'    :   3,
            'delayMsgs'      :   1,
            'delayCycle'     :   0,
            'deleteAfter'    :   False,
        },
    },

    'warn': {
        'discription'        :   'Warn notification',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [
                emoji['expoint']+'Внимание, внимание'+emoji['expoint'],
                emoji['expoint']+'Важная информация'+emoji['expoint'],
            ],
            'repeatTimes'    :   3,
            'delayMsgs'      :   1,
            'delayCycle'     :   0,
            'deleteAfter'    :   True,
        },
    },

    'post': {
        'discription'        :   'Post notification',
        'type'               :   'standart',
        'func'               :   None,
        'algorithm'          :   {
            'cmd': [
                emoji['expoint']+'Внимание, внимание'+emoji['expoint'],
                emoji['expoint']+'Важное объявление'+emoji['expoint'],
            ],
            'repeatTimes'    :   3,
            'delayMsgs'      :   1,
            'delayCycle'     :   0,
            'deleteAfter'    :   True,
        },
    },

    'slide': {
        'discription'        :   'Slide the message',
        'type'               :   'custom',
        'func'               :   fn.slide_func
    },

    'scroll': {
        'discription'        :   'Scroll the message',
        'type'               :   'custom',
        'func'               :   fn.scroll_func,
    }
}