from django.shortcuts import render

# Create your views here.

def A_a(request):
    return render(request, 'A-a.html')
def A_b(request):
    return render(request, 'A-b.html')
def A_c(request):
    return render(request, 'A-c.html')
def A(request):
    return render(request, 'A.html')
def B(request):
    return render(request, 'B.html')
def B_a(request):
    return render(request, 'B-a.html')
def B_b(request):
    return render(request, 'B-b.html')
def act(request):
    return render(request, 'act.html')
def content(request):
    return render(request, 'content.html')
def create(request):
    return render(request, 'create.html')
def dance(request):
    return render(request, 'dance.html')
def music(request):
    return render(request, 'music.html')
def nature(request):
    return render(request, 'nature.html')
def picture(request):
    return render(request, 'picture.html')
def Qna(request):
    return render(request, 'Qna.html')
def idea(request):
    return render(request, 'idea.html')
def society(request):
    return render(request, 'society.html')
def sports(request):
    return render(request, 'sports.html')
def start(request):
    return render(request, 'start.html')
def startend(request):
    return render(request, 'start.html')

def volunteer(request):
    return render(request, 'volunteer.html')
def listall(request):
    return render(request, 'list.html')