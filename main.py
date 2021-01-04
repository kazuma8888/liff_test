
import flask

    
app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def toppage():
    if flask.request.method == 'GET':
        return flask.render_template('toppage.html')
    elif flask.request.method == 'POST':
        name = flask.request.form.get('name')
        print(name)
        return flask.render_template('toppage.html')



if __name__ == '__main__':
    app.run()