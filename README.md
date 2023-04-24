# Installation
Aller dans le dossier `librairies` et lancer `pygame_install.bat` pour télécharger pyGame sur votre ordinateur.  
Ajouter le dossier `Assets` avec la commande `git clone https://github.com/STudio-Chorizo/Assets.git` executer dans le projet, essayer de le tenir à jour quand vous voyez un changement, et en cas de bug, vous pouvez changer de version uniquement les assets ou inversement que le code.  

# Architecture
(essayer de tenir cette architechture à jour)
```
MiniStudio
    ├── Assets
    │   └── *voir https://github.com/STudio-Chorizo/blob/main/README.md*
    ├── dependencies
    │   ├── engine
    │   │   ├── engine.py *Contient le gui en jeu*
    │   │   └── gameobject.py
    │   ├── parsejson
    │   │   └── parse.py
    │   ├── scripts
    │   │   └── entities
    │   │       └── player.py
    │   └── moderngl
    │       ├── main.py
    │       ├── camera.py
    │       ├── light.py
    │       ├── mesh.py
    │       ├── model.py
    │       ├── scene_rerender.py
    │       ├── scene.py
    │       ├── shader_program.py
    │       ├── texture.py
    │       ├── vao.py
    │       └── vbo.py
    │   ├── engine
    │   │   ├── engine.py
    │   │   └── gameobject.py
    │   ├── parsejson
    │   │   └── parse.py
    │   ├── scripts
    │   │   └── entities
    │   │       └── player.py
    │   └── moderngl
    │       ├── main.py
    │       ├── camera.py
    │       ├── light.py
    │       ├── mesh.py
    │       ├── model.py
    │       ├── scene_rerender.py
    │       ├── scene.py
    │       ├── shader_program.py
    │       ├── texture.py
    │       ├── vao.py
    │       └── vbo.py
    ├── main.py
    ├── install_librairies.bat
    ├── update_all_project.bat
    ├── .gitignore
    └── README.md
```

# Credits
## G.Buisness
- `référent` CHARLES Vincent `vcharles@gaming.bs`
- CHAUMAT Luka `lchaumat@gaming.bs`
- GLOMET Quentin `qglomet@gaming.bs`
## G.Art
- `référent` FERREIRA Thomas `tferreira@gaming.art`
## G.Tech
- `référent` LABOURDETTE Arno `alabourdette@gaming.tech`
- ACQUART--REYLANS Gwendal `contact@gwenitora.com`
- CAMANDONA Alexandre `acamandona@gaming.tech`
- FAYE Clément `cfaye@gaming.tech`
- RENAUD Quentin `qrenaud@gaming.tech`
- TOURNIER Lenny `ltournier@gaming.tech`