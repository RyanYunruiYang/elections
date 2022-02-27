import numpy as np

# Pseudocode from Wikipedia and Ian Haile
# # Input: d[i,j], the number of voters who prefer candidate i to candidate j.
# # Output: p[i,j], the strength of the strongest path from candidate i to candidate j.

def path_strength(num_cand, d): #finds the path strength between each pair of candidates
    p = [[0 for i in range(num_cand)] for j in range(num_cand)]
    for i in range(num_cand): 
        for j in range(num_cand):
            if (i!=j):
                if (d[i][j] > d[j][i]):
                    p[i][j] = d[i][j]
                else:
                    p[i][j] = 0

    for i in range(num_cand): 
        for j in range(num_cand):
            if (i!=j):
                for k in range(num_cand):
                    if ((i!=k) and (j!=k)):
                        p[j][k] = max(p[j][k], min(p[j][i], p[i][k]))
    return p

def sum_preferences(num_cand, votes): # builds out prefer() graph
    graph = [[0 for i in range(num_cand)] for j in range(num_cand)]
    for i in range(num_cand):
        for j in range(num_cand):
            if i != j:
                graph[i][j] = prefer(num_cand, i, j, votes)
    return graph

def prefer(n,i,j, votes): #counts number of voters who prefer candidate i to j
    count = 0
    for ballot in votes:
        if (np.where(ballot==i)<np.where(ballot==j)):
            count+=1
    return count


# def strength():
#     for i in range(1,C):
#         for j in range(1,C):    
#             pass

def schulze(num_cand, votes): #main function
    d = sum_preferences(num_cand,votes)
    p = path_strength(num_cand,d)
    preferred = [sum(p[i]) for i in range(num_cand)]

    return preferred



def main():
    n = 10
    num_voters = 1
    votes = []
    for i in range(num_voters):
        votes.append(np.random.permutation(n))
    print(votes)

    print(schulze(n,votes))



if __name__ == "__main__":
    main()