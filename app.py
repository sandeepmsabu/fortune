from flask import Flask, request, redirect, render_template
import sqlite3

app = Flask(__name__)


# Database function to insert contact information
def insert_contact(name, phone, email, message):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('INSERT INTO contacts (name, phone, email, message) VALUES (?, ?, ?, ?)',
              (name, phone, email, message))
    conn.commit()
    conn.close()


# Home page route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        message = request.form['message']

        print(f"Inserting contact: {name}, {phone}, {email}, {message}")  # Debugging line
        insert_contact(name, phone, email, message)
        return redirect('/')

    return render_template('index.html')
#home
@app.route('/')
def home():
    return render_template('index.html')
# Gallery page route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


# Service page route
@app.route('/service')
def service():
    return render_template('service.html')


# Blog page route
@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

def insert_contact(name, phone, email, message):
    try:
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('INSERT INTO contacts (name, phone, email, message) VALUES (?, ?, ?, ?)',
                  (name, phone, email, message))
        conn.commit()
    except Exception as e:
        print(f"Error inserting data: {e}")  # Debugging line
    finally:
        conn.close()

@app.route('/contacts')
def show_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts')
    contacts = c.fetchall()
    conn.close()
    return render_template('contacts.html', contacts=contacts)


if __name__ == '__main__':
    app.run(debug=True)

