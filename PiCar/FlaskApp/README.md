#Getting Started with Running a Flask Server
This document is a quick start guide to getting a Flask Server up and running on this PiCar.

###What Is Flask?
Flask is a framework for creating light weight and manageable web servers using Python with only a few lines of code.

###Why on PiCar?
This is a good question! Using Flask with a pi / single board computer robot allows a user to start to interact with a PiCar via the web either as a dashboard to display information, an interface to drive a PiCar through the browser or other devices that can make web requests.

###How Do I get Started?
We have already installed the Flask module on the Pi Raspian image your PiCar is currently using.  

####To Run a Flask App:
1. In the command prompt navigate to this FlaskApp directory... `cd /Desktop/PiCar/FlaskApp`
2. add your file name to the variable list with `export FLASK_APP=helloWorld.py`
3. Run the HelloWorld.py Flask app by typing the following command `flask run`
3. Open a browser to http://localhost:5000 and you should see a simple "Hello World" displayed as a webpage. This is your PiCar serving that small bit of information to your local network in the form of a humble webpage.

####Stopping, Editing and Restarting Your app
blah...

####Taking the Next Step:
The hello world example serves up the single two word string of "Hello World" when your browser makes a request to the servers address. To level up the amount of information you can serve in an efficient way would be to have it serve up an html page.

The script `simpleServer.py` is an example of this. It serves up the `index.html` page found in the /templates directory of this project. Open the `index.html` file with nano by typing the following command : `nano index.html` while in the templates directory. You should see the following html...

```
<html>
<h1>This is being served by a PiCar</h1>
My name is _______! I just created a web server using Flask!!!

</html>
```
Insert your name instead of "_____________" and save the file.

You can now move up a level by typing `cd ..` and change your FLASK_APP variable to `serve.py` by typing `export FLASK_APP=serve.py` and hitting enter. Now run the server by typing `flask run`. Once the app runs refresh your http://localhost:5000 page and you should see the webpage change to your html file. 
