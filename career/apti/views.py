from django.shortcuts import render
from .services.calc_weights import get_weights, generate_field, normalize_ratings
from career.student.models import StudentBuffer
from career.apti.services.get_student_details import getStudentBuffer
# Create your views here.
def student_dashboard(request,responses):
    student = getStudentBuffer(1)
    # add id
    if student is None:
        return
    student.recommended=generate_field(responses)


