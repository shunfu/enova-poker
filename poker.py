import requests
import time
import json

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
            card1 = data['hand'][0]
            card2 = data['hand'][1]
            current_money = data['stack']
            return_action = {}

            #deal phase
            if data["betting_phase"] == "deal":

                bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money:
                    bet_amount = current_money

                return_action = {'action_name': "bet", 'amount': bet_amount}

            #flop phase
            if data["betting_phase"] == "flop":

                bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money :
                    bet_amount = current_money

                return_action = {'action_name': "bet", 'amount': bet_amount}
            #turn phase
            if data["betting_phase"] == "turn":
                bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money :
                    bet_amount = current_money

                return_action = {'action_name':"bet", 'amount': bet_amount}

            #river phase
            if data["betting_phase"] == "river":
                bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money :
                    bet_amount = current_money

                return_action = {'action_name': "bet", 'amount': bet_amount}

            # POST a request to the server
            response = player_action(PLAYER_KEY, return_action)
            
# GET
def game_state(key):
    # do a get request to http://nolimitcodeem.com/api/players/:key
    # get a Response object
    # return json
    r = requests.get('http://nolimitcodeem.com/api/players/{}'.format(key))
    return r.json()

# POST
def player_action(key, json_params):
    # do a post request to http://nolimitcodeem.com/api/players/:key/action
    # get a Response object
    # return json
    # r = requests.post(url, data=json.dumps(payload), headers=headers)
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://nolimitcodeem.com/api/players/{}/action'.format(key), 
        data=json.dumps(json_params), 
        headers=headers)
    return r.json()

def main():
    # the key is generated when we register for the tournament
    poker('60fd7cbe-f9e0-4ebe-a0e3-f554872a312f')

if __name__ == '__main__':
    main()