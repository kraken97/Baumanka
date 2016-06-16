class Table:
    def __init__(self, m, n):
        self.__tbl = [[0]*n for j in range(m)]

    def get_tbl(self):
        return self.__tbl

    def get_row(self, m):
        return self.__tbl[m]

    def get_col(self, n):
        ret = []
        for row in self.__tbl:
            ret.append(row[n])
        return ret

    def set_cell(self,a,b,val):
        self.__tbl[a][b] = val

    def get_cell(self,a,b):
        return self.__tbl[a][b]

a = Table(4,2)
a.set_cell(2,1,3)
print(a.get_col(1))
print(a.get_row(2))