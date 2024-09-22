from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Image
from .forms import ImageForm

class ImageListView(ListView):
    model = Image
    template_name = 'index.html'
    context_object_name = 'images'

    def get_queryset(self):
        return Image.objects.all().order_by('-created_at')




class ImageCreateView(LoginRequiredMixin, CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'image_form.html'
    success_url = reverse_lazy('image_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ImageDeleteView(LoginRequiredMixin, DeleteView):
    model = Image
    template_name = 'image_confirm_delete.html'
    success_url = reverse_lazy('image_list')

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)
