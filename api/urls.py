from django.conf.urls import url
from api.views import test
urlpatterns = [
    url(r"^user/$",test.UserViews.as_view())
]