from flask import Flask, render_template_string, request   # Importing the Flask modules 
from gpiozero import Robot 
from time import sleep      # Import sleep module from time library 

app = Flask(__name__)
robot = Robot(left=(18,3), right=(15,14))
#HTML Code 
TPL = '''
<html>
    <head><title>Web Page Controlled Robot</title></head>
    <body>
    <h2> Web Page to Control Robot</h2>
        <form method="POST" action="test">
            <h3> Use the button to control motors  </h3>
            <input type="submit" name="forward" value="forward">
            <input type="submit" name="backward" value="backward">
            <input type="submit" name="left" value="left">
            <input type="submit" name="right" value="right">
        </form>
    </body>
</html>

'''
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST","GET"])
def forward():
    if request.method == 'POST':
        fwd = request.form.get('forward')
        bwd = request.form.get('backward')
        lt = request.form.get('left')
        rt = request.form.get('right')
        if fwd == "forward":
            print('fwd')
        elif bwd == "backward":
            print('bwd')

    return render_template_string(TPL)
# Run the app on the local development server
if __name__ == "__main__":
    app.run()