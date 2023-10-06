from flask import Flask, render_template 
import datetime 
import calendar 
import pytz 
test = Flask(__name__)
#routing at '/'
@test.route('/')
def index():
#Zone based time
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))

    ctime = current_time.strftime("%B %d %Y %H:%M:%S")

    return render_template('index.html', ctime = calendar.day_name[current_time.weekday()] + ', ' +ctime)

if __name__ == '__main__':

    test.run()

