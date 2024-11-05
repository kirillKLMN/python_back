from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, CreateAPIView

from main.models import Task, Command, Project
from main.serializer import ProjectSerializer


class ProjectList(ListAPIView, CreateAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        queryset = Project.objects.filter(leader = self.request.user)
        return queryset







