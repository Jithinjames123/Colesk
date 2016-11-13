from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm, UserForm, UserProfileForm, DocumentForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
import os

def main_page(request):
	posts = Post.objects.all()
	return render(request, 'core/main_post.html', {'posts' : posts[::-1]}) #Displaying Post On Main Page

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'core/post_detail.html', {'post' : post})

def networks(request):
	return render(request, 'core/networks.html', {})

def profile(request):
	return render(request, 'core/profile.html', {})		

def my_feed(request):
	return render(request, 'core/my_feed.html', {})	

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == 'POST':
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm(instance = post)
		return render(request, 'core/post_edit.html', {'form' : form})	

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit = False)
			post.docfile.save(content = request.FILES["docfile"],save=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk = post.pk)
	else:
		form = PostForm()
	return render(request, 'core/post_edit.html', {'form' : form})

def login(request):
	if request.method == 'POST':
		username = request.POST[username]
		password = request.POST[password]
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				login(request, user)
				return redirect('main_post')
			else:
				return HttpResponse('Your account is  currently deactivated')
		else:
			print('Invalid login credentials: {0}, {1}'.format(username, password))
			return HttpResponse("Invalid Login Credentials")		
	else:
		return render(request, 'core/login.html', {} )			


	return render(request, 'core/login.html', {})	

def sign_up(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.post)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit = False)
			profile.user = user
 
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print( user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'core/sign_up.html', {'user_form' : user_form, 
		'profile_form' : profile_form, 'registered' : registered})				 
	