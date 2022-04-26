
import time

def edit(vk, peer_id, msg, msg_id, capchaLog=True):
    while True:
        try:
            return vk.method('messages.edit', {'peer_id': peer_id, 'message': msg, 'message_id': msg_id})
        except:
            if capchaLog:
                print('WARNING: Capcha has arrived')
            time.sleep(5)

def delete(vk, peer_id, msg_id, capchaLog=True):
    while True:
        try:
            return vk.method('messages.delete', {'message_ids': msg_id, 'peer_id': peer_id})
        except:
            if capchaLog:
                print('WARNING: Capcha has arrived')
            time.sleep(5)



def example_func(vk, peer_id, msg_id, msg_text, capchaLog=True): # Example of algorithm function
    pass



def slide_func(vk, peer_id, msg_id, msg_text, capchaLog=True):
    msg_text = msg_text[7:]
    fun = ''
    for i in msg_text:
        fun += i
        edit(vk, peer_id, fun, msg_id, capchaLog=capchaLog)
        time.sleep(1)

def scroll_func(vk, peer_id, msg_id, msg_text, capchaLog=True):
    full_msg = msg_text
    fun = ''

    msg_text = msg_text[8:][::-1]
    for i in msg_text:
        fun = i + fun
        edit(vk, peer_id, fun, msg_id, capchaLog=capchaLog)
        time.sleep(1)

    msg_text = msg_text[::-1]
    for i in range(1, len(msg_text)):
        edit(vk, peer_id, msg_text[:i-i-i], msg_id, capchaLog=capchaLog)
        time.sleep(1)
    
    edit(vk, peer_id, full_msg[8:], msg_id, capchaLog=capchaLog)