import numpy as np


def main():
	n = 10
	k = 1

	voters = 5


	candidates = [0 for i in range(n)]
	for i in range(voters):
		arr = np.random.permutation(n)
		print(arr)
		for j in range(k):
			candidates[arr[j]]+=1

	print(candidates)

if __name__ == "__main__":
	main()