import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

ad_clicks.head(10)

ad_clicks.groupby('utm_source')\
    .user_id.count()\
    .reset_index()

ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()   
  
clicks_by_source = ad_clicks\
   .groupby(['utm_source',
             'is_click'])\
   .user_id.count()\
   .reset_index()

clicks_pivot = clicks_by_source\
   .pivot(index='utm_source',
          columns='is_click',
          values='user_id')\
   .reset_index()
    
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])   
    
ad_clicks.groupby('experimental_group')\
.user_id.count().reset_index()

percentage_clicks = ad_clicks.groupby(['experimental_group', 'is_click',]).user_id.count().reset_index()

percentage_clicks['percentage'] = percentage_clicks['user_id']/ad_clicks.shape[0]

a_clicks= ad_clicks[
   ad_clicks.experimental_group
   == 'A']

b_clicks= ad_clicks[
   ad_clicks.experimental_group
   == 'B']

day_groups= a_clicks.groupby('day').user_id.count().reset_index()

day_groups['percentage'] = day_groups['user_id']/a_clicks.shape[0]



print(clicks_pivot)
