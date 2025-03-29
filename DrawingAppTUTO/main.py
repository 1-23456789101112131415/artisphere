from artisphere import create_app #name of folder is python package

app=create_app()

if __name__ == '__main__': #checks for imported file are we going to execute
    app.run(debug=True)