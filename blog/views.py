from django.shortcuts import render

def sob(request):
    return render(request, 'blog/index.html', {})
