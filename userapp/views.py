from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from userapp.forms import CustomUserCreationForm


class SignUp(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")

    def get(self, request):
        """"""
        return render(
            request,
            "userapp/signup.html",
            {
                "signupform": self.form_class,
            },
        )
