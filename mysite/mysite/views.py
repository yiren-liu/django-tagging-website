from django.http import HttpResponseRedirect


def redirect_tagging(request):
    return HttpResponseRedirect('/tagging/')