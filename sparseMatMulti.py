class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # T: O(m * k + k * n + t), S: O(m * n)
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        # Preprocess mat1
        mat1_dict = {}
        for i in range(m):
            mat1_dict[i] = []
            for j in range(k):
                if mat1[i][j]:
                    mat1_dict[i].append((j, mat1[i][j]))

        # Preprocess mat2
        mat2_dict = {}
        for j in range(k):
            mat2_dict[j] = []
            for l in range(n):
                if mat2[j][l]:
                    mat2_dict[j].append((l, mat2[j][l]))

        # Initialize result matrix
        result = [[0] * n for _ in range(m)]

        # Compute the product
        for i in range(m):
            for j, val1 in mat1_dict.get(i, []):
                for l, val2 in mat2_dict.get(j, []):
                    result[i][l] += val1 * val2

        return result
