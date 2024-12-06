# Organisation du projet
---
## Les dossiers

* **App**
    Le dossier contenant tout le projet.
    1. **Icons**
        Le dossier contenant tous les icônes.
    2. **Packages**
        Tous les fichiers complémentaires sont dedans.
        1. **Data**
            Tout ce qui regroupe variables du jeu et variables système pour permette le bon fonctionnement de la sauvegarde/ du chargement et de l'exportation.
        2. **utilities**
            Les modules qui ne sont pas utilisés graphiquement (*ou presque*) sont regroupés dans ce dossier.
        3. **visuals**
            *LE* dossier le plus important du projet: ici se trouvent toutes les fenêtres pour la création des différents objets du jeu.
* **Docs**
    Ici se retrouvent toutes les informations utiles sur le projet (*comme ce guide par exemple*)

---
## Les fichiers
* **`Main.py`**
    Basiquement la fenêtre principale du logiciel, un peu le *root* du logiciel.
* **`__init__.py`**
    Ce qui permet d'acceder a l'entièreté des fichiers python sans problèmes.
> [!CAUTION] 
> Si supprimé Tout le projet ne fonctionne plus.
