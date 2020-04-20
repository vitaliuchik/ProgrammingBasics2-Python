class Graph:
    """Represents graph"""

    def __init__(self, matrix):
        """Initializes graph by adjacency matrix"""
        self._matrix = matrix

    def isCorrect(self):
        """Checks if adjacency matrix is correct"""
        vertices_num = len(self._matrix)
        for row in self._matrix:
            if vertices_num != len(row):
                return False
            for el in row:
                if el not in (0, 1):
                    return False
        for i in range(vertices_num):
            if self._matrix[i][i] == 1:
                return False
            for j in range(vertices_num):
                if self._matrix[i][j] != self._matrix[j][i]:
                    return False
        return True

    def dfs(self):
        """Builds carcass using depth first search"""
        self._carcass = [[0 for _ in range(len(self._matrix))] \
            for _ in range(len(self._matrix))]
        vertices = [0 for _ in range(len(self._matrix))]

        def recurse(vertix):
            """Recursive function for dfs"""
            vertices[vertix] = 1
            for i in range(len(self._matrix)):
                if self._matrix[vertix][i] and not vertices[i]:
                    self._carcass[vertix][i], self._carcass[i][vertix] = 1, 1
                    recurse(i)

        recurse(0)  

    def __str__(self):
        """Represents graph by adjacency matrix"""
        result = ''
        for row in self._carcass:
            for el in row:
                result += str(el) + ' '
            result += '\n'
        return result

                  
if __name__ == "__main__":
    
    print("Input adjacency matrix.\n\
In row separate each element by space.\n\
Click 'enter' after each row and skip empty row to finish inputing.")
    matrix = [] 
    while True:
        row = list(map(int, input().split()))
        if not row:
            graph = Graph(matrix)
            if not graph.isCorrect():
                print('Matrix is incorrect. Try again!')
                matrix = []
                continue
            break
        matrix.append(row)
    
    graph.dfs()
    print(graph)
    

        