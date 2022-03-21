from django.urls import path

from article.views import ArticleAPIView, FeedbackAPIView


urlpatterns = [
    path('', ArticleAPIView.as_view()),
    path('feedback/', FeedbackAPIView.as_view()),
]
