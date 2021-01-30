from telethon.sync import TelegramClient, events
from telethon.tl.types import PeerUser

######################
pairs = [
	{
		"source_id": 1476381705,
		"dest_id": 1153680585
	},
	{
		"source_id": 0,
		"dest_id": 0
	},
	{
		"source_id": 0,
		"dest_id": 0
	},
]
######################

client_name = 'online-sender'
API_ID = 1945628
API_HASH = '2c96a07930fe107684ab108250886d49'

client = TelegramClient(client_name, API_ID, API_HASH)

client.start()

me = client.get_me()

@client.on(events.NewMessage)
async def cnmh(event):
	if type(event.original_update.message.to_id) == PeerUser:
		if event.original_update.message.to_id.user_id == me.id:
			if event.original_update.message.fwd_from:
				await client.send_message('me', f'the id of the cahnnel is:')
				await client.send_message('me', f'{event.original_update.message.fwd_from.channel_id}')
				return
			elif event.raw_text.startswith('getid>') or event.raw_text.startswith('Getid>'):
				ent = await client.get_entity(event.raw_text.split('>')[1])
				await client.send_message('me', f'the id is:')
				await client.send_message('me', f'{ent.id}')
	else:
		for pair in pairs:
			if pair['source_id'] == event.message.to_id.channel_id:
				await client.forward_messages(pair['dest_id'], event.message)

client.run_until_disconnected()
