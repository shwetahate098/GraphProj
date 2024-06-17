from flask import Flask ,render_template
import csv

app=Flask(__name__)

csv_file_path='data.csv'

@app.route('/')
def index():
    data=read_csv(csv_file_path)
    return render_template('dashboard.html', data=data)

def read_csv(csv_file):
    with open(csv_file, 'r') as csvfile:
        csv_reader=csv.DictReader(csvfile)
        data=[row for row in csv_reader]
    return data

if __name__== '__main__':
    app.run(debug=True)