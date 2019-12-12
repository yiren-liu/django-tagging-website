from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import FieldError
# Create your views here.
from django.shortcuts import render

from .forms import TaggingForm
from .models import SearchResult

global last_data


def tagging(request):
    global last_data



    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TaggingForm(request.POST)
        # check whether it's valid:
        if not form.is_valid() or form.cleaned_data["data_tag"] not in ["0", "1", "2", "3"]:
            form.add_error("data_tag", ValueError("Wrong input: must input 0, 1, 2, 3"))
            form.clean()

            emptyFlag = True
            # get unlabeled data
            unlabeled = SearchResult.objects.filter(label="")
            if len(unlabeled) != 0:
                unlabeled = unlabeled[0]
                emptyFlag = False
            last_data = unlabeled

        else:
            last_data.label = request.POST['data_tag']
            last_data.save()
            return HttpResponseRedirect('/tagging')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = TaggingForm()

        emptyFlag = True
        # get unlabeled data
        unlabeled = SearchResult.objects.filter(label="")
        if len(unlabeled) != 0:
            unlabeled = unlabeled[0]
            emptyFlag = False
        last_data = unlabeled

    return render(request, 'tagging_template.html', {'form': form, 'unlabeled': unlabeled, 'emptyFlag': emptyFlag})


