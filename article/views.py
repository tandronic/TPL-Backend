from django.utils.translation import gettext_lazy as _
from rest_framework import filters
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from article.models import Article
from article.serializers import ArticleSerializer, FeedbackSerializer


class ArticleAPIView(ListAPIView):
    queryset = Article.objects.all()
    search_fields = ['tags__name', 'title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)


class FeedbackAPIView(APIView):

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": _("Feedback created.")}, status=status.HTTP_200_OK)
