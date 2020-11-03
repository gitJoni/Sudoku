class SudokuSolver:
    def __init__(self, ruudukko:list):
        self.ruudukko = ruudukko

    def missaNolla(self) -> tuple or bool:
        """Finds zero from given list and returns it's place as tuple (x, y).
        If no zero is found, return False.

        Returns:
            tuple or bool: (x, y) or False if no zeros found.
        """
        for x in range(len(self.ruudukko)):
            for y in range(len(self.ruudukko[x])):
                if self.ruudukko[x][y] == 0:
                    return (x, y)
        return False

    def tulostaRuudukko(self):
        """Prints the given list in terminal
        """
        for x in range(len(self.ruudukko)):
            if x % 3 == 0 and x != 0:
                print('-' * 6 + '+' + '-' * 7 + '+' + '-' * 6)
            for y in range(len(self.ruudukko[x])):
                if y % 3 == 0 and y != 0:
                    print('| ', end='')
                print(self.ruudukko[x][y], end=' ')
            print()
        print()
    
    def luoTyhjaRuudukko(self, size:int = 9) -> list:
        """Returns an empty list of given size in argument
        If no arguments are given, default size is 9

        Args:
            size (int): creates square like list of zeros

        Returns:
            list: square list of zeros
        """
        return [[0 for i in range(size)] for j in range(size)]
    
    def sopiikoNumero(self, x:int, y:int, numero:int) -> bool:
        """Tests if the given number is valid to the coordinates of x and y in a list.

        Args:
            x (int): Which row as an integer.
            y (int): Which column as an integer.
            numero (int): Number that will be tested in the given x and y coordinates of the list.

        Returns:
            bool: True or False whether the given number is valid to the given coordinates.
        """
        for i in range(len(self.ruudukko[x])):
            if self.ruudukko[x][i] == numero:
                return False
        for i in range(len(self.ruudukko)):
            if self.ruudukko[i][y] == numero:
                return False
        lootax = x // 3 * 3
        lootay = y // 3 * 3
        for i in range(lootax, lootax + 3):
            for j in range(lootay, lootay + 3):
                if self.ruudukko[i][j] == numero:
                    return False
        return True

    def ratkaise(self) -> bool:
        """Finds the correct pattern for the given list in a recursive way.

        Returns:
            bool: True or False in a recursive way
        """
        nolla = self.missaNolla()
        if nolla:
            x = nolla[0]
            y = nolla[1]
        else:
            return True
        for numero in range(1, 10):
            if self.sopiikoNumero(x, y, numero):
                self.ruudukko[x][y] = numero
                if self.ratkaise():
                    return True
                self.ruudukko[x][y] = 0
        return False


ruudukko = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 3, 6, 0, 0, 0, 0, 0],
            [0, 7, 0, 0, 9, 0, 2, 0, 0],
            [0, 5, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 4, 5, 7, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 3, 0],
            [0, 0, 1, 0, 0, 0, 0, 6, 8],
            [0, 0, 8, 5, 0, 0, 0, 1, 0],
            [0, 9, 0, 0, 0, 0, 4, 0, 0]]

if __name__ == "__main__":
    ruutu = SudokuSolver(ruudukko)
    ruutu.tulostaRuudukko()
    ruutu.ratkaise()
    ruutu.tulostaRuudukko()