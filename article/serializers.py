from rest_framework import serializers

from article.models import Article, Tags, Feedback


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'name')


class ArticleSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('text', 'email')
