---
language: cz
title: Kombinatorika a Grafy II
category: "lecture notes"
---


- .
{:toc}

{% lecture_notes_preface Martina Kouteckého|2021/2022%}

### 1. přednáška

#### Největší párování

{% math definition %}Párování v {% latex %}G = \left(V, E\right){% endlatex %} je {% latex %}M \subseteq E{% endlatex %} t. ž. {% latex %}\forall v \in V \exists \le 1{% endlatex %} hrana {% latex %}e \in M: v \in e{% endlatex %}{% endmath %}

- **maximální** (do inkluze) -- přidání další hrany pro dané párování už není možné
	- nezajímá nás (v přednášce), prostě hladově přidávejme
- **největší** -- {% latex %}\mathrm{max}(|M|){% endlatex %}

{% math definition %}**volný vrchol** (vzhledem k {% latex %}M{% endlatex %}) -- vrchol, kterého se nedotýká žádná hrana párování{% endmath %}

{% math definition %}**střídavá cesta** (vzdledem k {% latex %}M{% endlatex %}) -- cesta, na které se střídají hrany v párování a hrany mimo párování: {% latex %}u_0, \ldots, u_k{% endlatex %}, kde každá sudá/lichá hrana je v {% latex %}M{% endlatex %}, lichá/sudá není v {% latex %}M{% endlatex %}{% endmath %}

- **volná** střídavá cesta (VSC) -- krajní vrcholy jsou volné (vůči párování)
- {% latex %}\implies{% endlatex %} obsahuje lichý počet hran, sudý počet vrcholů

{% math lemma %}Nechť {% latex %}G = \left(V, E\right){% endlatex %} je graf, {% latex %}M{% endlatex %} párování v {% latex %}G{% endlatex %}. Pak {% latex %}G{% endlatex %} obsahuje VSC (vzhledem k {% latex %}M{% endlatex %}), právě když {% latex %}M{% endlatex %} není největší párování v {% latex %}G{% endlatex %}.{% endmath %}

{:.rightFloatBox}
<div markdown="1">
{:.center}
![](/assets/kombinatorika-a-grafy-ii/alter.svg)
</div>
- {% latex %}\Leftarrow{% endlatex %} pokud {% latex %}M{% endlatex %} má VSC, mohu {% latex %}M{% endlatex %} zvětšit prohozením hran

- {% latex %}\Leftarrow{% endlatex %} nechť {% latex %}M'{% endlatex %} je párování v {% latex %}G{% endlatex %} t. ž {% latex %}|M'| \ge |M|{% endlatex %}
	- uvažme {% latex %}H = \left(V, M \cup M'\right){% endlatex %}; pak má každý vrchol supeň {% latex %}0, 1{% endlatex %} nebo {% latex %}2{% endlatex %} \implies komponenty souvislosti jsou kružnice sudé délky a cesty
	- (👀) -- musí existovat komponenta, která má více hran z {% latex %}M'{% endlatex %}
		- není to kružnice (musela by být lichá a měli bychom máme kolizi ve vrcholu)
		- je to volná (z definice, vzhledem k {% latex %}M{% endlatex %}) střídavá (jinak by měly stejný počet hran) cesta

---

{% math definition %}květ -- lichá „střídavá“ kružnice s vrcholem {% latex %}v_1{% endlatex %}, ke kterému přiléhají dva vrcholy {% latex %}\not\in M{% endlatex %}{% endmath %}
{% math definition %}stonek -- střídavá cesta z {% latex %}v_1{% endlatex %} (i nulové) délky končící volným vrcholem (dál od květu){% endmath %}
- {% latex %}v_1{% endlatex %} může (a nemusí) být volný vrchol -- stačí, aby byl volný vzhledem ke květu

{% math definition %}kytka -- květ + stonek{% endmath %}

{:.center}
![](/assets/kombinatorika-a-grafy-ii/kytka.svg)

{% math definition %} Nechť {% latex %}G = \left(V, E\right){% endlatex %} je neorientovaný graf a {% latex %}e = \left\{u, v\right\}{% endlatex %} jeho hrana. Zápis {% latex %}G . e{% endlatex %} označuje graf vzniklý z {% latex %}G{% endlatex %} kontrakcí („smrštěním“) hrany {% latex %}e{% endlatex %} do jednoho vrcholu:{% endmath %}

{:.center}
![](/assets/kombinatorika-a-grafy-ii/kontrakce.svg)

{% math lemma %}Nechť {% latex %}C{% endlatex %} je květ v grafu {% latex %}G{% endlatex %}. Potom párování {% latex %}M{% endlatex %} v {% latex %}G{% endlatex %} je maximální, právě když {% latex %}M \setminus E(C){% endlatex %} je maximální párování v grafu {% latex %}G . C{% endlatex %}, tj. s květem {% latex %}C{% endlatex %} zkontrahovaným do jediného vrcholu.{% endmath %}

TODO: důkaz?

{% math algorithm %}Edmondsův „zahradní“ algoritmus -- Vstupem je graf {% latex %}G{% endlatex %} a jeho libovolné párování {% latex %}M{% endlatex %}, třeba prázdné. Výstupem je párování {% latex %}M'{% endlatex %}, které je alespoň o {% latex %}1{% endlatex %} větší, než {% latex %}M{% endlatex %}, případně {% latex %}M{% endlatex %} pokud bylo maximální.{% endmath %}

- zkonstruujeme maximální možný **Edmondsův les** vzhledem k aktuálnímu {% latex %}M{% endlatex %} tím, že z volných vrcolů pustíme BFS a střídavě přidáváme vrcholy
	- hranám, které se v lese neobjeví, se říká kompost a nebudou pro nás důležité

{:.center}
![](/assets/kombinatorika-a-grafy-ii/les.svg)

- pokud existuje hrana mezi sudými hladinami různých stromů, pak máme volnou střídavou cestu, kterou zalterujeme
- pokud existuje hrana mezi sudými hladinami jednoho stromu, máme květ {% latex %}C{% endlatex %} -- ten zkontrahujeme a rekurzivně se zavolame
	- vrátí-li {% latex %}M' = M{% endlatex %}, pak nic dalšího neděláme
	- vratí-li nějaké větší párování, tak vhodně zpárujeme {% latex %}C{% endlatex %}
- neexistuje-li hrana mezi sudými hladinami, pak {% latex %}M' = M{% endlatex %}

TODO: časová složitost, důkaz správnosti?

### 2. přednáška

{% math definition %}Párování {% latex %}M{% endlatex %} je perfektní, pokud neexistuje v {% latex %}G{% endlatex %} žádný volný vrchol (vůči {% latex %}M{% endlatex %}).{% endmath %}

#### Tutteova věta
{% math definition %}Tutteova podmínka: {% latex %}\forall S \subseteq V: \mathrm{odd}(G - S) \le |S|{% endlatex %}
- kde {% latex %}\mathrm{odd}{% endlatex %} je počet lichých komponent grafu{% endmath %}.

{% math theorem %}Tutteova věta: {% latex %}G{% endlatex %} má perfektní párování {% latex %}\iff{% endlatex %} platí Tutteova podmínka.{% endmath %}

{% math proof %}
{% latex %}\Rightarrow{% endlatex %} obměna: neplatí TP {% latex %}\implies{% endlatex %} není PP. Nehchť {% latex %}\exists S \subseteq V{% endlatex %} t. ž. {% latex %}\mathrm{odd(G - S)} > |S|{% endlatex %}. V perfektním párování by se alespoň {% latex %}1{% endlatex %} vrchol musel spárovat s {% latex %}S{% endlatex %}. To ale nejde, protože jich v {% latex %}S{% endlatex %} není dostatek.

{% latex %}\Leftarrow{% endlatex %} nechť {% latex %}G{% endlatex %} splňuje Tutteovu podmínku. {% latex %}|V|{% endlatex %} je sudá (nastavíme množinu prázdnou). Dokážeme, že {% latex %}G{% endlatex %} má PP indukcí podle počtu nehran.

- základ: {% latex %}G = K_{2n}{% endlatex %}, ten PP má
- indukční podmínka: {% latex %}G{% endlatex %} má nehranu a každý graf na {% latex %}V{% endlatex %}s počtem hran alespoň o 1 větší než {% latex %}|E|{% endlatex %} a platí TP, pak má perfektní párování

- (👀) -- přidáním hrany do grafu se neporuší TP ({% latex %}\forall S \subseteq V{% endlatex %} počet lichých komponent {% latex %}G - S{% endlatex %} buď klesne o {% latex %}2{% endlatex %} nebo zůstane stejný).

{% math definition %}{% latex %}S = \left\{v \in V\ |\ \mathrm{deg}(v) = n - 1\right\} = \left\{v \mid \text{$v$ je spojený se všemi vrcholy} \right\}{% endlatex %}{% endmath %}
- lehký příklad: každá komponenta {% latex %}G - S{% endlatex %} je lichá klika
	- v rámci dané kliky vypáruji vše až na jeden vrchol, ten spáruji v rámci {% latex %}S{% endlatex %} ({% latex %}S{% endlatex %} vidí všechny) a zbytek v {% latex %}S{% endlatex %} spáruji spolu
- alespoň {% latex %}1{% endlatex %} komponenta {% latex %}K{% endlatex %} není klika, tedy {% latex %}\exists x, y{% endlatex %} nesousedi {% latex %}x, y{% endlatex %}
	- ti mají společného souseda {% latex %}u{% endlatex %} (TODO tvrzení)
	- jelikož {% latex %}u{% endlatex %} není spojený s {% latex %}S{% endlatex %}, tak je spojený s nějakým vrcholem {% latex %}v{% endlatex %}

{:.center}
![](/assets/kombinatorika-a-grafy-ii/xyuv.svg)

{% latex %}G_1 = G + e_1{% endlatex %} a {% latex %}G_2 = G + e_2{% endlatex %} díky předchozímu pozorování splňují TP a spolu s IP {% latex %}\implies \exists{% endlatex %} PP {% latex %}M_1, M_2{% endlatex %} v {% latex %}G_1, G_2{% endlatex %}
- jednoduchý příklad: {% latex %}e_1{% endlatex %} nepatří do {% latex %}M_1 \implies M_1{% endlatex %} je PP pro {% latex %}G{% endlatex %}, analogicky pro {% latex %}G{% endlatex %} (případně přealternuju cyklus, na kterém je)

Předpokládejme {% latex %}e_1 \in M_1, e_2 \in M_2, H = (V, M_1 \cup M_2){% endlatex %}. {% latex %}H {% endlatex %} tedy obsahuje „dvoubarevné hrany“ {% latex %}e \in M_1 \cap M_2{% endlatex %} nebo střídavé sudé cykly. Navíc neobsahuje izolované vrcholy a střídavé cesty, protože {% latex %}M_1, M_2{% endlatex %} byly perfektní.
- jednodušší případ: {% latex %}e_1{% endlatex %} leží v jiné komponentě {% latex %}H{% endlatex %} než {% latex %}e_2{% endlatex %} -- stačí přealternovat hrany tak, aby ani {% latex %}e_1{% endlatex %} ani {% latex %}e_2{% endlatex %} v {% latex %}H{% endlatex %} neležely.

{:.center}
![](/assets/kombinatorika-a-grafy-ii/easy.svg)

- složitější příklad: spojíme {% latex %}uy{% endlatex %} a zbytek patřičně doplníme

{:.center}
![](/assets/kombinatorika-a-grafy-ii/hard.svg)

{% endmath %}

{% math theorem %}Petersen: každý {% latex %}3{% endlatex %}-regulární {% latex %}2{% endlatex %}-souvislý (vrcholově i hranově, pro 2-souvislost) graf má PP.{% endmath %}

{% math proof %}Nechť {% latex %}G = (V, E){% endlatex %} je {% latex %}3{% endlatex %}-regulární a {% latex %}2{% endlatex %}-souvislý. Chci ukázat, že {% latex %}G{% endlatex %} splňuje TP. Předpokládejme danou {% latex %}S \subseteq V{% endlatex %}.

1. každá {% latex %}G - S{% endlatex %} je v {% latex %}G{% endlatex %} spojena aspoň dvěma hranami s {% latex %}S{% endlatex %} (je {% latex %}2{% endlatex %}-souvislý...)
2. každá lichá komponenta {% latex %}G - S{% endlatex %} je s {% latex %}S{% endlatex %} spojena lichým počtem hran
	- nechť {% latex %}L{% endlatex %} je lichá komponenta {% latex %}G - S{% endlatex %}; pak:
{% latex display %}\sum_{x \in V(L)}^{\mathrm{deg}_G(x)} \overset{3-\text{reg.}}{=} \underbrace{3|V(L)|}_{\text{liché}} = \underbrace{2 (\text{\# hran vedoucích uvnitř $L$})}_{\text{sudé}} + \underbrace{1 (\text{\# hran vedoucích uvnitř $L$})}_{\text{liché}}{% endlatex %}
což je přesně to, co jsem potřeboval (počet hran vedoucích z {% latex %}L{% endlatex %})

TODO: obrázek

{% latex %}p = \text{\# hran mezi $S$ a lichou komponentou $G - S$}{% endlatex %}
- {% latex %}p \ge 3 \cdot \mathrm{odd(G - S)}{% endlatex %}
- {% latex %}p \le 3 \cdot |S|{% endlatex %} (každý vrchol {% latex %}S{% endlatex %} vysílá ven {% latex %}\le 3{% endlatex %} hrany (z 3-regularity))

{% latex %}3|S| \ge 3 \cdot \mathrm{odd}(G - S){% endlatex %}, tedy TP platí a graf má perfektní párování.
{% endmath %}

### 3. přednáška


#### Tutte v2.0

{% math lemma %}O kontrahovatelné hraně: Nechť {% latex %}G{% endlatex %} je 3-souvislý různý od {% latex %}K_4{% endlatex %} ({% latex %}|V| \ge 5{% endlatex %}). Potom {% latex %}G{% endlatex %} obsahuje hranu t. ž. {% latex %}G \ e{% endlatex %} je 3-souvislý.{% endmath %}

{% math proof %}Sporem -- nechť {% latex %}G{% endlatex %} je 3-souvislý ale neexistuje žádná hrana. Tedy {% latex %}\forall e \in E: G \ e{% endlatex %} není 3-souvislý.

{% math theorem %}Pomocné: {% latex %}\forall e = \left\{x, y\right\} \exists z_e \in V \setminus \left\{x, y\right\}{% endlatex %} t. ž. {% latex %}\left\{x, y, z_e\right\}{% endlatex %} tvoří vrcholový řez v G, navíc každý z {% latex %}\left\{x, y, z_e\right\}{% endlatex %} má alespoň jednoho souseda v každé komponentě {% latex %}G \setminus \left\{x, y, z_e\right\}{% endlatex %}.
- počítáme s předpokladem, že žádná hrana není kontrahovatelná!
{% endmath %}

- (👀) -- {% latex %}S{% endlatex %} minimální vrcholový řez {% latex %}G{% endlatex %}, pak každý vrchol {% latex %}S{% endlatex %} má souseda v každé komponentě {% latex %}G \setminus S{% endlatex %} (když to pro nějaký {% latex %}v{% endlatex %} neplatí, tak {% latex %}S \setminus v{% endlatex %} je pořád řez).

TOOD: obrázek?

{% math proof %}
Vím, že {% latex %}G \setminus e{% endlatex %} není 3-souvislý, tedy má vrcholový řez velikosti 2. Nechť {% latex %}v_e = {% endlatex %} vrchol vzniklý kontrakcí {% latex %}\left\{x, y\right\} = e{% endlatex %}. Tento řez obsahuje {% latex %}v_e{% endlatex %}, jinak by to byl řez už pro {% latex %}G{% endlatex %}.

Označme řez {% latex %}v_e, z_e{% endlatex %}.

TODO: obrázek?

Po rozkontrahování vidíme, že {% latex %}\forall \left\{x, y, z_e\right\}{% endlatex %} musí mít souseda v každé komponentě (jinak spor s 3-souvislostí). Tedy {% latex %}z_e{% endlatex %} je hledaný vrchol.
{% endmath %}

Pro důkaz původního lemmatu si zvolím {% latex %}e = \left\{x, y \right\} \in E{% endlatex %} a {% latex %}z_e{% endlatex %} z pomocného tvrzení tak, aby nejmenší komponenta {% latex %}G - z, y, z_e{% endlatex %} byla co nejmenší (co do počtu vrcholů).

TODO: obrázek?

Protože {% latex %}z_e{% endlatex %} má souseda ve všech komponentách, má nějakého souseda {% latex %}u \in C, f = \left\{z_e, u\right\}{% endlatex %} (kde {% latex %}C{% endlatex %} je naše nejmenší komponenta). Pomocné tvrzení pro {% latex %}f{% endlatex %} dá nějaký {% latex %}z_f \in V{% endlatex %} t. ž. {% latex %}\left\{z_e, z_f, u\right\}{% endlatex %} je vrcholový řez {% latex %}G{% endlatex %}.

Nechť {% latex %}D{% endlatex %} je komponenta {% latex %}G - z_e, z_f, u{% endlatex %} neobsahující {% latex %}x, y{% endlatex %} (existuje, protože {% latex %}x, y{% endlatex %} jsou spojené a graf se rozpadne alespoň na 2 komponenty). Tvrdím, že {% latex %}D \subseteq C \setminus \left\{u\right\}{% endlatex %}, protože {% latex %}D{% endlatex %} nemůže obsahovat {% latex %}z_e, z_f, u{% endlatex %} (vrcholy řezu), {% latex %}x, y{% endlatex %} (z definice {% latex %}D{% endlatex %}), ale {% latex %}u{% endlatex %} má souseda, takže v {% latex %}D{% endlatex %} ještě něco zbyde. Tedy {% latex %}|D| < |C|{% endlatex %}, což je spor s minimalitou.
{% endmath %}

{% math theorem %}Tutteova charakterizace 3-souvislých grafů: Graf {% latex %}G{% endlatex %} je 3-souvislý {% latex %}\iff{% endlatex %} existuje posloupnost {% latex %}K_4 \cong G_0 \cong G_1 \cong \ldots \cong G{% endlatex %} t. ž. {% latex %}\forall i \in [n], G_{i - 1}{% endlatex %} vznikne z {% latex %}G_i{% endlatex %} kontrakcí hrany, navíc {% latex %}G_i{% endlatex %} má všechny vrcholy stupně {% latex %}\ge 3{% endlatex %}{% endmath %}

TODO: obrázek?

{% math proof %} {% latex %}\Rightarrow{% endlatex %} Jednoduchá induktivní aplikace lemma o kontrahovatelné hraně.
{% latex %}\Leftarrow{% endlatex %} Mějme {% latex %}G_0, \ldots, G_n{% endlatex %} dle předpokladu. Chceme, že {% latex %}G_n \cong G{% endlatex %} je 3-souvislý. Indukcí:
- {% latex %}K_4{% endlatex %} je 3-souvislý
- {% latex %}G_{i - 1}{% endlatex %} je 3-souvislý {% latex %}\implies G_i{% endlatex %} je 3-souvislý

Pro spor nechť {% latex %}G_i{% endlatex %} má vrcholový řez velikosti 2, označme ho {% latex %}R{% endlatex %}. Pak každá komponenta {% latex %}G_i - R{% endlatex %} má alespoň 2 vrcholy {% latex %}x, y{% endlatex %} (TODO: obrázek) (osamocený vrchol může sousedit jen s řezem, ale ten je velikosti 2, spor s {% latex %}\forall \mathrm{deg}(v) \ge 3{% endlatex %}).

Potom ani {% latex %}G_{i - 1}{% endlatex %} nebyl 3-souvislý.
- {% latex %}e = \left\{x, y\right\} \implies G_{i - 1}{% endlatex %} má řez velikosti 1.
- {% latex %}e{% endlatex %} celá obsažená v komponentě {% latex %}\implies \left\{x, y\right\}{% endlatex %} je stále {% latex %}G_{i - 1}{% endlatex %}
- {% latex %}e = \left\{z, y\right\}{% endlatex %} pro {% latex %}z{% endlatex %} z nějaké komponenty {% latex %}\implies \left\{zy, x\right\}{% endlatex %} je řez v {% latex %}G_{i - 1}{% endlatex %}
	- využíváme, že každá komponenta má alespoň {% latex %}2{% endlatex %} vrcholy -- kdyby ne, tak {% latex %}\left\{zy, x\right\}{% endlatex %} nemusí nic odříznout, pokud tam byla jednovrcholová komponenta
{% endmath %}

#### Minory

{% math definition %}Minor: Nechť {% latex %}H, G{% endlatex %} jsou grafy. Pak {% latex %}H{% endlatex %} je minor {% latex %}G{% endlatex %} (nebo že {% latex %}G {% endlatex %} obsahuje {% latex %}H{% endlatex %} jako minor), značíme {% latex %}H \preceq G{% endlatex %}, pokud {% latex %}H{% endlatex %} lze získat z {% latex %}G{% endlatex %} posloupností mazání vrcholů, mazání hran nebo kontrakcí hran.{% endmath %}

TODO: příklad

- (👀) -- {% latex %}\preceq{% endlatex %} je transitivní (prostě spojím posloupnosti)
- (👀) -- {% latex %}H{% endlatex %} podgraf {% latex %}G \implies H{% endlatex %} minor {% latex %}G{% endlatex %}
	- podgraf vzniká přesně mazáním vrcholů a mazáním hran
- (👀) -- {% latex %}G{% endlatex %} rovinný {% latex %}\implies{% endlatex %} jeho minory jsou také rovinné
	- pro podgraf očividné, je jen potřeba si rozmyslet kontrakci (že nic topologicky nerozbije)

{% math theorem %}Kuratowského (pro připomenutí): {% latex %}G{% endlatex %} rovinný {% latex %}\iff{% endlatex %} neobsahuje jako dělení {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %}{% endmath %}
- umíme {% latex %}\implies{% endlatex %}, protože {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} nejsou rovinné a dělením se to rovinným také nestane)

{% math theorem %}Kuratowski 1930, Warner 1937: Následující jsou ekvivalentní:
1. {% latex %}G{% endlatex %} je rovinný
2. {% latex %}G{% endlatex %} neobsahuje dělení {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} jako podgraf
3. {% latex %}G{% endlatex %} neobsahuje dělení {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} jako minor.
{% endmath %}

- Kuratowski dokázal {% latex %}1\iff 2{% endlatex %}, Wagner {% latex %}1\iff 3{% endlatex %}

{% math proof %}
- {% latex %}1 \implies 2{% endlatex %} (z prváku)
- {% latex %}3 \implies 2{% endlatex %} (obměna + „obsahuej dělení jako podgraf“ {% latex %}\implies{% endlatex %} „obsahuje minor“)
- {% latex %}1 \implies 3{% endlatex %}: vyplývá z pozorování, že je-li rovinný, tak i minor bude rovinný
- {% latex %}2 \implies 3{% endlatex %} na cvičení.
- {% latex %}3 \implies 1{% endlatex %}: hlavní důkaz.

Indukcí podle {% latex %}|V(G)|{% endlatex %}, pro {% latex %}|V(G)| \le 4{% endlatex %} ok; předpokládám {% latex %}G{% endlatex %} má alespoň 5 vrcholů a neobsahuje {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} jako minor. Rozeberu případy podle {% latex %}k_v(G){% endlatex %} (vrcholová souvislost {% latex %}G{% endlatex %}).
0. {% latex %}\implies{% endlatex %} nesouvislý graf, každá komponenta je rovina podle IP
1. {% latex %}\implies{% endlatex %} artikulačním vrcholem {% latex %}x{% endlatex %} rozpojíme, podle IP nakreslíme (s tím, že {% latex %}x{% endlatex %} bude na vnější stěně -- to umíme tím, že to dáme na kouli a projektujeme na rovinu).
2. {% latex %}\implies{% endlatex %} na cvičení.
3. {% latex %}\implies{% endlatex %} TODO: příští přednáška.
{% endmath %}

### Zdroje/materiály
- [Poznámky Václava Končického](https://kam.mff.cuni.cz/~koncicky/notes/kag2/pdf) z roku 2019.
