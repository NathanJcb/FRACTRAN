# Interpreteur FRACTRAN

## Fibonacci

1. Le code consiste à enregistrer les couples de Fibonacci dans les exposants de 2 et 3
2. On utilise la méthode **`suite()`** de **`Fractran`** pour garder l'historique de toutes les modifications réalisées sur l'entier de départ. De plus, l'utilisation de cette méthode permet d'arrêter après 1000 exécution du programme. On commence avec la valeur $3 = 2^0 + 3^1$ pour avoir le premier couple de Fibonacci $(0,1)$
3. Les fractions du programme utilisent beaucoup de nombre premiers comme variables temporaires pour l'addition. Afin de vérifier si une valeur n de **`sortie_brute`** correspond à un couple de Fibonacci, on vérifie si elle est de la forme $n = 2^i + 3^j$.
   1. Si c'est le cas, alors une boucle de calcul est terminée. L'exposant de 2 et l'exposant de 3 sont un couple de Fibonacci, on les extrait à l'aide de **`decomposition(n)`** et on les ajoute à **`sortie`**
   2. Sinon, d'autres facteurs sont présents dans la décomposition en facteurs premiers de n. Le programme est en plein milieu d'une boucle de calcul et les exposants de 2 et de 3 ne sont pas un couple de Fibonacci