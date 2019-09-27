# GPT Generated NFL-subreddit comments

A couple of weeks ago, a friend told me about the pushshift reddit comment database, an all-encompassing reddit comment dataset going back to 2005. As an avid sports fan, I had a strong interest in researching the differences in comment activity between subreddits for different American sports teams.   
&nbsp;
## Project Scope

With the NFL season fast-approaching, I honed in on subreddits for NFL teams as I figured the analysis would be especially interesting during this exciting time for fans. In particular, I wanted to make an interactive map where fans can look at sentiment and topics over time and view relevant news stories related to their teams that were published during that time. I also set out to independently train 32 GPT-2 models for each NFL team that would generate comments in the style of that subreddit. The goal of the GPT-2 portion of the project was just to see if the model could replicate humorous takes that are representative of the stereotypical attitude and culture of a given team’s fanbase.


&nbsp;

### Home Screen 
![Home Screen](https://github.com/sethweiland/reddit_nfl_comments/blob/master/football_home_page.png)

&nbsp;  

### Monthly Sentiment/Topics Map with NFL stories from that month
![Monthly Sentiment](https://github.com/sethweiland/reddit_nfl_comments/blob/master/monthly_sentiment_with_stories.png)

&nbsp;

### Input Parameters for the GPT-2 model to generate text


![Input bot parameters](https://github.com/sethweiland/reddit_nfl_comments/blob/master/bot_screen_input.png)

&nbsp;

### GPT-2 Model ouptut for the jets @ temperature=0.7

![jets-output](https://github.com/sethweiland/reddit_nfl_comments/blob/master/sample_jets_output.png)
