# View compilation time
import time as tm

def solve_maze(maze, start, end):
    stack = [start]
    while stack:
        x, y = stack[-1]

        # If reached the end point
        if (x, y) == end:
            return True, stack

        # Mark as visited
        maze[x][y] = '2'
        tuplesArr = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in tuplesArr:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == '0' or maze[nx][ny] == 'E':
                    stack.append((nx, ny))
                    break
                else:
                    stack.pop()

    return False, []

if __name__ == "__main__":
    startTime = tm.time()
    # 0 = open path, 1 = wall, S = start, E = end
    maze = [
        ['1', '1', '1', '1', '1'],
        ['S', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', 'E'],
        ['1', '1', '1', '1', '1']
    ]

    start = (1, 0)
    end = (3, 4)
    i = 0
    solved, path = solve_maze(maze, start, end)

    if solved:
        print("Maze Solved!")
        for x, y in path:
            # if maze[x][y] != 'S' and maze[x][y] != 'E':
            if maze[x][y] != 'S' or maze[x][y] != 'E':
                maze[x][y] = '*'
        # for row in maze:
        while i < len(maze):
            print("".join(maze[i]))
            i += 1 # Added
    else:
        print("No solution found.")
    endTime = tm.time()
    totalTime = endTime - startTime
    print("Compilation time: ", str(round(totalTime, 4)), "ms")