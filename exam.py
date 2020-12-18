class Progression:
    def __init__(self, n):
        self.n = n
        self.a = 3
        self.b = 5

    def summa(self):
        if self.n <= 0:
            raise ValueError
        s = (self.n * (2 * self.a + self.b * (self.n - 1))) / 2
        return s

def main():
    progression = Progression(10)
    print('Сума перших 10 елементів: {summa}'.format(summa=progression.summa()))
    print('Hello! =)')

if __name__ == '__main__':
    main()
