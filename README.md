# Projet_Analyse_Num
<p>Introduction général:</p>
<p> Ce projet permet de faire une etude de fonction avec un affichage des résultat.tout d'abord ,on peut  définir une fonction mathématique (polynome, trigonométrique..) avec son intervalle ,on donnant comme résultat son primitivé et sa représentation , dérivéet sa représentation et/ou aussi n ordre de dérivé avec spécification de n et sa représentation . En plus , on peut représenté ,avec la fonction donné au début ,plusierus méthodes de l'analyse numérique comme (méthode de rectangle , méthode des trapézes , méthode des points milieux , méthodes de simspon)en donnant pour chaque fonction sa valeur approché ,valeur exacte et l'erreur.</p>




<FONT color="#6A5ACD" size="8">Méthode de Réctangle:</FONT>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Cette méthode, très élémentaire, basée sur les sommes de Cauchy-Riemann (approchant l'aire sous une courbe) et appliquée à une fonction f continue, permet le calcul approché d'intégrales en choisissant une subdivision régulière de pas         xi+1 - xi = (b - a)/n, donc indépendant de i avec une valeur de n "suffisamment grande".</FONT>
  <FONT FACE="Arial, Helvetica, sans-serif" size="4">On obtient une succession de rectangles en rose ci-contre, d'où le nom de cette méthode, approchant l'aire sous la courbe,  où ci est choisi ici au "milieu" de [xi ; xi+1]. On calcule :</FONT>
  <FONT FACE="Arial, Helvetica, sans-serif" size="4"> Sn = h × Σf(ci) , i variant de 0 à n - 1</FONT>
<FONT FACE="Arial, Helvetica, sans-serif" size="4">avec : h = (b - a)/n , xi = a + i.h , ci = (xi+1 + xi)/2 = a + ih + h/2. Le passage à la limite fournit l'intégrale cherchée</FONT>
<FONT FACE="Arial, Helvetica, sans-serif" size="4">En analyse numérique, la méthode des trapèzes est une méthode pour le calcul numérique d'une intégrale ,s'appuyant sur l'interpolation linéaire par intervalles.</FONT>

<FONT color="#6A5ACD" size="8">Méthode des trapèzes:</FONT>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">En analyse numérique, la méthode des trapèzes est une méthode pour le calcul numérique d'une intégrale ,s'appuyant sur l'interpolation linéaire par intervalles.</FONT>
<p>intégrale</p>
<p>gif</p>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Le principe est d'assimiler la région sous la courbe représentative d'une fonction f définie sur un segment [a , b] à un trapèze et d'en calculer l'aire T :</FONT>


<FONT color="#6A5ACD" size="8">Méthode de simpson:</FONT> 

<FONT FACE="Arial, Helvetica, sans-serif" size="4">En analyse numérique, la méthode de Simpson, du nom de Thomas Simpson, est une technique de calcul numérique d'une intégrale, c'est-à-dire, le calcul approché de:</FONT>
<p>intégrale</p>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Cette méthode utilise l'approximation d'ordre 2 de f par un polynôme quadratique P prenant les mêmes valeurs que f aux points d'abscisse a, b et m = (a + b)⁄2. Pour déterminer l'expression de cette parabole (polynôme de degré 2), on utilise l'interpolation lagrangienne. Le résultat peut être mis sous la forme :</FONT>

<p>formule</p>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Un polynôme étant une fonction très facile à intégrer, on approche l'intégrale de la fonction f sur l'intervalle [a, b], par l'intégrale de P sur ce même intervalle. On a ainsi, la simple formule :</FONT>


<p>valeur approché</p>

<p>photo</p>

<FONT color="#6A5ACD" size="8">Méthode des points milieux:</FONT> 


<FONT FACE="Arial, Helvetica, sans-serif" size="4">En analyse numérique, la méthode du point médian est une méthode permettant de réaliser le calcul numérique d'une intégrale </FONT>


<p>intégrale</p>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Le principe est d'approcher l'intégrale de la fonction f par l'aire d'un rectangle de base le segment [a,b] et de hauteur </FONT>

<p>f(a+b/2)</p>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">ce qui donne : </FONT>

<p>r=b-a f(a+b/2)
  
  <FONT FACE="Arial, Helvetica, sans-serif" size="4">Cette aire est aussi celle du trapèze de base [a,b] et dont le côté opposé est tangent au graphe de f en  c= (a+b)/2 ce qui explique sa relative bonne précision.</FONT>

<p>taswira</p>





