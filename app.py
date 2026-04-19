from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pages/index.html')

  
@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/services')
def services():
    return render_template('pages/services.html')


@app.route('/projects')
def projects():
    return render_template('pages/projects.html')


@app.route('/gallery')
def gallery():
    return render_template('pages/gallery.html')


@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
