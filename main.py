#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║   COM FUN - Computer Fundamentals (أساسيات المعلوماتية)                     ║
║   Version: 2026/2027                                                          ║
║   Auteur: hackerstchad                                                          ║
║   Langues: Français / العربية                                                    ║
║   Description: Programme pédagogique avancé pour apprendre les fondamentaux    ║
║                de l'informatique de manière interactive et pratique.           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import random
import platform
import threading
import subprocess
from datetime import datetime
from enum import Enum, auto
from typing import Dict, List, Optional, Callable, Any, Tuple
from dataclasses import dataclass, asdict

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTANTES GLOBALES
# ═══════════════════════════════════════════════════════════════════════════════

VERSION = "2026/2027"
AUTHOR = "hackerstchad"
APP_NAME = "COM FUN"
APP_NAME_AR = "أساسيات المعلوماتية"

# Couleurs ANSI
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    ORANGE = "\033[38;5;208m"
    PINK = "\033[38;5;206m"
    PURPLE = "\033[38;5;93m"
    GOLD = "\033[38;5;220m"
    LIME = "\033[38;5;154m"
    TEAL = "\033[38;5;30m"

# Symboles Unicode
class Symbol:
    STAR = "★"
    HEART = "♥"
    DIAMOND = "♦"
    SPADE = "♠"
    CLUB = "♣"
    ARROW_R = "→"
    ARROW_L = "←"
    ARROW_U = "↑"
    ARROW_D = "↓"
    CHECK = "✓"
    CROSS = "✗"
    BULLET = "•"
    COMPUTER = "💻"
    CPU = "🖥️"
    MEMORY = "🧠"
    DISK = "💾"
    CHIP = "🔲"
    BOOK = "📚"
    GEAR = "⚙️"
    LIGHTNING = "⚡"
    ROCKET = "🚀"
    TARGET = "🎯"
    TROPHY = "🏆"
    FIRE = "🔥"

# Langues
class Language(Enum):
    FRENCH = "fr"
    ARABIC = "ar"

# ═══════════════════════════════════════════════════════════════════════════════
# CLASSES DE DONNÉES
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class UserProgress:
    """Stocke la progression de l'utilisateur"""
    username: str = ""
    language: str = "fr"
    total_score: int = 0
    lessons_completed: List[int] = None
    quizzes_completed: List[int] = None
    achievements: List[str] = None
    study_time_minutes: int = 0
    last_session: str = ""
    
    def __post_init__(self):
        if self.lessons_completed is None:
            self.lessons_completed = []
        if self.quizzes_completed is None:
            self.quizzes_completed = []
        if self.achievements is None:
            self.achievements = []

@dataclass
class Question:
    """Représente une question de quiz"""
    id: int
    question: Dict[str, str]
    options: Dict[str, List[str]]
    correct: int
    explanation: Dict[str, str]
    difficulty: str
    points: int

@dataclass
class Lesson:
    """Représente une leçon"""
    id: int
    title: Dict[str, str]
    icon: str
    duration: int
    difficulty: str
    sections: List[Dict[str, Any]]
    practical_exercises: List[Dict[str, Any]]

# ═══════════════════════════════════════════════════════════════════════════════
# TRADUCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

TRANSLATIONS = {
    "fr": {
        "app_title": "COM FUN - Fondamentaux de l'Informatique",
        "welcome": "Bienvenue dans COM FUN",
        "choose_language": "Choisissez votre langue",
        "french": "Français",
        "arabic": "العربية",
        "main_menu": "Menu Principal",
        "lessons": "Leçons",
        "quiz": "Quiz",
        "practical_lab": "Laboratoire Pratique",
        "progress": "Progression",
        "settings": "Paramètres",
        "about": "À propos",
        "exit": "Quitter",
        "back": "Retour",
        "next": "Suivant",
        "previous": "Précédent",
        "start": "Commencer",
        "validate": "Valider",
        "score": "Score",
        "correct": "Correct",
        "incorrect": "Incorrect",
        "explanation": "Explication",
        "lesson_complete": "Leçon terminée !",
        "quiz_complete": "Quiz terminé !",
        "enter_choice": "Votre choix",
        "press_enter": "Appuyez sur Entrée pour continuer...",
        "goodbye": "Au revoir et bonne continuation !",
        "total_progress": "Progression totale",
        "achievements": "Succès débloqués",
        "study_time": "Temps d'étude",
        "minutes": "minutes",
        "level": "Niveau",
        "beginner": "Débutant",
        "intermediate": "Intermédiaire",
        "advanced": "Avancé",
        "expert": "Expert",
        "hardware": "Matériel (Hardware)",
        "software": "Logiciel (Software)",
        "cpu": "Processeur (CPU)",
        "ram": "Mémoire vive (RAM)",
        "rom": "Mémoire morte (ROM)",
        "hdd": "Disque dur (HDD)",
        "ssd": "Stockage SSD",
        "motherboard": "Carte mère (Motherboard)",
        "bios_uefi": "BIOS et UEFI",
        "os": "Système d'exploitation",
        "architecture": "Architecture 32-bit / 64-bit",
        "arm_x86": "Architecture ARM et x86/x64",
        "processes": "Processus",
        "threads": "Threads",
        "memory_mgmt": "Gestion de la mémoire",
        "filesystem": "Système de fichiers",
    },
    "ar": {
        "app_title": "COM FUN - أساسيات المعلوماتية",
        "welcome": "مرحباً بك في COM FUN",
        "choose_language": "اختر لغتك",
        "french": "Français",
        "arabic": "العربية",
        "main_menu": "القائمة الرئيسية",
        "lessons": "الدروس",
        "quiz": "اختبار",
        "practical_lab": "المختبر العملي",
        "progress": "التقدم",
        "settings": "الإعدادات",
        "about": "حول",
        "exit": "خروج",
        "back": "رجوع",
        "next": "التالي",
        "previous": "السابق",
        "start": "ابدأ",
        "validate": "تحقق",
        "score": "النقاط",
        "correct": "صحيح",
        "incorrect": "خطأ",
        "explanation": "الشرح",
        "lesson_complete": "اكتمل الدرس!",
        "quiz_complete": "اكتمل الاختبار!",
        "enter_choice": "اختيارك",
        "press_enter": "اضغط Enter للمتابعة...",
        "goodbye": "وداعاً وموفقاً في استمرارك!",
        "total_progress": "التقدم الإجمالي",
        "achievements": "الإنجازات المفتوحة",
        "study_time": "وقت الدراسة",
        "minutes": "دقيقة",
        "level": "المستوى",
        "beginner": "مبتدئ",
        "intermediate": "متوسط",
        "advanced": "متقدم",
        "expert": "خبير",
        "hardware": "العتاد الحاسوبي",
        "software": "البرمجيات",
        "cpu": "المعالج (CPU)",
        "ram": "الذاكرة العشوائية (RAM)",
        "rom": "ذاكرة القراءة فقط (ROM)",
        "hdd": "القرص الصلب (HDD)",
        "ssd": "وحدة التخزين (SSD)",
        "motherboard": "اللوحة الأم",
        "bios_uefi": "BIOS وUEFI",
        "os": "نظام التشغيل",
        "architecture": "معمارية 32 بت و64 بت",
        "arm_x86": "معمارية ARM وx86/x64",
        "processes": "العمليات",
        "threads": "خيوط التنفيذ",
        "memory_mgmt": "إدارة الذاكرة",
        "filesystem": "نظام الملفات",
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# BASE DE DONNÉES PÉDAGOGIQUES
# ═══════════════════════════════════════════════════════════════════════════════

LESSONS_DATA = [
    {
        "id": 1,
        "title": {"fr": "1. Matériel informatique (Hardware)", "ar": "1. العتاد الحاسوبي"},
        "icon": "🖥️",
        "duration": 25,
        "difficulty": "beginner",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce que le hardware ?",
                    "content": [
                        "Le hardware (matériel) désigne l'ensemble des composants physiques d'un ordinateur.",
                        "Contrairement au software (logiciel), le hardware est tangible : on peut le toucher.",
                        "Exemples : clavier, souris, écran, disque dur, carte mère, processeur...",
                        "Un ordinateur sans hardware ne peut pas fonctionner, même avec les meilleurs logiciels."
                    ]
                },
                "ar": {
                    "title": "ما هو العتاد الحاسوبي؟",
                    "content": [
                        "العتاد الحاسوبي (Hardware) يعني جميع المكونات المادية للحاسوب.",
                        "على عكس البرمجيات، العتاد ملموس ويمكن لمسه.",
                        "أمثلة: لوحة المفاتيح، الفأرة، الشاشة، القرص الصلب، اللوحة الأم، المعالج...",
                        "الحاسوب بدون عتاد لا يعمل حتى مع أفضل البرامج."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Composants principaux",
                    "content": [
                        "1. Unité centrale (CPU) : le cerveau de l'ordinateur.",
                        "2. Mémoire RAM : mémoire de travail temporaire.",
                        "3. Stockage (HDD/SSD) : conservation des données.",
                        "4. Carte mère : connecte tous les composants.",
                        "5. Alimentation : fournit l'énergie électrique.",
                        "6. Carte graphique : traite les images et vidéos.",
                        "7. Périphériques : clavier, souris, écran, imprimante."
                    ]
                },
                "ar": {
                    "title": "المكونات الرئيسية",
                    "content": [
                        "1. وحدة المعالجة المركزية (CPU): عقل الحاسوب.",
                        "2. ذاكرة الوصول العشوائي (RAM): الذاكرة المؤقتة للعمل.",
                        "3. التخزين (HDD/SSD): حفظ البيانات.",
                        "4. اللوحة الأم: تربط جميع المكونات.",
                        "5. مزود الطاقة: يوفر الكهرباء.",
                        "6. بطاقة الرسوميات: تعالج الصور والفيديوهات.",
                        "7. الأجهزة الطرفية: لوحة المفاتيح، الفأرة، الشاشة، الطابعة."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Analogie pratique",
                    "content": [
                        "Imaginez un ordinateur comme une cuisine :",
                        "- Le CPU est le chef qui exécute les recettes.",
                        "- La RAM est le plan de travail où on place les ingrédients en cours d'utilisation.",
                        "- Le stockage (HDD/SSD) est le réfrigérateur où on conserve tout.",
                        "- La carte mère est le plan de la cuisine qui organise l'espace.",
                        "- L'alimentation est le gaz/électricité qui fait fonctionner les appareils."
                    ]
                },
                "ar": {
                    "title": "مثال عملي",
                    "content": [
                        "تخيل الحاسوب كمطبخ:",
                        "- المعالج هو الطباخ الذي ينفذ الوصفات.",
                        "- الذاكرة العشوائية هي سطح العمل حيث نضع المكونات أثناء الاستخدام.",
                        "- التخزين هو الثلاجة التي نحفظ فيها كل شيء.",
                        "- اللوحة الأم هي مخطط المطبخ الذي ينظم المساحة.",
                        "- مزود الطاقة هو الغاز/الكهرباء الذي يشغل الأجهزة."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Identification des composants",
                    "instruction": "Choisissez le composant décrit par chaque phrase.",
                    "questions": [
                        "Composant qui exécute les instructions du programme :",
                        "Mémoire temporaire qui se vide à l'arrêt :",
                        "Stockage permanent des fichiers :",
                        "Carte qui connecte tous les composants :"
                    ],
                    "answers": ["CPU", "RAM", "HDD/SSD", "Motherboard"]
                },
                "ar": {
                    "title": "تمرين عملي: التعرف على المكونات",
                    "instruction": "اختر المكون الموصوف في كل جملة.",
                    "questions": [
                        "المكون الذي ينفذ تعليمات البرنامج:",
                        "الذاكرة المؤقتة التي تُفرغ عند الإطفاء:",
                        "التخزين الدائم للملفات:",
                        "البطاقة التي تربط جميع المكونات:"
                    ],
                    "answers": ["CPU", "RAM", "HDD/SSD", "Motherboard"]
                }
            }
        ]
    },
    {
        "id": 2,
        "title": {"fr": "2. Logiciel (Software)", "ar": "2. البرمجيات"},
        "icon": "💾",
        "duration": 20,
        "difficulty": "beginner",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce que le software ?",
                    "content": [
                        "Le software (logiciel) est l'ensemble des programmes, données et instructions qui font fonctionner un ordinateur.",
                        "Contrairement au hardware, le software n'est pas tangible : c'est du code.",
                        "Sans software, le hardware est inutile.",
                        "Le software transforme le hardware en outil utile."
                    ]
                },
                "ar": {
                    "title": "ما هي البرمجيات؟",
                    "content": [
                        "البرمجيات (Software) هي مجموعة البرامج والبيانات والتعليمات التي تشغل الحاسوب.",
                        "على عكس العتاد، البرمجيات غير ملموسة: إنها كود.",
                        "بدون برمجيات، العتاد عديم الفائدة.",
                        "البرمجيات تحول العتاد إلى أداة مفيدة."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Types de software",
                    "content": [
                        "1. Système d'exploitation (OS) : Windows, Linux, macOS, Android.",
                        "2. Logiciels applicatifs : navigateurs, traitement de texte, jeux.",
                        "3. Logiciels de programmation : IDE, compilateurs, éditeurs de code.",
                        "4. Pilotes (drivers) : permettent au OS de communiquer avec le hardware.",
                        "5. Logiciels utilitaires : antivirus, gestionnaires de fichiers, nettoyeurs de disque."
                    ]
                },
                "ar": {
                    "title": "أنواع البرمجيات",
                    "content": [
                        "1. نظام التشغيل (OS): Windows، Linux، macOS، Android.",
                        "2. البرامج التطبيقية: المتصفحات، معالجات النصوص، الألعاب.",
                        "3. برامج البرمجة: بيئات التطوير، المترجمات، محررات الأكواد.",
                        "4. التعريفات (Drivers): تسمح لنظام التشغيل بالتواصل مع العتاد.",
                        "5. البرامج المساعدة: مضادات الفيروسات، مديرو الملفات، منظفو الأقراص."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Licences logicielles",
                    "content": [
                        "Logiciel propriétaire : code source fermé, licence payante (ex: Microsoft Office).",
                        "Logiciel libre (Open Source) : code source ouvert, modifiable (ex: Linux, Firefox).",
                        "Freeware : gratuit mais code source fermé.",
                        "Shareware : essai gratuit puis paiement requis.",
                        "Comprendre les licences est essentiel pour un usage légal et éthique."
                    ]
                },
                "ar": {
                    "title": "تراخيص البرمجيات",
                    "content": [
                        "البرمجيات المملوكة: المصدر مغلق، ترخيص مدفوع (مثال: Microsoft Office).",
                        "البرمجيات الحرة (مفتوحة المصدر): المصدر مفتوح وقابل للتعديل (مثال: Linux، Firefox).",
                        "Freeware: مجاني لكن المصدر مغلق.",
                        "Shareware: تجربة مجانية ثم يتطلب الدفع.",
                        "فهم التراخيص ضروري للاستخدام القانوني والأخلاقي."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Catégorisez le software",
                    "instruction": "Pour chaque logiciel, indiquez son type.",
                    "questions": ["Windows", "Chrome", "Visual Studio Code", "Norton Antivirus"],
                    "answers": ["OS", "Application", "Programming", "Utility"]
                },
                "ar": {
                    "title": "تمرين عملي: صنّف البرمجيات",
                    "instruction": "لكل برنامج، حدد نوعه.",
                    "questions": ["Windows", "Chrome", "Visual Studio Code", "Norton Antivirus"],
                    "answers": ["OS", "Application", "Programming", "Utility"]
                }
            }
        ]
    },
    {
        "id": 3,
        "title": {"fr": "3. Processeur (CPU)", "ar": "3. المعالج (CPU)"},
        "icon": "⚙️",
        "duration": 35,
        "difficulty": "intermediate",
        "sections": [
            {
                "fr": {
                    "title": "Rôle du CPU",
                    "content": [
                        "Le CPU (Central Processing Unit) est le cerveau de l'ordinateur.",
                        "Il exécute les instructions des programmes en effectuant des calculs.",
                        "Ses principales actions : récupérer, décoder, exécuter et écrire des données.",
                        "La vitesse du CPU se mesure en GHz (milliards de cycles par seconde)."
                    ]
                },
                "ar": {
                    "title": "دور المعالج",
                    "content": [
                        "المعالج (CPU) هو عقل الحاسوب.",
                        "ينفذ تعليمات البرامج من خلال إجراء العمليات الحسابية.",
                        "إجراءاته الرئيسية: جلب، فك تشفير، تنفيذ، وكتابة البيانات.",
                        "تقاس سرعة المعالج بالجيجاهرتز (مليارات الدورات في الثانية)."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Architecture du CPU",
                    "content": [
                        "Cœurs (Cores) : unités indépendantes capables d'exécuter des tâches.",
                        "Threads : flux d'exécution au sein d'un cœur.",
                        "Cache : mémoire ultra-rapide intégrée au CPU (L1, L2, L3).",
                        "ALU (Arithmetic Logic Unit) : effectue les calculs arithmétiques et logiques.",
                        "Control Unit : orchestre les opérations du CPU."
                    ]
                },
                "ar": {
                    "title": "بنية المعالج",
                    "content": [
                        "الأنوية (Cores): وحدات مستقلة قادرة على تنفيذ المهام.",
                        "خيوط التنفيذ (Threads): تدفق التنفيذ داخل النواة.",
                        "الذاكرة المؤقتة (Cache): ذاكرة فائقة السرعة داخل المعالج (L1، L2، L3).",
                        "وحدة الحساب والمنطق (ALU): تنفذ العمليات الحسابية والمنطقية.",
                        "وحدة التحكم: توجه عمليات المعالج."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Comprendre les cycles d'horloge",
                    "content": [
                        "Un cycle d'horloge est un battement électrique qui synchronise le CPU.",
                        "1 Hz = 1 cycle par seconde.",
                        "1 GHz = 1 milliard de cycles par seconde.",
                        "Plus la fréquence est élevée, plus le CPU peut traiter d'instructions.",
                        "Mais la consommation électrique et la chaleur augmentent aussi."
                    ]
                },
                "ar": {
                    "title": "فهم دورات الساعة",
                    "content": [
                        "دورة الساعة هي نبضة كهربائية تزامن عمل المعالج.",
                        "1 هرتز = دورة واحدة في الثانية.",
                        "1 جيجاهرتز = مليار دورة في الثانية.",
                        "كلما زادت التردد، زادت التعليمات التي يمكن للمعالج معالجتها.",
                        "لكن استهلاك الطاقة والحرارة يزدادان أيضاً."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Simulation de cycles CPU",
                    "instruction": "Observez comment un CPU exécute des instructions simples.",
                    "questions": [],
                    "answers": []
                },
                "ar": {
                    "title": "تمرين عملي: محاكاة دورات المعالج",
                    "instruction": "لاحظ كيف ينفذ المعالج تعليمات بسيطة.",
                    "questions": [],
                    "answers": []
                }
            }
        ]
    },
    {
        "id": 4,
        "title": {"fr": "4. Mémoire vive (RAM)", "ar": "4. الذاكرة العشوائية (RAM)"},
        "icon": "🧠",
        "duration": 25,
        "difficulty": "beginner",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce que la RAM ?",
                    "content": [
                        "La RAM (Random Access Memory) est la mémoire de travail de l'ordinateur.",
                        "Elle stocke temporairement les données et programmes en cours d'utilisation.",
                        "La RAM est volatile : son contenu est effacé à l'arrêt de l'ordinateur.",
                        "Plus la RAM est grande, plus l'ordinateur peut exécuter de programmes simultanément."
                    ]
                },
                "ar": {
                    "title": "ما هي الذاكرة العشوائية؟",
                    "content": [
                        "الذاكرة العشوائية (RAM) هي ذاكرة العمل للحاسوب.",
                        "تخزن مؤقتاً البيانات والبرامج قيد الاستخدام.",
                        "الذاكرة العشوائية متطايرة: يُمحى محتواها عند إطفاء الحاسوب.",
                        "كلما كانت الذاكرة أكبر، زاد عدد البرامج التي يمكن تشغيلها في نفس الوقت."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Types de RAM",
                    "content": [
                        "DRAM (Dynamic RAM) : nécessite un rafraîchissement constant, utilisée comme RAM principale.",
                        "SRAM (Static RAM) : plus rapide, plus chère, utilisée dans le cache CPU.",
                        "DDR (Double Data Rate) : SDRAM moderne (DDR3, DDR4, DDR5).",
                        "Chaque génération DDR double approximativement la bande passante."
                    ]
                },
                "ar": {
                    "title": "أنواع الذاكرة العشوائية",
                    "content": [
                        "DRAM: تحتاج إلى تحديث مستمر، تُستخدم كذاكرة رئيسية.",
                        "SRAM: أسرع وأغلى، تُستخدم في ذاكرة تخزين المعالج المؤقتة.",
                        "DDR (معدل البيانات المزدوج): SDRAM حديثة (DDR3، DDR4، DDR5).",
                        "كل جيل من DDR يضاعف عرض النطاق الترددي تقريباً."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Analogie de la RAM",
                    "content": [
                        "La RAM est comme le bureau sur lequel vous travaillez.",
                        "Plus le bureau est grand, plus vous pouvez y poser de documents.",
                        "Quand vous rangez les documents dans l'armoire (stockage), ils sont conservés.",
                        "Mais ceux sur le bureau disparaissent si vous quittez la pièce (arrêt de l'ordinateur)."
                    ]
                },
                "ar": {
                    "title": "مثل توضيحي للذاكرة العشوائية",
                    "content": [
                        "الذاكرة العشوائية مثل المكتب الذي تعمل عليه.",
                        "كلما كان المكتب أكبر، زاد عدد الوثائق التي يمكن وضعها عليه.",
                        "عندما تضع الوثائق في الخزانة (التخزين)، تُحفظ.",
                        "لكن التي على المكتب تختفي إذا غادرت الغرفة (إطفاء الحاسوب)."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Calcul de mémoire",
                    "instruction": "Répondez aux questions sur la RAM.",
                    "questions": [
                        "La RAM est-elle volatile ou permanente ?",
                        "Quel type de RAM est utilisé dans le cache CPU ?",
                        "Quelle génération DDR est la plus récente ?"
                    ],
                    "answers": ["Volatile", "SRAM", "DDR5"]
                },
                "ar": {
                    "title": "تمرين عملي: حساب الذاكرة",
                    "instruction": "أجب عن أسئلة حول الذاكرة العشوائية.",
                    "questions": [
                        "هل الذاكرة العشوائية متطايرة أم دائمة؟",
                        "أي نوع من الذاكرة يُستخدم في ذاكرة المعالج المؤقتة؟",
                        "أي جيل DDR هو الأحدث؟"
                    ],
                    "answers": ["Volatile", "SRAM", "DDR5"]
                }
            }
        ]
    },
    {
        "id": 5,
        "title": {"fr": "5. Mémoire morte (ROM)", "ar": "5. ذاكرة القراءة فقط (ROM)"},
        "icon": "🔒",
        "duration": 20,
        "difficulty": "beginner",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce que la ROM ?",
                    "content": [
                        "La ROM (Read Only Memory) est une mémoire non volatile.",
                        "Son contenu est conservé même sans alimentation électrique.",
                        "Elle contient généralement le firmware, comme le BIOS/UEFI.",
                        "Contrairement à la RAM, la ROM est destinée principalement à la lecture."
                    ]
                },
                "ar": {
                    "title": "ما هي ذاكرة القراءة فقط؟",
                    "content": [
                        "ذاكرة القراءة فقط (ROM) هي ذاكرة غير متطايرة.",
                        "يُحفظ محتواها حتى بدون طاقة كهربائية.",
                        "تحتوي عادةً على البرامج الثابتة مثل BIOS/UEFI.",
                        "على عكس الذاكرة العشوائية، ROM مخصصة بشكل أساسي للقراءة."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Types de ROM",
                    "content": [
                        "PROM (Programmable ROM) : programmable une seule fois.",
                        "EPROM (Erasable PROM) : effaçable par UV.",
                        "EEPROM (Electrically EPROM) : effaçable électriquement.",
                        "Flash memory : type d'EEPROM moderne (clés USB, SSD, cartes SD)."
                    ]
                },
                "ar": {
                    "title": "أنواع ROM",
                    "content": [
                        "PROM: قابلة للبرمجة مرة واحدة.",
                        "EPROM: قابلة للمسح بالأشعة فوق البنفسجية.",
                        "EEPROM: قابلة للمسح كهربائياً.",
                        "ذاكرة الفلاش: نوع حديث من EEPROM (مفاتيح USB، SSD، بطاقات SD)."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : ROM vs RAM",
                    "instruction": "Comparez ROM et RAM.",
                    "questions": [
                        "Laquelle est volatile ?",
                        "Laquelle contient le firmware ?",
                        "Laquelle est utilisée comme mémoire de travail ?"
                    ],
                    "answers": ["RAM", "ROM", "RAM"]
                },
                "ar": {
                    "title": "تمرين عملي: ROM مقابل RAM",
                    "instruction": "قارن بين ROM وRAM.",
                    "questions": [
                        "أيهما متطاير؟",
                        "أيهما يحتوي على البرنامج الثابت؟",
                        "أيهما يُستخدم كذاكرة عمل؟"
                    ],
                    "answers": ["RAM", "ROM", "RAM"]
                }
            }
        ]
    },
    {
        "id": 6,
        "title": {"fr": "6. Disque dur (HDD)", "ar": "6. القرص الصلب (HDD)"},
        "icon": "💽",
        "duration": 25,
        "difficulty": "beginner",
        "sections": [
            {
                "fr": {
                    "title": "Fonctionnement du HDD",
                    "content": [
                        "Le HDD (Hard Disk Drive) utilise des plateaux magnétiques tournants.",
                        "Une tête de lecture/écriture se déplace pour accéder aux données.",
                        "La vitesse de rotation se mesure en RPM (tours par minute).",
                        "HDD typiques : 5400 RPM (portables) et 7200 RPM (bureautiques)."
                    ]
                },
                "ar": {
                    "title": "كيفية عمل القرص الصلب",
                    "content": [
                        "القرص الصلب (HDD) يستخدم أقراصاً مغناطيسية دوارة.",
                        "رأس القراءة/الكتابة يتحرك للوصول إلى البيانات.",
                        "تقاس سرعة الدوران بالدورات في الدقيقة (RPM).",
                        "أقراص HDD نموذجية: 5400 RPM (محمولة) و7200 RPM (مكتبية)."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Avantages et inconvénients",
                    "content": [
                        "Avantages : grande capacité, prix au Go très bas, fiabilité éprouvée.",
                        "Inconvénients : mécanique, sensible aux chocs, plus lent qu'un SSD.",
                        "Idéal pour le stockage de masse (archives, sauvegardes).",
                        "Moins adapté aux applications nécessitant une vitesse élevée."
                    ]
                },
                "ar": {
                    "title": "المزايا والعيوب",
                    "content": [
                        "المزايا: سعة كبيرة، سعر منخفض لكل غيغابايت، موثوقية مثبتة.",
                        "العيوب: ميكانيكي، حساس للصدمات، أبطأ من SSD.",
                        "مثالي للتخزين الضخم (أرشيف، نسخ احتياطي).",
                        "أقل ملاءمة للتطبيقات التي تتطلب سرعة عالية."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Calcul de vitesse",
                    "instruction": "Répondez aux questions sur le HDD.",
                    "questions": [
                        "Quelle technologie utilise le HDD pour stocker les données ?",
                        "Quelle unité mesure la vitesse de rotation ?",
                        "Le HDD est-il plus rapide qu'un SSD ?"
                    ],
                    "answers": ["Magnetic platters", "RPM", "No"]
                },
                "ar": {
                    "title": "تمرين عملي: حساب السرعة",
                    "instruction": "أجب عن أسئلة حول القرص الصلب.",
                    "questions": [
                        "ما التقنية التي يستخدمها HDD لتخزين البيانات؟",
                        "ما الوحدة التي تقيس سرعة الدوران؟",
                        "هل HDD أسرع من SSD؟"
                    ],
                    "answers": ["Magnetic platters", "RPM", "No"]
                }
            }
        ]
    },
    {
        "id": 7,
        "title": {"fr": "7. Stockage SSD", "ar": "7. وحدة التخزين (SSD)"},
        "icon": "⚡",
        "duration": 25,
        "difficulty": "beginner",
        "sections": [
            {
                "fr": {
                    "title": "Fonctionnement du SSD",
                    "content": [
                        "Le SSD (Solid State Drive) utilise de la mémoire flash NAND.",
                        "Contrairement au HDD, il n'a aucune partie mécanique en mouvement.",
                        "Il est beaucoup plus rapide, plus léger et plus résistant aux chocs.",
                        "Le SSD est devenu le standard pour les systèmes d'exploitation modernes."
                    ]
                },
                "ar": {
                    "title": "كيفية عمل SSD",
                    "content": [
                        "وحدة التخزين الصلبة (SSD) تستخدم ذاكرة فلاش NAND.",
                        "على عكس HDD، ليس لديها أجزاء ميكانيكية متحركة.",
                        "أسرع بكثير، أخف، وأكثر مقاومة للصدمات.",
                        "أصبح SSD المعيار لأنظمة التشغيل الحديثة."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Types de SSD",
                    "content": [
                        "SATA SSD : utilise le port SATA, similaire aux HDD en connectique.",
                        "NVMe SSD : utilise le bus PCIe, beaucoup plus rapide.",
                        "M.2 SSD : format compact, peut être SATA ou NVMe.",
                        "Les SSD NVMe peuvent atteindre plusieurs Go/s en lecture/écriture."
                    ]
                },
                "ar": {
                    "title": "أنواع SSD",
                    "content": [
                        "SATA SSD: يستخدم منفذ SATA، مشابه للـ HDD في التوصيل.",
                        "NVMe SSD: يستخدم ناقل PCIe، أسرع بكثير.",
                        "M.2 SSD: حجم مضغوط، يمكن أن يكون SATA أو NVMe.",
                        "يمكن لـ SSD NVMe الوصول إلى عدة غيغابايت/ثانية في القراءة/الكتابة."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : SSD vs HDD",
                    "instruction": "Comparez SSD et HDD.",
                    "questions": [
                        "Lequel a des pièces mécaniques en mouvement ?",
                        "Lequel est plus rapide ?",
                        "Quel type de SSD utilise PCIe ?"
                    ],
                    "answers": ["HDD", "SSD", "NVMe"]
                },
                "ar": {
                    "title": "تمرين عملي: SSD مقابل HDD",
                    "instruction": "قارن بين SSD وHDD.",
                    "questions": [
                        "أيهما يحتوي على أجزاء ميكانيكية متحركة؟",
                        "أيهما أسرع؟",
                        "أي نوع من SSD يستخدم PCIe؟"
                    ],
                    "answers": ["HDD", "SSD", "NVMe"]
                }
            }
        ]
    },
    {
        "id": 8,
        "title": {"fr": "8. Carte mère (Motherboard)", "ar": "8. اللوحة الأم"},
        "icon": "🔌",
        "duration": 30,
        "difficulty": "intermediate",
        "sections": [
            {
                "fr": {
                    "title": "Rôle de la carte mère",
                    "content": [
                        "La carte mère est le squelette de l'ordinateur.",
                        "Elle connecte et permet la communication entre tous les composants.",
                        "Elle héberge le chipset, le socket CPU, les slots RAM et les ports d'extension.",
                        "Sans carte mère, les composants ne peuvent pas fonctionner ensemble."
                    ]
                },
                "ar": {
                    "title": "دور اللوحة الأم",
                    "content": [
                        "اللوحة الأم هي هيكل الحاسوب.",
                        "تربط بين جميع المكونات وتتيح التواصل بينها.",
                        "تحتوي على chipset، مقبس المعالج، منافذ الذاكرة، ومنافذ التوسعة.",
                        "بدون اللوحة الأم، لا يمكن للمكونات العمل معاً."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Composants de la carte mère",
                    "content": [
                        "Socket CPU : accueille le processeur.",
                        "Slots RAM : accueillent les barrettes de mémoire.",
                        "Chipset : gère la communication entre CPU, RAM, stockage et périphériques.",
                        "Slots d'extension : PCIe pour carte graphique, carte réseau, etc.",
                        "Connecteurs SATA/NVMe : pour disques durs et SSD.",
                        "Ports d'E/S : USB, HDMI, Ethernet, audio."
                    ]
                },
                "ar": {
                    "title": "مكونات اللوحة الأم",
                    "content": [
                        "مقبس المعالج: يستقبل المعالج.",
                        "منافذ الذاكرة: تستقبل شرائح الذاكرة.",
                        "Chipset: يدير التواصل بين المعالج والذاكرة والتخزين والأجهزة الطرفية.",
                        "منافذ التوسعة: PCIe لبطاقة الرسوميات، بطاقة الشبكة، إلخ.",
                        "موصلات SATA/NVMe: للأقراص الصلبة وSSD.",
                        "منافذ الإدخال/الإخراج: USB، HDMI، Ethernet، audio."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Identification",
                    "instruction": "Identifiez les composants de la carte mère.",
                    "questions": [
                        "Quel composant accueille le CPU ?",
                        "Quel chipset gère les communications ?",
                        "Quels slots accueillent les cartes graphiques ?"
                    ],
                    "answers": ["Socket CPU", "Chipset", "PCIe slots"]
                },
                "ar": {
                    "title": "تمرين عملي: التعرف",
                    "instruction": "حدد مكونات اللوحة الأم.",
                    "questions": [
                        "أي مكون يستقبل المعالج؟",
                        "أي chipset يدير الاتصالات؟",
                        "أي منافذ تستقبل بطاقات الرسوميات؟"
                    ],
                    "answers": ["Socket CPU", "Chipset", "PCIe slots"]
                }
            }
        ]
    },
    {
        "id": 9,
        "title": {"fr": "9. BIOS et UEFI", "ar": "9. BIOS وUEFI"},
        "icon": "🔧",
        "duration": 30,
        "difficulty": "intermediate",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce que le BIOS ?",
                    "content": [
                        "Le BIOS (Basic Input/Output System) est un firmware stocké sur une puce ROM.",
                        "Il s'exécute au démarrage pour initialiser le matériel.",
                        "Il effectue le POST (Power-On Self Test) pour vérifier les composants.",
                        "Il charge ensuite le système d'exploitation depuis le disque."
                    ]
                },
                "ar": {
                    "title": "ما هو BIOS؟",
                    "content": [
                        "BIOS (نظام الإدخال/الإخراج الأساسي) هو برنامج ثابت مخزن على شريحة ROM.",
                        "يعمل عند بدء التشغيل لتهيئة العتاد.",
                        "ينفذ POST (اختبار ذاتي عند التشغيل) للتحقق من المكونات.",
                        "ثم يحمل نظام التشغيل من القرص."
                    ]
                }
            },
            {
                "fr": {
                    "title": "UEFI : le successeur moderne",
                    "content": [
                        "UEFI (Unified Extensible Firmware Interface) remplace progressivement le BIOS.",
                        "Il offre une interface graphique, un démarrage plus rapide et une meilleure sécurité.",
                        "Il supporte les disques de plus de 2 To (GPT).",
                        "Secure Boot : vérifie la signature du système d'exploitation pour éviter les malwares."
                    ]
                },
                "ar": {
                    "title": "UEFI: الخلف الحديث",
                    "content": [
                        "UEFI (واجهة البرامج الثابتة القابلة للتوسيع الموحدة) يحل تدريجياً محل BIOS.",
                        "يوفر واجهة رسومية، بدء تشغيل أسرع، وأمان أفضل.",
                        "يدعم أقراص أكبر من 2 تيرابايت (GPT).",
                        "Secure Boot: يتحقق من توقيع نظام التشغيل لتجنب البرمجيات الخبيثة."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : BIOS vs UEFI",
                    "instruction": "Comparez BIOS et UEFI.",
                    "questions": [
                        "Lequel est le plus ancien ?",
                        "Lequel supporte Secure Boot ?",
                        "Lequel supporte les disques GPT de grande taille ?"
                    ],
                    "answers": ["BIOS", "UEFI", "UEFI"]
                },
                "ar": {
                    "title": "تمرين عملي: BIOS مقابل UEFI",
                    "instruction": "قارن بين BIOS وUEFI.",
                    "questions": [
                        "أيهما الأقدم؟",
                        "أيهما يدعم Secure Boot؟",
                        "أيهما يدعم أقراص GPT الكبيرة؟"
                    ],
                    "answers": ["BIOS", "UEFI", "UEFI"]
                }
            }
        ]
    },
    {
        "id": 10,
        "title": {"fr": "10. Système d'exploitation", "ar": "10. نظام التشغيل"},
        "icon": "🖥️",
        "duration": 40,
        "difficulty": "intermediate",
        "sections": [
            {
                "fr": {
                    "title": "Rôle du système d'exploitation",
                    "content": [
                        "Le système d'exploitation (OS) est le logiciel principal de l'ordinateur.",
                        "Il gère le matériel et fournit une interface à l'utilisateur.",
                        "Il alloue les ressources : CPU, mémoire, stockage, périphériques.",
                        "Il assure la sécurité, la stabilité et la multitâche."
                    ]
                },
                "ar": {
                    "title": "دور نظام التشغيل",
                    "content": [
                        "نظام التشغيل (OS) هو البرنامج الرئيسي للحاسوب.",
                        "يدير العتاد ويوفر واجهة للمستخدم.",
                        "يوزع الموارد: المعالج، الذاكرة، التخزين، الأجهزة الطرفية.",
                        "يوفر الأمان، الاستقرار، وتعدد المهام."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Types d'OS",
                    "content": [
                        "OS de bureau : Windows, macOS, Linux.",
                        "OS mobiles : Android, iOS.",
                        "OS serveur : Windows Server, Ubuntu Server, Red Hat Enterprise Linux.",
                        "OS embarqués : FreeRTOS, VxWorks (IoT, automobiles, avions).",
                        "OS temps réel : garantissent des temps de réponse précis."
                    ]
                },
                "ar": {
                    "title": "أنواع أنظمة التشغيل",
                    "content": [
                        "أنظمة سطح المكتب: Windows، macOS، Linux.",
                        "أنظمة محمولة: Android، iOS.",
                        "أنظمة الخوادم: Windows Server، Ubuntu Server، Red Hat Enterprise Linux.",
                        "أنظمة مدمجة: FreeRTOS، VxWorks (إنترنت الأشياء، السيارات، الطائرات).",
                        "أنظمة الوقت الحقيقي: تضمن أوقات استجابة دقيقة."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Fonctions principales",
                    "content": [
                        "Gestion des processus : création, planification, terminaison.",
                        "Gestion de la mémoire : allocation et libération.",
                        "Gestion des fichiers : organisation du stockage.",
                        "Gestion des périphériques : communication via les pilotes.",
                        "Interface utilisateur : CLI (ligne de commande) ou GUI (interface graphique)."
                    ]
                },
                "ar": {
                    "title": "الوظائف الرئيسية",
                    "content": [
                        "إدارة العمليات: إنشاء، جدولة، إنهاء.",
                        "إدارة الذاكرة: تخصيص وتحرير.",
                        "إدارة الملفات: تنظيم التخزين.",
                        "إدارة الأجهزة الطرفية: التواصل عبر التعريفات.",
                        "واجهة المستخدم: CLI (سطر الأوامر) أو GUI (الواجهة الرسومية)."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Fonctions de l'OS",
                    "instruction": "Associez chaque fonction à sa description.",
                    "questions": [
                        "Gère les programmes en cours d'exécution",
                        "Organise les données sur le disque",
                        "Permet à l'utilisateur d'interagir",
                        "Communique avec le matériel"
                    ],
                    "answers": ["Process management", "File management", "UI", "Device management"]
                },
                "ar": {
                    "title": "تمرين عملي: وظائف نظام التشغيل",
                    "instruction": "اربط كل وظيفة بوصفها.",
                    "questions": [
                        "يدير البرامج قيد التشغيل",
                        "ينظم البيانات على القرص",
                        "يتيح للمستخدم التفاعل",
                        "يتواصل مع العتاد"
                    ],
                    "answers": ["Process management", "File management", "UI", "Device management"]
                }
            }
        ]
    },
    {
        "id": 11,
        "title": {"fr": "11. Architecture 32-bit / 64-bit", "ar": "11. معمارية 32 بت و64 بت"},
        "icon": "🔢",
        "duration": 30,
        "difficulty": "intermediate",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce qu'une architecture ?",
                    "content": [
                        "L'architecture définit la taille des données que le CPU peut traiter à la fois.",
                        "32-bit : le CPU manipule 32 bits à la fois.",
                        "64-bit : le CPU manipule 64 bits à la fois.",
                        "Un OS 64-bit peut utiliser plus de 4 Go de RAM."
                    ]
                },
                "ar": {
                    "title": "ما هي المعمارية؟",
                    "content": [
                        "المعمارية تحدد حجم البيانات التي يمكن للمعالج معالجتها في المرة الواحدة.",
                        "32 بت: المعالج يتعامل مع 32 بت في المرة الواحدة.",
                        "64 بت: المعالج يتعامل مع 64 بت في المرة الواحدة.",
                        "نظام 64 بت يمكنه استخدام أكثر من 4 غيغابايت من الذاكرة."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Différences principales",
                    "content": [
                        "Mémoire adressable : 32-bit ≈ 4 Go max, 64-bit ≈ 16 exaoctets théoriques.",
                        "Performance : 64-bit est plus rapide pour les calculs complexes.",
                        "Compatibilité : un OS 64-bit peut exécuter des programmes 32-bit (souvent).",
                        "Programmes 64-bit nécessitent un OS 64-bit."
                    ]
                },
                "ar": {
                    "title": "الاختلافات الرئيسية",
                    "content": [
                        "الذاكرة القابلة للعنونة: 32 بت ≈ 4 غيغابايت كحد أقصى، 64 بت ≈ 16 إكسابايت نظرياً.",
                        "الأداء: 64 بت أسرع في العمليات الحسابية المعقدة.",
                        "التوافق: نظام 64 بت يمكنه تشغيل برامج 32 بت (عادة).",
                        "برامج 64 بت تتطلب نظام 64 بت."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : 32 vs 64 bits",
                    "instruction": "Répondez aux questions.",
                    "questions": [
                        "Quelle architecture supporte plus de 4 Go de RAM ?",
                        "Un programme 64-bit peut-il fonctionner sur OS 32-bit ?",
                        "Quelle architecture est plus moderne ?"
                    ],
                    "answers": ["64-bit", "No", "64-bit"]
                },
                "ar": {
                    "title": "تمرين عملي: 32 مقابل 64 بت",
                    "instruction": "أجب عن الأسئلة.",
                    "questions": [
                        "أي معمارية تدعم أكثر من 4 غيغابايت من الذاكرة؟",
                        "هل يمكن لبرنامج 64 بت العمل على نظام 32 بت؟",
                        "أي معمارية أكثر حداثة؟"
                    ],
                    "answers": ["64-bit", "No", "64-bit"]
                }
            }
        ]
    },
    {
        "id": 12,
        "title": {"fr": "12. Architecture ARM et x86/x64", "ar": "12. معمارية ARM وx86/x64"},
        "icon": "🧩",
        "duration": 35,
        "difficulty": "advanced",
        "sections": [
            {
                "fr": {
                    "title": "Architecture x86 / x64",
                    "content": [
                        "x86 est une architecture CISC (Complex Instruction Set Computer) développée par Intel.",
                        "x64 (ou x86-64) est l'extension 64-bit de x86, utilisée par Intel et AMD.",
                        "Dominante sur les ordinateurs de bureau, portables et serveurs.",
                        "Instructions complexes, haute performance brute."
                    ]
                },
                "ar": {
                    "title": "معمارية x86 / x64",
                    "content": [
                        "x86 هي معمارية CISC (حاسوب مجموعة تعليمات المعقدة) طورتها Intel.",
                        "x64 (أو x86-64) هي الامتداد 64 بت لـ x86، تُستخدم من Intel وAMD.",
                        "مهيمنة على أجهزة سطح المكتب والمحمولة والخوادم.",
                        "تعليمات معقدة، أداء خام عالي."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Architecture ARM",
                    "content": [
                        "ARM est une architecture RISC (Reduced Instruction Set Computer).",
                        "Elle utilise des instructions simples et consomme moins d'énergie.",
                        "Dominante dans les smartphones, tablettes et systèmes embarqués.",
                        "Apple M1/M2/M3 utilisent ARM, démontrant ses capacités sur ordinateur."
                    ]
                },
                "ar": {
                    "title": "معمارية ARM",
                    "content": [
                        "ARM هي معمارية RISC (حاسوب مجموعة تعليمات المختصرة).",
                        "تستخدم تعليمات بسيطة وتستهلك طاقة أقل.",
                        "مهيمنة في الهواتف الذكية والأجهزة اللوحية والأنظمة المدمجة.",
                        "Apple M1/M2/M3 تستخدم ARM، مما يظهر قدراتها على الحاسوب."
                    ]
                }
            },
            {
                "fr": {
                    "title": "CISC vs RISC",
                    "content": [
                        "CISC : instructions complexes, peu de registres, programmes plus courts.",
                        "RISC : instructions simples, nombreux registres, programmes plus longs mais efficaces.",
                        "CISC privilégie la performance brute.",
                        "RISC privilégie l'efficacité énergétique."
                    ]
                },
                "ar": {
                    "title": "CISC مقابل RISC",
                    "content": [
                        "CISC: تعليمات معقدة، عدد قليل من السجلات، برامج أقصر.",
                        "RISC: تعليمات بسيطة، سجلات أكثر، برامج أطول لكن أكثر كفاءة.",
                        "CISC يفضل الأداء الخام.",
                        "RISC يفضل كفاءة الطاقة."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Architectures",
                    "instruction": "Identifiez l'architecture.",
                    "questions": [
                        "Architecture des processeurs Intel/AMD de bureau ?",
                        "Architecture des smartphones ?",
                        "CISC ou RISC pour ARM ?"
                    ],
                    "answers": ["x86/x64", "ARM", "RISC"]
                },
                "ar": {
                    "title": "تمرين عملي: المعماريات",
                    "instruction": "حدد المعمارية.",
                    "questions": [
                        "معمارية معالجات Intel/AMD لسطح المكتب؟",
                        "معمارية الهواتف الذكية؟",
                        "CISC أو RISC لـ ARM؟"
                    ],
                    "answers": ["x86/x64", "ARM", "RISC"]
                }
            }
        ]
    },
    {
        "id": 13,
        "title": {"fr": "13. Processus", "ar": "13. العمليات"},
        "icon": "📊",
        "duration": 35,
        "difficulty": "advanced",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce qu'un processus ?",
                    "content": [
                        "Un processus est un programme en cours d'exécution.",
                        "Chaque processus possède son propre espace mémoire et ressources.",
                        "Le système d'exploitation attribue un PID (Process ID) unique.",
                        "Les processus peuvent être dans différents états : prêt, en exécution, en attente, terminé."
                    ]
                },
                "ar": {
                    "title": "ما هي العملية؟",
                    "content": [
                        "العملية هي برنامج قيد التنفيذ.",
                        "لكل عملية مساحة ذاكرة وموارد خاصة بها.",
                        "نظام التشغيل يعطي معرف عملية فريد (PID).",
                        "العمليات يمكن أن تكون في حالات مختلفة: جاهزة، قيد التنفيذ، في الانتظار، منتهية."
                    ]
                }
            },
            {
                "fr": {
                    "title": "États d'un processus",
                    "content": [
                        "New : le processus vient d'être créé.",
                        "Ready : en attente d'être exécuté par le CPU.",
                        "Running : instructions en cours d'exécution.",
                        "Waiting : en attente d'un événement ou d'une ressource.",
                        "Terminated : le processus a fini son exécution."
                    ]
                },
                "ar": {
                    "title": "حالات العملية",
                    "content": [
                        "New: العملية تم إنشاؤها للتو.",
                        "Ready: في انتظار التنفيذ من قبل المعالج.",
                        "Running: التعليمات قيد التنفيذ.",
                        "Waiting: في انتظار حدث أو مورد.",
                        "Terminated: العملية أنهت تنفيذها."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Simulation de processus",
                    "instruction": "Simulez l'ordonnancement de processus.",
                    "questions": [],
                    "answers": []
                },
                "ar": {
                    "title": "تمرين عملي: محاكاة العمليات",
                    "instruction": "حاكِ جدولة العمليات.",
                    "questions": [],
                    "answers": []
                }
            }
        ]
    },
    {
        "id": 14,
        "title": {"fr": "14. Threads", "ar": "14. خيوط التنفيذ"},
        "icon": "🧵",
        "duration": 30,
        "difficulty": "advanced",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce qu'un thread ?",
                    "content": [
                        "Un thread est un flux d'exécution au sein d'un processus.",
                        "Un processus peut contenir plusieurs threads qui partagent la même mémoire.",
                        "Les threads permettent le multitâche au sein d'une même application.",
                        "Ils sont plus légers à créer que les processus."
                    ]
                },
                "ar": {
                    "title": "ما هو خيط التنفيذ؟",
                    "content": [
                        "خيط التنفيذ (Thread) هو تدفق تنفيذ داخل عملية.",
                        "العملية الواحدة يمكن أن تحتوي على عدة خيوط تشارك نفس الذاكرة.",
                        "الخيوط تتيح تعدد المهام داخل نفس التطبيق.",
                        "هي أخف في الإنشاء من العمليات."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Processus vs Threads",
                    "content": [
                        "Processus : mémoire isolée, lourd à créer.",
                        "Threads : mémoire partagée, léger à créer.",
                        "La communication entre threads est plus rapide qu'entre processus.",
                        "Mais les threads partageant la mémoire nécessitent une synchronisation."
                    ]
                },
                "ar": {
                    "title": "العمليات مقابل الخيوط",
                    "content": [
                        "العمليات: ذاكرة معزولة، ثقيلة في الإنشاء.",
                        "الخيوط: ذاكرة مشتركة، خفيفة في الإنشاء.",
                        "التواصل بين الخيوط أسرع منه بين العمليات.",
                        "لكن الخيوط التي تشارك الذاكرة تحتاج إلى مزامنة."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Threads en Python",
                    "instruction": "Exécutez la démonstration de threads.",
                    "questions": [],
                    "answers": []
                },
                "ar": {
                    "title": "تمرين عملي: الخيوط في بايثون",
                    "instruction": "شغّل عرض الخيوط.",
                    "questions": [],
                    "answers": []
                }
            }
        ]
    },
    {
        "id": 15,
        "title": {"fr": "15. Gestion de la mémoire", "ar": "15. إدارة الذاكرة"},
        "icon": "🧮",
        "duration": 40,
        "difficulty": "advanced",
        "sections": [
            {
                "fr": {
                    "title": "Pourquoi gérer la mémoire ?",
                    "content": [
                        "La mémoire RAM est une ressource limitée.",
                        "Le système d'exploitation doit allouer et libérer la mémoire efficacement.",
                        "Une mauvaise gestion provoque des fuites de mémoire et des plantages.",
                        "La mémoire virtuelle permet d'utiliser le disque comme extension de la RAM."
                    ]
                },
                "ar": {
                    "title": "لماذا ندير الذاكرة؟",
                    "content": [
                        "ذاكرة الوصول العشوائي مورد محدود.",
                        "يجب على نظام التشغيل تخصيص وتحرير الذاكرة بكفاءة.",
                        "الإدارة السيئة تسبب تسربات الذاكرة والأعطال.",
                        "الذاكرة الافتراضية تسمح باستخدام القرص كامتداد للذاكرة العشوائية."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Concepts clés",
                    "content": [
                        "Segmentation : divise la mémoire en segments logiques.",
                        "Pagination : divise la mémoire en pages de taille fixe.",
                        "Mémoire virtuelle : utilise le disque pour simuler plus de RAM.",
                        "Swapping : déplace les processus inactifs vers le disque.",
                        "Fragmentation : gaspillage d'espace mémoire (interne/externe)."
                    ]
                },
                "ar": {
                    "title": "المفاهيم الأساسية",
                    "content": [
                        "التجزئة: تقسيم الذاكرة إلى أقسام منطقية.",
                        "التصفح: تقسيم الذاكرة إلى صفحات بحجم ثابت.",
                        "الذاكرة الافتراضية: استخدام القرص لمحاكاة المزيد من الذاكرة العشوائية.",
                        "التبديل: نقل العمليات غير النشطة إلى القرص.",
                        "التجزئة: هدر مساحة الذاكرة (داخلي/خارجي)."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Mémoire virtuelle",
                    "instruction": "Répondez aux questions.",
                    "questions": [
                        "Quel mécanisme utilise le disque comme RAM supplémentaire ?",
                        "Quel est le nom du déplacement des processus inactifs vers le disque ?",
                        "La pagination divise la mémoire en pages de taille fixe ou variable ?"
                    ],
                    "answers": ["Virtual memory", "Swapping", "Fixed"]
                },
                "ar": {
                    "title": "تمرين عملي: الذاكرة الافتراضية",
                    "instruction": "أجب عن الأسئلة.",
                    "questions": [
                        "ما الآلية التي تستخدم القرص كذاكرة عشوائية إضافية؟",
                        "ما اسم نقل العمليات غير النشطة إلى القرص؟",
                        "هل التصفح يقسم الذاكرة إلى صفحات بحجم ثابت أم متغير؟"
                    ],
                    "answers": ["Virtual memory", "Swapping", "Fixed"]
                }
            }
        ]
    },
    {
        "id": 16,
        "title": {"fr": "16. Système de fichiers", "ar": "16. نظام الملفات"},
        "icon": "📁",
        "duration": 35,
        "difficulty": "intermediate",
        "sections": [
            {
                "fr": {
                    "title": "Qu'est-ce qu'un système de fichiers ?",
                    "content": [
                        "Un système de fichiers organise et stocke les données sur un disque.",
                        "Il définit comment les fichiers sont nommés, stockés et récupérés.",
                        "Exemples : NTFS, FAT32, exFAT, ext4, APFS.",
                        "Le système de fichiers est essentiel au fonctionnement de l'OS."
                    ]
                },
                "ar": {
                    "title": "ما هو نظام الملفات؟",
                    "content": [
                        "نظام الملفات ينظم ويخزن البيانات على القرص.",
                        "يحدد كيفية تسمية الملفات وتخزينها واسترجاعها.",
                        "أمثلة: NTFS، FAT32، exFAT، ext4، APFS.",
                        "نظام الملفات ضروري لعمل نظام التشغيل."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Types de systèmes de fichiers",
                    "content": [
                        "NTFS : système de fichiers moderne de Windows.",
                        "FAT32 : ancien, compatible mais limité à 4 Go par fichier.",
                        "exFAT : optimisé pour les clés USB et cartes SD.",
                        "ext4 : système de fichiers standard de Linux.",
                        "APFS : système de fichiers moderne d'Apple."
                    ]
                },
                "ar": {
                    "title": "أنواع أنظمة الملفات",
                    "content": [
                        "NTFS: نظام ملفات حديث من Windows.",
                        "FAT32: قديم، متوافق لكن محدود بـ 4 غيغابايت لكل ملف.",
                        "exFAT: مُحسّن لمفاتيح USB وبطاقات SD.",
                        "ext4: نظام الملفات القياسي لـ Linux.",
                        "APFS: نظام الملفات الحديث من Apple."
                    ]
                }
            },
            {
                "fr": {
                    "title": "Hiérarchie des fichiers",
                    "content": [
                        "Les fichiers sont organisés en répertoires (dossiers).",
                        "La racine (/) est le dossier principal sur Linux/macOS.",
                        "Sur Windows, chaque disque a une lettre (C:\\, D:\\, etc.).",
                        "Les chemins absolus indiquent l'emplacement complet depuis la racine.",
                        "Les chemins relatifs indiquent l'emplacement par rapport au dossier actuel."
                    ]
                },
                "ar": {
                    "title": "تسلسل الملفات",
                    "content": [
                        "الملفات منظمة في أدلة (مجلدات).",
                        "الجذر (/) هو المجلد الرئيسي في Linux/macOS.",
                        "في Windows، لكل قرص حرف (C:\\، D:\\، إلخ).",
                        "المسارات المطلقة تشير إلى الموقع الكامل من الجذر.",
                        "المسارات النسبية تشير إلى الموقع بالنسبة للمجلد الحالي."
                    ]
                }
            }
        ],
        "practical_exercises": [
            {
                "fr": {
                    "title": "Exercice pratique : Systèmes de fichiers",
                    "instruction": "Répondez aux questions.",
                    "questions": [
                        "Quel système de fichiers est utilisé par Windows moderne ?",
                        "Quel système de fichiers est utilisé par Linux ?",
                        "Quel système de fichiers a une limite de 4 Go par fichier ?"
                    ],
                    "answers": ["NTFS", "ext4", "FAT32"]
                },
                "ar": {
                    "title": "تمرين عملي: أنظمة الملفات",
                    "instruction": "أجب عن الأسئلة.",
                    "questions": [
                        "ما نظام الملفات المستخدم في Windows الحديث؟",
                        "ما نظام الملفات المستخدم في Linux؟",
                        "أي نظام ملفات له حد 4 غيغابايت لكل ملف؟"
                    ],
                    "answers": ["NTFS", "ext4", "FAT32"]
                }
            }
        ]
    }
]

# ═══════════════════════════════════════════════════════════════════════════════
# QUESTIONS DE QUIZ
# ═══════════════════════════════════════════════════════════════════════════════

QUIZ_QUESTIONS = [
    Question(
        id=1,
        question={"fr": "Quel composant est considéré comme le cerveau de l'ordinateur ?", "ar": "أي مكون يعتبر عقل الحاسوب؟"},
        options={"fr": ["RAM", "CPU", "HDD", "Carte mère"], "ar": ["RAM", "CPU", "HDD", "اللوحة الأم"]},
        correct=1,
        explanation={"fr": "Le CPU exécute les instructions et effectue les calculs.", "ar": "المعالج ينفذ التعليمات ويجري العمليات الحسابية."},
        difficulty="easy",
        points=10
    ),
    Question(
        id=2,
        question={"fr": "La RAM est-elle volatile ou permanente ?", "ar": "هل الذاكرة العشوائية متطايرة أم دائمة؟"},
        options={"fr": ["Volatile", "Permanente", "Les deux", "Aucune"], "ar": ["متطايرة", "دائمة", "كلاهما", "لا شيء"]},
        correct=0,
        explanation={"fr": "La RAM perd ses données quand l'ordinateur s'éteint.", "ar": "الذاكرة العشوائية تفقد بياناتها عند إطفاء الحاسوب."},
        difficulty="easy",
        points=10
    ),
    Question(
        id=3,
        question={"fr": "Quel système de fichiers est utilisé principalement sous Linux ?", "ar": "أي نظام ملفات يُستخدم بشكل رئيسي في Linux؟"},
        options={"fr": ["NTFS", "FAT32", "ext4", "APFS"], "ar": ["NTFS", "FAT32", "ext4", "APFS"]},
        correct=2,
        explanation={"fr": "ext4 est le système de fichiers standard de Linux.", "ar": "ext4 هو نظام الملفات القياسي لـ Linux."},
        difficulty="medium",
        points=15
    ),
    Question(
        id=4,
        question={"fr": "Quelle architecture consomme moins d'énergie : ARM ou x86 ?", "ar": "أي معمارية تستهلك طاقة أقل: ARM أم x86؟"},
        options={"fr": ["x86", "ARM", "Les deux identiques", "Dépend de l'OS"], "ar": ["x86", "ARM", "متساويتان", "يعتمد على نظام التشغيل"]},
        correct=1,
        explanation={"fr": "ARM est une architecture RISC conçue pour l'efficacité énergétique.", "ar": "ARM هي معمارية RISC مصممة لكفاءة الطاقة."},
        difficulty="medium",
        points=15
    ),
    Question(
        id=5,
        question={"fr": "Que signifie UEFI ?", "ar": "ماذا تعني UEFI؟"},
        options={"fr": ["Unified Extensible Firmware Interface", "Universal External File Input", "Unified External Firmware Input", "Universal Extended File Interface"], "ar": ["واجهة البرامج الثابتة القابلة للتوسيع الموحدة", "إدخال ملف خارجي عالمي", "إدخال البرامج الثابتة الخارجية الموحدة", "واجهة ملف موسعة عالمية"]},
        correct=0,
        explanation={"fr": "UEFI est le successeur moderne du BIOS.", "ar": "UEFI هو الخلف الحديث لـ BIOS."},
        difficulty="medium",
        points=15
    ),
    Question(
        id=6,
        question={"fr": "Quel type de stockage n'a pas de pièces mécaniques en mouvement ?", "ar": "أي نوع تخزين لا يحتوي على أجزاء ميكانيكية متحركة؟"},
        options={"fr": ["HDD", "SSD", "DVD", "Bande magnétique"], "ar": ["HDD", "SSD", "DVD", "شريط مغناطيسي"]},
        correct=1,
        explanation={"fr": "Le SSD utilise de la mémoire flash, sans pièces mobiles.", "ar": "SSD يستخدم ذاكرة الفلاش، بدون أجزاء متحركة."},
        difficulty="easy",
        points=10
    ),
    Question(
        id=7,
        question={"fr": "Quel mécanisme utilise le disque comme extension de la RAM ?", "ar": "ما الآلية التي تستخدم القرص كامتداد للذاكرة العشوائية؟"},
        options={"fr": ["Swapping", "Multitâche", "Cache", "Fragmentation"], "ar": ["التبديل", "تعدد المهام", "ذاكرة التخزين المؤقت", "التجزئة"]},
        correct=0,
        explanation={"fr": "Le swapping déplace les données inactives vers le disque.", "ar": "التبديل ينقل البيانات غير النشطة إلى القرص."},
        difficulty="hard",
        points=20
    ),
    Question(
        id=8,
        question={"fr": "Quelle architecture supporte nativement plus de 4 Go de RAM ?", "ar": "أي معمارية تدعم أكثر من 4 غيغابايت من الذاكرة أصلاً؟"},
        options={"fr": ["32-bit", "64-bit", "16-bit", "8-bit"], "ar": ["32 بت", "64 بت", "16 بت", "8 بت"]},
        correct=1,
        explanation={"fr": "L'architecture 64-bit peut adresser beaucoup plus de mémoire.", "ar": "معمارية 64 بت يمكنها عنونة ذاكرة أكبر بكثير."},
        difficulty="easy",
        points=10
    ),
    Question(
        id=9,
        question={"fr": "Un thread partage-t-il la mémoire avec d'autres threads du même processus ?", "ar": "هل خيط التنفيذ يشارك الذاكرة مع خيوط أخرى في نفس العملية؟"},
        options={"fr": ["Oui", "Non", "Uniquement sur Linux", "Uniquement sur Windows"], "ar": ["نعم", "لا", "فقط على Linux", "فقط على Windows"]},
        correct=0,
        explanation={"fr": "Les threads d'un même processus partagent l'espace mémoire.", "ar": "خيوط نفس العملية تشارك مساحة الذاكرة."},
        difficulty="medium",
        points=15
    ),
    Question(
        id=10,
        question={"fr": "Quel système d'exploitation est basé sur le noyau Linux ?", "ar": "أي نظام تشغيل مبني على نواة Linux؟"},
        options={"fr": ["Windows", "macOS", "Ubuntu", "iOS"], "ar": ["Windows", "macOS", "Ubuntu", "iOS"]},
        correct=2,
        explanation={"fr": "Ubuntu est une distribution Linux.", "ar": "Ubuntu هي توزيعة من Linux."},
        difficulty="easy",
        points=10
    ),
    Question(
        id=11,
        question={"fr": "La ROM contient-elle généralement le firmware ?", "ar": "هل تحتوي ROM عادةً على البرنامج الثابت؟"},
        options={"fr": ["Oui", "Non", "Uniquement sur SSD", "Uniquement sur HDD"], "ar": ["نعم", "لا", "فقط على SSD", "فقط على HDD"]},
        correct=0,
        explanation={"fr": "La ROM stocke le firmware comme le BIOS/UEFI.", "ar": "ROM تخزن البرنامج الثابت مثل BIOS/UEFI."},
        difficulty="easy",
        points=10
    ),
    Question(
        id=12,
        question={"fr": "Quel composant connecte tous les autres composants de l'ordinateur ?", "ar": "أي مكون يربط جميع مكونات الحاسوب الأخرى؟"},
        options={"fr": ["CPU", "RAM", "Carte mère", "Alimentation"], "ar": ["CPU", "RAM", "اللوحة الأم", "مزود الطاقة"]},
        correct=2,
        explanation={"fr": "La carte mère interconnecte CPU, RAM, stockage et périphériques.", "ar": "اللوحة الأم تربط المعالج والذاكرة والتخزين والأجهزة الطرفية."},
        difficulty="easy",
        points=10
    ),
    Question(
        id=13,
        question={"fr": "Que fait le POST au démarrage ?", "ar": "ماذا يفعل POST عند بدء التشغيل؟"},
        options={"fr": ["Charge l'OS", "Vérifie le matériel", "Formate le disque", "Démarre Internet"], "ar": ["يحمل نظام التشغيل", "يفحص العتاد", "يهيئ القرص", "يشغل الإنترنت"]},
        correct=1,
        explanation={"fr": "POST vérifie que le matériel fonctionne correctement.", "ar": "POST يتحقق من أن العتاد يعمل بشكل صحيح."},
        difficulty="medium",
        points=15
    ),
    Question(
        id=14,
        question={"fr": "Le CISC est associé principalement à quelle architecture ?", "ar": "CISC مرتبط بشكل رئيسي بأي معمارية؟"},
        options={"fr": ["ARM", "x86", "RISC-V", "MIPS"], "ar": ["ARM", "x86", "RISC-V", "MIPS"]},
        correct=1,
        explanation={"fr": "x86 est une architecture CISC.", "ar": "x86 هي معمارية CISC."},
        difficulty="hard",
        points=20
    ),
    Question(
        id=15,
        question={"fr": "Quel système de fichiers a une limite de 4 Go par fichier ?", "ar": "أي نظام ملفات له حد 4 غيغابايت لكل ملف؟"},
        options={"fr": ["NTFS", "ext4", "FAT32", "APFS"], "ar": ["NTFS", "ext4", "FAT32", "APFS"]},
        correct=2,
        explanation={"fr": "FAT32 ne supporte pas les fichiers de plus de 4 Go.", "ar": "FAT32 لا يدعم الملفات الأكبر من 4 غيغابايت."},
        difficulty="medium",
        points=15
    ),
    Question(
        id=16,
        question={"fr": "Quel type de RAM est plus rapide et utilisé dans le cache CPU ?", "ar": "أي نوع من الذاكرة العشوائية أسرع ويُستخدم في ذاكرة تخزين المعالج المؤقتة؟"},
        options={"fr": ["DRAM", "SRAM", "DDR3", "DDR4"], "ar": ["DRAM", "SRAM", "DDR3", "DDR4"]},
        correct=1,
        explanation={"fr": "SRAM est plus rapide mais plus chère, utilisée dans les caches.", "ar": "SRAM أسرع وأغلى، تُستخدم في الذاكرة المؤقتة."},
        difficulty="hard",
        points=20
    )
]

# ═══════════════════════════════════════════════════════════════════════════════
# GESTION DE L'AFFICHAGE
# ═══════════════════════════════════════════════════════════════════════════════

class Display:
    """Gère l'affichage stylisé dans le terminal"""
    
    def __init__(self):
        self.terminal_width = self._get_terminal_width()
    
    def _get_terminal_width(self) -> int:
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 80
    
    def refresh_width(self):
        self.terminal_width = self._get_terminal_width()
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def color(self, text: str, color: str) -> str:
        return f"{color}{text}{Color.RESET}"
    
    def center(self, text: str, width: int = None) -> str:
        if width is None:
            width = self.terminal_width
        return text.center(width)
    
    def box(self, title: str, content_lines: List[str], color: str = Color.CYAN) -> str:
        width = min(self.terminal_width - 4, 76)
        lines = []
        lines.append(self.color("╔" + "═" * (width - 2) + "╗", color))
        title_line = f" {title} ".center(width - 2)
        lines.append(self.color("║" + title_line + "║", color))
        lines.append(self.color("╠" + "═" * (width - 2) + "╣", color))
        for line in content_lines:
            if len(line) > width - 4:
                wrapped = self._wrap_text(line, width - 4)
                for wl in wrapped:
                    lines.append(self.color("║ " + wl.ljust(width - 4) + " ║", color))
            else:
                lines.append(self.color("║ " + line.ljust(width - 4) + " ║", color))
        lines.append(self.color("╚" + "═" * (width - 2) + "╝", color))
        return "\n".join(lines)
    
    def _wrap_text(self, text: str, width: int) -> List[str]:
        words = text.split()
        lines = []
        current = ""
        for word in words:
            if len(current) + len(word) + 1 <= width:
                current += " " + word if current else word
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines
    
    def header(self, text: str, color: str = Color.GOLD):
        self.refresh_width()
        print(self.color("═" * self.terminal_width, color))
        print(self.color(self.center(text), color))
        print(self.color("═" * self.terminal_width, color))
    
    def separator(self, char: str = "─", color: str = Color.DIM):
        self.refresh_width()
        print(self.color(char * self.terminal_width, color))
    
    def menu_item(self, key: str, text: str, icon: str = "", color: str = Color.GREEN):
        icon_str = f"{icon} " if icon else ""
        print(f"  {self.color(f'[{key}]', Color.YELLOW)} {icon_str}{self.color(text, color)}")
    
    def info(self, text: str):
        print(f"{self.color('ℹ', Color.BLUE)} {text}")
    
    def success(self, text: str):
        print(f"{self.color('✓', Color.GREEN)} {text}")
    
    def error(self, text: str):
        print(f"{self.color('✗', Color.RED)} {text}")
    
    def warning(self, text: str):
        print(f"{self.color('⚠', Color.YELLOW)} {text}")
    
    def print_gradient_banner(self, text: str):
        self.refresh_width()
        colors = [Color.CYAN, Color.BLUE, Color.MAGENTA, Color.PURPLE, Color.PINK]
        lines = [
            "",
            "   ██████╗ ██████╗ ███╗   ███╗    ███████╗██╗   ██╗███╗   ██╗",
            "  ██╔════╝██╔═══██╗████╗ ████║    ██╔════╝██║   ██║████╗  ██║",
            "  ██║     ██║   ██║██╔████╔██║    █████╗  ██║   ██║██╔██╗ ██║",
            "  ██║     ██║   ██║██║╚██╔╝██║    ██╔══╝  ██║   ██║██║╚██╗██║",
            "  ╚██████╗╚██████╔╝██║ ╚═╝ ██║    ██║     ╚██████╔╝██║ ╚████║",
            "   ╚═════╝ ╚═════╝ ╚═╝     ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝",
            ""
        ]
        for i, line in enumerate(lines):
            c = colors[i % len(colors)]
            print(self.color(self.center(line), c))
        print(self.color(self.center(f"★ {text} ★"), Color.GOLD))
        print(self.color(self.center(f"v{VERSION} | {AUTHOR}"), Color.DIM))

# ═══════════════════════════════════════════════════════════════════════════════
# SIMULATIONS ET UTILITAIRES PÉDAGOGIQUES
# ═══════════════════════════════════════════════════════════════════════════════

class Simulator:
    """Simulations interactives pour comprendre les concepts"""
    
    def __init__(self, display: Display, lang: str):
        self.display = display
        self.lang = lang
        self.t = TRANSLATIONS[lang]
    
    def cpu_pipeline(self):
        """Simule le pipeline d'instructions CPU"""
        self.display.clear()
        self.display.header(self.t["cpu"] if self.lang == "fr" else self.t["cpu"])
        instructions = [
            ("LOAD R1, 10", "Charger la valeur 10 dans R1"),
            ("LOAD R2, 20", "Charger la valeur 20 dans R2"),
            ("ADD R3, R1, R2", "Additionner R1 et R2, stocker dans R3"),
            ("STORE R3, MEM", "Stocker R3 en mémoire"),
            ("PRINT R3", "Afficher la valeur de R3")
        ]
        print(self.display.color("\n📋 Programme à exécuter:", Color.CYAN))
        for i, (inst, desc) in enumerate(instructions, 1):
            print(f"  {i}. {self.display.color(inst, Color.YELLOW)} - {desc}")
        print()
        registers = {"R1": 0, "R2": 0, "R3": 0}
        stages = ["FETCH", "DECODE", "EXECUTE", "WRITE-BACK"]
        for i, (inst, desc) in enumerate(instructions):
            print(self.display.color(f"▶ Instruction {i+1}: {inst}", Color.GREEN))
            for stage in stages:
                print(f"  {self.display.color('→', Color.YELLOW)} {stage}...", end=" ")
                time.sleep(0.4)
                if stage == "EXECUTE":
                    if "LOAD R1" in inst:
                        registers["R1"] = 10
                    elif "LOAD R2" in inst:
                        registers["R2"] = 20
                    elif "ADD" in inst:
                        registers["R3"] = registers["R1"] + registers["R2"]
                    elif "STORE" in inst:
                        pass
                    elif "PRINT" in inst:
                        pass
                print(self.display.color("OK", Color.GREEN))
            print(f"  Registres: {self.display.color(str(registers), Color.CYAN)}\n")
            time.sleep(0.3)
        print(self.display.color(f"\n🏁 Résultat final: R3 = {registers['R3']}", Color.GOLD))
    
    def process_scheduler(self):
        """Simule un ordonnanceur de processus"""
        self.display.clear()
        self.display.header(self.t["processes"] if self.lang == "fr" else self.t["processes"])
        processes = [
            {"name": "P1", "burst": 4, "arrival": 0},
            {"name": "P2", "burst": 2, "arrival": 1},
            {"name": "P3", "burst": 6, "arrival": 2},
            {"name": "P4", "burst": 3, "arrival": 3}
        ]
        print(self.display.color("\n📊 Ordonnancement FIFO (First In First Out):", Color.CYAN))
        print("Processus | Temps d'exécution | Arrivée")
        print("-" * 40)
        for p in processes:
            print(f"    {p['name']}    |        {p['burst']}         |    {p['arrival']}")
        print()
        current_time = 0
        for p in processes:
            print(self.display.color(f"▶ Exécution de {p['name']} pendant {p['burst']} unités", Color.GREEN))
            for t in range(p["burst"]):
                bar = "█" * (t + 1) + "░" * (p["burst"] - t - 1)
                print(f"  [{bar}] {t+1}/{p['burst']}", end="\r")
                time.sleep(0.3)
            print()
            current_time += p["burst"]
            print(f"  {self.display.color('✓ Terminé à t=' + str(current_time), Color.YELLOW)}\n")
        print(self.display.color(f"Temps total: {current_time} unités", Color.GOLD))
    
    def thread_demo(self):
        """Démontre l'exécution parallèle de threads"""
        self.display.clear()
        self.display.header(self.t["threads"] if self.lang == "fr" else self.t["threads"])
        results = {}
        def worker(name: str, duration: int):
            for i in range(duration):
                time.sleep(0.3)
                results[name] = i + 1
                print(f"  {self.display.color(name, Color.CYAN)}: progression {i+1}/{duration}")
        threads = [
            threading.Thread(target=worker, args=("Thread-A", 4)),
            threading.Thread(target=worker, args=("Thread-B", 3)),
            threading.Thread(target=worker, args=("Thread-C", 5))
        ]
        print(self.display.color("\n🧵 Lancement de 3 threads simultanés...", Color.GREEN))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        print(self.display.color("\n✅ Tous les threads ont terminé!", Color.GOLD))
    
    def memory_visualizer(self):
        """Visualise la mémoire RAM et le swap"""
        self.display.clear()
        self.display.header(self.t["memory_mgmt"] if self.lang == "fr" else self.t["memory_mgmt"])
        memory_blocks = [
            ("OS Kernel", 20, Color.RED),
            ("Chrome", 30, Color.BLUE),
            ("VS Code", 25, Color.GREEN),
            ("Libre", 15, Color.DIM),
            ("Swap (inactif)", 10, Color.YELLOW)
        ]
        total = 100
        print(self.display.color("\n🧠 Visualisation de la mémoire RAM (100 unités):", Color.CYAN))
        bar = ""
        labels = []
        pos = 0
        for name, size, color in memory_blocks:
            bar += self.display.color("█" * size, color)
            labels.append(f"{self.display.color('■', color)} {name}: {size}%")
            pos += size
        print(f"[{bar}]")
        print()
        for label in labels:
            print(f"  {label}")
        print(self.display.color("\n💡 Le swap est utilisé quand la RAM est pleine.", Color.GOLD))
    
    def filesystem_tree(self):
        """Affiche un arbre de fichiers"""
        self.display.clear()
        self.display.header(self.t["filesystem"] if self.lang == "fr" else self.t["filesystem"])
        tree = [
            ("/", 0, Color.RED),
            ("├── home", 1, Color.GREEN),
            ("│   ├── user", 2, Color.CYAN),
            ("│   │   ├── documents", 3, Color.YELLOW),
            ("│   │   ├── pictures", 3, Color.YELLOW),
            ("│   │   └── downloads", 3, Color.YELLOW),
            ("│   └── admin", 2, Color.CYAN),
            ("├── etc", 1, Color.GREEN),
            ("│   ├── config.txt", 2, Color.YELLOW),
            ("│   └── hosts", 2, Color.YELLOW),
            ("├── var", 1, Color.GREEN),
            ("│   └── log", 2, Color.YELLOW),
            ("└── usr", 1, Color.GREEN),
            ("    ├── bin", 2, Color.YELLOW),
            ("    └── lib", 2, Color.YELLOW)
        ]
        print(self.display.color("\n🌳 Structure d'un système de fichiers Linux:", Color.CYAN))
        for item, level, color in tree:
            indent = "    " * level
            print(f"{indent}{self.display.color(item, color)}")
        print(self.display.color("\n💡 Les chemins absolus commencent par /", Color.GOLD))

# ═══════════════════════════════════════════════════════════════════════════════
# GESTION DE LA PROGRESSION
# ═══════════════════════════════════════════════════════════════════════════════

class ProgressManager:
    """Gère la sauvegarde et le chargement de la progression"""
    
    def __init__(self):
        self.data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
        os.makedirs(self.data_dir, exist_ok=True)
        self.file_path = os.path.join(self.data_dir, "progress.json")
    
    def load(self) -> UserProgress:
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                return UserProgress(**data)
            except Exception:
                pass
        return UserProgress()
    
    def save(self, progress: UserProgress):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(asdict(progress), f, ensure_ascii=False, indent=2)

# ═══════════════════════════════════════════════════════════════════════════════
# APPLICATION PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════════════

class ComFunApp:
    """Application principale COM FUN"""
    
    def __init__(self):
        self.display = Display()
        self.progress_manager = ProgressManager()
        self.progress = self.progress_manager.load()
        self.lang = self.progress.language if self.progress.language else "fr"
        self.t = TRANSLATIONS[self.lang]
        self.simulator = Simulator(self.display, self.lang)
        self.running = True
        self.achievements_list = [
            ("first_steps", "🌟 Premiers pas", "Premiers pas"),
            ("lesson_master", "📚 Maître des leçons", "Maître des leçons"),
            ("quiz_warrior", "⚔️ Guerrier du quiz", "Guerrier du quiz"),
            ("hardware_expert", "🖥️ Expert matériel", "Expert matériel"),
            ("os_guru", "🖥️ Guru OS", "Guru OS"),
            ("architecture_ninja", "🧩 Ninja architecture", "Ninja architecture"),
            ("memory_wizard", "🧙 Sorcier de la mémoire", "Sorcier de la mémoire"),
            ("perfect_score", "🏆 Score parfait", "Score parfait"),
        ]
    
    def set_language(self, lang: str):
        self.lang = lang
        self.progress.language = lang
        self.t = TRANSLATIONS[lang]
        self.simulator.lang = lang
        self.progress_manager.save(self.progress)
    
    def get_text(self, key: str) -> str:
        return self.t.get(key, key)
    
    def wait_for_enter(self):
        input(f"\n{self.display.color(self.get_text('press_enter'), Color.DIM)}")
    
    def prompt_choice(self, prompt: str = None) -> str:
        if prompt is None:
            prompt = self.get_text("enter_choice")
        try:
            return input(f"\n{self.display.color('➤', Color.GOLD)} {prompt}: ").strip()
        except (EOFError, KeyboardInterrupt):
            return "0"
    
    def show_banner(self):
        self.display.clear()
        self.display.print_gradient_banner(self.get_text("app_title"))
        print()
        if self.progress.username:
            welcome = f"{self.get_text('welcome')}, {self.display.color(self.progress.username, Color.CYAN)}"
            print(self.display.center(welcome))
        print(self.display.center(f"{self.get_text('score')}: {self.display.color(str(self.progress.total_score), Color.GOLD)} | {self.get_text('level')}: {self.display.color(self.get_level(), Color.GREEN)}"))
        print()
    
    def get_level(self) -> str:
        score = self.progress.total_score
        if score < 50:
            return self.get_text("beginner")
        elif score < 150:
            return self.get_text("intermediate")
        elif score < 300:
            return self.get_text("advanced")
        else:
            return self.get_text("expert")
    
    def language_menu(self):
        self.display.clear()
        self.display.header(self.get_text("choose_language"))
        print()
        self.display.menu_item("1", self.get_text("french"), "🇫🇷")
        self.display.menu_item("2", self.get_text("arabic"), "🇸🇦")
        print()
        choice = self.prompt_choice()
        if choice == "1":
            self.set_language("fr")
        elif choice == "2":
            self.set_language("ar")
        if not self.progress.username:
            self.setup_username()
    
    def setup_username(self):
        self.display.clear()
        self.display.header(self.get_text("welcome"))
        print()
        try:
            name = input(f"{self.display.color('👤', Color.CYAN)} {'Entrez votre nom' if self.lang == 'fr' else 'أدخل اسمك'}: ").strip()
            if name:
                self.progress.username = name
                self.progress_manager.save(self.progress)
        except (EOFError, KeyboardInterrupt):
            pass
    
    def main_menu(self) -> str:
        self.show_banner()
        self.display.header(self.get_text("main_menu"), Color.BLUE)
        print()
        self.display.menu_item("1", self.get_text("lessons"), Symbol.BOOK)
        self.display.menu_item("2", self.get_text("quiz"), Symbol.TARGET)
        self.display.menu_item("3", self.get_text("practical_lab"), Symbol.ROCKET)
        self.display.menu_item("4", self.get_text("progress"), Symbol.TROPHY)
        self.display.menu_item("5", self.get_text("settings"), Symbol.GEAR)
        self.display.menu_item("6", self.get_text("about"), Symbol.STAR)
        self.display.menu_item("0", self.get_text("exit"), Symbol.CROSS)
        print()
        return self.prompt_choice()
    
    def lessons_menu(self):
        while True:
            self.display.clear()
            self.display.header(self.get_text("lessons"), Color.GREEN)
            print()
            for lesson in LESSONS_DATA:
                completed = "✅" if lesson["id"] in self.progress.lessons_completed else "⬜"
                title = lesson["title"][self.lang]
                diff_color = Color.GREEN if lesson["difficulty"] == "beginner" else (Color.YELLOW if lesson["difficulty"] == "intermediate" else Color.RED)
                diff_label = self.get_text(lesson["difficulty"])
                print(f"  {completed} {self.display.color(f'[{lesson['id']}]', Color.YELLOW)} {lesson['icon']} {self.display.color(title, Color.CYAN)} ({self.display.color(diff_label, diff_color)})")
            print()
            self.display.menu_item("0", self.get_text("back"), Symbol.ARROW_L)
            choice = self.prompt_choice()
            if choice == "0":
                break
            try:
                lesson_id = int(choice)
                lesson = next((l for l in LESSONS_DATA if l["id"] == lesson_id), None)
                if lesson:
                    self.run_lesson(lesson)
                else:
                    self.display.error("Leçon non trouvée" if self.lang == "fr" else "الدرس غير موجود")
                    self.wait_for_enter()
            except ValueError:
                self.display.error("Choix invalide" if self.lang == "fr" else "اختيار غير صالح")
                self.wait_for_enter()
    
    def run_lesson(self, lesson: Dict):
        self.display.clear()
        title = lesson["title"][self.lang]
        self.display.header(f"{lesson['icon']} {title}", Color.GREEN)
        print()
        for i, section in enumerate(lesson["sections"], 1):
            sec = section[self.lang]
            self.display.separator()
            print(self.display.color(f"  {Symbol.BULLET} {sec['title']}", Color.GOLD))
            print()
            for line in sec["content"]:
                print(f"    {self.display.color('•', Color.CYAN)} {line}")
            print()
            if i < len(lesson["sections"]):
                cont = self.prompt_choice("1. Continuer / 0. Retour" if self.lang == "fr" else "1. متابعة / 0. رجوع")
                if cont == "0":
                    return
        self.run_practical_exercise(lesson)
        if lesson["id"] not in self.progress.lessons_completed:
            self.progress.lessons_completed.append(lesson["id"])
            self.progress.total_score += 20
            self.check_achievements()
            self.progress_manager.save(self.progress)
        self.display.success(self.get_text("lesson_complete"))
        self.wait_for_enter()
    
    def run_practical_exercise(self, lesson: Dict):
        if not lesson["practical_exercises"]:
            return
        exercise = lesson["practical_exercises"][0]
        ex = exercise[self.lang]
        self.display.separator()
        print(self.display.color(f"\n🔧 {ex['title']}", Color.PURPLE))
        print(self.display.color(ex["instruction"], Color.DIM))
        print()
        if ex.get("questions"):
            score = 0
            for i, (q, ans) in enumerate(zip(ex["questions"], ex["answers"]), 1):
                print(f"  {i}. {q}")
                user_ans = input(f"     {'Réponse' if self.lang == 'fr' else 'إجابة'}: ").strip()
                if user_ans.lower() == ans.lower():
                    self.display.success(self.get_text("correct"))
                    score += 1
                else:
                    self.display.error(f"{self.get_text('incorrect')}. {self.get_text('explanation')}: {ans}")
            print(self.display.color(f"\nScore: {score}/{len(ex['questions'])}", Color.GOLD))
    
    def quiz_menu(self):
        self.display.clear()
        self.display.header(self.get_text("quiz"), Color.MAGENTA)
        print()
        print(self.display.color(f"{'Nombre de questions' if self.lang == 'fr' else 'عدد الأسئلة'}: {len(QUIZ_QUESTIONS)}", Color.CYAN))
        print()
        self.display.menu_item("1", "Démarrer le quiz" if self.lang == "fr" else "ابدأ الاختبار", Symbol.TARGET)
        self.display.menu_item("0", self.get_text("back"), Symbol.ARROW_L)
        choice = self.prompt_choice()
        if choice == "1":
            self.run_quiz()
    
    def run_quiz(self):
        score = 0
        total_points = 0
        earned_points = 0
        for q in QUIZ_QUESTIONS:
            total_points += q.points
        for i, q in enumerate(QUIZ_QUESTIONS, 1):
            self.display.clear()
            question_label = "Question" if self.lang == "fr" else "سؤال"
            self.display.header(f"{self.get_text('quiz')} - {question_label} {i}/{len(QUIZ_QUESTIONS)}", Color.MAGENTA)
            print()
            print(self.display.color(q.question[self.lang], Color.CYAN))
            print()
            for j, opt in enumerate(q.options[self.lang]):
                print(f"  {self.display.color(f'[{j+1}]', Color.YELLOW)} {opt}")
            print()
            try:
                choice = int(self.prompt_choice()) - 1
            except ValueError:
                choice = -1
            if choice == q.correct:
                self.display.success(f"{self.get_text('correct')}! +{q.points} pts")
                score += 1
                earned_points += q.points
            else:
                correct_text = q.options[self.lang][q.correct]
                self.display.error(f"{self.get_text('incorrect')}. {self.get_text('explanation')}: {correct_text}")
                print(self.display.color(q.explanation[self.lang], Color.DIM))
            self.wait_for_enter()
        self.progress.total_score += earned_points
        for q_id in [q.id for q in QUIZ_QUESTIONS]:
            if q_id not in self.progress.quizzes_completed:
                self.progress.quizzes_completed.append(q_id)
        if score == len(QUIZ_QUESTIONS):
            self.unlock_achievement("perfect_score")
        self.check_achievements()
        self.progress_manager.save(self.progress)
        self.display.clear()
        self.display.header(self.get_text("quiz_complete"), Color.GOLD)
        print()
        print(self.display.color(f"{'Score' if self.lang == 'fr' else 'النقاط'}: {score}/{len(QUIZ_QUESTIONS)}", Color.GREEN))
        print(self.display.color(f"{'Points gagnés' if self.lang == 'fr' else 'النقاط المكتسبة'}: {earned_points}/{total_points}", Color.GOLD))
        self.wait_for_enter()
    
    def practical_lab_menu(self):
        while True:
            self.display.clear()
            self.display.header(self.get_text("practical_lab"), Color.PURPLE)
            print()
            self.display.menu_item("1", self.t["cpu"], Symbol.GEAR)
            self.display.menu_item("2", self.t["processes"], Symbol.TARGET)
            self.display.menu_item("3", self.t["threads"], Symbol.ROCKET)
            self.display.menu_item("4", self.t["memory_mgmt"], Symbol.MEMORY)
            self.display.menu_item("5", self.t["filesystem"], Symbol.BOOK)
            self.display.menu_item("0", self.get_text("back"), Symbol.ARROW_L)
            choice = self.prompt_choice()
            if choice == "1":
                self.simulator.cpu_pipeline()
            elif choice == "2":
                self.simulator.process_scheduler()
            elif choice == "3":
                self.simulator.thread_demo()
            elif choice == "4":
                self.simulator.memory_visualizer()
            elif choice == "5":
                self.simulator.filesystem_tree()
            elif choice == "0":
                break
            if choice in ["1", "2", "3", "4", "5"]:
                self.wait_for_enter()
    
    def progress_menu(self):
        self.display.clear()
        self.display.header(self.get_text("progress"), Color.GOLD)
        print()
        total_lessons = len(LESSONS_DATA)
        completed_lessons = len(self.progress.lessons_completed)
        total_quizzes = len(QUIZ_QUESTIONS)
        completed_quizzes = len(self.progress.quizzes_completed)
        lesson_pct = (completed_lessons / total_lessons) * 100 if total_lessons else 0
        quiz_pct = (completed_quizzes / total_quizzes) * 100 if total_quizzes else 0
        overall = (lesson_pct + quiz_pct) / 2
        bar = self.display.color("█" * int(overall / 5), Color.GREEN) + self.display.color("░" * (20 - int(overall / 5)), Color.DIM)
        print(f"  {self.get_text('total_progress')}: [{bar}] {overall:.1f}%")
        print(f"  {self.get_text('lessons')}: {completed_lessons}/{total_lessons}")
        print(f"  {self.get_text('quiz')}: {completed_quizzes}/{total_quizzes}")
        print(f"  {self.get_text('score')}: {self.display.color(str(self.progress.total_score), Color.GOLD)}")
        print(f"  {self.get_text('level')}: {self.display.color(self.get_level(), Color.CYAN)}")
        print(f"  {self.get_text('study_time')}: {self.progress.study_time_minutes} {self.get_text('minutes')}")
        print()
        print(self.display.color(f"  {self.get_text('achievements')}:", Color.YELLOW))
        for key, name_fr, name_ar in self.achievements_list:
            status = "✅" if key in self.progress.achievements else "🔒"
            name = name_fr if self.lang == "fr" else name_ar
            print(f"    {status} {name}")
        print()
        self.wait_for_enter()
    
    def settings_menu(self):
        while True:
            self.display.clear()
            self.display.header(self.get_text("settings"), Color.CYAN)
            print()
            self.display.menu_item("1", self.get_text("choose_language"), "🌐")
            self.display.menu_item("2", "Réinitialiser la progression" if self.lang == "fr" else "إعادة تعيين التقدم", "🔄")
            self.display.menu_item("0", self.get_text("back"), Symbol.ARROW_L)
            choice = self.prompt_choice()
            if choice == "1":
                self.language_menu()
            elif choice == "2":
                self.reset_progress()
            elif choice == "0":
                break
    
    def reset_progress(self):
        confirm = self.prompt_choice("Tapez OUI pour confirmer" if self.lang == "fr" else "اكتب نعم للتأكيد")
        if confirm.lower() in ["oui", "yes", "نعم"]:
            self.progress = UserProgress(username=self.progress.username, language=self.lang)
            self.progress_manager.save(self.progress)
            self.display.success("Progression réinitialisée" if self.lang == "fr" else "تم إعادة تعيين التقدم")
        else:
            self.display.info("Annulé" if self.lang == "fr" else "تم الإلغاء")
        self.wait_for_enter()
    
    def about_menu(self):
        self.display.clear()
        self.display.header(self.get_text("about"), Color.GOLD)
        print()
        lines = [
            f"{Symbol.ROCKET} {APP_NAME} - {APP_NAME_AR}",
            f"{Symbol.STAR} {self.get_text('app_title')}",
            f"{Symbol.COMPUTER} Version: {VERSION}",
            f"{Symbol.GEAR} Auteur: {AUTHOR}",
            f"{Symbol.BOOK} Cours: {self.get_text('lessons')}",
            f"{Symbol.TARGET} Quiz: {len(QUIZ_QUESTIONS)} questions",
            f"{Symbol.ROCKET} Labo pratique: simulations interactives",
            "",
            "Objectif: Apprendre les fondamentaux de l'informatique",
            "de manière interactive, en français et en arabe."
        ]
        for line in lines:
            print(self.display.center(line))
        print()
        self.wait_for_enter()
    
    def check_achievements(self):
        if not self.progress.achievements:
            self.unlock_achievement("first_steps")
        if len(self.progress.lessons_completed) >= 5:
            self.unlock_achievement("lesson_master")
        if len(self.progress.quizzes_completed) >= 5:
            self.unlock_achievement("quiz_warrior")
        hardware_lessons = {1, 2, 3, 4, 5, 6, 7, 8}
        if hardware_lessons.issubset(set(self.progress.lessons_completed)):
            self.unlock_achievement("hardware_expert")
        if 10 in self.progress.lessons_completed:
            self.unlock_achievement("os_guru")
        if 11 in self.progress.lessons_completed and 12 in self.progress.lessons_completed:
            self.unlock_achievement("architecture_ninja")
        if 15 in self.progress.lessons_completed and 16 in self.progress.lessons_completed:
            self.unlock_achievement("memory_wizard")
    
    def unlock_achievement(self, key: str):
        if key not in self.progress.achievements:
            self.progress.achievements.append(key)
            names = {k: (fr, ar) for k, fr, ar in self.achievements_list}
            name_fr, name_ar = names.get(key, (key, key))
            name = name_fr if self.lang == "fr" else name_ar
            self.display.success(f"🏆 Succès débloqué: {name}" if self.lang == "fr" else f"🏆 تم فتح الإنجاز: {name}")
            time.sleep(1)
    
    def run(self):
        if not self.progress.username:
            self.language_menu()
        while self.running:
            choice = self.main_menu()
            if choice == "1":
                self.lessons_menu()
            elif choice == "2":
                self.quiz_menu()
            elif choice == "3":
                self.practical_lab_menu()
            elif choice == "4":
                self.progress_menu()
            elif choice == "5":
                self.settings_menu()
            elif choice == "6":
                self.about_menu()
            elif choice == "0":
                self.running = False
                self.display.clear()
                self.display.header(self.get_text("goodbye"), Color.GOLD)
                print()
                print(self.display.center(f"{Symbol.STAR} {AUTHOR} - {VERSION} {Symbol.STAR}"))
                print()
            else:
                self.display.error("Choix invalide" if self.lang == "fr" else "اختيار غير صالح")
                self.wait_for_enter()

# ═══════════════════════════════════════════════════════════════════════════════
# POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    try:
        app = ComFunApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nAu revoir ! / وداعاً!")
        sys.exit(0)

if __name__ == "__main__":
    main()
