import os
from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=template_path)




# Initialize database
def init_db():
    conn = sqlite3.connect('what.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS what (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            
            problem TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()




@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        
        problem = request.form['problem']
        

        conn = sqlite3.connect('what.db')
        c = conn.cursor()
        # Prevent duplicate submissions
        
        c.execute(
                "INSERT INTO what (problem) VALUES (?)",
                (problem, )
            )
        conn.commit()
        message = "شكرا لك على ثقتك بنا، تم تسجيل مشكلتك بنجاح!"
        
        conn.close()

    return render_template('index.html', message=message)






if __name__ == "__main__":
    print("Flask server is starting...")  # for debugging
    app.run(host='0.0.0.0', port=5000, debug=True)







if __name__ == "__main__":
    print("Flask server is starting...")  # for debugging
    app.run(host='0.0.0.0', port=5000, debug=True)
