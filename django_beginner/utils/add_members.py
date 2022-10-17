import os
import django

from members.models import Members

def populate():
    firstnames = ["Marlon", "Rainbow", "Ripmee", "The"]
    lastnames = ["Diaz", "Dash", "Peace", "Baconator"]

    for index, firstname in enumerate(firstnames):
        member: Members = Members(firstname=firstname, lastname=lastnames[index])
        member.save()

if __name__ == "__main__":

    print("main")
    os.environ.setdefault("DJANGO_SETTING_MODULE", "django_begginer.settings")

    django.setup()

    populate()
