from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Member, User, MovieData
from rank_bm25 import BM25Okapi
import pandas as pd
from .utils import get_loaded_data # Import only get_loaded_data


@csrf_protect
def members(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if confirm_password == None:
            confirm_password = password
        print(email_id)
        print(password)
        print(confirm_password)
        person = User.objects.all()
        if any(user1.email == email_id for user1 in person):
            return HttpResponse('User with this email already exists')
        if password != confirm_password:
            return HttpResponse('Confirm Password is not same as password given')

        user1 = User(email=email_id, password=password)
        user1.save()
        return render(request, 'search.html')

def landing(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request=request))

@csrf_protect
def signup(request):
        return render(request, 'signup.html', )


def signin(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render(request=request))

@csrf_protect
def members1(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        password = request.POST.get('password')

        print(email_id)
        print(password)
        person = User.objects.all()
        if any(user1.email == email_id and user1.password == password for user1 in person):
            return render(request, 'search.html')
        if any(user1.email != email_id for user1 in person):
            return HttpResponse('User doesnot exist')




def search(request):
    if request.method == 'GET':
        # Ensure data is loaded (lazy loading)
        maindata_df, bm25_model = get_loaded_data() # Call the getter function

        title = request.GET.get('movie_title', '').lower()  # Convert input to lowercase
        title = ' '.join(title.split())  # Remove extra spaces
        global fetch_movie
        fetch_movie = '' # Initialize fetch_movie here
        
        # maindata_df and bm25_model are now directly assigned by get_loaded_data()

        print(f"[views.py] maindata_df is None: {maindata_df is None}")
        print(f"[views.py] bm25_model is None: {bm25_model is None}")

        if maindata_df is None or bm25_model is None:
            # Handle case where data is not loaded (e.g., empty DB on startup)
            print("Movie data or BM25 model not loaded. Please ensure data is imported.")
            return render(request, 'result.html', {'movie_ids': []})
        
        print("[views.py] First 5 rows of maindata_df:\n", maindata_df.head())

        if 'suggestion' in request.GET:
            suggestions = maindata_df['title'].str.lower().str.contains(request.GET['suggestion'].lower()).tolist()
            suggestions = [title for title, match in zip(maindata_df['title'], suggestions) if match][:10]
            print(suggestions)
            if len(suggestions) > 0:
                fetch_movie = suggestions[0]
            print(fetch_movie)
            return JsonResponse({'suggestions': suggestions})

        print(fetch_movie)

        def get_top_similar_movie_ids(movie_title, n=10):
            movie_content = \
            maindata_df.loc[maindata_df['title'].apply(lambda x: x.lower() == movie_title), 'tags'].iloc[0]
            scores = bm25_model.get_scores(movie_content.split())  # Split movie content into lowercase tokens
            top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:n]  # Include top N
            return [str(movieid).zfill(7) if len(str(movieid)) < 7 else str(movieid) for movieid in
                    maindata_df.iloc[top_indices]['movieid']]

        if title in maindata_df['title'].values:
            movie_title = title
        elif len(fetch_movie) != 0:
            movie_title = fetch_movie
        else:
            movie_title = title
        print(movie_title)

        if movie_title in maindata_df['title'].values:
            top_similar_movie_ids = get_top_similar_movie_ids(movie_title)
        else:
            return render(request, 'result.html', {'movie_ids': []})

        return render(request, 'result.html', {'movie_ids': top_similar_movie_ids})
    return render(request, 'result.html')

def hello(request):
    return render(request, 'hello.html')
