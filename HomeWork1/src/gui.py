from appJar import gui
import sys
import importlib

sys.path.append('../')
q = importlib.import_module("quadratic-equation-mhasan-v3.quadratic")
app = None
values = {
    "a" : 0,
    "b" : 0,
    "c" : 0
}

result = {
    "x1" : 0.0,
    "x2": 0.0
}

'''
sets up the gui with all the appropriate entires and buttons
'''
def setupGui(app):
    app.addLabelEntry("a")
    app.addLabelEntry("b")
    app.addLabelEntry("c")

    app.addLabelEntry("x1")
    app.addLabelEntry("x2")
    app.addButtons(["Submit", "Exit"], buttonCB)

'''
callback executed when one of the button is pressed
'''

def buttonCB(button):
    global values
    if button == "Exit":
        app.stop()
    else:
        values["a"] = int(app.getEntry("a"))
        values["b"] = int(app.getEntry("b"))
        values["c"] = int(app.getEntry("c"))
        printVal(app)

'''
this is executed to set the values of the output entries (if there is no value present, None is output)
'''

def displayResult(app,result):
    app.setEntry("x1",result["x1"])
    app.setEntry("x2",result["x2"])

'''
calculates the result from the module, gets the result as a tuple.
'''
    
def printVal(app):
    res = q.calculate(values["a"],values["b"],values["c"])
    if res == ():
        result["x1"] = None
        result["x2"] = None
    else:
        result["x1"] = res[0]
        result["x2"] = res[1]
    displayResult(app,result)

'''
init function for the gui
'''

def init():
    global app
    app = gui()
    setupGui(app=app)
    app.go()

if __name__ == "__main__":
    init()
