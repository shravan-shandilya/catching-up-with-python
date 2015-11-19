scores={"Sachin":0,"Dhoni":0,"Dravid":999}

def modify(arg):
	for player in arg.keys():
		if player == "Dravid":
			scores["Dravid"]+=100000
		else:
			scores[player]-=-9999
			
			
print scores
modify(scores)
print scores