from django.shortcuts import render

# Create your views here.
def upload_csv(request, school_id):
    if request.method == "POST":
        csv = request.FILES['csv']
        print(school_id)
        lines = csv.read().decode().split('\r\n')
        print(lines)
        for i,line in enumerate(lines):
            try:
                print(line)
                if i == 0 or i == len(lines) -1:
                    continue
                elements = line.split(',')
                print(elements)
                
            except:
                pass
    if request.method == 'GET':
        school_id=school_id
        context={
            'school_id':school_id
        }
        return render(request,'upload_csv.html',context)