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

class Fraction(object):
  def __init__(self, top, bottom):
      '''
      分數類別的構造函數，初始化分子和分母
      '''
      self.num = top
      self.den = bottom

  def __add__(self, other_fraction):
      '''
      定義特殊方法實現加法運算，返回一個新的分數對象
      '''
      new_num = self.num * other_fraction.den + self.den * other_fraction.num
      new_den = self.den * other_fraction.den
      return Fraction(new_num, new_den)

  def __sub__(self, other_fraction):
      '''
      定義特殊方法實現減法運算，返回一個新的分數對象
      '''
      new_num = self.num * other_fraction.den - self.den * other_fraction.num
      new_den = self.den * other_fraction.den
      return Fraction(new_num, new_den)

  def __mul__(self, other_fraction):
      '''
      定義特殊方法實現乘法運算，返回一個新的分數對象
      '''
      new_num = self.num * other_fraction.num
      new_den = self.den * other_fraction.den
      return Fraction(new_num, new_den)

  def __truediv__(self, other_fraction):
      '''
      定義特殊方法實現除法運算，返回一個新的分數對象
      '''
      new_num = self.num * other_fraction.den
      new_den = self.den * other_fraction.num
      return Fraction(new_num, new_den)

  def __str__(self):
      '''
      方法來打印分數對象
      '''
      return f"{self.num}/{self.den}"

  def invert(self):
      '''
      方法來倒轉分數對象
      '''
      return Fraction(self.den, self.num)

  def value(self):
      '''
      方法來計算分數的值
      '''
      return self.num / self.den

  def value_as_str(self):
      '''
      方法來計算分數的值並以字串形式返回（小數點後面沒有0）
      '''
      value = self.num / self.den
      if value.is_integer():
          return str(int(value))
      else:
          return f"{value:.3f}".rstrip('0').rstrip('.')

# +++加入你的程式碼+++
# 呼叫你完成的函數

# 假設我們有以下股票的市場價格和每月配息
market_price = Fraction(1100, 1)  # 市場價格 1100 元/股
monthly_dividend_per_share = Fraction(15, 10)  # 每月每股配息 1.5 元（用15/10表示）

# 計算每年的總配息
annual_dividend_per_share = monthly_dividend_per_share * Fraction(12, 1)
print(f"台積電股價1100元\n計畫改月配息每股: {monthly_dividend_per_share.value_as_str()} 元")
print(f"每年可獲股息: 等於 {annual_dividend_per_share.value_as_str()} 元")

# 計算殖利率
dividend_yield = annual_dividend_per_share / market_price
print(f"殖利率: 等於 {dividend_yield.value_as_str()}%")
# 評論
print()
print("評論: \n台積電股配息太低了?\n還是股價漲太高?")


