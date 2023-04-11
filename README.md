# Installation
Aller dans le dossier `librairies` et lancer `pygame_install.bat` pour télécharger pyGame sur votre ordinateur.  
Ajouter le dossier `Assets` avec la commande `git clone https://github.com/STudio-Chorizo/Assets.git` executer dans le projet, essayer de le tenir à jour quand vous voyez un changement, et en cas de bug, vous pouvez changer de version uniquement les assets ou inversement que le code.  

# Architecture
(essayer de tenir cette architechture à jour)
```
.
	├── Assets
	│   └── *voir https://github.com/STudio-Chorizo/Assets/blob/main/README.md*
	├── dependencies
	│   └── dependencies_controler.py
	├── librairies
	│   └── pygame_install.bat
	├── moteur3d
	│   └── *work in progress*
	├── main.py
	├── .gitignore
	└── README.md
```