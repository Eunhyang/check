from rest_framework.routers import DefaultRouter

from note.api.views import IssueViewSet, CategoryViewSet, MemoViewSet
router = DefaultRouter()
router.register(r'issue', IssueViewSet, base_name='issue')
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'memo', MemoViewSet, base_name='memo')
app_name = 'note'

urlpatterns = router.urls