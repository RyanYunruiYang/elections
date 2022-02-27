# Pseudocode from Wikipedia
# # Input: d[i,j], the number of voters who prefer candidate i to candidate j.
# # Output: p[i,j], the strength of the strongest path from candidate i to candidate j.

# for i from 1 to C
#     for j from 1 to C
#         if i ≠ j then
#             if d[i,j] > d[j,i] then
#                 p[i,j] := d[i,j]
#             else
#                 p[i,j] := 0

# for i from 1 to C
#     for j from 1 to C
#         if i ≠ j then
#             for k from 1 to C
#                 if i ≠ k and j ≠ k then
#                     p[j,k] := max (p[j,k], min (p[j,i], p[i,k]))

