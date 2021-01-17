from django.shortcuts import render, redirect
from feedback.forms import CreateFeedback
from account.models import Account
from django.contrib import messages

def feedback_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateFeedback(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        user = Account.objects.filter(username=user.username).first()
        obj.user = user
        obj.save()
        messages.success(request, 'Hvala Vam na povratnoj informaciji.')
        return render(request, 'feedback/feedback_confirm.html')

    context['form'] = form

    return render(request, "feedback/feedback.html", {})


def feedback_confirm_view(request):
    return render(request, 'feedback/feedback_confirm.html')
