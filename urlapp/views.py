from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from .models import Url
from .forms import UrlForm


class UrlView(generic.ListView):

    model = Url
    template_name = 'urlapp/home.html'
    context_object_name = 'urls'

    def get_context_data(self, **kwargs):
        context = super(UrlView, self).get_context_data(**kwargs)
        context['form'] = UrlForm
        return context


class UrlCreateView(generic.View):
    template_name = 'urlapp/result.html'
    context = {}

    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            self.context['message'] = 'Url cadastrada com sucesso'
            form.save()
        return render(
            request,
            template_name=self.template_name,
            context=self.context
        )


class UrlRequestView(generic.View):

    def get(self, request, id=None):
        if id:
            url = Url.objects.get(short_id=id)
            url.counter += 1
            url.save()
            return redirect(url.full_url)
        else:
            return redirect('/home/')
