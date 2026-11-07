from django.shortcuts import render
from .models import GalleryPhoto


def _base_context():
    return {"quartier_nom": "Mom Sa Rew"}


def home(request):
    context = {
        **_base_context(),
        "valeurs": [
            {
                "numero": "01",
                "titre": "La paix au quotidien",
                "description": "Un quartier où chacun se sent bien, écouté et en sécurité.",
                "icone": "☮",
            },
            {
                "numero": "02",
                "titre": "Le plaisir d'être ensemble",
                "description": "Des voisins qui se connaissent, s'entraident et partagent de bons moments.",
                "icone": "♡",
            },
            {
                "numero": "03",
                "titre": "La joie de participer",
                "description": "Des idées, des rencontres et des initiatives pour faire vivre le quartier.",
                "icone": "✺",
            },
        ],
        "initiatives": [
            {
                "categorie": "Ensemble",
                "titre": "Un coup de main entre voisins",
                "description": "Partager ses talents, donner un peu de son temps et rendre service autour de soi.",
                "icone": "↗",
            },
            {
                "categorie": "Rencontres",
                "titre": "La fête des voisins",
                "description": "Une belle occasion de faire connaissance et de célébrer ce qui nous rassemble.",
                "icone": "♫",
            },
            {
                "categorie": "Cadre de vie",
                "titre": "Un quartier plus accueillant",
                "description": "Prendre soin de nos espaces communs et garder nos rues agréables pour tous.",
                "icone": "✿",
            },
        ],
    }
    return render(request, "accueil/home.html", context)


def histoire(request):
    return render(request, "accueil/histoire.html", _base_context())


def galerie(request):
    context = {
        **_base_context(),
        "photos": GalleryPhoto.objects.all(),
    }
    return render(request, "accueil/galerie.html", context)


def lieux(request):
    context = {
        **_base_context(),
        "cem_photo": GalleryPhoto.objects.filter(lieu="cem").first(),
        "terrain_photo": GalleryPhoto.objects.filter(lieu="terrain").first(),
    }
    return render(request, "accueil/lieux.html", context)
