from django.urls import path

from .views import *
from .apiviews import *
from .apiviews import *
#from Project.ProjectApp.Accounts.accountsviews import *
from .Accounts.accountsviews import *

from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/", views.obtain_auth_token, name="login"),

    path("users_list/", UsersList.as_view(), name="AllUsers"),

    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),

    # path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),

    # path("vote/", CreateVote.as_view(), name="create_vote")
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         CreateVote.as_view(), name="create_vote"),

    # views.py
    path("polls0/", polls_list, name="polls_list"),
    path("polls0/<int:pk>/", polls_detail, name="polls_detail"),
]

urlpatterns += router.urls
