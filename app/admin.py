from django.contrib import admin
from .models import Key, Card, Bin, Item, ReleaseNote
from django import forms

admin.site.site_header = "Assman Administration"
admin.site.site_title = "Assman Administration"
admin.site.register(Key)
admin.site.register(Bin)
admin.site.register(Item)
admin.site.register(Card)

# Release notes form including textarea for body
class ReleaseModelForm(forms.ModelForm):
	note_body = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = ReleaseNote
		fields = '__all__'

# Register release notes to order by date
@admin.register(ReleaseNote)
class ReleseAdmin(admin.ModelAdmin):
	form = ReleaseModelForm
	list_display = ('note_name', 'note_stamp', 'note_body')
	ordering = ('note_stamp', )