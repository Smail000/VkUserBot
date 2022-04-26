
		elif text[0:6] == 'scroll' and from_id == config.owner_id:
			text = text[7:]
			text = text[::-1]
			err = False
			for i in text:
				fun = i + fun
				try:
					edit(peer_id, fun, msg_id)
					time.sleep(wait)
				except:
					print('Введите капчу')
					err = True
					break
			if not err:
				text = text[::-1]
				for i in range(1, len(text)):
					try:
						edit(peer_id, text[:i-i-i], msg_id)
						time.sleep(wait)
					except:
						print('Введите капчу')
						break
				edit(peer_id, full_msg[7:], msg_id)
		elif text[0:5] == 'wheel' and from_id == config.owner_id:
			text = text[6:]











