import random
class Maze:
    def __init__(self):
        self.wall = '#'
        self.cell = ' '
        self.unvisited = 'u'
        self.height = 10
        self.width = 10
        self.maze = []
        self.c=['0','1','2','3','4','5','6','7','8','9']
        self.cc=[0,1,2,3,4,5,6,7,8,9]

    def genWithGrid(self):
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                line.append(self.unvisited)
            self.maze.append(line)

        starting_height = int(random.random() * self.height)
        starting_width = int(random.random() * self.width)
        if (starting_height == 0):
            starting_height += 1
        if (starting_height == self.height - 1):
            starting_height -= 1
        if (starting_width == 0):
            starting_width += 1
        if (starting_width == self.width - 1):
            starting_width -= 1

        self.maze[starting_height][starting_width] = self.cell
        walls = []
        walls.append([starting_height - 1, starting_width])
        walls.append([starting_height, starting_width - 1])
        walls.append([starting_height, starting_width + 1])
        walls.append([starting_height + 1, starting_width])

        self.maze[starting_height - 1][starting_width] = '#'
        self.maze[starting_height][starting_width - 1] = '#'
        self.maze[starting_height][starting_width + 1] = '#'
        self.maze[starting_height + 1][starting_width] = '#'

        while (walls):
            rand_wall = walls[int(random.random() * len(walls)) - 1]

            if (rand_wall[1] != 0):
                if (self.maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] + 1] == ' '):
                    s_cells = self.surroundingCells(rand_wall)

                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0] - 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        if (rand_wall[0] != self.height - 1):
                            if (self.maze[rand_wall[0] + 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] + 1, rand_wall[1]])

                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1] - 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '#'
                            if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            if (rand_wall[0] != 0):
                if (self.maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] + 1][rand_wall[1]] == ' '):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0] - 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1] - 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '#'
                            if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                        if (rand_wall[1] != self.width - 1):
                            if (self.maze[rand_wall[0]][rand_wall[1] + 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '#'
                            if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            if (rand_wall[0] != self.height - 1):
                if (self.maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] - 1][rand_wall[1]] == ' '):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[0] != self.height - 1):
                            if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '#'
                            if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] - 1])
                        if (rand_wall[1] != self.width - 1):
                            if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '#'
                            if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            if (rand_wall[1] != self.width - 1):
                if (self.maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] - 1] == ' '):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[1] != self.width - 1):
                            if (self.maze[rand_wall[0]][rand_wall[1] + 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '#'
                            if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] + 1])
                        if (rand_wall[0] != self.height - 1):
                            if (self.maze[rand_wall[0] + 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0] - 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == 'u'):
                    self.maze[i][j] = '#'


    def surroundingCells(self,rand_wall):
        s_cells = 0
        if (self.maze[rand_wall[0] - 1][rand_wall[1]] == ' '):
            s_cells += 1
        if (self.maze[rand_wall[0] + 1][rand_wall[1]] == ' '):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1] - 1] == ' '):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1] + 1] == ' '):
            s_cells += 1

        return s_cells

    def __repr__(self):
        return self.finalmaze


    def placen(self,n):
        while True:
            x=random.randint(0,self.width-1)
            y=random.randint(0,self.width-1)
            if self.maze[x][y] == ' ':
                self.maze[x][y] = n
                break


    def sortie(self):
        self.maze[-1][-1] = '$'
        self.maze[-1][-2] = '$'
        self.maze[-2][-1] = '$'
        self.maze[-2][-2] = ' '

    def convert_str(self):
        self.finalmaze = ""

        for i in self.maze:
            for j in i:
                self.finalmaze += str(j)

        for i in range(10):
            print(self.finalmaze[i * 10:(i + 1) * 10])


    def collectibles(self):
        for i in range(10):
            self.placen(str(i))


class SuperMaze:
    def __init__(self,size):
        self.size = size
        self.maze = []

    def generates(self):
        for j in range(self.size):
            mm= Maze()
            mm.genWithGrid()
            mm.sortie()
            mm.convert_str()
            self.maze.append(mm.finalmaze)
        return self.maze
