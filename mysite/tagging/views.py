from django.shortcuts import render
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import FieldError
# Create your views here.
from django.shortcuts import render

from .forms import TaggingForm
from .models import SearchResult, get_model_fields
# global last_data
# last_data = ""


def tagging(request):
    # global last_data

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print(request.POST)
        # create a form instance and populate it with data from the request:
        form = TaggingForm(request.POST)
        # check whether it's valid:
        # print(form.cleaned_data["data_tag"])
        if form.is_valid():
            if form.cleaned_data['data_tag'] in ["0", "1", "2", "3"]:
                unlabeled = SearchResult.objects.get(pk=form.cleaned_data["data_pk"])
                unlabeled.label = form.cleaned_data["data_tag"]
                unlabeled.save()

                return HttpResponseRedirect('/tagging')
            else:
                form.add_error("data_tag", ValueError("Wrong input: must input 0, 1, 2, 3"))
                form.clean()


        # emptyFlag = True
        # get unlabeled data

        unlabeled = SearchResult.objects.filter(label="")
        # last_data = unlabeled

        if len(unlabeled) != 0:
            unlabeled = unlabeled[0]

            form.data_pk = unlabeled.pk
            # form = TaggingForm(initial={'data_pk': unlabeled.pk})

            print(form)


    # if a GET (or any other method) we'll create a blank form
    else:

        form = TaggingForm()

        # emptyFlag = True
        # get unlabeled data

        unlabeled = SearchResult.objects.filter(label="")
        # last_data = unlabeled


        if len(unlabeled) != 0:
            unlabeled = unlabeled[0]

            form = TaggingForm(initial={'data_pk': unlabeled.pk})

            print(form)
            # last_data = unlabeled

            # unlabeled.label = "#"
            # unlabeled.save()
        # if unlabeled.pk in assigned_pk: return HttpResponseRedirect('/tagging')
        #
        # if len(assigned_pk) > 100: assigned_pk.pop(0)

        # assigned_pk.append(unlabeled.pk)

    return render(request, 'tagging_template.html', {'form': form, 'unlabeled': unlabeled})


def reset_test_database(request):
    targets = SearchResult.objects.get(pk = "2")
    targets.label = ""
    targets.save()

    targets = SearchResult.objects.get(pk = "3")
    targets.label = ""
    targets.save()

    targets = SearchResult.objects.get(pk = "4")
    targets.label = ""
    targets.save()

    return HttpResponseRedirect('/tagging')

def download_as_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="AllData.csv"'

    writer = csv.writer(response)
    # write your header first
    writer.writerow([field.name for field in get_model_fields(SearchResult)])

    for obj in SearchResult.objects.all():
        row = []
        for field in get_model_fields(SearchResult):
            row.append(str(getattr(obj, field.name)))
        writer.writerow(row)

    return response