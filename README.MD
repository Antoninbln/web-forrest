# web-run-forest
L'idée est de rendre disponible dans un client web une API simple de classification basée sur RandomForest.
L'utilisateur peut ainsi uploader un dataset et saisir les clés (colonnes) qu'il souhaite utiliser pour classifier son dataset.

## Comment ça marche ?
L'utilisateur upload son dataset, la vue est mise à jour avec une liste de colonnes à choisir pour l'entraînement.
Les colonnes choisis sont envoyées au serveur pour réaliser le traitement.
Une fois le traitement réalisé les résultats sont renvoyés dans la vue.

## Quelques commandes
Virtualenv
Windows (dans le CMD) : `Disk:\\path\to\wrf-venv\Scripts\activate`

MacOs :
```
$ source venv/bin/activate
$ deactivate
```

Installer les dépendances.
`pip install -r requirements.txt`

Après l'installation d'un module.
`pip freeze > requirements.txt`
