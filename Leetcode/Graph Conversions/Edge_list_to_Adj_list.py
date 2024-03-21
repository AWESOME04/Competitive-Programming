# Question 3: Convert from Edge List to Adjacency List

# --------------------------------------
# Function to convert Edge List to Adjacency List
from collections import defaultdict
def edge_list_to_adjacency_list(edge_list):

	# Write your code here to convert the edge list to an adjacency list.
    adj_list =  defaultdict(list)
    for u, v in edge_list:
        adj_list[u].append(v)

    return adj_list

# Test case
edge_list_sample = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

result_adj_list = edge_list_to_adjacency_list(edge_list_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")
# --------------------------------------

