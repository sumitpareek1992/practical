from django.shortcuts import render, redirect
from student.forms import ScoreForm
from student.models import Score


# Create your views here.
def home_view(request):
    data = Score.objects.all()
    print(data)
    return render(request, 'home.html', {'data': data})


def index(request):
    if request.method == 'POST':
        form = ScoreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ScoreForm()
    return render(request, 'index.html', {'form': form})
