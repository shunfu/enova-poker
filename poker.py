import requests
import time
import json

valuecode = {'A':14,'K':13,'Q':12,'J':11, '10':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}

def poker(PLAYER_KEY):
    # Infinite Loop
    while True:
    
        # Your client should sleep 1 second.
        # If you send too many requests at once, we will start throttling your requests.
        # This will cause you to reach the timeout limit which will cause your player to FOLD.
        time.sleep(1)

        # GET request.
        # Ask the server "What is going on?"
        # Gets JSON in response
        turn_data = game_state(PLAYER_KEY)
        
        # Logic!
        # Check if it's your turn
        if turn_data["your_turn"]:
            card1 = turn_data['hand'][0]
            card2 = turn_data['hand'][1]
            current_money = turn_data['stack']
            return_action = {}

            #deal phase
            if turn_data["betting_phase"] == "deal":
                if prob_deal(card1, card2) or duplicates(turn_data['hand'], []):
                    return_action = {'action_name': "call"}
                else:
                    return_action = {'action_name': "fold"}

            #flop phase
            if turn_data["betting_phase"] == "flop":
                is_flush(turn_data['hand'], turn_data['community_cards'])

                return_action = {'action_name': "call"}

            #turn phase
            if turn_data["betting_phase"] == "turn":
                return_action = {'action_name': "call"}

            #river phase
            if turn_data["betting_phase"] == "river":
                return_action = {'action_name': "call"}

            #showdown phase
            if turn_data["betting_phase"] == "showdown":
                return_action = {'action_name': "call"}

            #bet_amount = turn_data['call_amount']

            # POST a request to the server
            response = player_action(PLAYER_KEY, return_action)

def prob_deal(card1, card2):

    num_card1 = card1[0]
    num_card2 = card2[0]

    suit_card1 = card1[1]
    suit_card2 = card2[1]

    return abs(valuecode[num_card1] - valuecode[num_card2]) > 4 and suit_card1 != suit_card2

# def is_flush(our_hand, community_cards):

# def is_straight(our_hand, community_cards):

def duplicates(our_hand, community_cards):
    all_cards = our_hand + community_cards
    all_nums = [card[0] for card in all_cards]
    for x in all_nums:
        if all_nums.count(x) > 1:
            return True
    return False

"""
GETs are made to the following URL:
http://nolimitcodeem.com/sandbox/players/SANDBOX_KEY

POSTs are made to the following URL:
http://nolimitcodeem.com/sandbox/players/SANDBOX_KEY/action

To simulate how the game would look after the initial deal, use deal-phase-key as SANDBOX_KEY.
To simulate how the game would look after the flop, use flop-phase-key as SANDBOX_KEY.
To simulate how the game would look in the turn phase, use turn-phase-key as SANDBOX_KEY.
To simulate how the game would look in the final, river phase, use river-phase-key as SANDBOX_KEY.
"""

# GET
def game_state(key):
    # do a get request to http://nolimitcodeem.com/api/players/:key
    # get a Response object
    # return json
    # r = requests.get('http://nolimitcodeem.com/sandbox/players/deal-phase-key')
    r = requests.get('http://nolimitcodeem.com/api/players/{}'.format(key))
    return r.json()

# POST
def player_action(key, json_params):
    # do a post request to http://nolimitcodeem.com/api/players/:key/action
    # get a Response object
    # return json
    headers = {'Content-type': 'application/json'}
    # r = requests.post('http://nolimitcodeem.com/sandbox/players/deal-phase-key/action', 
    r = requests.post('http://nolimitcodeem.com/api/players/{}/action'.format(key), 
        data=json.dumps(json_params), 
        headers=headers)
    return r.json()

def main():
    # the key is generated when we register for the tournament
    our_key = 'b76f4f34-83cd-442b-94a3-f0a30df62655'

    if our_key:
        poker(our_key)
    else:
        print "No key entered!"

if __name__ == '__main__':
    main()