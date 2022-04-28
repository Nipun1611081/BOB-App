from flask import Flask, render_template, request
import pandas as pd
app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    file= request.form['qa']
    data=pd.read_excel(file).head(5)
    return render_template('data.html', data = data.to_html())
    

if __name__ == "__main__":
    app.run(debug=True)