# Projet_Analyse_Num
<h1>Sommaire:</h1>

<ul>
  <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#introduction-g%C3%A9n%C3%A9ral">Introduction Générale</a>
    </li>
  <li>
    <a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#etude-dune-fonction--">
      Etude d'une fonction</a>
    <ul>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-1but-">But</a>
        </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-2etude-de-fonction">
        Etude de fonction</a>
        </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-3etude-graphique">Etude Graphique</a>
      </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-4etude-de-primitive-">
        Etude de primitive</a>
        </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-5etude-de-d%C3%A9riv%C3%A9">
        Etude de dérivé</a>
        </li>
      <ul><li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-5aordre-de-d%C3%A9riv%C3%A9"> 
        Ordre de dérivé</a>
        </li></ul>
   </ul>
  </li>
  <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-m%C3%A9thodes-dint%C3%A9gration-num%C3%A9rique">
    Methode d'intégration numérique </a>
    <ul>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-1but">
        But</a>
        </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-2m%C3%A9thode-de-r%C3%A9ctangle">
        Méthode de Réctangle</a>
        </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-3m%C3%A9thode-des-trap%C3%A8zes">
        Méthode des Trapézes</a>
        </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-4m%C3%A9thode-de-simpson">
        Méthode de Simpson</a>
        </li>
      <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-5m%C3%A9thode-des-points-milieux">
        Méthode des Points Milieux</li>
    </ul>
  </li>
  <li><a href="https://github.com/MohamedAmineBoufares/Projet_Analyse_Num/blob/main/README.md#-conclustion-et-perspectives">
    Conclustion et perspectives </a></li>
</ul>

<h1>Introduction général:</h1>

<p> Ce projet permet d'étuder une fonction <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)" target="_blank"> <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" /></a> et de la  représenter graphiquement  aussi de calculer et de représenter les méthodes d'intégration numériques .</p>
<p>Tout d'abord ,on peut  définir une fonction mathématique <i>(polynome, trigonométrique..)</i> avec son intervalle ,on donnant comme résultat son primitivé et sa représentation , dérivéet sa représentation et/ou aussi n ordre de dérivé en spécifiant n et sa représentation . </p>

<img src="/Pictures/demo_f.gif" alt="Calculer le dérive et prémitive de f(x) et afficher les 3 courbes" width="800" height="400">

<p>En plus , on peut représenté ,avec la fonction donné au début ,plusierus méthodes d'intégration numérique comme <i>(méthode de rectangle , méthode des trapézes , méthode des points milieux , méthodes de simspon)</i> en donnant pour chaque fonction sa valeur approché ,valeur exacte et l'erreur.</p>

<img src="/Pictures/demo_integ.gif" alt="Calculer la valeur exacte d'un itégrale et calculer et afficher la valeur approché ansi que l'erreur d'une méthode d'analyse numérique" width="800" height="400">

<h1>Etude d'une fonction : </h1>

<h2> 1.But </h2>
<p>Une étude de fonction est la détermination de certaines propriétés d'une fonction numérique pour en tracer une représentation graphique à partir d'une expression analytique ou d'une équation fonctionnelle, ou encore pour en déduire le nombre et la disposition d'antécédents pour diverses valeurs numériques.</p>


<h2> 2.Etude de fonction:</h2>
<p>Pour étudier une fonction <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)" target="_blank"> <img src="https://latex.codecogs.com/gif.latex?f(x)" title="f(x)" /></a>, il faut passer d'abord par la détermination du domaine de définition et vise essentiellement la description des variations, voire des lignes de niveau dans le cas de fonctions de plusieurs variables.</p>

<h2> 3.Etude graphique:</h2>
<p>Lorsqu'une fonction est donnée par une représentation de courbe, la lecture graphique permet de lire son domaine de définition, à savoir l'ensemble des points de l'axe des abscisses pour lesquels la courbe associe une ordonnée.</p>
<p>Les intersections de la courbe avec l'axe des abscisses indiquent les points d'annulation de la fonction,si la fonction est continue,déterminer sa signe <i>(si la courbe est au-dessus de l'axe des abscisses, la fonction est positive sur cet intervalle et si la courbe est en dessous de l'axe des abscisses, la fonction est négative sur cet intervalle)</i></p>
<p>La lecture graphique permet aussi de repérer les intervalles en abscisse sur lesquels la fonction est monotone, c'est-à-dire soit croissante, soit décroissante.</p>

<h2> 4.Etude de primitive :</h2>
<p>Une primitive d’une fonction  f est une fonction F dont f est la dérivée : <a href="https://www.codecogs.com/eqnedit.php?latex=F'=f" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F'=f" title="F'=f" style="text-align:center;" /></a>. Il s’agit donc d’un antécédent pour l’opération de dérivation.</p>

<p>La détermination d’une primitive sert d’abord au calcul des intégrales de fonctions continues sur un segment, en application du théorème fondamental de l'analyse:</p> 
<a href="https://www.codecogs.com/eqnedit.php?latex=\int_{a}^{b}f(x)dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{a}^{b}f(x)dx" title="\int_{a}^{b}f(x)dx" /></a>

<h2 > 5.Etude de dérivé:</h2>
<p>La dérivée d'une fonction f est une fonction qui, à tout nombre pour lequel f admet un nombre dérivé, associe ce nombre dérivé. La dérivée en un point d'une fonction de plusieurs variables réelles, ou à valeurs vectorielles, est plus couramment appelée différentielle de la fonction en ce point, et n'est pas traitée ici. La dérivée d'une fonction f en x est usuellement notée</p> 
<a href="https://www.codecogs.com/eqnedit.php?latex=f'(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f'(x)" title="f'(x)" /></a> 
<p>ou</p> 
<a href="https://www.codecogs.com/eqnedit.php?latex=df/dx(x)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?df/dx(x)" title="df/dx(x)" /></a>
 
 <h3> 5.a.Ordre de dérivé:</h3>
<p> Soit f une fonction dérivable sur un intervalle I ,  Si <a href="https://www.codecogs.com/eqnedit.php?latex=f'" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f'" title="f'" /></a> est dérivable sur I sa fonction dérivée <a href="https://www.codecogs.com/eqnedit.php?latex=f''" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f''" title="f''" /></a> <i>(ou  est appelée dérivée seconde de <a href="https://www.codecogs.com/eqnedit.php?latex=f''" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f" title="f" /></a>.</i>
On peut continuer le processus de dérivation et définir une relation de récurrence pour calculer la fonction dérivée  à l'ordre <a href="https://www.codecogs.com/eqnedit.php?latex=f^{(n{\color{Red}&space;})}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f^{(n{\color{Red}&space;})}" title="f^{(n{\color{Red} })}" /></a> à l'ordre n.
La fonction <a href="https://www.codecogs.com/eqnedit.php?latex=f^{(n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f^{(n)}" title="f^{(n)}" /></a> est de classe <a href="https://www.codecogs.com/eqnedit.php?latex=C^{(n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C^{(n)}" title="C^{(n)}" /></a> sur l'intervalle I si <a href="https://www.codecogs.com/eqnedit.php?latex=f^{(n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f^{(n)}" title="f^{(n)}" /></a> existe sur I en étant continue sur I.</p>

<h1> Méthodes d'intégration numérique:</h1> 

<h2> 1.But</h2>
<p>Le but  est d’aborder le calcul général de l’intégrale d’une fonction  <a href="https://www.codecogs.com/eqnedit.php?latex=C^{(n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C^{(n)}" title="f(x)" /></a> sur un domaine fini délimité par des bornes finies a et b.</p>


<h2> 2.Méthode de Réctangle:</h2>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Cette méthode, très élémentaire, basée sur les sommes de Cauchy-Riemann (approchant l'aire sous une courbe) et appliquée à une fonction f continue, permet le calcul approché d'intégrales en choisissant une subdivision régulière de pas </Font> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=xi&plus;1&space;-&space;xi&space;=&space;\frac{(b-a)}{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?xi&plus;1&space;-&space;xi&space;=&space;\frac{(b-a)}{n}" title="xi+1 - xi = \frac{(b-a)}{n}" /></a>
<p>donc indépendant de i avec une valeur de n <i>"suffisamment grande"</i>.</p>
<FONT FACE="Arial, Helvetica, sans-serif" size="4">On obtient une succession de rectangles en rose ci-contre, d'où le nom de cette méthode, approchant l'aire sous la courbe,  où ci est choisi ici au "milieu" de </FONT> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=[xi&space;,&space;xi&plus;1]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?[xi&space;,&space;xi&plus;1]" title="[xi , xi+1]" /></a>
<p>On calcule :</p>
<a href="https://www.codecogs.com/eqnedit.php?latex=S_{n}&space;=&space;h&space;*&space;\sum&space;f(c_{i})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?S_{n}&space;=&space;h&space;*&space;\sum&space;f(c_{i})" title="S_{n} = h * \sum f(c_{i})" /></a>
<p><b>i variant de 0 à n - 1</b></p>
<p>Avec : </p>
<a href="https://www.codecogs.com/eqnedit.php?latex=h&space;=&space;\frac&space;{b-a}{n}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?h&space;=&space;\frac&space;{b-a}{n}" title="h = \frac {b-a}{n}" /></a> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=x_i&space;=&space;a&space;&plus;&space;i.h" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_i&space;=&space;a&space;&plus;&space;i.h" title="x_i = a + i.h" /></a> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=c_i&space;=&space;(x_i&plus;1&space;&plus;&space;x_i)/2&space;=&space;a&space;&plus;&space;i.h&space;&plus;&space;\frac&space;{h}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?c_i&space;=&space;(x_i&plus;1&space;&plus;&space;x_i)/2&space;=&space;a&space;&plus;&space;i.h&space;&plus;&space;\frac&space;{h}{2}" title="c_i = (x_i+1 + x_i)/2 = a + i.h + \frac {h}{2}" /></a>
<p>Le passage à la limite fournit l'intégrale cherchée</p>

<h2> 3.Méthode des trapèzes:</h3>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">En analyse numérique, la méthode des trapèzes est une méthode pour le calcul numérique d'une intégrale ,s'appuyant sur l'interpolation linéaire par intervalles.</FONT> </br>
<a href="https://www.codecogs.com/eqnedit.php?latex=\int_{a}^{b}&space;f(x)dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{a}^{b}&space;f(x)dx" title="\int_{a}^{b} f(x)dx" /></a>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Le principe est d'assimiler la région sous la courbe représentative d'une fonction f définie sur un segment </br>
<a href="https://www.codecogs.com/eqnedit.php?latex=[a&space;,&space;b]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?[a&space;,&space;b]" title="[a , b]" /></a> à un trapèze et d'en calculer l'aire T :</FONT>
<br/><a href="https://www.codecogs.com/eqnedit.php?latex=T&space;=&space;(b-a)&space;\frac{f(a)&plus;f(b)}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T&space;=&space;(b-a)&space;\frac{f(a)&plus;f(b)}{2}" title="T = (b-a) \frac{f(a)+f(b)}{2}" /></a>

<h2> 4.Méthode de simpson:</h2>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">En analyse numérique, la méthode de Simpson,<i>du nom de Thomas Simpson</i>, est une technique de calcul numérique d'une intégrale, c'est-à-dire, le calcul approché de:</FONT> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=\int_{a}^{b}&space;f(x)dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{a}^{b}&space;f(x)dx" title="\int_{a}^{b} f(x)dx" /></a>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Cette méthode utilise l'approximation d'ordre 2 de f par un polynôme quadratique P prenant les mêmes valeurs que f aux points d'abscisse a, b et <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=m&space;=&space;\frac&space;{(a&space;&plus;&space;b)}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?m&space;=&space;\frac&space;{(a&space;&plus;&space;b)}{2}" title="m = \frac {(a + b)}{2}" /></a> <br/>
Pour déterminer l'expression de cette parabole <i>(polynôme de degré 2)</i>, on utilise l'interpolation lagrangienne. Le résultat peut être mis sous la forme :</FONT><br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=P(x)=f(a)\frac{(x-m)(x-b)}{(a-m)(a-b)}&space;&plus;&space;f(m)\frac&space;{(x-a)(x-b)}{(m-a)(m-b)}&space;&plus;&space;f(b)\frac{(x-a)(x-m)}{(b-a)(b-m)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P(x)=f(a)\frac{(x-m)(x-b)}{(a-m)(a-b)}&space;&plus;&space;f(m)\frac&space;{(x-a)(x-b)}{(m-a)(m-b)}&space;&plus;&space;f(b)\frac{(x-a)(x-m)}{(b-a)(b-m)}" title="P(x)=f(a)\frac{(x-m)(x-b)}{(a-m)(a-b)} + f(m)\frac {(x-a)(x-b)}{(m-a)(m-b)} + f(b)\frac{(x-a)(x-m)}{(b-a)(b-m)}" /></a>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">Un polynôme étant une fonction très facile à intégrer, on approche l'intégrale de la fonction f sur l'intervalle [a, b], par l'intégrale de P sur ce même intervalle. On a ainsi, la simple formule :</FONT> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=\int_{a}^{b}f(x)dx&space;\approx&space;\int_{a}^{b}P(x)dx&space;=&space;\frac{b-a}{6}&space;\left&space;[&space;f(a)&plus;4f\left&space;(&space;\frac{a&plus;b}{2}&space;\right&space;)&space;&plus;f(b)\right&space;]" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{a}^{b}f(x)dx&space;\approx&space;\int_{a}^{b}P(x)dx&space;=&space;\frac{b-a}{6}&space;\left&space;[&space;f(a)&plus;4f\left&space;(&space;\frac{a&plus;b}{2}&space;\right&space;)&space;&plus;f(b)\right&space;]" title="\int_{a}^{b}f(x)dx \approx \int_{a}^{b}P(x)dx = \frac{b-a}{6} \left [ f(a)+4f\left ( \frac{a+b}{2} \right ) +f(b)\right ]" /></a>

<h2> 5.Méthode des points milieux:</h2>


<FONT FACE="Arial, Helvetica, sans-serif" size="4">En analyse numérique, la méthode du point médian est une méthode permettant de réaliser le calcul numérique d'une intégrale </FONT> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=\int_{a}^{b}&space;f(x)dx" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_{a}^{b}&space;f(x)dx" title="\int_{a}^{b} f(x)dx" /></a>


<FONT FACE="Arial, Helvetica, sans-serif" size="4">Le principe est d'approcher l'intégrale de la fonction f par l'aire d'un rectangle de base le segment [a,b] et de hauteur </FONT> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=f\left&space;(&space;\frac{a&plus;b}{2}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f\left&space;(&space;\frac{a&plus;b}{2}&space;\right&space;)" title="f\left ( \frac{a+b}{2} \right )" /></a>

<FONT FACE="Arial, Helvetica, sans-serif" size="4">ce qui donne : </FONT>

<a href="https://www.codecogs.com/eqnedit.php?latex=R&space;=&space;(b-a)f\left&space;(&space;\frac{a&plus;b}{2}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R&space;=&space;(b-a)f\left&space;(&space;\frac{a&plus;b}{2}&space;\right&space;)" title="R = (b-a)f\left ( \frac{a+b}{2} \right )" /></a>
  
<FONT FACE="Arial, Helvetica, sans-serif" size="4">Cette aire est aussi celle du trapèze de base [a,b] et dont le côté opposé est tangent au graphe de f en <br/>  
<a href="https://www.codecogs.com/eqnedit.php?latex=C&space;=&space;\frac{a&plus;b}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?C&space;=&space;\frac{a&plus;b}{2}" title="C = \frac{a+b}{2}" /></a> <br/>
ce qui explique sa relative bonne précision.</FONT>

<h1> Conclustion et perspectives</h1>

<p>La thématique centrale de ce projet était l'étude de fonction f(x) donnée en donnant le primitive et le dérivée avec une représentation graphique .Aussi,avec la fonction f(x) donnée, les méthodes d'intégration numérique avec n nombre de subdivision d'intervalle et la valeur exact,valeur approché et la valeur de l'erreur.  </p>
<p>Ce projet peut être bien développer en une application mobile .Et par conséquence ,on peut lire automatiquement la fonction f(x) à partir de la caméra de téléphone sans besion de l'ecrire à l'aide de la technique intélligence artificielle. Cette dernière nécessite une large base de données qui permet de trainer notre modéle avec des images contenant plusierus equations pour le permettre ,enfin, la reconnaissance d'equation avec valeur 100 % de précsions.</p>

<p>Exemple d'application mobile avec I.A qui permet la reconnaissance d'equation mathématique et ensuite l'etude et la résolution de l'équation .</p>

<img src="/Pictures/photomathapp.gif" alt="Calculer le dérive et prémitive de f(x) et afficher les 3 courbes" width="800" height="400">
