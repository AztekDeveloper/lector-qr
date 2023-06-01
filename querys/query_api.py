from functions.config import getConfig

import requests

server = "http://192.168.1.18:8000"

def get_ticket_info(card_code):
    config = getConfig()
    return requests.get(config['protocolo'] + '://' + config['servidor'] + '/tickets/card/last/' + card_code)