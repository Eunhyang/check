from rest_framework import serializers

from ..models import Issue, Category, Memo


class ParentCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'name')
        extra_kwargs = {
            'url': {'view_name': 'api:note:category-detail', },
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    parent = ParentCategorySerializer()

    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'parent')
        extra_kwargs = {
            'url': {'view_name': 'api:note:category-detail', },
        }


class ParentIssueSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Issue
        fields = ('url', 'id', 'status', 'content', 'categories')
        extra_kwargs = {
            'url': {'view_name': 'api:note:issue-detail', },
        }


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    parent = ParentIssueSerializer()

    class Meta:
        model = Issue
        fields = ('url', 'id', 'status', 'content', 'categories', 'parent')
        extra_kwargs = {
            'url': {'view_name': 'api:note:issue-detail', },
        }


class MemoSerializer(serializers.HyperlinkedModelSerializer):
    issue = IssueSerializer()

    class Meta:
        model = Memo
        fields = ('url', 'content', 'is_base')
        extra_kwargs = {
            'url': {'view_name': 'api:note:memo-detail', },
        }
