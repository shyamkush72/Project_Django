from django.shortcuts import render


# Create your views here.
def skill_home(request):
    context = {'skills': 'active'}
    return render(request, 'ed/skill.html', context)
