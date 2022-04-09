from student.models import StudentBuffer

def getStudentBuffer(id):
    try:
        student = StudentBuffer.objects.get(id=id)
        return student
    except:
        raise Exception('student details not found')