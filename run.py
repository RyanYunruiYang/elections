import numpy as np
from approvalK import approvalK

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