import pandas as pd
import gpt_2_simple as gpt2
import tensorflow as tf
model_name="117M"

teams = ['nyjets', 'CHIBears', 'cowboys', 'Texans', 'panthers', 'Patriots',
       'LosAngelesRams', 'DenverBroncos', 'steelers', 'Browns',
       'buffalobills', 'miamidolphins', 'GreenBayPackers', 'Seahawks',
       'eagles', 'ravens', 'falcons', 'Tennesseetitans',
       'KansasCityChiefs', '49ers', 'NYGiants', 'bengals', 'detroitlions',
       'minnesotavikings', 'Chargers', 'Jaguars', 'Colts', 'Redskins',
       'oaklandraiders', 'Saints', 'buccaneers', 'AZCardinals']

#for obj,team in zip(models[3:],teams[4:]): 
    #tf.get_variable_scope().reuse_variables()
 #   obj=None
def run_model(team):
        obj = gpt2.start_tf_sess()
        file_name=f"{team}new.csv"
        gpt2.finetune(obj,file_name,run_name=team,model_name="117M",steps=186)
#for team in teams[6:7]:
 #       print(f"running {team}")
  #      run_model(team)
for team in teams[28:29]:

        print(f"running {team}")
        run_model(team)
""" 
    obj = gpt2.start_tf_sess() 
    file_name = f"panthersnew.csv"
    gpt2.finetune(obj,file_name,run_name=teams[4],model_name=model_name,steps=186)
    
    obj1 = gpt2.start_tf_sess() 
    file_name = f"Patriotsnew.csv"
    gpt2.finetune(obj1,file_name,run_name=teams[5],model_name=model_name,steps=186)  
    
    obj2 = gpt2.start_tf_sess()
    file_name = f"{teams[6]}new.csv"
    gpt2.finetune(obj2,file_name,run_name=teams[6],model_name=model_name,steps=186)
    
    obj3 = gpt2.start_tf_sess() 
    file_name = f"{teams[7]}new.csv"
    gpt2.finetune(obj3,file_name,run_name=teams[7],model_name=model_name,steps=186)

    obj4 = gpt2.start_tf_sess() 
    file_name = f"{team}new.csv"
    gpt2.finetune(obj,file_name,run_name=team,model_name=model_name,steps=186)
    
    obj = gpt2.start_tf_sess()
    file_name = f"{team}new.csv"
    gpt2.finetune(obj,file_name,run_name=team,model_name=model_name,steps=186)
"""
