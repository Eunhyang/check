from model_mommy.mommy import make as mm

from check.tests.testcase import TestCase
from note.models import Issue, Category, Memo


class TestIssueModels(TestCase):
    def setUp(self):
        self.category = mm(Category, name='배송')
        self.issue = mm(Issue, content='이거 잘 모르겠음', categories=[self.category], status = 1)
        self.memo = mm(Memo, content='url 참고하기', issue = self.issue)

    def test_issue(self):
        assert str(self.issue) == '이거 잘 모르겠음'
        assert self.issue.status == 1
        issue2 = mm(Issue, content = '하위 이슈', parent = self.issue)
        assert issue2.parent == self.issue
        issue3 = mm(Issue, content='세번째 이슈', parent=issue2)
        assert issue3.parent.parent == self.issue

    def test_memo(self):
        assert str(self.memo) == 'url 참고하기'
        assert not self.memo.is_base
        self.memo.is_base = True
        assert self.memo.is_base