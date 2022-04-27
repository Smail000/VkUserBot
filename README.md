# Notice
If you dont want to read docs and discription, go to the "How to test?" (botom of this page)
# Discription
This is simple python script for making animations in messages. Made with vk_api
# How it works
After typing the command, script will edit last message for a few times creating an animation effect.
There is only one problem which i cant solve - capcha. If you request a lot of requests, VK and script will not edit message and animation will be stoped, 
but not broked. Animation will continue after ending capcha delay.
So, with convenient system you can create you own animation by using emoji and one of following types of methods.
# System
You have two ways to create animation
- Standart
- Custom
## Standart
It is simple but limited method. By editing template you can set messages, delay and times to repeat. (see all base emojis in config.py and add more if you want)
```
# config.py
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
```
With this method available to create template animation, but with second method you dont have limit (only you imagination)
## Custom 
Thre is full functional of python. Write you own algorithm and dont forget to connect it in comfig.py file
```
# config.py
{
  'empty': {
      'discription'        :   'Discription',
      'type'               :   'custom',
      'func'               :   fn.some_func,
}

# functions.py
def example_func(vk, peer_id, msg_id, msg_text, capchaLog=True): # Example of algorithm function
    pass
```
# How to install
Python v3.7+ and git is required. Then follow the commands
```
pip install vk_api

git clone https://github.com/Smail000/VkUserBot.git
cd VkUserBot
```
then you need to edit config.py file
```
# get you access token here - https://vkhost.github.io/
auth_token = '' # str

# owner id is required
owner_id = 0    # int
```
then write this command
```
python main.py
```
and open the dialog with someone. To start using the script write ```!``` and command.
Base commands: 
- ```!test``` gives you info that script is working
- ```!help``` gives you info about all commands
- ```!stop``` stops script

Commands which was made by standart method:
- ```!catwow``` Cat says "WOW" and becomes lovely
- ```!catty``` Cat becomes sad, fun and lovely
- ```!bigeyes``` Emoji with big eyes
- ```!rain``` Crying emoji
- ```!wink``` Winking emoji
- ```!warn``` Warn notification
- ```!post``` Post notification

And commands which was made my custom method:
- ```!slide text``` makes slide effect with text
- ```!scroll text``` makes scroll effect with text

P.S. I will be glad if someone fork my froject and make hisown effects ;-)




