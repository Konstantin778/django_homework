from django.urls import path
from homework.views import binary_sum, sentence_case, lower_case, upper_case, \
    capitalize_each_word, toggle_case, text_replace

urlpatterns = [
    path('binary-sum', binary_sum),
    path('change_case/sentence_case', sentence_case),
    path('change_case/lower_case', lower_case),
    path('change_case/upper_case', upper_case),
    path('change_case/capitalize_each_word', capitalize_each_word),
    path('change_case/toggle_case', toggle_case),
    path('text_replace/', text_replace)
]
