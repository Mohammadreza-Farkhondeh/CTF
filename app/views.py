import django.views.decorators.csrf
import jwt
from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def level1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not (username or password):
            raise ValidationError("username and password must be provided", 400)
        if username == 'm7arm4n':
            if password == "*#spider!":
                response = redirect(reverse("level3"))
                response.set_cookie("A", "da4b9237bacccdf19c0760cab7aec4a8359010b0")
                response.set_cookie("B", "12dea96fec20593566ab75692c9949596833adc9")
                return response
            else:
                jwt_token = jwt.encode({"username": "m7arm4n"}, "*#spider!")
                response = HttpResponse()
                response['X-Password'] = jwt_token
                return response
        else:
            return HttpResponse("username does not exist.", status=401)
    elif request.method == "GET":
        return render(request, 'login.html')


def level3(request):
    cookie_a = request.COOKIES.get('A')
    cookie_b = request.COOKIES.get('B')

    if cookie_a == '356a192b7913b04c54574d18c28d46e6395428ab' and \
            cookie_b == 'd033e22ae348aeb5660fc2140aec35850c4da997':
        if request.method == "POST":
            secret = request.POST.get("secret")
            if secret == "opp3nh3im3r":
                return redirect(reverse('level4'))
        elif request.method == "GET":
            return render(request, 'index.html')
    else:
        return HttpResponse("Access denied. Cookies A and B do not match expected values.", status=401)


def level4(request):
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        if entered_code == 'tob3y_m4guire':
            return redirect(reverse('level5'))
        else:
            return HttpResponse("Incorrect code. Try again.", status=401)
    else:
        return render(request, 'level4.html')


def level5(request):
    if request.method == 'GET':
        user_name = request.GET.get('name')
        if user_name:
            if 'iframe' in user_name or 'src=' in user_name:
                if 'file:///etc/passwd' in user_name:
                    return redirect('level6')
                else:
                    return HttpResponse("Access denied. Invalid 'name' parameter.", status=401)
            else:
                # Render an HTML page that says "Hi {name}"
                return render(request, 'level5.html', {'user_name': user_name})
        else:
            return HttpResponse("Missing 'name' parameter. Please provide a 'name'.", status=400)
    else:
        return HttpResponse("Unsupported method.", status=405)


def level6(request):
    if 'HTTP_HOST' in request.META and request.META['HTTP_HOST'] == 'localhost':
        # Check if the request includes the expected header
        return HttpResponse("/CH3rN08Y1")
    else:
        return HttpResponse("""Only Accessible from local <!--<?php\n if ($_SERVER['HTTP_HOST'] !== 'localhost')
         {\n\thttp_response_code(403); // Forbidden\n\techo "Only Accessible from local";
         \n\t exit;\n}\necho "/<censored>"\n?>-->""",
                            status=403)


def level7(request):
    # Check if the "background" cookie is set
    background_color = request.COOKIES.get('background')

    if background_color:
        if background_color == "#ffffff":
            message = """I'm a cipher technique, a digital veil,A key you hold, a secret to unveil.In the realm of codes,
            I play my role,Encrypting messages, like a secret scroll.My key, a word, in a disaster's name,Chernobyl's shadow,
            in history's flame.With XOR I dance, bits twist and twirl,Unraveling secrets in a digital swirl.What am I,
            this cryptographic lore?With "chernobyl" key, I do implore."What am I, and what's the key that I adore?
            </br></br></br></br>"I am the absence of color, a shade so deep,In the dark of night, my secrets I keep.
            A void of light, a canvas blank,I'm the color that's often used to prank.What am I, this enigmatic hue?
            A shadow's partner, I'm hiding in plain view."What am I?"""
        elif background_color == "#000000":
            message = "#MC?|E<6R="
        else:
            message = """I am pure as snow, yet I am not cold.
            I am often worn in weddings, pure and bold.
            You can find me in pearls, shining so bright.
            What am I, hiding in plain sight?"
            What am I?'"""

        response = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Background Color Changer</title>
            <style>
                body {{ background-color: {background_color}; }}
            </style>
        </head>
        <body>
            <p>{message}</p>
        </body>
        </html>
        '''
        return HttpResponse(response)
    else:
        return HttpResponse('No "background" cookie set!', status=404)


def level8(request):
    if 'HTTP_IF_MATCH' in request.META:
        if request.META['HTTP_IF_MATCH'] == 'admin':
            return HttpResponse("/5H3r10CK", content_type='text/plain')
        else:
            return HttpResponse("Nice Shot but not enough", content_type='text/plain')
    else:
        return HttpResponse("<strong>If</strong> you were <strong>Match</strong> the admin user", content_type='text/html')

@csrf_exempt
def level9(request):
    if request.method == 'PROPFIND':
        return HttpResponse("/4rC4N3", content_type='text/plain')
    else:
        return HttpResponse("Retrieve my properties from my WebDAV", content_type='text/plain')
