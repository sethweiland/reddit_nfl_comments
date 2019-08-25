import gpt_2_simple as gpt2

model_name="117M"
gpt2.download_gpt2(model_name=model_name)

high_score = gpt2.start_tf_sess()
gpt2.finetune(high_score,
             'high_scores_just_review.csv',run_name="high",
              model_name=model_name,
              steps=1000)  
gpt2.generate(high_score) 


