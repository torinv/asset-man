from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django import forms
from django.template import RequestContext
from django.views.defaults import page_not_found
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Key, Card, Bin, Item

# Custom form classes
class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['item_name', 'item_location', 'item_qty', 'item_longdescription']
		widgets = {
			'item_longdescription' : forms.Textarea()
		}

class BinForm(forms.ModelForm):
	class Meta:
		model = Bin
		fields = ['bin_name', 'bin_location', 'bin_contents' ]
		widgets = {
			'bin_contents' : forms.Textarea()
		}
		
# Items views
class ItemList(LoginRequiredMixin, ListView):
	model = Item

class ItemDetail(LoginRequiredMixin, DetailView):
	model = Item

class ItemCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
	permission_required = 'app.add_item'
	model = Item
	form_class = ItemForm
	success_url = reverse_lazy('item_list')

class ItemUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = 'app.change_item'
	model = Item
	form_class = ItemForm
	success_url = reverse_lazy('item_list')

class ItemDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
	permission_required = 'app.delete_item'
	model = Item
	success_url = reverse_lazy('item_list')

class ItemSearchResultsView(LoginRequiredMixin, ListView):
	model = Item
	template_name = 'app/item_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Item.objects.filter(
				Q(item_name__icontains=query) | Q(item_longdescription__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")


# Keys views
class KeyList(LoginRequiredMixin, ListView):
	model = Key

class KeyDetail(LoginRequiredMixin, DetailView):
	model = Key

class KeyCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
	permission_required = 'app.add_key'
	model = Key
	fields = ['key_name', 'key_location', 'key_owner']
	success_url = reverse_lazy('key_list')

class KeyUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = 'app.change_key'
	model = Key
	fields = ['key_name', 'key_owner', 'key_location']
	success_url = reverse_lazy('key_list')

class KeyDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
	permission_required = 'app.delete_key'
	model = Key
	success_url = reverse_lazy('key_list')

class KeySearchResultsView(LoginRequiredMixin, ListView):
	model = Key
	template_name = 'app/key_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Key.objects.filter(
				Q(key_name__icontains=query) | Q(key_owner__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")


# Cards views
class CardList(LoginRequiredMixin, ListView):
	model = Card

class CardDetail(LoginRequiredMixin, DetailView):
	model = Card

class CardCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
	permission_required = 'app.add_card'
	model = Card
	fields = ['card_name', 'card_owner', 'card_location']
	success_url = reverse_lazy('card_list')

class CardUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = 'app.change_card'
	model = Card
	fields = ['card_name', 'card_owner', 'card_location']
	success_url = reverse_lazy('card_list')

class CardDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
	permission_required = 'app.delete_card'
	model = Card
	success_url = reverse_lazy('card_list')

class CardSearchResultsView(LoginRequiredMixin, ListView):
	model = Card
	template_name = 'app/card_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Card.objects.filter(
				Q(card_name__icontains=query) | Q(card_owner__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")


# Items views
class BinList(LoginRequiredMixin, ListView):
	model = Bin

class BinDetail(LoginRequiredMixin, DetailView):
	model = Bin

class BinCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
	permission_required = 'app.add_bin'
	model = Bin
	form_class = BinForm
	success_url = reverse_lazy('bin_list')

class BinUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
	permission_required = 'app.change_bin'
	model = Bin
	form_class = BinForm
	success_url = reverse_lazy('bin_list')

class BinDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
	permission_required = 'app.delete_bin'
	model = Bin
	success_url = reverse_lazy('bin_list')

class BinSearchResultsView(LoginRequiredMixin, ListView):
	model = Bin
	template_name = 'app/bin_search_results.html'

	def get_queryset(self):
		if self.request.GET.get('q'):
			query = self.request.GET.get('q')
			object_list = Bin.objects.filter(
				Q(bin_name__icontains=query) | Q(bin_contents__icontains=query)
			)
			return object_list

		else: raise ValueError("Invalid search query")


# Help/about view
class Help(LoginRequiredMixin, TemplateView):
	template_name = 'app/help.html'

class About(LoginRequiredMixin, TemplateView):
	template_name = 'app/about.html'


# Custom error views
def handler403(request, exception):
	return render_to_response('app/403.html')

def handler404(request, exception):
	return render(request, 'app/404.html')

def handler500(request):
	response = render_to_response("app/500.html")
	response.status_code = 500
	return response
