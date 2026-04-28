python
import pandas as pd
import plotly.express as px
from flask import Flask, render_template

# Load the dataset
data = pd.read_excel('Distribution_of_Active_Members_2022_0.xlsx')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    # Create a sample visualization for total active members by quarter
    fig = px.bar(data, x='Quarter', y='Total Active Members', title='Total Active Members by Quarter')
    graph_html = fig.to_html(full_html=False)
    return render_template('index.html', graph_html=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
