import requests

server = "http://192.168.1.18:8000"

def get_ticket_info(card_code):
    return requests.get(server + '/tickets/card/last/' + card_code)
