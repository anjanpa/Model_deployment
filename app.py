from flask import Flask ,render_template,request

import marks
app=Flask(__name__)


@app.route("/",methods=["POST"])
def hello():
	if request.method=="POST":
		rooms=float(request.form["rooms"])
		marks_pred=marks.marks_prediction(rooms)
		mk=marks_pred
	return render_template("index.html",my_price=mk)

# @app.route("/",methods=["POST"])
# def submit():
# 	#HTML file-> python file
# 	if request.method=="POST":
# 		hrs=request.form["hrs"]
# 	#py ->html
# 	return render_template("sub.html",Hours=hrs) #n is paramter to send

if __name__=="__main__":
	app.run(debug=True)


