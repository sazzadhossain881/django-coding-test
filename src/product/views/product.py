from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import TemplateView

from product.models import Variant, Product, ProductVariant
from product.forms import  ProductForm
from product.filters import ProductFilter 


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

# class BaseProductView(generic.View):
#     form_class = ProductForm
#     model = Product
#     template_name = 'products/create.html'
#     success_url = 'product/products'


class ProductView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['product'] = True
        context['variants'] = Variant.objects.all()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context

    # def get_queryset(self):
    #     filter_string = {}
    #     print(self.request.GET)
    #     for key in self.request.GET:
    #         if self.request.GET.get(key):
    #             filter_string[key] = self.request.GET.get(key)
    #     return Product.objects.filter(**filter_string)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['variant'] = True
    #     context['request'] = ''
    #     if self.request.GET:
    #         context['request'] = self.request.GET['title__icontains']
    #     return context    

    






# class ProductCreateView(CreateProductView, CreateView):
#     pass
    