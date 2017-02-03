from django.shortcuts import render
from .models import Group
from .forms import GroupForm
from django.http import JsonResponse
from django.views.generic import View

class CreateGroup(View):
	def get(self, request):
		group_list = Group.objects.all()
		return render(self.request, 'index.html', {'groups': group_list})

	def post(self, request):
		form = GroupForm(self.request.POST, self.request.FILES)
		if form.is_valid():
			group = form.save()
			data = {'is_valid': True, 'name': group.file.name, 'url': group.file.url}
		else:
			data = {'is_valid': False}
		return JsonResponse(data)
