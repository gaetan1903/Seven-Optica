import eel 

eel.init('view')

@eel.expose
def hello(word):
    return 'Hello World again ' + word


eel.start('index.html', size=(1000, 600), position=(175, 75), mode=None)