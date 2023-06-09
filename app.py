from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def a():
    return render_template('index.html')

@app.route('/1.html')
def b():
    return render_template('1.html')

@app.route('/13.html')
def z():
    return render_template('13.html')

@app.route('/14.html')
def s():
    return render_template('14.html')

@app.route('/3.html')
def d():
    return render_template('3.html')


@app.route('/17.html')
def e():
    return render_template('17.html')

@app.route('/18.html')
def f():
    return render_template('18.html')

@app.route('/13.html')
def g():
    return render_template('13.html')

@app.route('/50.html')
def h():
    return render_template('50.html')

@app.route('/p.html')
def i():
    return render_template('p.html')

@app.route('/r.html')
def j():
    return render_template('r.html')

@app.route('/t.html')
def k():
    return render_template('t.html')

@app.route('/12.html')
def l():
    return render_template('12.html')

@app.route('/18 - 복사본.html')
def n():
    return render_template('18 - 복사본.html')

@app.route('/18 - 복사본 (2).html')
def m():
    return render_template('18 - 복사본 (2).html')

@app.route('/18 - 복사본 (3).html')
def o():
    return render_template('/18 - 복사본 (3).html')

@app.route('/18 - 복사본 (4).html')
def p():
    return render_template('/18 - 복사본 (4).html')

@app.route('/18 - 복사본 (5).html')
def c():
    return render_template('/18 - 복사본 (5).html')

@app.route('/18 - 복사본 (6).html')
def q():
    return render_template('/18 - 복사본 (6).html')

@app.route('/검색.html')
def r():
    return render_template('검색.html')



@app.route('/execute', methods=['POST'])
def execute():
    dk = int(request.form['dk'])
    b = request.form['b']
    c = request.form['c']
    result = None

    if dk == 1:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = a + i
        result = "%d에서 %d까지 자연수의 합은: %d" % (int(b), int(c), a)
    elif dk == 2:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = i ** 2 + a
        result = "%d²에서 %d²까지 자연수의 합은: %d" % (int(b), int(c), a)
    elif dk == 3:
        i = 0
        a = 0
        for i in range(int(b), int(c) + 1, 1):
            a = i ** 3 + a
        result = "%d³에서 %d³까지 자연수의 합은: %d" % (int(b), int(c), a)
    else:
        result = "다시 입력해주세요"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()
