from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

registered_users = {}
organizations = ['Organization 1', 'Organization 2', 'Organization 3', 'Organization 4', 'Organization 5']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        organization = request.form.get('organization')

        if not name or not organization:
            error = 'Both Name and Organization are required fields.'
            return render_template('home.html', organizations=organizations, error=error)

        if organization not in organizations:
            error = 'Invalid organization selected.'
            return render_template('home.html', organizations=organizations, error=error)

        registered_users[name] = organization
        return redirect(url_for('registered')) 

    return render_template('home.html', organizations=organizations)

@app.route('/registered')
def registered():
    return render_template('registered.html', registered_users=registered_users)
if __name__ == '__main__':
    app.run(debug=True)  
