from django.shortcuts import render
from django.http import Http404
from polling.models import Poll

# Create your views here.
def list_view(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'index.html', context)

def detail_view(request, id):
    try:
        poll = Poll.objects.get(pk=id)
    except Poll.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        if request.POST.get("vote") == 'Yes':
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()
    context = {'poll': poll}
    return render(request, 'detail.html', context)