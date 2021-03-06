from django.shortcuts import render  #For render templates
from DjangoApp1.models import Bares, Tapas
from DjangoApp1.forms import UserForm, UserProfileForm, TapaForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from datetime import datetime
from django.template import Context, Template,  RequestContext
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from django.http import JsonResponse
from django.shortcuts import redirect


''' Basic index
def index(request):
    return HttpResponse("Hello world!")
'''

#Now we show an index with templates

def index(request):
    context = RequestContext(request)
    #Ordenamos los bares en orden descendente por nombre
    bares_list = Bares.objects.order_by('-nombre')
    context_dict = {'bares': bares_list}

    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits


    response = render(request,'DjangoApp1/index.html', context_dict)

    return response

def mainpage(request):
    #Ordenamos los bares en orden descendente por nombre
    bares_list = Bares.objects.order_by('-nombre')
    context_dict = {'bares': bares_list}

    # Render the response and send it back!
    return render(request, 'DjangoApp1/mainpage.html', context_dict)

def bares(request, bar_name_slug):
    context = RequestContext(request)
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:

        bar = Bares.objects.get(slug=bar_name_slug)
        context_dict['bar_nombre'] = bar.nombre
        tapas = Tapas.objects.filter(bar=bar)
        context_dict['tapas'] = tapas
        context_dict['bar'] = bar          
        counter = bar.num_visitas + 1
        bar.num_visitas = counter
        context_dict['num_visitas'] = bar.num_visitas
        bar.save()
       
    except Bares.DoesNotExist:

        pass

        
       # Go render the response and return it to the client.
    return render_to_response('DjangoApp1/bar.html', context_dict, context)

def about(request):
	return render(request, 'DjangoApp1/about.html')


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the User

 #instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'DjangoApp1/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/DjangoApp1/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'DjangoApp1/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/DjangoApp1')

def profile(request):
    # Go render the response and return it to the client.
    return render(request, 'DjangoApp1/profile.html')

@login_required
def like_bar(request):
    bar_id = None
    if request.method == 'GET':
        bar_id = request.GET['bar_slug']
    likes = 0
    if bar_id:
        bar = Bares.objects.get(slug=bar_id)
        if bar:
	        likes = bar.likes + 1
	        bar.likes = likes
	        bar.save()
    return HttpResponse(likes)   

@login_required
def like_tapas(request):
    tapas_id = None
    if request.method == 'GET':
        tapas_id = request.GET['tapas_id']
    likes = 0
    if tapas_id:
        tapa = Tapas.objects.get(id=int(tapas_id))
        if tapa:
	        likes = tapa.likes + 1
	        tapa.likes = likes
	        tapa.save()
    return HttpResponse(likes) 

@login_required    
def add_tapa(request, bar_name_slug):

    try:
        bar = Bares.objects.get(slug=bar_name_slug)
    except Bares.DoesNotExist:
                bar = None

    if request.method == 'POST':
        form = TapaForm(request.POST)
        if form.is_valid():
            if bar:
                tapa = form.save(commit=False)
                tapa.bar = bar
                tapa.likes = 0
                tapa.save()
                # probably better to use a redirect here.
                return redirect('add_tapa',bar_name_slug)
        else:
            print (form.errors)
    else:
        form = TapaForm()

    context_dict = {'form':form, 'bar': bar}

    return render(request, 'DjangoApp1/add_tapa.html', context_dict)

def reclama_datos(request):
	list_bar = Bares.objects.order_by('nombre')
	datos={}
	datos[0]=list()
	datos[1]=list()
	datos[2]=list()
	for bar in list_bar:
		datos[0].append(bar.nombre)
		datos[1].append(bar.num_visitas)
		datos[2].append(bar.likes)
	return JsonResponse(datos, safe=False)
