from pytg import Telegram
from pytg.sender import Sender

# tg = Telegram(telegram="telegram-cli", pubkey_file="/etc/telegram-cli/server.pub")
# sender = tg.sender

sender = Sender('localhost', 4457)

contacts = sender.dialog_list()

for c in contacts:
    if c.get('phone'):
        msg = 'Happy Christmas {}!!'.format(c.get('first_name'))
        print('Send "{}" to {}'.format(msg, c.get('print_name')))

        # sender.msg('@{}'.format(c.get('print_name')), msg)
        # sender.msg('@{}'.format(c.get('username')), msg)

print('Done.')
