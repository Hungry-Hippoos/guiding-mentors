from django.shortcuts import redirect, render
from apti.models import RecordBuffer
from school.forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def upload_csv(request, school_id):
    if request.method == "POST":
        csv = request.FILES['csv']
        print(school_id)
        record = RecordBuffer()
        record.file=csv
        record.school_id=school_id
        try:
            record.save()
            return redirect('login')
        except:
            raise Exception("Could not save record")
    if request.method == 'GET':
        school_id=school_id
        context={
            'school_id':school_id
        }
        return render(request,'upload_csv.html',context)
    
def schoolRegisterPage(request):
        form=CreateUserForm
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'account created')
                return redirect('login')

        context={
            "form":form,
        }
        return render(request,'registerschool.html',context)