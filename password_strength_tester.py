# 简易密码强度测试器 - Python代码示例
# 这个简单的Web应用使用Flask框架，评估密码的强度
# 请确保安装了Flask (`pip install flask`) 来运行这个示例

from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML模板，包含一个简单的表单用于输入密码
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Password Strength Tester</title>
</head>
<body>
    <h2>Password Strength Tester</h2>
    <form method="post">
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Test Password">
    </form>
    {% if strength %}
        <p>Password strength: {{ strength }}</p>
    {% endif %}
</body>
</html>
'''

def test_password_strength(password):
    """简单的密码强度测试函数"""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    # 简单评分系统，基于满足的条件数
    score = sum([has_upper, has_lower, has_digit, has_special, length >= 8])

    # 转换分数为强度描述
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = ""
    if request.method == 'POST':
        password = request.form['password']
        strength = test_password_strength(password)
    return render_template_string(HTML_TEMPLATE, strength=strength)

if __name__ == '__main__':
    app.run(debug=True)
