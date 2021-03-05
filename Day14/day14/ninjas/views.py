from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Developer, Skill

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ninjas/index.html'
    context_object_name = 'devs'

    def get_queryset(self):
        return Developer.objects.all()

class DetailsView(generic.DetailView):
    model = Developer
    template_name = 'ninjas/details.html'

def level(request, dev_id):
    dev = get_object_or_404(Developer, pk=dev_id)
    try:
        dev_skill = dev.skill_set.get(pk=request.POST['skill'])  
    except(KeyError, Skill.DoesNotExist):
        return render(request, 'ninjas/details.html',{
            'dev' : dev,
            'error_message' : 'No such skill found'
        })
    else:
        dev_skill.level += 1
        dev_skill.save()
        return  HttpResponseRedirect(reverse('ninjas:details', args=(dev.id,)))          
    

