import numpy as np
from flask import Flask,request,jsonify
import flask
from flask import send_file
#from table import ItemTable,Item
import pandas as pd
import pickle
#from lightgbm import LGBMClassifier
import csv
from graph import create_map,create_table,create_month_map,create_overall_table
import gpt_2_simple as gpt2
from process_text import convert_name

app = Flask(__name__)



@app.route("/",methods=['POST','GET'])
def home():
        return flask.render_template("main_menu.html")



@app.route("/see_map", methods=['POST','GET'])
def map():
    with open("pickled_map_df","rb") as f:
        df_map = pickle.load(f) 
    my_map = create_map(df_map) 
    with open("obj_happy.pkl","rb") as f:
        df_happy = pickle.load(f) 
    happy_table = create_overall_table(df_happy)  
    return flask.render_template("show_map.html",
                                 plot=my_map,
                                 table=happy_table
                                )

@app.route("/see_month_map",methods=['POST','GET'])
def month_map():
    with open("df_final_2.pkl","rb") as f:
        df_final = pickle.load(f)
    month = request.form["month"]
    year = request.form['year']
    month=str(month)
    year=str(year) 
    year_month = str(month) + " " + str(year)
    #title=f"Sentiment and Topics during {year_month}"
    df_of_interest = df_final.loc[df_final['year_month']==year_month]
    #print(df_of_interest.shape)
    my_map = create_month_map(df_of_interest) 
    
    with open("df_copy.pkl","rb") as f:
        df_stories = pickle.load(f) 
    df_of_interest_stories = df_stories.loc[df_stories['year_month']==year_month]
    #df_of_interest_stories = df_of_interest_stories.sample(50) 
    #print(df_of_interest_stories.shape)
    #print(df_of_interest_stories.columns) 
    my_table = create_table(df_of_interest_stories) 

    return flask.render_template("show_month_map.html",
                                 plot=my_map,
                                 table=my_table,
                                )

@app.route("/generate_text",methods=['POST','GET'])
def receive_input():
    return flask.render_template("get_info.html",gif="/static/styles/logos/giphy.gif") 

@app.route("/generate_comment",methods=["POST","GET"])
def generate_comment():
    model_name="117M"
    team_form = request.form['team']
    team = convert_name(team_form) 
    team_lower = team_form.lower() 
    temp = request.form['temperature']
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess,run_name=team) 
    single_text = gpt2.generate(sess,nsamples=1,temperature=float(temp),return_as_list=True)[0]
    single_text = single_text.replace("<|startoftext|>","\n")
    single_text = single_text.replace("<|endoftext|>","\n")
    format_src = f"/static/styles/logos/{team_lower}.png"
    return flask.render_template("show_comment.html",text = single_text,team=format_src)    



if __name__ == '__main__':
    app.run(port=5000,debug=True)
