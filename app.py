from website import db, create_app


app = create_app()
db.create_all(app=create_app())

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=False)
   #app.run(debug=False)
