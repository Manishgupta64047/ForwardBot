from os import environ

API_ID = int(environ.get('API_ID', '12267130'))
API_HASH = environ.get('API_HASH', '6ddb28a13ffc2f15dc16f06be6ca3c1f')
BOT_TOKEN = environ.get('BOT_TOKEN', '6102798689:AAElGzeXcg8L-uWL5vs5a4oBkl1fL7lQKFs')
FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
OWNER = int(environ.get('OWNER', '5259051520'))
PRIVATE_BOT = bool(environ.get('PRIVATE_BOT', False))
