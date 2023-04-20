from flask import Flask, render_template, redirect, url_for

#instantiating a flask object -WSGI application
app = Flask(__name__)

#this decorator is for the home page
#the decorator creates the webpages/subpages
@app.route('/')
def welcome():
    ''''
    this function is specific to the home page
    '''
    return "Welcome"

#tutorial 3a
##creating two separate pages - one for success and one for failure
###in these pages we enter a user entered integer parameter called score - generally parameters are string format
@app.route('/success/<int:points>')
def success(points):
    return f"Success at {points}."


@app.route('/failure/<int:points>')
def failure(points):
    return f"Failure at {points}."

#tutorial 3b
##to dynamically select the page based on a user entered parameter
##in the example below, on this page, user entered parameter will call one of the above pages
@app.route('/score/<int:points>')
def score(points):
    if points < 40:
        #redirect function here calls the url for 'failure' or 'success' based on the points
        #below, points= is the required argument from the 'failure' or 'success' webpages & points is value entered by the user
        return redirect(url_for('failure',points=points))
    else:
        return redirect(url_for('success',points=points))

#this ensures the run when called in the terminal
#will need to use ^C to shut the webserver down
if __name__ == '__main__':
    #app.run()
    #the above does not close the server by default if there are changes made
    #below closes the server by default when changes are made to the code and allows refreshing of the browser
    #can specify host and port here
    app.run(debug=True)




