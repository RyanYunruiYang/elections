import numpy as np
import random


def sortPower(val): #used for sorting in toSTUCO
    return val[0] 

def generate_votes(num_voters, num_cand):
	votes = []
	for i in range(num_voters):
		votes.append(np.random.permutation(num_cand))

	return votes

def dot(K, L):
   if len(K) != len(L):
      return 0
   return sum(i[0] * i[1] for i in zip(K, L))


def generate_votes2(num_voters, num_cand): #inspired by word2vec, we represent voters and candidates as vectors
	#and the voters rank based on the dot product <v,c>

	dim = 10 #hardcoded representation lmao

	voters = []
	for i in range(num_voters):
		voters.append(Voter(dim))
		# print(voters[i])

	candidates = []
	for i in range(num_cand):
		candidates.append(Candidate(dim))
		# print(candidates[i])

	ballots = []
	for voter in voters:
		powerranks = [(dot(voter.MBTI,candidates[i].MBTI),i) for i in range(num_cand)]
		# print(powerranks)
		powerranks.sort(key=sortPower, reverse=True)
		# print(powerranks)

		ballot = [i[1] for i in powerranks]
		ballots.append(ballot)

	# print(ballots)
	return ballots

class Voter: #n numbers each from [-1,1], and a 1
	def __init__(self, n): #n is number of attributes
		self.MBTI = [random.uniform(-1,1) for i in range(n)]
		self.MBTI.append(1)

	def __str__(self):
		return ' '.join(str(i) for i in self.MBTI)

class Candidate: #n numbers from [-1,1], and one number from [0,weighter]
	def __init__(self, n): #n is number of attributes
		self.MBTI = [random.uniform(-1,1) for i in range(n)]
		weighter = 1 #used to be n**2
		self.MBTI.append(weighter*random.random())
	def __str__(self):
		return ' '.join(str(i) for i in self.MBTI)


def main():
	n=2
	# abe = Voter(n)
	# print(abe)

	# joy = Candidate(n)
	# print(joy)

	generate_votes2(3,8)


if __name__ == "__main__":
	main()