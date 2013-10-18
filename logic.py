#Logic for the Texas Holdem Bot

#Check if it is your turn
card1 = data['hand'][0]
card2 = data['hand'][1]

	if data["your_turn"]:
		#check what turn it is

		#deal phase
		if data["betting_phase"] == "deal":
			#if the ante is just normal ante then just pay ante
			if data[]
			#if the ante is higher and your hand sucks then fold
			#if ante and your hand is good then pay/raise
			if data["call_amount"] == :
				return_action = {'action_name':"call"}

			#else fold
			else:
				return_action{'action_name':"fold"}

		#flop phase
		if data["betting_phase"] == "flop":
			#calcuate the probability of winning the turn
			#if probability is greater than 50% then bet

			#else fold
			else:
				return_action{'action_name':"fold"}
		#turn phase
		if data["betting_phase"] == "turn":
			#update the probability
			#if it is still greater than 50% then continue
			
			#else fold
			else:
				return_action{'action_name':"fold"}

		#river phase
		if data["betting_phase"] == "river":
			#update the final probabilty
			#if the chance of winning is still greater than 50% then raise
			
			#else fold
			else:
				return_action{'action_name':"fold"}
				
	#calculate the probabilty of each hand
	def probability(card1, card2):




