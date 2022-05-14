from turtle import width
import pandas as pd
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output, State
import numpy as np
import dash
import base64
import datetime
import io


rating_list = [["sub_ID", "first_rate", "second_rate", "it1", "it2", "it3", "it4"]]
array_rating = np.array(rating_list)
ini_rate = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
ini_df = pd.DataFrame(ini_rate, columns = rating_list[0])
df = ini_df
app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Title"),
    html.Div([
        html.Div([""], style = {'width':'10%', 'height':'100%'}),
        html.Div([
            html.H3("Select Subject:"),
            dcc.Dropdown(options=[
                            {'label': 'sub_1', 'value': 'sub_1'},
                            {'label': 'sub_2', 'value': 'sub_2'},
                            {'label': 'sub_3', 'value': 'sub_3'},
                            {'label': 'sub_4', 'value': 'sub_4'},
                            {'label': 'sub_5', 'value': 'sub_5'},
                        ], 
                        value = 'sub_1', 
                        id='sub-dropdown'),
            html.Br(), 
            html.Br(), 
             
            html.H3("First rate:"),
            dcc.Slider(min=0, max=10, 
            step=0.5, 
            marks = {0:"Good", 10: "Bad"}, 
            
            id='first-rate-slider'),

            html.Br(), 
            html.Br(), 
             
            html.H3("Second rate:"),
            dcc.RadioItems(
                options=[
                    {'label':'Good', 'value':'Good'},
                    {'label':'Moderate', 'value':'Moderate'},
                    {'label':'Bad', 'value':'Bad'}
                    ],
                inline=True,
                
                id='second-rate-slider'),

            html.Br(), 
            html.Br(), 
             
            html.H3("Item 1 error count:"),
            dcc.Input(
                    id="Item-1", 
                    type="number", 
                    placeholder="Item 1 error count",
                    
                    min=0, max=100, step=1,
                ),
            html.Br(), 
            html.Br(), 
             
            html.H3("Item 2 error count:"),
            dcc.Input(
                    id="Item-2", 
                    type="number", 
                    placeholder="Item 2 error count",
                    
                    min=0, max=100, step=1,
                ),
            html.Br(), 
            html.Br(), 
             
            html.H3("Item-3 error count:"),
            dcc.Input(
                    id="Item-3", 
                    type="number", 
                    placeholder="Item 3 error count",
                    
                    min=0, max=100, step=1,
                ),
            html.Br(), 
            html.Br(), 
             
            html.H3("Item 4 error count:"),
            dcc.Input(
                    id="Item-4", 
                    type="number", 
                    placeholder="Item 4 error count",
                    
                    min=0, max=100, step=1,
                ),
            html.Br(),
            html.Br(),
            
            html.Button('Submit', id='submit-val', n_clicks=0)
        ], style = {'width':'40%', 'height':'100%'}),
        html.Div([], style = {'width':'1%', 'height':'100%'}),
        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                # Allow multiple files to be uploaded
                multiple=False
                ),
            html.Div(
                [html.Div([dash_table.DataTable(data=ini_df.to_dict('records'), columns=[{"name": i, "id": i} for i in ini_df.columns])], 
                id = 'showed-labeled-sub'),
                ]),
            html.Br(),
            html.Br(),
            html.H3("Where you want to store your file?"),
            dcc.Input(id="save-path", type="text", placeholder="C:/Users.....", style = {"width":"100%"}),
            html.Br(),
            html.Br(),
            html.Button("Download CSV", id="btn-csv", n_clicks=0),
            html.Br(),
            html.Br(),
            html.Div(id = "save-return")
                ], 
                style = {'width':'40%', 'height':'100%'}),

        html.Div([], style = {'width':'10%', 'height':'100%'})
    ], style = {'display':'flex'})    

])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])

    return df

@app.callback(
    Output('showed-labeled-sub', 'children'),
    Input('submit-val', 'n_clicks'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified'),
    State('sub-dropdown', 'value'),
    State('first-rate-slider', 'value'),
    State('second-rate-slider', 'value'),
    State('Item-1', 'value'),
    State('Item-2', 'value'),
    State('Item-3', 'value'),
    State('Item-4', 'value'),


)
#sub_ID, first_rate, second_rate, it1, it2, it3, it4

def update_output(n_clicks, list_of_contents, list_of_names, list_of_dates, sub_ID, first_rate, second_rate, it1, it2, it3, it4):
    global array_rating
    global rating_list
    global df
    if list_of_contents is not None and n_clicks != 0:

        if sub_ID not in array_rating[:,0] and sub_ID != "sub_ID":
            rating_list.append([sub_ID, first_rate, second_rate, it1, it2, it3, it4])
            array_rating = np.array(rating_list)
            df = pd.DataFrame(array_rating[1:,:], columns = rating_list[0])
            return html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])
        else:
            overlap_index = (np.where(array_rating[:,0] == sub_ID))[0][0]
            array_rating[overlap_index,:] = [sub_ID, first_rate, second_rate, it1, it2, it3, it4]
            array_rating = array_rating
            rating_list = list(array_rating)
            df = pd.DataFrame(array_rating[1:,:], columns = rating_list[0])
            return html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])
    elif list_of_contents is not None and n_clicks == 0:
        rating_list = [["sub_ID", "first_rate", "second_rate", "it1", "it2", "it3", "it4"]]
        df = parse_contents(list_of_contents, list_of_names, list_of_dates)
        array_rating = df.values
        information = array_rating.tolist()
        for info in information:
            rating_list.append(info)
        return html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])
    elif list_of_contents is  None and n_clicks == 0:
        df = ini_df
        return html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])
    elif list_of_contents is  None and n_clicks != 0:
        
        if sub_ID not in array_rating[:,0]:
            rating_list.append([sub_ID, first_rate, second_rate, it1, it2, it3, it4])
            array_rating = np.array(rating_list)
            df = pd.DataFrame(array_rating[1:,:], columns = array_rating[0,:])
            return html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])
        elif sub_ID in array_rating[:,0]:
            overlap_index = (np.where(array_rating[:,0] == sub_ID))[0][0]
            array_rating[overlap_index,:] = [sub_ID, first_rate, second_rate, it1, it2, it3, it4]
            array_rating = array_rating
            rating_list = list(array_rating)
            df = pd.DataFrame(array_rating[1:,:], columns = array_rating[0,:])
            return html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])
        
        
@app.callback(
    Output("save-return", "children"),
    Input("btn-csv", "n_clicks"),
    State("save-path", "value")
)

def func(n_clicks, path):
    global df
    global text_return
    df = df
    text_return = "ready to download"
    if n_clicks != 0:
        try:
            df.to_csv(path + "/OLST_assessment.csv", index = 0)
            text_return = "OLST_assessment.csv is successfully downloaded in " + path + ". Click times: " + str(n_clicks)
        except:
            text_return = "Failed to download"
    return [text_return]
if __name__ == '__main__':
    app.run_server(debug=True)