from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, URLField, DateField, TimeField, SelectField
from wtforms.validators import DataRequired, URL, InputRequired, AnyOf, Optional
import csv

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


def validate_time(form, field):
    # if field.data:
        pass


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField(label='Cafe location on Google map(URL)',
                        validators=[URL(require_tld=True,
                                        message="Please enter a valid URL")])
    open_time = StringField(label='Opening Time', validators=[InputRequired(message="Please input a time")])
    close_time = StringField(label='Closing Time', validators=[InputRequired(message="Please input a time")])
    coffee = SelectField(label='Coffee rating',
                         choices=['✘', '☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'],
                         validators=[Optional()])
    wifi = SelectField(label='WiFi strength rating',
                       choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                       validators=[Optional()])
    power = SelectField(label='Power socket availability',
                        choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                        validators=[Optional()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/☕/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        val = form.data
        print(val)
        cafe_details = [item for item in val if item != 'submit' and item != 'csrf_token']
        # for item in val:
        #     if item != 'submit' and item != 'csrf_token':
        print(cafe_details)
        #
                # print(val)
                # print(val[1])
        with open("cafe-data.csv", mode="a", encoding="utf-8") as data:
            data.write("\n")
            for datas in cafe_details:
                # print(datas)
                data.write(f"{val[datas]},")
            print("True")

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

        # print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)

# add_cafe()