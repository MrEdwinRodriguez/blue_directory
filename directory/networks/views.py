from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from django.core.urlresolvers import reverse
from django.view import generic

from networks.models import Network, NetworkMember

class CreateNetwork(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Network

class SingleGroup (generic.DetailView):
    model = Network

class ListGroups(generic.ListView):
    model = Network