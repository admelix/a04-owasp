from flask import Flask, render_template, request, redirect, make_response
import os
import csv
from datetime import datetime
from models import credenciales

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        filename = save_data(name, email)
        return redirect(f'/?filename={filename}')  
    return render_template('index.html', filename=request.args.get('filename'))

@app.route('/download', methods=['GET'])
def download():
    filename = request.args.get('filename')  
    with open(f'/tmp/{filename}', 'rb') as f:  
        data = f.read()
    resp = make_response(data)
    resp.headers['Content-Disposition'] = 'attachment; filename=ejemplo_owasp.csv'
    resp.mimetype = 'text/csv'
    return resp

def save_data(name, email):
    now = datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{name}_{timestamp}.csv'
    filepath = os.path.join('/tmp', filename)
    with open(filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Name', 'Email'])
        csvwriter.writerow([name, email])
    return filename

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=8000)
