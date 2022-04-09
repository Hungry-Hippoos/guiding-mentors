from django.shortcuts import redirect, render
from apti.services.calc_weights import get_weights, generate_field, normalize_ratings
from student.models import StudentBuffer
from apti.services.get_student_details import getStudentBuffer
from django.views.decorators.csrf import csrf_exempt
from .services.skills import skills
import pandas as pd
import plotly
import plotly.express as px
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Create your views here.
def student_dashboard(request,responses=None):
    student = getStudentBuffer(1)
    # add id
    # if student is None:
    #     return
    if responses is not None:
        student.recommended=generate_field(responses)
    else:
        return render(request,'student-dashboard.html')

@csrf_exempt
def quizPage(request,student_id=None):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST
        print(student_id)
        if student_id is None:
            return redirect('login')
        student = getStudentBuffer(student_id)
        student.q1=",".join(data['0'])
        student.q2=",".join(data['1'])
        student.q3=",".join(data['2'])
        student.q4=",".join(data['3'])
        student.q5=",".join(data['4'])
        student.q6=",".join(data['5'])
        student.q7=",".join(data['6'])
        ski=[]
        for i in data['4']:
            ski+=skills[i]
        student.skills=",".join(ski)
        student.recommended = generate_field(data)
        try:
            student.save()
            return redirect('student_dashboard')
        except:
            return redirect('login')
    return render(request,'quiz.html')


def graph_student(request):
    df = pd.read_csv('career\School_records.csv')
    print(request.user.id)
    student_data = df[df.Id == request.user.id].iloc[:,2:-1]
    fig = go.Figure([go.Bar(x=list(student_data.columns), y=list(student_data.iloc[0,:].values))])
    graph2 = plotly.offline.plot(fig, auto_open=False, output_type="div")
    #   graph4 = plotly.offline.plot(fig, auto_open=False, output_type="div")
    context = {"graph": [graph1, graph2, graph3],
               'name': request.user.school,
                'city': request.user.school.city,
                'state': request.user.school.state,
               'rank': request.user.school.rank,
               'happinessindex': request.user.school.happiness_score
               }
    return render(request,'Analytics/dashboard.html',context)
