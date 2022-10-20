from django.urls import path

from subscriptionapp.views import SubscriptionView

app_name = 'subscriptionapp'

urlpatterns = [
    path('subscription/',SubscriptionView.as_view(), name='subscription'),

]