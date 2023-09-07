from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Rakha Fahim Shahab',
        'class': 'PBP KI'
    }

    return render(request, 'main.html', context)