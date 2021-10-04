from django.urls import path

from newsletter.views import NewsLetterView, SuccessTemplateView

app_name = 'newsletter'

urlpatterns = [
    path(
        '',
        NewsLetterView.as_view(),
        name='newsletter_form',
    ),
    path(
        'success/',
        SuccessTemplateView.as_view(),
        name='success',
    )
]
