########################################################################
# Python x AI Agent
# class, special operators 類別、特殊運算子
#
# [作業]
# 分數(Fraction)類別
#
# 規劃：撰寫程式制定新的型態(類別)：Fraction，以分數形式表現數字
#    1)屬性：由兩個整數組成 - 分子、分母
#    2)方法：
#      a)加、減、乘(__add__,__sub__,__mul__)
#      b)以分數型式(分子/分母) 印出(print)結果
#      c)算出分數的值(轉成浮點數輸出)
#      c)倒數(invert), 如：2/3 -> 3/2
#
# 問題：請執行以下操作
#    建立實體：half = Fraction(1,2)
#              quarter = Fraction(1,4)
#    1)印出：half = 1/2
#            quarter = 1/4
#            1/2 + 1/4 = 6/8，等於 0.75
#            1/2 - 1/4 = 2/8，等於 0.25
#            1/2 * 1/4 = 1/8，等於 0.125
#    2)印出：2/3 的倒數是 3/2，等於 1.5
#########################################################################

## Methods to add and multiply two Fraction objects
class Fraction(object):
    def __init__(self, top, bottom):
        '''
        Constructor of Fraction class'''


    def __add__(self, other_fraction):
        '''
        Defines special method to implement + operator;
        returns a new Fraction object'''


    def __sub__(self, other_fraction):
        '''
        Defines special method to implement - operator;
        returns a new Fraction object'''


    def __mul__(self, other_fraction):
        '''
        Special method to multiply 2 Fraction objects;
        returns a new Fraction object'''


    def __str__(self):
        '''Method to print a Fraction object'''


    def invert(self):
        '''Method to invert the Fraction object'''


    def value(self):
        '''Method to calculate into a value'''


# +++加入你的程式碼+++
# 呼叫你完成的函數


