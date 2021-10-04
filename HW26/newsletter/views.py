from django.views.generic import FormView, TemplateView
from newsletter.forms import NewsLetterForm


class NewsLetterView(FormView):
    template_name = 'newsletter/form.html'
    form_class = NewsLetterForm
    success_url = '/newsletter/success'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SuccessTemplateView(TemplateView):
    template_name = 'newsletter/success.html'
