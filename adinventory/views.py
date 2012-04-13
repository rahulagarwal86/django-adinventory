from core.models import Institute, CourseCategory, CourseSubcategory
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def google_html( request ):
    if request.method == 'POST':
        slug = request.POST['slug']
        sub_cat = request.POST['sub_cat']
        cat = request.POST['cat']
        result = Institute.objects.get( slug = slug )
        try:
            cat_obj = CourseCategory.objects.get( slug = cat )
            cat_slug = cat_obj.slug
        except:
            cat_obj = CourseSubcategory.objects.get( slug = sub_cat )
            cat_slug = cat_obj.category.all()
            cat_slug = ( cat_slug[0] ).slug
        return render_to_response( "adunit/featured_template.html", locals(), context_instance = RequestContext( request ) )
    else:
        inst_list = Institute.objects.filter( display_flag = 1 ).values( 'name', 'slug' )
        cat_list = CourseCategory.objects.values( 'name', 'slug' )
        sub_cat_list = CourseSubcategory.objects.values( 'name', 'slug' )
        return render_to_response( "adunit/inst_dropdown.html", locals(), context_instance = RequestContext( request ) )
# Create your views here.
