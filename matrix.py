# Copyright 2020 by Illnytskiy Victor and Michael Fedoruk, Taras Shevchenko National University of Kyiv
# All rights reserved.
# This file is part of the DevOps lab2020
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.


import copy
import unittest
#Ввід першої матриці

keyR = int(input('Введіть кількість рядків матриці А '))
keyS = int(input('Введіть кількість стовпців матриці А '))
A = []
for i in range(keyR):
    A.append([])
    for j in range(keyS):
        A[i] += [int(input())]
print('\n')

#Ввід другої матриці

keyV = int(input('Введіть кількість рядків матриці В '))
keyB = int(input('Введіть кількість стовпців матриці В '))
B = []
for i in range(keyV):
    B.append([])
    for j in range(keyB):
        B[i] += [int(input())]
        
#Вивід заданих матриць

print('Введені матриці: \n')
print('Матриця А: ')
for i in range(len(A)):
    print(A[i])  
print('Матриця В: ')
for i in range(len(B)):
    print(B[i])  


def minor( A, i, j ):
    M = copy.deepcopy(A)
    del M[ i ]
    for i in range( len( A[0] ) - 1 ):
        del M[ i ] [ j ]
    return M   

def det( A ):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    
    for j in range(n):
        determinant += A[0][j]*signum*det(minor(A, 0, j))
        signum *= -1
    print(determinant)
    return determinant
                     
def matmult(A,B):
    r=[]
    m=[]
    for i in range(len(A)):
        for j in range(len(B[0])):
            sums=0
            for k in range(len(B)):
                sums=sums+(A[i][k]*B[k][j])
            r.append(sums)
        m.append(r)
        r=[]
        
    for i in range(len(m)):
        print(m[i])
    return m

def transp(A):
    for i in range(0,keyR):
        for j in range(i):
            A[i][j],A[j][i]=A[j][i],A[i][j]
    for i in range(0,keyS):
        print(A[i])

def sum1(A,B):
    SUM = []
    for i in range(len(A)):
        
        SUM.append([])
        for j in range(len(A[0])):
            SUM[i] += [int(A[i][j] + B[i][j])]
    for i in range(len(SUM)):
        print(SUM[i])

        
def rez(A,B):
    REZ = []
    for i in range(len(A)):
        REZ.append([])
        for j in range(len(A[0])):
            REZ[i] += [int(A[i][j] - B[i][j])]
    for i in range(len(REZ)):
        print(REZ[i])

print('Множення матриць: ')
matmult(A,B)
print('Дискримінант матриці А: ')
det(A)
print('Траспонована матриця А:')
transp(A)
print('Сума матриць: ')
sum1(A,B)
print( "Різниця матриць: " )
rez(A,B)
print( "\n" )
print('Результати тестування:')





class MyTest(unittest.TestCase): #створення класу для реалізації тестів
    def test_usage1(self):#створення функції для тесту
        self.assertIsNot(A, transp(A))#використання команди self.assertIsNot() для порівняння матриці та транспонованої до неї
    def test_usage2(self):#створення функції для тесту
        self.assertIsNotNone(det( A )) #використання команди self.assertIsNotNone() для перевірки значення дескримінанту
    def test_usage3(self):#створення функції для тесту
        self.assertIsNotNone(matmult(A,B)) #використання команди self.assertIsNotNone для перевірки значення множення
if __name__ == "__main__":
    unittest.main()#команда яка запускає всі тести із заданого модуля


