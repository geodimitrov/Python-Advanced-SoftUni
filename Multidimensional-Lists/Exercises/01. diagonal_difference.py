# use functions to break down the code/problem to different parts/steps
# let's define a func that creates the matrix
def create_matrix(n_lines):
    result = []
    for _ in range(n_lines):
        result.append([int(el) for el in input().split()]) #use list compreh to turn the nums into ints
    return result

def print_result(sum_one, sum_two):
    result = abs(sum_one - sum_two) #they ask for the ABSOLUTE value of the difference
    print(result)

n = int(input())  #number of lines (size of matrix)
matrix = create_matrix(n)

# Once the matrix has been create, let's calculate the sums of the diagonals
sum_diagonal_one = 0
sum_diagonal_two = 0

# use a simple for loop to calc sums of diagonals
for i in range(n):
    sum_diagonal_one += matrix[i][i] #row & column index are the same
    sum_diagonal_two += matrix[i][n - 1 - i]  # we start from the last element of the 1st row

#let's create a func to calc difference between the sums
print_result(sum_diagonal_one, sum_diagonal_two)