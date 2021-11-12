from django.urls import path, include

from .views import CategoryListView, QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView, \
    AnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('answers', AnswerViewSet)


urlpatterns = [
    # path('categories-list/', category_list),
    path('categories-list/', CategoryListView.as_view()),
    path('questions-list/', QuestionListView.as_view()),
    path('questions-create/', QuestionCreateView.as_view()),
    path('question-update/<int:pk>', QuestionUpdateView.as_view()),
    path('question-delete/<int:pk>', QuestionDeleteView.as_view()),
    path('', include(router.urls))
]
