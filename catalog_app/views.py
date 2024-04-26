from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import View
from .models import ProductCategory, Product


class CategoriesPageView(View):
    def get(self, request):
      context = {
        "page_title" : "Категории товаров",
        #"page_subtitle" : "Связано с любовью"  
        "categories" : ProductCategory.objects.all()
      }
      return render(request, "catalog_app/categories_template.html", context)
    
class ProductsByCategoryView(View):
  def get(self, request, category_id):
    this_category = get_object_or_404(ProductCategory, pk=category_id)
    context = {
      "page_title" : f'Все продукты в категории:',
      "page_subtitle" : this_category.name,
      "products" : get_list_or_404(Product, category=this_category)
    }      
    return render(request, "catalog_app/products_overview_template.html", context)


class ProductByIdView(View):
  def get(self, request, product_id):    
    product = get_object_or_404(Product, pk=product_id)
    context = {
      "page_title" : product.name,
      #"page_subtitle" : this_category.description,
      "product" : product, 
    }      
    print()
    return render(request, "catalog_app/product_card_template.html", context)
  