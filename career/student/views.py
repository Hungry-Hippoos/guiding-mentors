from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm,NewQuestionForm,NewReplyForm,NewResponseForm
from .models import Question, Response
from django.contrib.auth.decorators import login_required
from school.models import SchoolBuffer

def landingPage(request):
    
    return render(request,'landingpage.html')

# Create your views here.
def loginPage(request):
    
     
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request,username=username,password=password)
    school=None
    try:
        school = SchoolBuffer.objects.get(username=username,password=password)
        if school is not None:
            return redirect('student_dashboard')            
    except:
        ...
    if user is not None:
        login(request,user)
        return redirect('student_dashboard')
    else :
        messages.info(request,'Username or password incorrect')


    context={}
    return render(request,'login.html',context)
@login_required(login_url='/login')
def forum(request):
    if request.user.is_anonymous:
        return redirect('/login')

    questions=Question.objects.all().order_by('-created_at')
    context={'questions':questions}
    return render(request,'forum.html',context)

@login_required(login_url='/login')
def searchForum(request):
    if request.user.is_anonymous:
        return redirect('/login')

    if request.method=='POST':
        questionInitials=request.POST.get('questionInitials')

    questions = Question.objects.filter(title__icontains=questionInitials).order_by('-created_at')
    print(questions)
    context = {'questions':questions}
    return render(request,'forum.html',context)


@login_required(login_url='/login')
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


def questionPage(request,id):
    response_form=NewResponseForm()
    reply_form=NewReplyForm()

    if request.method == 'POST':
        try:
            response_form=NewResponseForm(request.POST)
            if response_form.is_valid():
                response=response_form.save(commit=False)
                response.user=request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            messages.warning(request, 'Something went wrong!')

    question=Question.objects.get(id=id)
    context={'question':question,'response_form':response_form,'reply_form':reply_form}
    return render(request,'question.html',context)


@login_required(login_url='login')
def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            messages.warning(request, 'Something went wrong!')

    return redirect('forum')

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
def homepage(request):
    
    return render(request,'homepage.html')