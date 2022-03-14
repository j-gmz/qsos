from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Womt
from .forms import WomtForm
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import WomtSerializer


# Create your views here.
class WomtViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Womts to be viewed or edited.
    """
    queryset = Womt.objects.all().order_by('-created_date')
    serializer_class = WomtSerializer
    permission_classes = [permissions.IsAuthenticated]


# class MyLoginRequiredMixin(LoginRequiredMixin):
#     login_url = 'http://127.0.0.1:8000/accounts/login'
    
# class WomtCreateView(MyLoginRequiredMixin, CreateView):
#     template_name = 'womt_record/womt_create.html'
#     queryset = Womt.objects.all()
    
#     def get(self, request, *args, **kwards):

#         form = WomtForm(request.user)
#         context = {"form": form}
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         form = WomtForm(request.user, request.POST)
#         if form.is_valid():
#             form.save()
#         context = {"form": form}
#         return render(request, self.template_name, context)

#     def get_success_url(self):
#         return '/'

# class WomtUpdateView(MyLoginRequiredMixin, UpdateView):
#     template_name = 'womt_record/womt_update.html'
#     model = Womt
#     queryset = Womt.objects.all()

#     fields = [
#         'status',
#         'assigned_to'
#     ]
    
    # def get_object(self):
    #     id_ = self.kwargs.get("pk")
    #     print(id_)
    #     return get_object_or_404(Womt, id=id_)

    # def get(self, request, *args, **kwards):
    #     form = WomtForm(request.user)
    #     context = {"form": form}
    #     return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form = WomtForm(request.user, request.POST)
    #     if form.is_valid():
    #         form.save()
    #     context = {"form": form}
    #     return render(request, self.template_name, context)

# class WomtListView(MyLoginRequiredMixin, ListView):
#     template_name = 'womt_record/womt_list.html'
#     queryset = Womt.objects.all()

# class WomtDetailView(MyLoginRequiredMixin, DetailView):
#     template_name = 'womt_record/womt_detail.html'
#     queryset = Womt.objects.all()
    
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     return get_object_or_404(Womt, id=id_)

# def womt_create_view(request):
#     form = WomtForm(request.user, request.POST or None)
#     if form.is_valid():
#         form.save()
#     print(request)
#     print(request.user)
#     context = {
#         'form': form
#     }
#     return render(request, 'womt_record/womt_create.html', context)

# def womt_detail_view(request, id):
#     obj = get_object_or_404(Womt, id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "womt_record/detail.html", context)

# def womt_list_view(request):
#     queryset = Womt.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, "womt_record/womt_list.html", context)


