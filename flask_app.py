from flask import Flask,render_template,request
import pickle
app=Flask(__name__)

@app.route("/")
def fun1():
    return render_template("titanic.html") # it provides html page as response

@app.route("/predict",methods=["POST","GET"])
def fun2():
    Pclass=float(request.form["PClass"])
    Age=float(request.form["Age"])
    SibSp=float(request.form["SibSp"])
    Parch=float(request.form["Parch"])
    Fare=float(request.form["Fare"])
    Sex_male=float(request.form["Sex_male"])
    Embarked_Q=float(request.form["Embarked_Q"])
    Embarked_S=float(request.form["Embarked_S"])
    mymodel=pickle.load(open("mymodel1.pkl","rb"))
    survival=mymodel.predict([[Pclass, Age, SibSp, Parch, Fare, Sex_male, Embarked_Q,Embarked_S]])[0]
    return "Survival of Person is {}".format(survival)
    

if __name__=="__main__":
    app.run(debug=True)
    
    
    
