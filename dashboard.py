#Imports
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

#Reading the dataset
data = pd.read_csv('data/PCOS_data.csv')  #Source: Kaggle, Owner: Shreyas Vedpathak

#Dash app initilization 
app = Dash(__name__)

#Layout
app.layout = html.Div([
    html.H1('PCOS Health Dashboard'),
    
    dcc.Dropdown(
        id='indicator-dropdown',
        options=[
            {'label': 'BMI vs PCOS', 'value': 'BMI_PCOS'}, #First Toggle Title 
            {'label': 'Age Distribution by PCOS', 'value': 'Age_PCOS'}, #Second Toggle Title
            {'label': 'Blood Pressure by PCOS', 'value': 'BP_PCOS'}, #Third Toggle Title
            {'label': 'Follicle Size Distribution', 'value': 'Follicle_PCOS'} #Forth Toggle Title
        ],
        value='BMI_PCOS',
        clearable=False
    ),
    dcc.Graph(id='indicator-graph')
])

#Callback to update the graph
@app.callback(
    Output('indicator-graph', 'figure'),
    [Input('indicator-dropdown', 'value')]
)
def update_graph(selected_indicator):
    if selected_indicator == 'BMI_PCOS': #First Toggle Graph
        fig = px.box(data, x='PCOS (Y/N)', y='BMI', title='BMI vs PCOS')
    elif selected_indicator == 'Age_PCOS': #Second Toggle Graph
        fig = px.histogram(data, x='Age (yrs)', color='PCOS (Y/N)', title='Age Distribution by PCOS')
    elif selected_indicator == 'BP_PCOS': #Third Toggle Graph
        fig = px.scatter(data, x='BP _Systolic (mmHg)', y='BP _Diastolic (mmHg)', color='PCOS (Y/N)',
                         title='Blood Pressure by PCOS', labels={'BP _Systolic (mmHg)': 'Systolic', 'BP _Diastolic (mmHg)': 'Diastolic'})
    elif selected_indicator == 'Follicle_PCOS': #Forth Toggle Graph
        fig = px.violin(data, y=['Follicle No. (L)', 'Follicle No. (R)'], color='PCOS (Y/N)',
                        title='Follicle Number Distribution by PCOS')
    return fig

#Running
if __name__ == '__main__':
    app.run_server(debug=True)
