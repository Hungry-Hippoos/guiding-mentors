from django.shortcuts import redirect, render
from apti.services.calc_weights import get_weights, generate_field, normalize_ratings
from student.models import StudentBuffer
from school.models import SchoolBuffer
from apti.services.get_student_details import getStudentBuffer
from django.views.decorators.csrf import csrf_exempt
from .services.skills import skills
import pandas as pd
import json
import plotly
import plotly.express as px
import os
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Create your views here.
def student_dashboard(request,responses=None,student_id=None):
    student = getStudentBuffer(student_id)
    df = pd.read_csv('School_records.csv')
    student_data = df[df.Id == student_id].iloc[:,2:-1]
    fig = go.Figure([go.Bar(x=list(student_data.columns), y=list(student_data.iloc[0,:].values))])
    graph2 = plotly.offline.plot(fig, auto_open=False, output_type="div")
    #   graph4 = plotly.offline.plot(fig, auto_open=False, output_type="div")
    context = {"graph": graph2,
               'school': student.school,
               'name': student.name,
                'roll': student.id,
                'age': student.age,
               'standard': student.standard,
               'field': student.recommended,
               'interest': student.q4,
               'skills': student.skills
               }
    return render(request, 'student-dashboard.html', context)
    # # add id
    # # if student is None:
    # #     return
    # if responses is not None:
    #     student.recommended=generate_field(responses)
    # else:
    #     return render(request,'student-dashboard.html')

def school_dashboard(request,responses=None,school_id=None):
    df = pd.read_csv('School_records.csv')
    df.iloc[:,2:-1].mean()
    go_fig = go.Figure()
    obj = go.Scatter(
        x=list(df.iloc[:,2:-1].columns),
        y=list(df.iloc[:, 2:-1].mean().values),
        mode='lines',
    )
    go_fig.add_trace(obj)
    graph1 = plotly.offline.plot(go_fig, auto_open=False, output_type="div")
    school = SchoolBuffer.objects.get(id = school_id)
    #   graph4 = plotly.offline.plot(fig, auto_open=False, output_type="div")
    students = StudentBuffer.objects.all()
    fields = []
    for student in students:
        fields.append(student.recommended)
    g2 = go.Figure(go.Pie(labels=["Science","Commerce","Arts"],values=[43,27,30]))
    graph2 = plotly.offline.plot(g2, auto_open=False, output_type="div")
    context = {"graph": graph1,
               'name': school.name,
                'roll': school.id,
                'board': school.board,
               'graph2': graph2
               }
    return render(request, 'school-dashboard.html', context)


@csrf_exempt
def quizPage(request,student_id=None):
    if request.method == 'POST':
        print(request.POST)
        data = {
            'q1':json.loads(request.POST['0'])['ans'],
            'q2': json.loads(request.POST['1'])['ans'],
            'q3': json.loads(request.POST['2'])['ans'],
            'q4': json.loads(request.POST['3'])['ans'],
            'q5': json.loads(request.POST['4'])['ans'],
            'q6': json.loads(request.POST['5'])['ans'],
            'q7': json.loads(request.POST['6'])['ans']
        }
        print(data)
        print(student_id)
        if student_id is None:
            return redirect('login')
        student = getStudentBuffer(student_id)
        student.q1=",".join(data['q1'])
        student.q2=",".join(data['q2'])
        student.q3=",".join(data['q3'])
        student.q4=",".join(data['q4'])
        student.q5=",".join(data['q5'])
        student.q6=",".join(data['q6'])
        student.q7=",".join(data['q7'])
        ski=[]
        for i in data['q5']:
            print(list(skills.keys())[int(i)])
            ski+=skills[list(skills.keys())[int(i)]]
        student.skills=",".join(ski)
        student.recommended = generate_field(data)
        print("Recommended: ", student.recommended)
        try:
            student.save()
            return redirect('student_dashboard',student_id=student.id)
        except:
            print('hello world')
            return redirect('login')
    print(student_id)
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
