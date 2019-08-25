import gpt_2_simple as gpt2

model_name="117M"
gpt2.download_gpt2(model_name=model_name)

highest = gpt2.start_tf_sess()
gpt2.finetune(highest,
             'highest_scores_just_review.csv',run_name="highest",
              model_name=model_name,
              steps=1000)  
gpt2.generate(highest) 


