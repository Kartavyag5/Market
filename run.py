from flask_app import app, create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)