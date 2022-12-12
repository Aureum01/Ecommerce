# Import necessary libraries and modules
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings

# Define URL patterns for the website
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about', TemplateView.as_view(template_name='about.html'), name='about'),
    path('products', TemplateView.as_view(template_name='products.html'), name='products'),
    path('prices', TemplateView.as_view(template_name='prices.html'), name='prices'),
]

# Define settings for the website, such as the template directory
settings.configure(
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    }],
)
