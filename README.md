# Créer une plateforme pour amateurs de Nutella

Ce site propose à l'utilisateur des substituts alimentaires plus sains pour la santé.
L'utilisateur peut aussi créer un compte afin de sauvegarder un substitut en favoris.

## Getting Started

Créer votre environnement virtuel puis copier ce repo sur votre système.

### Prerequis

Installer tous les packages en tapant:

```
pip install -r pur_beurre/requirements.txt
```
Puis créer les modèles avec:

```
cd pur_beurre/
python manage.py migrate
```

Remplisser la base de données via le shell de Django:

```
python manage.py shell
```

Une fois dans le shell, taper:

```
exec(open('myapp/products.py').read())
```

Vous pouvez lancer le projet en local avec:

```
python manage.py runserver
```

## Tests

Pour lancer les tests, taper:

```
python manage.py test
```

Si vous voulez avoir une couverture de tests, vous pouvez taper:

```
coverage run --source='.' manage.py test myapp
coverage html
```
Puis accéder au fichier index.html dans le dossier htmlcov qui a été créé 

### Acceder au site en ligne

Vous pouvez aussi accéder au site en ligne via le lien:

https://projet8-purbeurre.herokuapp.com

