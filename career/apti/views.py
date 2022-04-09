from django.shortcuts import redirect, render
from apti.services.calc_weights import get_weights, generate_field, normalize_ratings
from student.models import StudentBuffer
from apti.services.get_student_details import getStudentBuffer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def student_dashboard(request,responses=None):
    student = getStudentBuffer(1)
    # add id
    # if student is None:
    #     return
    if responses is not None:
        student.recommended=generate_field(responses)
    else:
        return render(request,'dashboard/index.html')

@csrf_exempt
def quizPage(request,student_id=None):
    if request.method == 'POST':
        print(request.POST)
        print(student_id)
        return redirect('login')
    return render(request,'quiz.html')
