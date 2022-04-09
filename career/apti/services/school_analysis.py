import pandas as pd
import plotly
import plotly.express as px
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def graphs():
    df = pd.read_csv('career\School_records.csv')
    df.iloc[:,2:-1].mean()
    go_fig = go.Figure()
    obj = go.Scatter(
        x=list(df.iloc[:,2:-1].columns),
        y=list(df.iloc[:, 2:-1].mean().values),
        mode='lines',
    )
    go_fig.add_trace(obj)
    graph1 = plotly.offline.plot(go_fig, auto_open=False, output_type="div")
    #   graph4 = plotly.offline.plot(fig, auto_open=False, output_type="div")
    context = {"graph": [graph1, graph2, graph3],

               'name': request.user.school,
                'city': request.user.school.city,
                'state': request.user.school.state,
               'rank': request.user.school.rank,
               'happinessindex': request.user.school.happiness_score
               }
    return render(request,'Analytics/dashboard.html',context)
