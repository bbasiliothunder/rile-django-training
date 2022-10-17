from json import load
from typing import Any, Dict
from django.http import HttpResponse as http_response, HttpRequest as http_request, HttpResponseRedirect as redirect
from django.template import loader
from django.urls import reverse
from members.models import Members


def index(request: http_request) -> http_response:
    main = loader.get_template("main.html")
    return http_response(main.render())

def show_members(request: http_request) -> http_response:
    mymembers: Members = Members.objects.all().values()
    members_page = loader.get_template("who_we_are.html")
    context: Dict[str, Any] = {
        'mymembers': mymembers
    }
    return http_response(members_page.render(context, request))

def add_new_members(request: http_request) -> http_response:
    add_page = loader.get_template("add_new_member.html")
    return http_response(add_page.render({}, request))

def add_new_members_process(request: http_request) -> redirect:
    firstname: str = request.POST['firstname']
    lastname: str = request.POST['lastname']
    new_member: Members = Members(firstname=firstname, lastname=lastname)
    new_member.save()
    return redirect(reverse("show-members"))

def delete_member(request, id: int) -> redirect:
    mymember = Members.objects.get(id=id)
    mymember.delete()
    return redirect(reverse("show-members"))

def update_member(request, id: int) -> http_response:
    mymember = Members.objects.get(id=id)
    update_page = loader.get_template("update_member.html")
    context: Dict[str, Any] = {
        "mymember": mymember,
        "id": id
    }
    return http_response(update_page.render(context, request))

def update_members_process(request: http_request, id: int) -> redirect:
    firstname: str = request.POST['firstname']
    lastname: str = request.POST['lastname']
    mymember = Members.objects.get(id=id)
    mymember.firstname = firstname
    mymember.lastname = lastname
    mymember.save()
    return redirect(reverse("show-members"))

# Create your views here.
