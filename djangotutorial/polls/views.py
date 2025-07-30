"""
When somebody requests a page from your website – say, 
“/polls/34/”, Django will load the mysite.urls Python module because it’s 
pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and 
traverses the patterns in order. After finding the match at 'polls/', it strips off 
the matching text ("polls/") and sends the remaining text – "34/" – to the ‘polls.urls’ 
URLconf for further processing. There it matches '<int:question_id>/', resulting in a 
call to the detail() view like so:

detail(request=<HttpRequest object>, question_id=34)
The question_id=34 part comes from <int:question_id>. 
Using angle brackets “captures” part of the URL and sends it as a 
keyword argument to the view function. The question_id part of the string defines 
the name that will be used to identify the matched pattern, and the int part is a 
converter that determines what patterns should match this part of the URL path. The colon (:) separates the converter and pattern name.

"""


from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html",  context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)