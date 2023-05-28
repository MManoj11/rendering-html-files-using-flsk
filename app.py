from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/first')
def first():
    return render_template('first.html')



@FAI.route('/data')
def data():
    return render_template('data.html',name='abhi',age=21)


if __name__=='__main__':
    FAI.run(debug=True)