from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm,NewQuestionForm,NewReplyForm,NewResponseForm
from .models import Question, Response
from django.contrib.auth.decorators import login_required
from school.models import SchoolBuffer
from student.models import StudentBuffer

def landingPage(request):
    
    return render(request,'landingpage.html')

# Create your views here.
# function to create a login page
def loginPage(request):
    
     
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=None
    try:
        user=StudentBuffer.objects.get(username=username,password=password)
    except:
        ...
    if user is not None:
        return redirect('student_dashboard',student_id=user.id)
    print(username, password)
    school=None
    try:
        school = SchoolBuffer.objects.get(username=username,password=password)
        if school is not None:
            return redirect('school_dashboard',school_id=school.id)            
    except:
        ...
    if user is not None:
        test=login(request,user)
        print(test)
        return redirect('student_dashboard')
    else :
        # messages.info(request,'Username or password incorrect')
        ...

    context={}
    return render(request,'login.html',context)

#function to display all questions
def forum(request):
    

    questions=Question.objects.all().order_by('-created_at')
    context={'questions':questions}
    return render(request,'forum.html',context)

#function to search question in the forum
def searchForum(request):
    

    if request.method=='POST':
        questionInitials=request.POST.get('questionInitials')

    questions = Question.objects.filter(title__icontains=questionInitials).order_by('-created_at')
    print(questions)
    context = {'questions':questions}
    return render(request,'forum.html',context)


#function to add new question to the forum
def newQuestionPage(request):
    form = NewQuestionForm()

    if request.method=='POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
                messages.success(request, 'Your question has been posted!')
                return redirect('/forum')
        except Exception as e:
            print(e)
            messages.warning(request, 'Something went wrong!')

    context={'form':form}
    return render(request,'newQuestion.html',context)

#fucntion to view the question and its replies
def questionPage(request,id):
    response_form=NewResponseForm()
    reply_form=NewReplyForm()

    if request.method == 'POST':
        try:
            response_form=NewResponseForm(request.POST)
            if response_form.is_valid():
                response=response_form.save(commit=False)
                
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            messages.warning(request, 'Something went wrong!')

    question=Question.objects.get(id=id)
    context={'question':question,'response_form':response_form,'reply_form':reply_form}
    return render(request,'question.html',context)


# function to add response to a question
def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            messages.warning(request, 'Something went wrong!')

    return redirect('forum')

#function to register yourself
def registerPage(request):
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
        return render(request,'register.html',context)
#function to display homepage
def homepage(request):
    
    return render(request,'homepage.html')
