L'objectif de ce test est d'évaluer ta rigueur à l'écriture de code, ton abstraction d'un problème donné ainsi que tes aptitudes à documenter ton avancée. Ça sera aussi l'occasion de remettre les mains dans python si besoin et de monter en compétence sur certaines librairies qui te seront utiles dans ta carrière à venir. Tes objectifs, si tu les acceptes:
A partir de la documentation donnée ci-dessous, calculer les temps de cycles de l'ensemble des modules, ainsi que leur MTTRs et MTTFs respectifs.
Réaliser une visualisation 2D du graphe de la ligne de production, et déterminer une manière efficace de rendre compte des différences entre modules.
Construire un algorithme de détection d'anomalies basé sur l'analyse des données de passage des pièces (exits), valable pour chaque module (ce qui ne veut pas dire que la data des autres machines ne peut pas être utilisée). Cet algorithme mettra en évidence, pour un module donné, certains événements anormaux tout en pondérant leur caractère anormal (pondération à déterminer et pouvoir défendre).
Définitions rapides:

Le temps de cycle d'un module est donné par la moyenne des temps de cycle instantanés entre deux pièces dans un flux stationnaire (la machine est opérée normalement et aucun événement ne vient affecter ses opérations).
Le MTTR (mean time to repair) se définit comme la durée moyenne des événements ****'PANNES MICRO ARRETS', 'ATTENTE OPERATEUR', 'ARRETS FONCTIONNELS', 'PERTE EXPLOITATION' qui se produisent pendant la période d'opération d'un module.
Le MTTF (mean time to fail) d'un module est donnée par la formule suivante: (temps de cycle * nombre de pièces produites) / (nombre d'événements bloquants - 1); où les événements bloquants sont ceux donnés juste au-dessus.
Ce qu'il faut savoir:

Je joins à cet email deux fichiers: graph.yaml est une représentation d'un graphe de production réel; sandbox.db est un extrait de données.
Conventions dans graph.yaml: module, qui représente une machine; buffer, qui représente des stocks intermédiaires; artifact, qui a la même vocation que les buffers à la différence qu'ils sont artificiels et créés pour des besoins de cohérence; operator, qui représente un poste avec lequel des ouvriers interagissent directement. Par convention, un buffer (ou artifact) relie un ou deux modules au maximum, alors qu'un module n'a pas un nombre de liens maximum.
Conventions dans sandbox.yaml: DF109BFD_Exits contient les timestamps (secondes, UTC) de sorties de pièce de certaines machines; DF109BFD_Buffers qui contient la valeur des stocks à chaque événement (remplissage, déstockage); DF109BFD_Events qui contient l'ensemble des événements qui se produisent sur l'ensemble des machines; DF109BFD_Teams correspond aux calendriers des rotations des équipes opérant sur ces machines.
Finalement, deux petits détails:

Tu peux interagir avec le fichier graph.yaml de la même manière que tu interagis avec un fichier JSON, mais cette fois en utilisant un package de type PyYAML.
La base de données sandbox.db a été créée en utilisant la librairie python sqlite3, une version light et très utile en développement de SQL.