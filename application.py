from flask import Flask ,render_template, request# -*- coding: utf-8 -*-
from datetime import date



app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Amount', methods=['POST'])
def Amount():
    error=''
    borrow_date= request.form.get("borrow_date")
    if((borrow_date == '') | (len(borrow_date.split(','))!=3) ):
        return render_template('home.html', error='Please enter valid borrow date in required format')
    day,month,year= map(int, borrow_date.split(','))
    d0 = date(year,month,day)
    d1 = date.today()#date(2008, 9, 26)
    delta = d1 - d0
    Days=delta.days
    
    intrest= int(request.form.get('intrest_per_100Rupees'))
    if( (intrest <=0)  & (intrest>100) ):
        return render_template('home.html', error='Please enter valid Interest rate')
    item_value=int(request.form.get('item value'))
    if(type(item_value) != int):
        return render_template('home.html', error='** Please enter valid Price')
    #item_value= 5000
    #print(Days)
    total_amount = item_value+((item_value * intrest * Days)/3000)
    return render_template('home.html',current_date=d1, result=total_amount, days=Days, borrow_date=borrow_date, item_value=item_value , intrest=intrest)

@app.route('/Reset' ,methods=['POST'])
def Reset():
    return render_template('home.html', result='', days=0)



if __name__== "__main__":
    app.run(debug=True)
