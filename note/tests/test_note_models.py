from model_mommy.mommy import make as mm

from check.tests.testcase import TestCase
from note.models import Issue, Category, Memo


class TestIssueModels(TestCase):
    def setUp(self):
        self.category = mm(Category, name='배송')
        self.issue = mm(Issue, content='이거 잘 모르겠음', category=self.category)
        self.memo = mm(Memo, name='url 참고하기', issue = self.issue)

    def test_issue(self):
        assert str(self.issue) == '이거 잘 모르겠음'
