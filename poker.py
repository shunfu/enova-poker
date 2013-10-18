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
        
        # Logic!!
        # This logic is boring. But, yours should be more epic!
        if turn_data["your_turn"]:
            # LOGIC GOES HERE

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
    
        # POST a request to the server
        response = player_action(PLAYER_KEY, my_action)

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