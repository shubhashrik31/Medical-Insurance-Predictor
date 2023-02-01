from flask import Flask,jsonify,render_template,request
from project_app.utils import MedicalInsurance
import numpy as np
app = Flask(__name__)

####home page
@app.route('/')
def homepage():
    print('Medical Insurance Project')
    return render_template('display.html')


####result.html
@app.route('/predict_charges',methods = ['POST','GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        print(data)
        name=data['name']
        sex=data['sex']
        age = eval(data['age'])
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        print(children)
        smoker = data['smoker']
        region = data['region']
        print(data)
        print(f'age >> {age}, sex >>{sex} , bmi >> {bmi}, children >> {children}, smoker >> no, region >> {region} ')
        med_ins = MedicalInsurance(age, bmi,sex, children,smoker, region)    
        Charges = med_ins.predict_charges()
        return render_template('result.html',name=name,Charges=Charges)
        # return jsonify({f'Hello {name}': f' Your Predicted Medical Insurance Charges are:  RS.{Charges} '})
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)   