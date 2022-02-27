import numpy as np

def approvalK(n, votes, k): #runs approval voting where everyone votes for their k favorites
	candidates = [0 for i in range(n)]
	for ballot in votes:
		for j in range(k):
			candidates[ballot[j]]+=1
	return candidates

def main():
	n = 10
	k = 1

	num_voters = 5
	votes = []
	for i in range(num_voters):
		votes.append(np.random.permutation(n))
	print(votes)

	print(approvalK(n,votes, k))




if __name__ == "__main__":
	main()