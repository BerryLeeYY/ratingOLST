import pandas as pd
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output, State
import numpy as np
import dash
import base64
import io
from dash.exceptions import PreventUpdate

rating_list = [["sub_ID", "first_rate", "second_rate", "rating reason", "it1", "it2", "it3", "it4", "it5", "other comments"]]
array_rating = np.array(rating_list)
ini_rate = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
ini_df = pd.DataFrame(ini_rate, columns = rating_list[0])
df = ini_df

labeled_list = [
                {'label': 'sub_01_EP_W2', 'value': 'sub_01_EP_W2'},
                {'label': 'sub_01_EC_W2', 'value': 'sub_01_EC_W2'},
                {'label': 'sub_02_EP_W2', 'value': 'sub_02_EP_W2'},
                {'label': 'sub_02_EC_W2', 'value': 'sub_02_EC_W2'},
                {'label': 'sub_03_EP_W2', 'value': 'sub_03_EP_W2'},
                {'label': 'sub_03_EC_W2', 'value': 'sub_03_EC_W2'},
                {'label': 'sub_04_EP_W2', 'value': 'sub_04_EP_W2'},
                {'label': 'sub_04_EC_W2', 'value': 'sub_04_EC_W2'},
                {'label': 'sub_05_EP_W2', 'value': 'sub_05_EP_W2'},
                {'label': 'sub_05_EC_W2', 'value': 'sub_05_EC_W2'},
                {'label': 'sub_06_EP_W2', 'value': 'sub_06_EP_W2'},
                {'label': 'sub_06_EC_W2', 'value': 'sub_06_EC_W2'},
                {'label': 'sub_07_EP_W2', 'value': 'sub_07_EP_W2'},
                {'label': 'sub_07_EC_W2', 'value': 'sub_07_EC_W2'},
                {'label': 'sub_08_EP_W2', 'value': 'sub_08_EP_W2'},
                {'label': 'sub_08_EC_W2', 'value': 'sub_08_EC_W2'},
                {'label': 'sub_09_EP_W2', 'value': 'sub_09_EP_W2'},
                {'label': 'sub_09_EC_W2', 'value': 'sub_09_EC_W2'},
                {'label': 'sub_10_EP_W2', 'value': 'sub_10_EP_W2'},
                {'label': 'sub_10_EC_W2', 'value': 'sub_10_EC_W2'},
                {'label': 'sub_11_EP_W2', 'value': 'sub_11_EP_W2'},
                {'label': 'sub_11_EC_W2', 'value': 'sub_11_EC_W2'},
                {'label': 'sub_12_EP_W2', 'value': 'sub_12_EP_W2'},
                {'label': 'sub_12_EC_W2', 'value': 'sub_12_EC_W2'},
                {'label': 'sub_13_EP_W2', 'value': 'sub_13_EP_W2'},
                {'label': 'sub_13_EC_W2', 'value': 'sub_13_EC_W2'},
                {'label': 'sub_14_EP_W2', 'value': 'sub_14_EP_W2'},
                {'label': 'sub_14_EC_W2', 'value': 'sub_14_EC_W2'},
                {'label': 'sub_15_EP_W2', 'value': 'sub_15_EP_W2'},
                {'label': 'sub_15_EC_W2', 'value': 'sub_15_EC_W2'},
                {'label': 'sub_16_EP_W2', 'value': 'sub_16_EP_W2'},
                {'label': 'sub_16_EC_W2', 'value': 'sub_16_EC_W2'},
                {'label': 'sub_17_EP_W2', 'value': 'sub_17_EP_W2'},
                {'label': 'sub_17_EC_W2', 'value': 'sub_17_EC_W2'},
                {'label': 'sub_18_EP_W2', 'value': 'sub_18_EP_W2'},
                {'label': 'sub_18_EC_W2', 'value': 'sub_18_EC_W2'},
                {'label': 'sub_19_EP_W2', 'value': 'sub_19_EP_W2'},
                {'label': 'sub_19_EC_W2', 'value': 'sub_19_EC_W2'},
                {'label': 'sub_20_EP_W2', 'value': 'sub_20_EP_W2'},
                {'label': 'sub_20_EC_W2', 'value': 'sub_20_EC_W2'},
                {'label': 'sub_21_EP_W2', 'value': 'sub_21_EP_W2'},
                {'label': 'sub_21_EC_W2', 'value': 'sub_21_EC_W2'},
                {'label': 'sub_22_EP_W2', 'value': 'sub_22_EP_W2'},
                {'label': 'sub_22_EC_W2', 'value': 'sub_22_EC_W2'},
                {'label': 'sub_23_EP_W2', 'value': 'sub_23_EP_W2'},
                {'label': 'sub_23_EC_W2', 'value': 'sub_23_EC_W2'},
                {'label': 'sub_24_EP_W2', 'value': 'sub_24_EP_W2'},
                {'label': 'sub_24_EC_W2', 'value': 'sub_24_EC_W2'},
                {'label': 'sub_25_EP_W2', 'value': 'sub_25_EP_W2'},
                {'label': 'sub_25_EC_W2', 'value': 'sub_25_EC_W2'},
                {'label': 'sub_26_EP_W2', 'value': 'sub_26_EP_W2'},
                {'label': 'sub_26_EC_W2', 'value': 'sub_26_EC_W2'},
                {'label': 'sub_27_EP_W2', 'value': 'sub_27_EP_W2'},
                {'label': 'sub_27_EC_W2', 'value': 'sub_27_EC_W2'},
                {'label': 'sub_28_EP_W2', 'value': 'sub_28_EP_W2'},
                {'label': 'sub_28_EC_W2', 'value': 'sub_28_EC_W2'},
                {'label': 'sub_29_EP_W2', 'value': 'sub_29_EP_W2'},
                {'label': 'sub_29_EC_W2', 'value': 'sub_29_EC_W2'},
                {'label': 'sub_30_EP_W2', 'value': 'sub_30_EP_W2'},
                {'label': 'sub_30_EC_W2', 'value': 'sub_30_EC_W2'},
                {'label': 'sub_31_EP_W2', 'value': 'sub_31_EP_W2'},
                {'label': 'sub_31_EC_W2', 'value': 'sub_31_EC_W2'},
                        ]

main_layout = html.Div([
        html.Div([dcc.Store(id='loaded-memory'),
                dcc.Store(id='total-memory')
        ], style = {'width':'10%', 'height':'100%'}),
        html.Div([
            html.H1("OLST Assessment Webapp"),
            #html.Button("clear", id='clear', n_clicks=0),
            #html.Br(),
            #html.Br(),
            #html.Div(id = "clear-return"),
            html.H3("Select Subject:"),
            dcc.Dropdown(options=labeled_list,
                        id='sub-dropdown'),
            html.Br(),

            html.H3("First rate:"),
            dcc.Slider(min=0, max=10,
            step=0.5,
            marks = {0:"Good", 10: "Bad"},

            id='first-rate-slider'),

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

            html.H3("Rating reason"),
            dcc.Input(
                    id="rating-reason",
                    type="text",
                    placeholder="e.g., body sway too much... ",
                    style = {"width":"100%"}),
            html.Br(),
            html.H3("1.	Lifting forefoot or heel: "),
            dcc.Input(
                    id="Item-1",
                    type="number",
                    placeholder="Item 1 error count",

                    min=0, max=100, step=1,
                ),
            html.Br(),

            html.H3("2.	Moving hip into more than 30 degrees of flexion or abduction: "),
            dcc.Input(
                    id="Item-2",
                    type="number",
                    placeholder="Item 2 error count",

                    min=0, max=100, step=1,
                ),
            html.Br(),

            html.H3("3.	Stepping, stumbling, or falling: "),
            dcc.Input(
                    id="Item-3",
                    type="number",
                    placeholder="Item 3 error count",

                    min=0, max=100, step=1,
                ),
            html.Br(),
            html.H3("4.	Lifting hands off iliac crests: "),
            dcc.Input(
                    id="Item-4",
                    type="number",
                    placeholder="Item 4 error count",

                    min=0, max=100, step=1,
                ),
            html.Br(),
            html.H3("5.	Remaining out of the test position for more than 5s: "),
            dcc.Input(
                    id="Item-5",
                    type="number",
                    placeholder="Item 5 error count",

                    min=0, max=100, step=1,
                ),
            html.Br(),
            html.H3("Other comments"),
            dcc.Input(
                    id="other-comments",
                    type="text",
                    placeholder="e.g., hard to rate because.... ",
                    style = {"width":"100%"}),
            html.Br(),
            html.Br(),
            html.Button('Submit', id='submit-val', n_clicks=0)
        ], style = {'width':'40%', 'height':'100%'}),
        html.Div([], style = {'width':'1%', 'height':'100%'}),
        html.Div([
            html.H1("   "),
            html.Br(),
            html.Br(),
            html.Br(),
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
            html.H3("Current loaded table (last 5 rows): "),
            html.Div(id = "download-return"),
            html.H3("Current working table: "),
            html.Div(
                [html.Div([dash_table.DataTable(data=ini_df.to_dict('records'), columns=[{"name": i, "id": i} for i in ini_df.columns])],
                id = 'showed-labeled-sub'),
                ]),
            html.Br(),
            html.Button("Download CSV", id="btn-csv", n_clicks=0),
            dcc.Download(id="download-dataframe-csv"),
            html.Br(),
            html.Br(),
            html.Div(id = "save-return")
                ],
                style = {'width':'40%', 'height':'100%'}),

        html.Div([], style = {'width':'10%', 'height':'100%'})
    ], style = {'display':'flex'})

app = Dash(__name__)
#server = app.server



app.layout = html.Div([
                    html.Button("Start", id = "start"),
                    html.Div(id = "main-page")
    ])


@app.callback(
    Output('main-page', 'children'),
    Input('start', 'n_clicks'),
)

def start(n_clicks):
    global array_rating
    global rating_list
    global df
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'start' in changed_id:
        rating_list = [["sub_ID", "first_rate", "second_rate", "rating reason", "it1", "it2", "it3", "it4", "it5", "other comments"]]
        array_rating = np.array(rating_list)
        ini_rate = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
        ini_df = pd.DataFrame(ini_rate, columns = rating_list[0])
        df = ini_df
        return main_layout
    else:
        return [" "]

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
            Output('loaded-memory', 'data'),
            Output('download-return', 'children'),
            Input('upload-data', 'contents'),
            State('upload-data', 'filename'),
            State('upload-data', 'last_modified')
            )

def on_click(list_of_contents, list_of_names, list_of_dates):
    global ini_df
    if list_of_contents is None:
        # prevent the None callbacks is important with the store component.
        # you don't want to update the store for nothing.
        raise PreventUpdate

    df = parse_contents(list_of_contents, list_of_names, list_of_dates)
    array_rating = df.values
    rating_list = array_rating.tolist()
    if df.shape[0] > 5:
        showed_df = df.iloc[-5:]
        return [rating_list, html.Div([
            dash_table.DataTable(data=showed_df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])]
    else:
        showed_df = df
        return [rating_list, html.Div([
            dash_table.DataTable(data=showed_df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])]


@app.callback(
    Output('total-memory', 'data'),
    Output('showed-labeled-sub', 'children'),
    Input('loaded-memory', 'modified_timestamp'),
    Input('submit-val', 'n_clicks'),
    State('total-memory', 'data'),
    State('loaded-memory', 'data'),
    State('sub-dropdown', 'value'),
    State('first-rate-slider', 'value'),
    State('second-rate-slider', 'value'),
    State('rating-reason', 'value'),
    State('Item-1', 'value'),
    State('Item-2', 'value'),
    State('Item-3', 'value'),
    State('Item-4', 'value'),
    State('Item-5', 'value'),
    State('other-comments', 'value')
)

def update_output(loaded_ts, n_clicks, total_memory, loaded_memory, sub_ID, first_rate, second_rate, rating_reason, it1, it2, it3, it4, it5, other_comments):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    
    if n_clicks is None and loaded_ts is None:
        raise PreventUpdate
    if total_memory is None:
        total_memory = ini_rate
        df= pd.DataFrame(total_memory, columns = ["sub_ID", "first_rate", "second_rate", "rating reason", "it1", "it2", "it3", "it4", "it5", "other comments"])
        return [total_memory, html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])]
    else:
        total_memory = total_memory
    if loaded_ts is not None and "submit-val" not in changed_id:
        total_memory = loaded_memory
        curr_content = list(np.array(total_memory)[:,:])
        df= pd.DataFrame(curr_content, columns = ["sub_ID", "first_rate", "second_rate", "rating reason", "it1", "it2", "it3", "it4", "it5", "other comments"])
        return [curr_content, html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])]
        
    elif "submit-val" in changed_id:
        total_memory = total_memory
        if sub_ID not in np.array(total_memory)[:,0] and sub_ID != "sub_ID":
            total_memory.append([sub_ID, first_rate, second_rate, rating_reason, it1, it2, it3, it4, it5, other_comments])
            curr_content = list(np.array(total_memory)[:,:])
            df= pd.DataFrame(curr_content, columns = ["sub_ID", "first_rate", "second_rate", "rating reason", "it1", "it2", "it3", "it4", "it5", "other comments"])
            return [total_memory, html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])]
        elif sub_ID in np.array(total_memory)[:,0] and sub_ID != "sub_ID":
            curr_array = np.array(total_memory)
            overlap_index = (np.where(np.array(total_memory)[:,0] == sub_ID))[0][0]
            curr_array[overlap_index,:] = [sub_ID, first_rate, second_rate, rating_reason, it1, it2, it3, it4, it5, other_comments]
            array_rating = curr_array
            total_memory = list(array_rating)
            curr_content = list(np.array(total_memory)[:,:])
            df= pd.DataFrame(curr_content, columns = ["sub_ID", "first_rate", "second_rate", "rating reason", "it1", "it2", "it3", "it4", "it5", "other comments"])
            return [total_memory, html.Div([dash_table.DataTable(data=df.to_dict('records'), columns=[{"name": i, "id": i} for i in df.columns])])]

@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn-csv", "n_clicks"),
    Input('total-memory', 'modified_timestamp'),
    State('total-memory', 'data'),
)

def func(download_n_clicks, total_ts, total_memory):
    if total_ts is None:
        raise PreventUpdate
    total_memory = total_memory
    curr_content = total_memory
    download_csv = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-csv' in download_csv:
        df = df= pd.DataFrame(curr_content, columns = ["sub_ID", "first_rate", "second_rate", "rating reason", "it1", "it2", "it3", "it4", "it5", "other comments"])
        save_df = df.copy()
        save_df.index = save_df.sub_ID
        save_df = save_df.drop(['sub_ID'], axis = 1)
        return dcc.send_data_frame(save_df.to_csv, "OLST_assessment.csv")

if __name__ == '__main__':
    app.run_server(debug=True)
