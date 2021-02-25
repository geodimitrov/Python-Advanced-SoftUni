def get_magic_triangle(n):
    magic_triangle = [[1], [1, 1]]

    for row in range(1, n - 1):
        magic_triangle.append([1,])

        for i in range(len(magic_triangle[row]) - 1):
            sum_nums = magic_triangle[row][i] + magic_triangle[row][i + 1]
            magic_triangle[row +1].append(sum_nums)
        magic_triangle[row+1].append(1)

    return magic_triangle

# print(get_magic_triangle(5))