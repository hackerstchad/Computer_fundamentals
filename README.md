<!-- ===================================================================== -->
<!--   COM FUN - Computer Fundamentals | أساسيات المعلوماتية               -->
<!--   Auteur  : hackerstchad                                              -->
<!--   Version : 2026/2027                                                 -->
<!--   Langues : Francais | Arabe                                          -->
<!-- ===================================================================== -->

COM FUN - Computer Fundamentals
===============================

    Auteur  : hackerstchad
    Version : 2026/2027
    Langues : Francais / Arabe
    Lignes  : 2000+ lignes de code Python

Description
-----------

COM FUN est un script Python pedagogique tres avance pour apprendre les
fondamentaux de l'informatique de maniere pratique, interactive et bilingue.

Il propose 16 lecons completes, un quiz avance avec explications detaillees,
un laboratoire pratique avec simulations interactives, un systeme de
progression et de succes, et une interface terminal stylisee en couleurs.

Objectif : transformer les concepts abstraits de l'informatique en
experiences concretes, accessibles en francais et en arabe.

    +---------------------------------------------+
    |   COM FUN - Computer Fundamentals           |
    |   v2026/2027  |  hackerstchad               |
    +---------------------------------------------+
    |  [1] Lecons     |  الدروس                   |
    |  [2] Quiz       |  اختبار                   |
    |  [3] Laboratoire|  المختبر العملي           |
    |  [4] Progression|  التقدم                   |
    |  [5] Parametres |  الإعدادات                |
    |  [6] A propos   |  حول                      |
    |  [0] Quitter    |  خروج                     |
    +---------------------------------------------+

Fonctionnalites avancees
------------------------

* 16 lecons couvrant le hardware, le software, le CPU, la RAM, le stockage,
  les systemes d'exploitation, les architectures, les processus, les threads,
  la gestion de la memoire et les systemes de fichiers.
* Quiz interactif avec niveaux de difficulte et explications detaillees.
* Laboratoire pratique avec simulations :
  - Pipeline du CPU
  - Ordonnancement de processus (FIFO)
  - Demonstration de threads
  - Visualisation de la memoire RAM
  - Arbre de systeme de fichiers
* Systeme de progression sauvegarde en JSON.
* Systeme de succes / achievements.
* Interface terminal bilingue Francais / Arabe.
* Affichage stylise avec couleurs ANSI et bannieres ASCII.
* Plus de 2000 lignes de code Python pour une experience complete.

Liens internes 4D View
----------------------

    [Vue 1] Vue globale du projet
        |-- main.py              : Application principale
        |-- requirements.txt     : Dependances Python
        |-- README.md            : Ce fichier
        |-- __init__.py          : Package Python
        '-- data/
            '-- progress.json    : Progression sauvegardee

    [Vue 2] Architecture du code
        |-- Constantes           : Color, Symbol, Language
        |-- Classes de donnees   : UserProgress, Question, Lesson
        |-- Traductions          : TRANSLATIONS (FR/AR)
        |-- Base pedagogique     : LESSONS_DATA
        |-- Quiz                 : QUIZ_QUESTIONS
        |-- Affichage            : Display
        |-- Simulations          : Simulator
        |-- Progression          : ProgressManager
        '-- Application          : ComFunApp

    [Vue 3] Parcours utilisateur
        |-- Choix de la langue
        |-- Saisie du nom
        |-- Menu principal
        |   |-- Lecons
        |   |-- Quiz
        |   |-- Laboratoire
        |   |-- Progression
        |   |-- Parametres
        |   |-- A propos
        |   '-- Quitter
        '-- Sauvegarde JSON

    [Vue 4] Contenu pedagogique
        '-- Computer Fundamentals
            |-- Hardware
            |-- Software
            |-- CPU
            |-- RAM / ROM
            |-- HDD / SSD
            |-- Motherboard
            |-- BIOS / UEFI
            |-- Operating System
            |-- Architectures 32/64-bit
            |-- Architectures ARM / x86
            |-- Processes
            |-- Threads
            |-- Memory Management
            '-- File System

Installation
------------

Prerequis :

* Python 3.8 ou superieur
* Terminal supportant UTF-8 et couleurs ANSI

Etapes :

    cd com_fun
    python -m venv venv

Sur Linux / macOS :

    source venv/bin/activate

Sur Windows :

    venv\Scripts\activate

Installation des dependances :

    pip install -r requirements.txt

Utilisation
-----------

    python main.py

Menu principal
--------------

    [1] Lecons            -> Cours theoriques interactifs
    [2] Quiz              -> Tester vos connaissances
    [3] Laboratoire       -> Simulations et visualisations
    [4] Progression       -> Score, niveaux et succes
    [5] Parametres        -> Langue et reinitialisation
    [6] A propos          -> Informations sur COM FUN
    [0] Quitter           -> Fermer l'application

Lecons - الدرس الأول: أساسيات المعلوماتية
------------------------------------------

    01. Materiel informatique (Hardware)
        -> العتاد الحاسوبي
        -> Vue 4D : [Hardware] -> CPU, RAM, Stockage, Carte mere

    02. Logiciel (Software)
        -> البرمجيات
        -> Vue 4D : [Software] -> OS, Applications, Drivers, Licences

    03. Processeur (CPU)
        -> المعالج
        -> Vue 4D : [CPU] -> Cores, Threads, GHz, Pipeline

    04. Memoire vive (RAM)
        -> الذاكرة العشوائية
        -> Vue 4D : [RAM] -> Volatilite, Capacite, Frequences

    05. Memoire morte (ROM)
        -> ذاكرة القراءة فقط
        -> Vue 4D : [ROM] -> Firmware, BIOS, Non-volatile

    06. Disque dur (HDD)
        -> القرص الصلب
        -> Vue 4D : [HDD] -> Disques magnetiques, Platters, Latence

    07. Stockage SSD
        -> وحدة التخزين
        -> Vue 4D : [SSD] -> NAND Flash, Cellules, Controleur

    08. Carte mere (Motherboard)
        -> اللوحة الأم
        -> Vue 4D : [Motherboard] -> Chipset, Bus, Slots, Connecteurs

    09. BIOS et UEFI
        -> BIOS وUEFI
        -> Vue 4D : [Firmware] -> Boot, Secure Boot, Partitions GPT

    10. Systeme d'exploitation
        -> نظام التشغيل
        -> Vue 4D : [OS] -> Kernel, Processus, API, GUI/CLI

    11. Architecture 32-bit / 64-bit
        -> معمارية 32 بت و64 بت
        -> Vue 4D : [Architecture] -> Adressage memoire, Registres

    12. Architecture ARM et x86/x64
        -> معمارية ARM وx86/x64
        -> Vue 4D : [ISA] -> RISC, CISC, Mobile vs PC/Serveur

    13. Processus
        -> العمليات
        -> Vue 4D : [Processes] -> PID, Etats, Ordonnancement

    14. Threads
        -> خيوط التنفيذ
        -> Vue 4D : [Threads] -> Parallelisme, Concurrence, Synchronisation

    15. Gestion de la memoire
        -> إدارة الذاكرة
        -> Vue 4D : [Memory Management] -> Pagination, Segmentation, Swap

    16. Systeme de fichiers
        -> نظام الملفات
        -> Vue 4D : [File System] -> NTFS, ext4, FAT32, Chemins

Laboratoire pratique
--------------------

Le laboratoire propose des simulations interactives dans le terminal :

1. Pipeline du CPU
   Affichage etape par etape : FETCH, DECODE, EXECUTE, WRITE-BACK.

2. Ordonnancement de processus (FIFO)
   Simulation de l'execution sequentielle de plusieurs processus.

3. Demonstration de threads
   Lancement simultane de plusieurs threads avec affichage de progression.

4. Visualisation de la memoire RAM
   Representation graphique de la repartition memoire (OS, applications, swap).

5. Arbre de systeme de fichiers
   Affichage d'une structure de fichiers Linux type : /, /home, /etc, /var, /usr.

Quiz et achievements
--------------------

Le quiz contient des questions a choix multiples avec :

* Explications apres chaque reponse
* Systeme de points
* Suivi des questions reussies

Liste des succes disponibles :

    Premiers pas          -> Commencer a utiliser COM FUN
    Maitre des lecons     -> Completer 5 lecons
    Guerrier du quiz      -> Completer 5 quiz
    Expert materiel       -> Terminer les lecons hardware
    Guru OS               -> Terminer la lecon systeme d'exploitation
    Ninja architecture    -> Terminer les lecons architectures
    Sorcier de la memoire -> Terminer les lecons gestion memoire
    Score parfait         -> Reussir un quiz sans faute

Architecture du projet
----------------------

    com_fun/
    |
    |-- main.py              -> Application principale (2000+ lignes)
    |-- requirements.txt     -> Dependances Python
    |-- README.md            -> Documentation
    |-- __init__.py          -> Package Python
    |
    |-- data/
        |-- progress.json    -> Progression sauvegardee (auto)

Classes principales :

    Color             -> Palette de couleurs ANSI
    Symbol            -> Symboles Unicode
    UserProgress      -> Donnees de progression utilisateur
    Question          -> Modele de question de quiz
    Lesson            -> Modele de lecon
    Display           -> Gestion de l'affichage terminal
    Simulator         -> Simulations pedagogiques
    ProgressManager   -> Sauvegarde et chargement JSON
    ComFunApp         -> Application principale

Dependances
-----------

Fichier requirements.txt :

    colorama>=0.4.6
    psutil>=5.9.0

    colorama  -> Compatibilite des couleurs ANSI sur Windows
    psutil    -> Informations systeme pour demonstrations avancees

Personnalisation
----------------

Modifier les couleurs :

Editez la classe Color dans main.py :

    class Color:
        RED   = "\033[31m"
        GREEN = "\033[32m"
        BLUE  = "\033[34m"
        # ...

Ajouter une lecon :

Ajoutez un dictionnaire dans LESSONS_DATA avec les cles fr et ar :

    {
        "id": 17,
        "title": {"fr": "Nouvelle lecon", "ar": "درس جديد"},
        "icon": "Nouveau",
        "duration": 20,
        "difficulty": "intermediate",
        "sections": [...],
        "practical_exercises": [...]
    }

Ajouter une question au quiz :

Creez un nouvel objet Question dans QUIZ_QUESTIONS :

    Question(
        id=...,
        question={"fr": "...", "ar": "..."},
        options={"fr": [...], "ar": [...]},
        correct=0,
        explanation={"fr": "...", "ar": "..."},
        difficulty="medium",
        points=10
    )

Feuille de route
----------------

    [OK] 16 lecons completes
    [OK] Quiz interactif
    [OK] Laboratoire pratique
    [OK] Sauvegarde de progression
    [OK] Systeme de succes
    [OK] Interface bilingue FR/AR
    [  ] Mode sombre / clair
    [  ] Export PDF des lecons
    [  ] Version web avec Flask
    [  ] Support audio / vocal
    [  ] Certificat de completion

Auteur et credits
-----------------

    Auteur  : hackerstchad
    Version : 2026/2027
    Projet  : COM FUN - Computer Fundamentals
    Objectif: Apprendre l'informatique de maniere interactive, avancee
              et accessible en francais et en arabe.

    Bon apprentissage ! / بالتوفيق في التعلم !
