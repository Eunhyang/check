from rest_framework import viewsets
from .serializers import IssueSerializer, CategorySerializer, MemoSerializer
from ..models import Issue, Category, Memo

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerializer

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all().order_by('-id')
    serializer_class = IssueSerializer

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all().order_by('-id')
    serializer_class = MemoSerializer