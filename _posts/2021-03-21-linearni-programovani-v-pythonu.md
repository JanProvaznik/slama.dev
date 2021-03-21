---
language: cz
title: Lineární programování v Pythonu
---


- .
{:toc}

### Úvodní informace
Tato stránka obsahuje náhodné programy ze cvičení/přednášky předmětu Lineární programování a kombinatorická optimalizace. Ke spuštění programů je potřeba nainstalovat Pythoní knihovnu `pulp` (přes `pip install pulp`), kterou k řešení problémů používám.

Pokud s `pulp`em také vyřešíte nějaký problém, tak budu moc rád za email/pull request, ať tu máme příkladů co možná nejvíce 🙂.

### Praktické příklady

#### Problém pekárny
Pekárna má k dispozici {% latex %}5{% endlatex %} kilo mouky, {% latex %}125{% endlatex %} vajec a půl kila soli. Za jeden chleba získá pekárna {% latex %}20{% endlatex %} korun, za housku {% latex %}2{% endlatex %} koruny, za bagetu {% latex %}10{% endlatex %} korun a za koblihu {% latex %}7{% endlatex %} korun. Pekárna se snaží vydělat co nejvíce. Jak ale zjistí kolik chlebů, housek, baget a koblih má upéci?

<details>
	<summary class="code-summary">Zdrojový kód</summary>
	<div markdown="1">
```py
{% include linearni-programovani-v-pythonu/pekarna.py %}```
</div>
</details>

#### Problém batohu
Pro {% latex %}n{% endlatex %} předmětů, kde {% latex %}i{% endlatex %}-tý má nějakou váhu {% latex %}v_i{% endlatex %} a cenu {% latex %}c_i{% endlatex %}, máme batoh s danou nosností {% latex %}V{% endlatex %} a my se do něj snažíme naskládat předměty tak, abychom maximalizovali celkovou cenu předmětů v batohu.

<details>
	<summary class="code-summary">Zdrojový kód</summary>
	<div markdown="1">
```py
{% include linearni-programovani-v-pythonu/batoh.py %}```
</div>
</details>

#### Prokládání přímkou

Máme-li {% latex %}n{% endlatex %} bodů {% latex %}(x_1 , y_1 ), \ldots, (x_n , y_n ){% endlatex %} v rovině, tak najděte přímku {% latex %}\left\{x \in \mathbb{R}: y = ax + b\right\}{% endlatex %}, která minimalizuje součet vertikálních vzdáleností bodů od výsledné přímky. Vertikální vzdálenost je vzdálenost měřena pouze na ose {% latex %}y{% endlatex %}. Pro jednoduchost předpokládejte, že výsledná přímka není kolmá na osu {% latex %}x{% endlatex %}.

<details>
	<summary class="code-summary">Zdrojový kód</summary>
	<div markdown="1">
```py
{% include linearni-programovani-v-pythonu/prokladani.py %}```
</div>
</details>

#### Obarvitelnost grafu

Nalezněte minimální {% latex %}k{% endlatex %} takové, že vrcholy grafu {% latex %}G{% endlatex %} lze korektně obarvit {% latex %}k{% endlatex %} barvami.

<details>
	<summary class="code-summary">Zdrojový kód</summary>
	<div markdown="1">
```py
{% include linearni-programovani-v-pythonu/obarvitelnost.py %}```
</div>
</details>

#### Problém obchodního cestujícího
Pro daný ohodnocený neorientovaný graf {% latex %}G = (V, E, f){% endlatex %}, kde {% latex %}f : E \mapsto \mathbb{R}^+_0{% endlatex %}, chceme najít Hamiltonovskou kružnici v {% latex %}G{% endlatex %} s nejmenším ohodnocením.

<details>
	<summary class="code-summary">Zdrojový kód</summary>
	<div markdown="1">
```py
{% include linearni-programovani-v-pythonu/tsp.py %}```
</div>
</details>

#### Bin packing
Zjistěte, do kolika nejméně krabic lze rozdělit množinu {% latex %}n{% endlatex %} předmětů s vahami {% latex %}w_1, \ldots, w_i{% endlatex %}. Do každého koše lze umístit předměty o celkové váze nejvýše {% latex %}C{% endlatex %}.

<details>
	<summary class="code-summary">Zdrojový kód</summary>
	<div markdown="1">
```py
{% include linearni-programovani-v-pythonu/bin.py %}```
</div>
</details>

#### Partition problem
Zjistěte, zda množinu {% latex %}n{% endlatex %} předmětů s vahami {% latex %}w_1, \ldots, w_i{% endlatex %} jde rozdělit na dvě části tak, aby součty vah těchto částí byly stejné.

<details>
	<summary class="code-summary">Zdrojový kód</summary>
	<div markdown="1">
```py
{% include linearni-programovani-v-pythonu/partition.py %}```
</div>
</details>

### Zdroje/materiály
- [Hands-On Linear Programming: Optimization With Python](https://realpython.com/linear-programming-python/)
- [Dokumentace k PuLPu](https://coin-or.github.io/pulp/)
- [Datasety obecně](https://people.sc.fsu.edu/~jburkardt/datasets/)
- [Datasety k TSP](https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html)
- [Datasety k batohu](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)
- [Datasety k partition problému](https://people.sc.fsu.edu/~jburkardt/datasets/partition_problem/partition_problem.html)
