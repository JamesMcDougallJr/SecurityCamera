from app import app
app.jinja_env.cache = {}
if __name__=='__main__':
  app.run(host='0.0.0.0', debug=True)