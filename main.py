from trello import TrelloApi

trello = TrelloApi('********************************')
trello.set_token('****************************************************************')
boardid = '************************'

board = trello.boards.get(boardid)
cards = trello.boards.get_card(boardid)
trello_member = trello.boards.get_member(boardid)
member = {i['id']: i['fullName'] for i in trello_member }
count = {i['id']: 0 for i in trello_member}

for card in cards:
    for m in card['idMembers']:
        count[m] += 1

for m in count:
    if count[m] != 0:
        print member[m], str(count[m])
