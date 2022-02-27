import numpy as np
import time

from approvalK import approvalK
from schulze import schulze
import sys

def printf(format, *args):
    sys.stdout.write(format % args)


def sortPower(val): #used for sorting in toSTUCO
    return val[0] 

#take a "powerscore" assigned to each candidate, and turn this into a student council
def toSTUCO(preferences, a, b):#a is num of pos1, b is num of pos2
	powerranks = [(preferences[i],i) for i in range(len(preferences))]
	# print(powerranks)
	powerranks.sort(key=sortPower, reverse=True)
	# print(powerranks)
	
	pos1 = [i[1] for i in powerranks[0:a]]
	pos2 = [i[1] for i in powerranks[a:a+b]]

	pos1.sort()
	pos2.sort()
	return [pos1,pos2]

def difElectResult(num_cand, cab1, cab2): #measure the difference between two student councils
	w1=3 #value of president
	w2=1 #value of tier2

	val1 = [0 for i in range(num_cand)]
	for pres in cab1[0]:
		val1[pres] += w1
	for cou in cab1[1]:
		val1[cou]+= w2

	val2 = [0 for i in range(num_cand)]
	for pres in cab2[0]:
		val2[pres] += w1
	for cou in cab2[1]:
		val2[cou]+=w2

	return sum([abs(val1[i]-val2[i]) for i in range(num_cand)])

def main():
	sim_length = 500
	num_cand = 8
	num_voters = 200

	offFromSchulze = [0 for i in range(num_cand)] #sum of dif
	for o in range(sim_length):
		votes = []
		for i in range(num_voters):
			votes.append(np.random.permutation(num_cand))
	
		# if(num_voters<10):
		# 	print('votes:')
		# 	print(votes)


		rankS = schulze(num_cand,votes)
		# print(toSTUCO(rankS))
		num_pos1 = 1
		num_pos2 = 1

		for k in range(1,num_cand):
			rankA = approvalK(num_cand,votes, k)
			# print(toSTUCO(rankA))			
			# print("k: "+ str(k) + " dif: "+ str(difElectResult(num_cand, toSTUCO(rankS), toSTUCO(rankA))))
			offFromSchulze[k]+= difElectResult(num_cand, toSTUCO(rankS, num_pos1,num_pos2), toSTUCO(rankA,num_pos1,num_pos2))

	print(offFromSchulze)

	best_num = offFromSchulze.index(min(offFromSchulze[1:num_cand]))	
	print(num_pos2)	
	printf("This means that when there are n=%d candidates running for [%d,%d],\nthe \"Optimal\" number of people to vote for is: k=%d\n", num_cand, num_pos1, num_pos2, best_num)




if __name__ == "__main__":
	start_time = time.time()
	main()
	print("execution time: " + str(time.time()-start_time) + "s")