from .models import Product, Category
from comments.models import Comment
from comments.forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.views.generic import (
    ListView,
    DetailView,
)


def menu_items(request):
    items = Category.objects.all()
    return dict(items=items)


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    #   ordering = ['-date_posted']
    paginate_by = 8


class CategoryProductListView(ListView):
    model = Product
    template_name = 'products/category_product_list.html'
    context_object_name = 'products'
    #   ordering = ['-date_posted']
    paginate_by = 8

    def get_queryset(self):
        name = get_object_or_404(Category, title=self.kwargs.get('category'))
        return Product.objects.filter(category=name)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail_product.html'
    comment_form = CommentForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        user = self.request.user
        # Add in a QuerySet of all the books
        context['comments'] = Comment.objects.filter(product=product.id)
        if user.is_authenticated:
            context['form'] = self.comment_form
        return context

    def post(self, request, pk, **kwargs):
        if request.method == 'POST':
            form = CommentForm(request.POST)
            product = Product.objects.filter(id=pk)
            if form.is_valid():
                comment = Comment(
                    product=self.get_object(),
                    author=auth.get_user(request),
                    content=form.cleaned_data['comment_area'],
                )
            comment.save()
            return redirect('product-list')


@login_required()
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author == request.user:
        comment.delete()
    return redirect('product-list')
