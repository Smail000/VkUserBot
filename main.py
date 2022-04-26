from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import time, sys, random as rn, vk_api
import config, functions as fn

vk = vk_api.VkApi(token=config.auth_token)
vk.get_api()

print('VkUserBot started')

# Base
# fn.edit(vk, peer_id, 'msg', msg_id) -> edit message by msg_id and peer_id (companion id)
# fn.delete(vk, peer_id, 'msg', msg_id) -> edit message by msg_id and peer_id (companion id)

while True:
	for conv in vk.method('messages.getConversations', {'filter': 'all', 'count': 3})['items']:
		msg_text = conv['last_message']['text']
		if conv['last_message']['from_id'] == config.owner_id and msg_text != '' and msg_text[0] == '!':
			peer_id, msg_id = conv['last_message']['peer_id'], conv['last_message']['id']

			if msg_text == '!help':
				fn.edit(vk, peer_id, '\n'.join(['name : discription']+[i+' : '+config.commands[i]['discription'] for i in config.commands]), msg_id)

			elif msg_text == '!test':
				fn.edit(vk, peer_id, config.emoji['normal']+' Everything is OK, master '+config.emoji['normal'], msg_id)

			elif msg_text == '!stop':
				fn.edit(vk, peer_id, config.emoji['expoint']+' VkUserBot stopped '+config.emoji['expoint'], msg_id)
				sys.exit()
			
			else:

				if msg_text[1:].split()[0] in config.commands:

					if config.commands[msg_text[1:].split()[0]]['type'] == 'standart':

						algorithm = config.commands[msg_text[1:].split()[0]]['algorithm']
						for _ in range(algorithm['repeatTimes']):
							for cmd in algorithm['cmd']:
								fn.edit(vk, peer_id, cmd, msg_id)
								if algorithm['delayMsgs']: time.sleep(algorithm['delayMsgs'])
							if algorithm['delayCycle']: time.sleep(algorithm['delayCycle'])
						if algorithm['deleteAfter']: fn.delete(vk, peer_id, msg_id)

					elif config.commands[msg_text[1:].split()[0]]['type'] == 'custom':
						config.commands[msg_text[1:].split()[0]]['func'](vk, peer_id, msg_id, msg_text, capchaLog=config.capchaLog)

					else:
						print('ERROR: Command type is unknown')
				
				else:
					fn.edit(vk, peer_id, 'Command was not found '+config.emoji['crying'], msg_id)
					time.sleep(config.long_wait)
					fn.delete(vk, peer_id, msg_id)

	time.sleep(0.5)
