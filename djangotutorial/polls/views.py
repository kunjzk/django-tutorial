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



from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


from .models import Choice, Question


# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

