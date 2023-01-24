class Solution:
    def bfs(self, n, cells, board):
        distances = [-1] * ((n ** 2) + 1)
        queue = deque([1])
        distances[1] = 0
        
        while queue:
            current = queue.popleft()
            for cell in range(current + 1, min(current + 6, (n ** 2)) + 1):
                row, column = cells[cell]
                destination = (
                    board[row][column] 
                    if board[row][column] != -1
                    else cell
                )
    
                if distances[destination] == -1:
                    distances[destination] = distances[current] + 1
                    queue.append(destination)
        
        return distances[(n ** 2)]

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * ((n ** 2) + 1)
        label = 1
        leftDirection = True
        for row in range(n - 1, -1, -1):
            start, end, direction = (0, n, 1) if leftDirection else (n - 1, -1, -1)
            for column in range(start, end, direction):
                cells[label] = (row, column)
                label += 1
            leftDirection = not leftDirection

        return self.bfs(n, cells, board)