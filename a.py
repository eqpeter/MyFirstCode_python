from flask import Flask

# 建立 Flask 應用程式實例
app = Flask(__name__)

# 處理加法的路由（兩個數字相加）
@app.route('/add/<float:num1>/<float:num2>')
def add(num1, num2):
    result = num1 + num2
    return f'{result}'

# 處理乘法的路由（兩個數字相乘）
@app.route('/mul/<float:num1>/<float:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f'{result}'

# 處理總和的路由（可處理任意數量的數字）
@app.route('/sum/<path:numbers>')
def sum_numbers(numbers):
    # 將數字字串分割並轉換為浮點數列表
    num_list = [float(num) for num in numbers.split('/')]
    result = sum(num_list)
    return f'{result}'

# 處理無效運算的預設路由
@app.route('/<path:invalid_path>')
def invalid_operation(invalid_path):
    return '不正確的運算子'

if __name__ == '__main__':
    app.run(debug=True)