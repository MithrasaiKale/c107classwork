import plotly.graph_objects as po
import pandas as pd

df = pd.read_csv("data.csv")


#df.loc will help us filter out all the rows with the given student id

student_df = df.loc[ df["student_id"] == "TRL_abc" ]

print( student_df.groupby("level")["attempt"].mean() )
fig= po.Figure( po.Bar(
    x= student_df.groupby("level")["attempt"].mean() , 
    y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
    orientation='h'
))
fig.show()
