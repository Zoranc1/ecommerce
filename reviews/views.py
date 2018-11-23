from django.shortcuts import render,redirect
from .models import review
from .forms import reviewForm


# Create your views here.

def make_review(request,id):
    
    if request.method =='POST':
        saved_review=reviewForm(request.POST)
        savedReview = saved_review.save(commit=False)
        savedReview.author =request.user
        savedReview.product_id =id
        
        
        savedReview.save()
        review_blog = savedReview
        
        return redirect('products_detail',id=id,)
    else:
        
        form= reviewForm()
   
    
        return render(request,'reviews/review.html',{'form':form})

