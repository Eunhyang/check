from django.contrib.auth import get_user_model
from model_mommy import mommy


def make_user(username=None, email=None, password='password', is_admin=False, **kwargs):
    kwargs.update({'_model': get_user_model()})
    if username:
        kwargs['username'] = username
    if email:
        kwargs['email'] = email
    user = mommy.make(**kwargs)
    if is_admin:
        user.is_superuser = True
        user.is_staff = True
    user.set_password(password)
    user.save()
    return user
