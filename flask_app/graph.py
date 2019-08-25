import plotly
import plotly.graph_objs as go
import pandas as pd
import json
import pickle

#data = pd.read_csv("sample.csv")
def create_map(df):
    data = [ 
        go.Scattergeo(
           lon=df['long'],
           lat = df['lat'],
           mode="markers" ,
           locationmode="USA-states",
           hovertext = df['text']
        )   
    ]   

    graphJSON = json.dumps(data,cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON
def create_month_map(df):
    data = [
        go.Scattergeo(
           lon=df['long'],
           lat = df['lat'],
           mode="markers" ,
           locationmode="USA-states",
           hovertext = df['test_text']
        )
    ]

    graphJSON = json.dumps(data,cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def create_table(df):
    #with open("df_copy.pkl","rb") as f:
        #df_stories = pickle.load(f) 
    data = [
        go.Table(
            header=dict(values=['Title of Article'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
            cells=dict(values=[df['title'].values],
                  line_color='darkslategray',
                  fill_color='lightcyan',
                  align='left')
        )
        ]
    graphJSON = json.dumps(data,cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def create_overall_table(df):
    data = [ 
        go.Table(
            header=dict(values=['Subreddit',"Positive Sentiment"],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
            cells=dict(values=[df['subreddit'].values,df['pos'].values],
                  line_color='darkslategray',
                  fill_color='lightcyan',
                  align='left')
        )   
        ]   
    graphJSON = json.dumps(data,cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON
