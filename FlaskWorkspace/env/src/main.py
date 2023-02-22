#website folder becomes a python package thanks to the __init__ file
from website import create_app


#creating flask application instance
app = create_app()


#only if we run this file, not import it, are we going to run the code below
#the reason is to prevent main.py from running the server when we import it somewhere else
if __name__ == '__main__':
    app.run(debug=True)