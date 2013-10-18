import requests
import time

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

            #deal phase
            if data["betting_phase"] == "deal":

                bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money :
                    bet_amount = current_money

                return_action{'action_name':"bet", 'amount': bet_amount}

            #flop phase
            if data["betting_phase"] == "flop":
               bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money :
                    bet_amount = current_money

                return_action{'action_name':"bet", 'amount': bet_amount}
            #turn phase
            if data["betting_phase"] == "turn":
               bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money :
                    bet_amount = current_money

                return_action{'action_name':"bet", 'amount': bet_amount}

            #river phase
            if data["betting_phase"] == "river":
               bet_amount = data['call_amount']
                
                if bet_amount == 0:
                    bet_amount == 20
                elif bet_amount >= current_money :
                    bet_amount = current_money

                return_action{'action_name':"bet", 'amount': bet_amount}
            
""" 
        This is the provided sample dumb_bot code
        # Is it a betting round, but not the river? Let's always call.
        if  turn_data["betting_phase"] == "deal" or
            turn_data["betting_phase"] == "flop" or
            turn_data["betting_phase"] == "turn":
            action = "call"
            params = nil
                  
        # Is it the river phase? Always bet 10 more.
        elif turn_data["betting_phase"] == "river":
            action = "bet"
            params = 10
  
        # Stores all your parameters in a single variable
        my_action = {action_name: action, amount: params}
"""
    
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
    r = requests.post('http://nolimitcodeem.com/api/players/{}/action'.format(key))
    return r.json()