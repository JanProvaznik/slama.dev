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

- **maximální** (do inkluze) -- přidání další hrany pro dané párování už není možné; v přednášce nás nezajímá
- **největší** -- {% latex %}\mathrm{max}(|M|){% endlatex %}

{% math definition "volný vrchol" %} (vzhledem k {% latex %}M{% endlatex %}) -- vrchol, kterého se nedotýká žádná hrana párování.{% endmath %}

{% math definition "střídavá cesta" %} (vzdledem k {% latex %}M{% endlatex %}) -- cesta, na které se střídají hrany v párování a hrany mimo párování: {% latex %}u_0, \ldots, u_k{% endlatex %}, kde každá sudá/lichá hrana je v {% latex %}M{% endlatex %}, lichá/sudá není v {% latex %}M{% endlatex %}{% endmath %}

- **volná** střídavá cesta (VSC) -- krajní vrcholy jsou volné (vůči párování)
- {% latex %}\implies{% endlatex %} obsahuje lichý počet hran, sudý počet vrcholů

{% math lemma %}Nechť {% latex %}G = \left(V, E\right){% endlatex %} je graf, {% latex %}M{% endlatex %} párování v {% latex %}G{% endlatex %}. Pak {% latex %}G{% endlatex %} obsahuje VSC (vzhledem k {% latex %}M{% endlatex %}), právě když {% latex %}M{% endlatex %} není největší párování v {% latex %}G{% endlatex %}.{% endmath %}

{:.rightFloatBox}
<div markdown="1">
{:.center}
![](/assets/kombinatorika-a-grafy-ii/alter.svg)
</div>
- {% latex %}\Rightarrow{% endlatex %} pokud {% latex %}M{% endlatex %} má VSC, mohu {% latex %}M{% endlatex %} zvětšit prohozením hran

- {% latex %}\Leftarrow{% endlatex %} pro spor nechť {% latex %}M'{% endlatex %} je párování v {% latex %}G{% endlatex %} t. ž {% latex %}|M'| \ge |M|{% endlatex %}
	- uvažme {% latex %}H = \left(V, M \cup M'\right){% endlatex %}; pak má každý vrchol stupeň {% latex %}0, 1{% endlatex %} nebo {% latex %}2{% endlatex %} {% latex %}\implies{% endlatex %} komponenty souvislosti jsou kružnice sudé délky a cesty (navíc jsou střídavé)
	- (👀) -- musí existovat komponenta, která má více hran z {% latex %}M'{% endlatex %} (je větší)
		- není to kružnice (musela by být lichá a měli bychom máme kolizi ve vrcholu)
		- je to volná (z definice, vzhledem k {% latex %}M{% endlatex %}) střídavá (jinak by měly stejný počet hran) cesta

---

{% math definition "květ" %} lichá „střídavá“ kružnice s vrcholem {% latex %}v_1{% endlatex %}, ke kterému přiléhají dva vrcholy {% latex %}\not\in M{% endlatex %}{% endmath %}
{% math definition "stonek" %} střídavá cesta z {% latex %}v_1{% endlatex %} (i nulové) délky končící volným vrcholem (dál od květu){% endmath %}
- {% latex %}v_1{% endlatex %} může (a nemusí) být volný vrchol -- stačí, aby byl volný vzhledem ke květu

{% math definition "kytka" %} květ + stonek{% endmath %}

{:.center}
![](/assets/kombinatorika-a-grafy-ii/kytka.svg)

{% math definition %} Nechť {% latex %}G = \left(V, E\right){% endlatex %} je neorientovaný graf a {% latex %}e = \left\{u, v\right\}{% endlatex %} jeho hrana. Zápis {% latex %}G . e{% endlatex %} označuje graf vzniklý z {% latex %}G{% endlatex %} kontrakcí („smrštěním“) hrany {% latex %}e{% endlatex %} do jednoho vrcholu:{% endmath %}

{:.center}
![](/assets/kombinatorika-a-grafy-ii/kontrakce.svg)

{% math lemma %}Nechť {% latex %}C{% endlatex %} je květ v grafu {% latex %}G{% endlatex %}. Potom párování {% latex %}M{% endlatex %} v {% latex %}G{% endlatex %} je maximální, právě když {% latex %}M \setminus E(C){% endlatex %} je maximální párování v grafu {% latex %}G . C{% endlatex %}, tj. s květem {% latex %}C{% endlatex %} zkontrahovaným do jediného vrcholu. Navíc pokud znám VSC pro {% latex %}M . C{% endlatex %}, tak v poly. čase najdu VSC pro {% latex %}M{% endlatex %} v {% latex %}G{% endlatex %}.{% endmath %}

TODO: důkaz z textu Matouška!

{% math algorithm "Edmondsův „zahradní/blossom“" %} vstupem je graf {% latex %}G{% endlatex %} a jeho libovolné párování {% latex %}M{% endlatex %}, třeba prázdné. Výstupem je párování {% latex %}M'{% endlatex %}, které je alespoň o {% latex %}1{% endlatex %} větší, než {% latex %}M{% endlatex %}, případně {% latex %}M{% endlatex %} pokud bylo maximální.{% endmath %}

- zkonstruujeme maximální možný **Edmondsův les** vzhledem k aktuálnímu {% latex %}M{% endlatex %} tím, že z volných vrcolů pustíme BFS a střídavě přidáváme vrcholy
	- hranám, které se v lese neobjeví, se říká kompost a nebudou pro nás důležité

{:.center}
![](/assets/kombinatorika-a-grafy-ii/les.svg)

- pokud existuje hrana mezi (potenciálně různými) sudými hladinami různých stromů, pak máme volnou střídavou cestu, kterou zalterujeme a jsme hotovi (párování je o $1$ větší)
- pokud existuje hrana mezi (potenciálně různými) sudými hladinami jednoho stromu, máme květ {% latex %}C{% endlatex %} -- ten zkontrahujeme a rekurzivně se zavoláme
	- vrátí-li {% latex %}M' = M{% endlatex %}, pak nic dalšího neděláme
	- vratí-li nějaké větší párování, tak z něho zkonstruujeme párování v {% latex %}G{% endlatex %}
- neexistuje-li hrana mezi sudými hladinami, pak {% latex %}M' = M{% endlatex %}

{% math lemma %}Edmondsův algoritmus spuštěný na {% latex %}G{% endlatex %} a {% latex %}M{% endlatex %} doběhne v čase {% latex %}\mathcal{O}(n \cdot (n + m)){% endlatex %} a najde párování {% latex %}M'{% endlatex %} alespoň o {% latex %}1{% endlatex %} hranu větší než {% latex %}M{% endlatex %}, případně oznámí, že {% latex %}M{% endlatex %} je největší {% latex %}\implies{% endlatex %} nejlepší párování lze nalézt v čase {% latex %}\mathcal{O}(n^2 (n + m)){% endlatex %}.{% endmath %}

### 2. přednáška

{% math definition "perfektní párování" %}Párování {% latex %}M{% endlatex %} je perfektní, pokud neexistuje v {% latex %}G{% endlatex %} žádný volný vrchol.{% endmath %}

#### Tutteova věta
{% math definition "Tutteova podmínka" %} {% latex %}\forall S \subseteq V: \mathrm{odd}(G - S) \le |S|{% endlatex %}
- kde {% latex %}\mathrm{odd}{% endlatex %} je počet lichých komponent grafu{% endmath %}.

{% math theorem "Tutteova věta" %} {% latex %}G{% endlatex %} má perfektní párování {% latex %}\iff{% endlatex %} platí Tutteova podmínka.{% endmath %}

{% math proof %}
{% latex %}\Rightarrow{% endlatex %} obměna: neplatí TP {% latex %}\implies{% endlatex %} není PP. Nehchť {% latex %}\exists S \subseteq V{% endlatex %} t. ž. {% latex %}\mathrm{odd(G - S)} > |S|{% endlatex %}. V perfektním párování se alespoň {% latex %}1{% endlatex %} vrchol z každé liché komponenty musí spárovat s nějakým z {% latex %}S{% endlatex %}, ale těch není dostatek.

{% latex %}\Leftarrow{% endlatex %} nechť {% latex %}G{% endlatex %} splňuje Tutteovu podmínku. {% latex %}|V|{% endlatex %} je sudá (nastavíme {% latex %}S{% endlatex %} prázdnou). Dokážeme, že {% latex %}G{% endlatex %} má PP indukcí podle počtu nehran.

- **základ:** {% latex %}G = K_{2n}{% endlatex %}, ten PP má
- **indukční podmínka:** {% latex %}G{% endlatex %} má nehranu a každý graf na {% latex %}V{% endlatex %}s počtem hran alespoň o 1 větší než {% latex %}|E|{% endlatex %} a platí TP, pak má perfektní párování

{% math definition %}{% latex %}S = \left\{v \in V\ |\ \mathrm{deg}(v) = n - 1\right\} = \left\{v \mid \text{$v$ je spojený se všemi vrcholy} \right\}{% endlatex %}{% endmath %}
- lehký případ: každá komponenta {% latex %}G - S{% endlatex %} je lichá klika
	- v rámci dané kliky vypáruji vše až na jeden vrchol, ten spáruji v rámci {% latex %}S{% endlatex %} ({% latex %}S{% endlatex %} vidí všechny) a zbytek v {% latex %}S{% endlatex %} spáruji spolu (sudé komponenty do parity nepřispívají, liché + {% latex %}1{% endlatex %} z {% latex %}S{% endlatex %} také ne a v {% latex %}S{% endlatex %} tedy zbyde sudý počet vrcholů)

{:.center}
![](/assets/kombinatorika-a-grafy-ii/1.svg)

- alespoň {% latex %}1{% endlatex %} komponenta {% latex %}K{% endlatex %} není klika, tedy {% latex %}\exists x, y{% endlatex %} nesousedi
	- ti mají společného souseda {% latex %}u{% endlatex %} (tvrzení, že každý souvislý neúplný graf má třešničku)
	- jelikož {% latex %}u{% endlatex %} není spojený s {% latex %}S{% endlatex %}, tak je spojený s nějakým vrcholem {% latex %}v{% endlatex %}


{:.center}
![](/assets/kombinatorika-a-grafy-ii/2.svg)

- (👀) -- přidáním hrany do grafu se neporuší TP ({% latex %}\forall S \subseteq V{% endlatex %} počet lichých komponent {% latex %}G - S{% endlatex %} buď klesne o {% latex %}2{% endlatex %} nebo zůstane stejný).

Indukujeme dvakrát: {% latex %}G_1 = G + e_1{% endlatex %} a {% latex %}G_2 = G + e_2{% endlatex %} díky předchozímu pozorování splňují TP a spolu s IP {% latex %}\implies \exists{% endlatex %} PP {% latex %}M_1, M_2{% endlatex %} v {% latex %}G_1, G_2{% endlatex %}
- jednoduchý případ: {% latex %}e_1 \not\in M_1 \implies M_1{% endlatex %} je PP pro {% latex %}G{% endlatex %}, analogicky pro {% latex %}M_2{% endlatex %}

Těžší případ: {% latex %}e_1 \in M_1, e_2 \in M_2, H = (V, M_1 \cup M_2){% endlatex %}
- {% latex %}H {% endlatex %} obsahuje **„dvoubarevné hrany“** {% latex %}e \in M_1 \cap M_2{% endlatex %} nebo **střídavé sudé cykly**
- {% latex %}H {% endlatex %} neobsahuje **izolované vrcholy** a **střídavé cesty,** protože {% latex %}M_1, M_2{% endlatex %} byly perfektní

{:.center}
![](/assets/kombinatorika-a-grafy-ii/3.svg)

- jednodušší případ: {% latex %}e_1{% endlatex %} leží v jiné komponentě {% latex %}H{% endlatex %} než {% latex %}e_2{% endlatex %} -- stačí přealternovat hrany tak, aby ani {% latex %}e_1{% endlatex %} ani {% latex %}e_2{% endlatex %} v {% latex %}H{% endlatex %} neležely.

{:.center}
![](/assets/kombinatorika-a-grafy-ii/4.svg)

- složitější případ: {% latex %}e_1{% endlatex %} a {% latex %}e_2{% endlatex %} leží ve stejné komponentě -- vybereme podle obrázku

{:.center}
![](/assets/kombinatorika-a-grafy-ii/5.svg)

{% endmath %}

{% math theorem "Petersen" %} každý {% latex %}3{% endlatex %}-regulární {% latex %}2{% endlatex %}-souvislý (vrcholově i hranově, pro 2-souvislost je to to samé; alternativně můžeme říct graf bez mostů a artikulací) graf má PP.{% endmath %}

{% math proof %}Nechť {% latex %}G = (V, E){% endlatex %} je {% latex %}3{% endlatex %}-regulární a {% latex %}2{% endlatex %}-souvislý. Chci ukázat, že {% latex %}G{% endlatex %} splňuje TP. Předpokládejme danou {% latex %}S \subseteq V{% endlatex %}.

1. každá komponenta {% latex %}G - S{% endlatex %} je v {% latex %}G{% endlatex %} spojena aspoň dvěma hranami s {% latex %}S{% endlatex %}
	- je {% latex %}2{% endlatex %}-souvislý, nemáme mosty

2. každá lichá komponenta {% latex %}G - S{% endlatex %} je s {% latex %}S{% endlatex %} spojena lichým počtem hran
	- nechť {% latex %}L{% endlatex %} je lichá komponenta {% latex %}G - S{% endlatex %}; pak:
{% latex display %}\sum_{x \in V(L)}^{\mathrm{deg}_G(x)} \overset{3-\text{reg.}}{=} \underbrace{3|V(L)|}_{\text{liché číslo}} = \underbrace{2 (\text{\# hran vedoucích uvnitř $L$})}_{\text{sudé číslo}} + \underbrace{1 (\text{\# hran vedoucích uvnitř $L$})}_{\text{musí být liché}}{% endlatex %}

- kombinace (1) a (2) říká, že každá lichá komponenta {% latex %}G - S{% endlatex %} je s {% latex %}S{% endlatex %} spojena {% latex %}\ge 3{% endlatex %} hranami; formálně:
	- {% latex %}p = \text{\# hran mezi $S$ a lichou komponentou $G - S$}{% endlatex %}
		- {% latex %}p \ge 3 \cdot \mathrm{odd(G - S)}{% endlatex %}
		- {% latex %}p \le 3 \cdot |S|{% endlatex %} (každý vrchol {% latex %}S{% endlatex %} vysílá ven {% latex %}\le 3{% endlatex %} hrany (z 3-regularity))

{:.center}
![](/assets/kombinatorika-a-grafy-ii/6.svg)

{% latex %}3|S| \ge 3 \cdot \mathrm{odd}(G - S){% endlatex %}, tedy TP platí a graf má perfektní párování.

{% endmath %}

### 3. přednáška


#### Tutte v2.0

{% math lemma "o kontrahovatelné hraně" %} Nechť {% latex %}G{% endlatex %} je vrcholově {% latex %}3{% endlatex %}-souvislý různý od {% latex %}K_4{% endlatex %} ({% latex %}|V| \ge 5{% endlatex %}). Potom {% latex %}G{% endlatex %} obsahuje hranu t. ž. {% latex %}G \setminus e{% endlatex %} je 3-souvislý.{% endmath %}

{% math proof %}Sporem -- nechť {% latex %}G{% endlatex %} je 3-souvislý ale neexistuje žádná hrana, která jde zkontrahovat. Tedy {% latex %}\forall e \in E: G \setminus e{% endlatex %} není {% latex %}3{% endlatex %}-souvislý.

{% math lemma "pomocné" %} {% latex %}\forall e = \left\{x, y\right\} \exists z_e \in V \setminus \left\{x, y\right\}{% endlatex %} t. ž. {% latex %}\left\{x, y, z_e\right\}{% endlatex %} tvoří vrcholový řez v G, navíc každý z {% latex %}\left\{x, y, z_e\right\}{% endlatex %} má alespoň jednoho souseda v každé komponentě {% latex %}G \setminus \left\{x, y, z_e\right\}{% endlatex %}.{% endmath %}
- přesně popisuje situaci, že kontrakce libovolné hrany nám dá řez velikosti {% latex %}2{% endlatex %}
- ve skutečnosti **neplatí** (ale dovětek ano) a dokazujeme ho pouze v rámci sporu!
- (👀 které platí) {% latex %}S{% endlatex %} minimální vrcholový řez {% latex %}G{% endlatex %}, pak každý vrchol {% latex %}S{% endlatex %} má souseda v každé komponentě {% latex %}G \setminus S{% endlatex %} -- když to pro nějaký {% latex %}v{% endlatex %} neplatí, tak {% latex %}S \setminus v{% endlatex %} je pořád řez

{% xopp 1 %}

{% math proof %}
Vím, že {% latex %}G \setminus e{% endlatex %} není {% latex %}3{% endlatex %}-souvislý, tedy má vrcholový řez velikosti {% latex %}2{% endlatex %}. Nechť {% latex %}v_e{% endlatex %} je vrchol vzniklý kontrakcí {% latex %}e = \left\{x, y\right\}{% endlatex %}. Řez velikosti {% latex %}2{% endlatex %} obsahuje {% latex %}v_e{% endlatex %}, jinak by to byl řez už pro {% latex %}G{% endlatex %} (obsahoval by vrcholy z původního grafu, které nekontrahujeme).

Označme řez {% latex %}v_e, z_e{% endlatex %}. Po rozkontrahování vidíme, že {% latex %}\forall \left\{x, y, z_e\right\}{% endlatex %} musí mít souseda v každé komponentě (jinak spor s 3-souvislostí). Tedy {% latex %}z_e{% endlatex %} je hledaný vrchol.
{% endmath %}

{% xopp 2 %}

---

Pro důkaz původního lemmatu si zvolím {% latex %}e = \left\{x, y \right\} \in E{% endlatex %} a {% latex %}z_e{% endlatex %} z pomocného tvrzení tak, aby nejmenší komponenta {% latex %}G - z, y, z_e{% endlatex %} byla co nejmenší (co do počtu vrcholů).

{% xopp 3 %}

Protože {% latex %}z_e{% endlatex %} má souseda ve všech komponentách, má nějakého souseda {% latex %}u \in C, f = \left\{z_e, u\right\}{% endlatex %} (kde {% latex %}C{% endlatex %} je naše nejmenší komponenta). Pomocné tvrzení pro {% latex %}f{% endlatex %} dá nějaký {% latex %}z_f \in V{% endlatex %} t. ž. {% latex %}\left\{z_e, z_f, u\right\}{% endlatex %} je vrcholový řez {% latex %}G{% endlatex %}. Chceme dokázat, že {% latex %}G - z_e, z_f, u{% endlatex %} má menší komponentu než {% latex %}C{% endlatex %}.

Nechť {% latex %}D{% endlatex %} je komponenta {% latex %}G - z_e, z_f, u{% endlatex %} neobsahující {% latex %}x, y{% endlatex %}. Existuje, protože {% latex %}x, y{% endlatex %} jsou spojené a graf se rozpadne alespoň na {% latex %}2{% endlatex %} komponenty). Tvrdím, že {% latex %}D \subseteq C \setminus \left\{u\right\}{% endlatex %}, protože {% latex %}D{% endlatex %} nemůže obsahovat {% latex %}z_e, z_f, u{% endlatex %} (vrcholy řezu), {% latex %}x, y{% endlatex %} (z definice {% latex %}D{% endlatex %}), ale {% latex %}u{% endlatex %} má souseda v {% latex %}C{% endlatex %} (podle pomocného tvrzení), takže v {% latex %}D{% endlatex %} ještě něco zbyde. Tedy {% latex %}|D| < |C|{% endlatex %}, což je spor s minimalitou.
{% endmath %}

- netvrdím, že {% latex %}D{% endlatex %} je nejmenší!

{% math theorem "Tutteova charakterizace 3-souvislých grafů" %} Graf {% latex %}G{% endlatex %} je 3-souvislý {% latex %}\iff{% endlatex %} existuje posloupnost {% latex %}K_4 \cong G_0 \cong G_1 \cong \ldots \cong G{% endlatex %} t. ž. {% latex %}\forall i \in [n], G_{i - 1}{% endlatex %} vznikne z {% latex %}G_i{% endlatex %} kontrakcí hrany, navíc {% latex %}G_i{% endlatex %} má všechny vrcholy stupně {% latex %}\ge 3{% endlatex %}.{% endmath %}

{% math proof %} {% latex %}\Rightarrow{% endlatex %} Induktivní aplikace lemmatu o kontrahovatelné hraně.

{% latex %}\Leftarrow{% endlatex %} Mějme {% latex %}G_0, \ldots, G_n{% endlatex %} dle předpokladu. Chceme, že {% latex %}G_n \cong G{% endlatex %} je 3-souvislý. Indukcí:
- {% latex %}K_4{% endlatex %} je 3-souvislý
- {% latex %}G_{i - 1}{% endlatex %} je 3-souvislý {% latex %}\implies G_i{% endlatex %} je 3-souvislý

Pro spor nechť {% latex %}G_i{% endlatex %} má vrcholový řez velikosti 2, označme ho {% latex %}R{% endlatex %}. Pak každá komponenta {% latex %}G_i - R{% endlatex %} má alespoň 2 vrcholy {% latex %}x, y{% endlatex %} (osamocený vrchol {% latex %}v{% endlatex %} mohl sousedit jen s řezem, ale ten je velikosti 2, což je spor se stupněm vrcholů {% latex %}\ge 3{% endlatex %} pro {% latex %}v{% endlatex %}).

Obměnou ani {% latex %}G_{i - 1}{% endlatex %} nebyl 3-souvislý, rozborem toho, kde vznikla hrana:
- {% latex %}e = \left\{x, y\right\} \implies G_{i - 1}{% endlatex %} má řez velikosti 1.
- {% latex %}e{% endlatex %} celá obsažená v komponentě {% latex %}\implies \left\{x, y\right\}{% endlatex %} je stále řez v {% latex %}G_{i - 1}{% endlatex %}
- {% latex %}e = \left\{z, y\right\}{% endlatex %} pro {% latex %}z{% endlatex %} z nějaké komponenty {% latex %}\implies \left\{zy, x\right\}{% endlatex %} je řez v {% latex %}G_{i - 1}{% endlatex %}
	- využíváme předchozí pozorování, že každá komponenta má alespoň {% latex %}2{% endlatex %} vrcholy -- kdyby ne, tak {% latex %}\left\{zy, x\right\}{% endlatex %} nemusí nic odříznout, pokud tam byla jednovrcholová komponenta
{% endmath %}

#### Minory

{% math definition "minor" %} Nechť {% latex %}H, G{% endlatex %} jsou grafy. Pak {% latex %}H{% endlatex %} je minor {% latex %}G{% endlatex %} (nebo že {% latex %}G {% endlatex %} obsahuje {% latex %}H{% endlatex %} jako minor), značíme {% latex %}H \preceq G{% endlatex %}, pokud {% latex %}H{% endlatex %} lze získat z {% latex %}G{% endlatex %} posloupností mazání vrcholů, mazání hran nebo kontrakcí hran.{% endmath %}

- (👀) {% latex %}\preceq{% endlatex %} je transitivní (prostě spojím posloupnosti operací)
- (👀) {% latex %}H{% endlatex %} podgraf {% latex %}G \implies H{% endlatex %} minor {% latex %}G{% endlatex %}
	- podgraf vzniká přesně mazáním vrcholů a mazáním hran
- (👀, spíš fakt) {% latex %}G{% endlatex %} rovinný {% latex %}\implies{% endlatex %} jeho minory jsou také rovinné
	- pro podgraf očividné, je jen potřeba si rozmyslet kontrakci (že nic topologicky nerozbije)

{% math theorem "Kuratowského" %} {% latex %}G{% endlatex %} rovinný {% latex %}\iff{% endlatex %} neobsahuje dělení {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %}{% endmath %}

{% math theorem "Kuratowski 1930, Warner 1937" %} Následující jsou ekvivalentní:{% endmath %}
1. {% latex %}G{% endlatex %} je rovinný
2. {% latex %}G{% endlatex %} neobsahuje dělení {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} jako podgraf
3. {% latex %}G{% endlatex %} neobsahuje dělení {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} jako minor.

{% math proof %} {% latex %}\\{% endlatex %}
- {% latex %}1 \implies 2{% endlatex %}: z prváku, protože {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} nejsou rovinné
- {% latex %}3 \implies 2{% endlatex %}: obměna: „obsahuje dělení jako podgraf“ {% latex %}\implies{% endlatex %} „obsahuje dělení jako minor“
- {% latex %}1 \implies 3{% endlatex %}: je-li rovinný, tak i minor bude rovinný (fakt výše)
- {% latex %}2 \implies 3{% endlatex %}: TODO: bylo na cvičení
- {% latex %}3 \implies 1{% endlatex %}: indukcí podle {% latex %}|V(G)|{% endlatex %}
	- pro {% latex %}|V(G)| \le 4{% endlatex %} vše funguje
	- předpokládám {% latex %}G{% endlatex %} má alespoň 5 vrcholů a neobsahuje {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} jako minor. Rozeberu případy podle {% latex %}k_v(G){% endlatex %} (vrcholová souvislost {% latex %}G{% endlatex %})
		- {% latex %}k_v(G) = 0\implies{% endlatex %} nesouvislý graf, použijeme indukci
		- {% latex %}k_v(G) = 1\implies{% endlatex %} artikulačním vrcholem {% latex %}x{% endlatex %} rozpojíme, podle IP nakreslíme
			- {% latex %}x{% endlatex %} musí být na vnější stěně, což umíme přes trik s projekcí z koule na rovinu
		- {% latex %}k_v(G) = 2\implies{% endlatex %}, rozložení podél dvou vrcholů tvořících řez. TODO: víc rozepsat?
{% endmath %}

### 4. přednáška
- {% latex %}k_v(G) \ge 3\implies{% endlatex %} použijeme lemma o kontrahovatelné hraně: {% latex %}\exists e = \left\{x, y\right\}{% endlatex %} t. ž. {% latex %}G \setminus e = G'{% endlatex %} je {% latex %}3{% endlatex %}-souvislý
	- (👀) {% latex %}G'{% endlatex %} nemůže obsahovat {% latex %}K_5{% endlatex %} ani {% latex %}K_{3, 3}{% endlatex %} jako minor (spor s předpokladem)
	- {% latex %}\mathcal{G}' \ldots{% endlatex %} rovinné nakreslení {% latex %}G'{% endlatex %} (z IP existuje)
	- {% latex %}G'' = G' - v_e{% endlatex %} (vrchol vzniklý kontrakcí {% latex %}e{% endlatex %}) {% latex %} = G - \left\{x, y\right\}{% endlatex %}
		- (👀) {% latex %}G''{% endlatex %} bude {% latex %}2{% endlatex %}-souvislý (protože {% latex %}G'{% endlatex %} je {% latex %}3{% endlatex %}-souvislý a {% latex %}G''{% endlatex %} vznikne odebráním vrcholu)
		- (👀) taky rovinný (odebráním mi žádný minor nevznikne)
		- {% latex %}\mathcal{G}''{% endlatex %} nakreslení {% latex %}G''{% endlatex %} vzniklé z {% latex %}\mathcal{G}'{% endlatex %} odebráním {% latex %}v_e{% endlatex %}

Označme {% latex %}C{% endlatex %} kružnici ohraničující stěnu {% latex %}\mathcal{G}''{% endlatex %}, v níž ležel (v {% latex %}\mathcal{G}'{% endlatex %} vrchol {% latex %}v_e{% endlatex %}) -- musí to být kružnice, protože v rovinném nakreslení každého {% latex %}2{% endlatex %}-souvislého grafu je každá stěna kružnice.

{% xopp tmp %}

- {% latex %}N(x){% endlatex %} -- sousedi {% latex %}x{% endlatex %}
- {% latex %}N(y){% endlatex %} -- sousedi {% latex %}y{% endlatex %}
- {% latex %}N(x) \cup N(y) \setminus \left\{x, y\right\} \subseteq C{% endlatex %} (každý soused {% latex %}x{% endlatex %} kromě {% latex %}y{% endlatex %} je i sousedem {% latex %}v_e{% endlatex %} v {% latex %}G'{% endlatex %}, stejně pro {% latex %}y{% endlatex %}

3 případy:
1. {% latex %}|N(x) \cap N(y)| \ge 3{% endlatex %} -- nenastane, protože kontrakcí dostanu {% latex %}K_5{% endlatex %}, což je spor s předpokladem

{% xopp p1 %}

2. {% latex %}\exists a_1, a_2 \in N(x) \cap C, \exists b_1, b_2 \in N(y) \cap C{% endlatex %}, na {% latex %}C{% endlatex %} jsou v pořadí {% latex %}a_1, b_1, a_2, b_2{% endlatex %} -- nenastane, protože kontrakcí dostanu {% latex %}K_{3, 3}{% endlatex %}

{% xopp p2 %}

3. zbytek -- nenasatane ani (1), ani (2)
	- označme {% latex %}a_1, \ldots, a_k \in N(x) \cap C{% endlatex %} v pořadí, jak se objevují na {% latex %}C{% endlatex %}
	- můžu nakreslit všechny hrany {% latex %}xa_1, \ldots xa_k{% endlatex %}
	- {% latex %}a_1, \ldots, a_k{% endlatex %} rozdělují {% latex %}C{% endlatex %} na vnitřně disjunktní cesty {% latex %}P_1, \ldots P_k{% endlatex %} ({% latex %}k \ge 2{% endlatex %} protože {% latex %}G{% endlatex %} je {% latex %}3{% endlatex %}-souvislý... {% latex %}x{% endlatex %} sousedí s {% latex %}y{% endlatex %} a s {% latex %}\ge 2{% endlatex %} dalšími vrcholy)
		- chceme: {% latex %}N(y) \setminus \left\{x\right\}{% endlatex %} patří do jediné {% latex %}P_i{% endlatex %} (pro nějaké {% latex %}i{% endlatex %}), jinak by nastaly předchozí případy
	- {% latex %}y{% endlatex %} nakreslím do té správně stěny, spojím s {% latex %}b_i{% endlatex %} a mám hotovo

{% xopp p3 %}
{% xopp p4 %}

#### Kreslení grafů na plochy
{% math definition %}Nechť {% latex %}X \subseteq \mathbb{R}^n, Y \subseteq \mathbb{R}^m{% endlatex %}. Potom homeomorfismus z {% latex %}X{% endlatex %} na {% latex %}Y{% endlatex %} je funkce {% latex %}f: X \mapsto Y{% endlatex %}, která je spojitá, bijekce a {% latex %}f^{-1}{% endlatex %} je spojitá. {% latex %}X, Y{% endlatex %} jsou homeomorfní ({% latex %}X \cong Y{% endlatex %}) pokud mezi nimi existuje homeomorfismus.{% endmath %}
- něco jako isomorfismus u grafů ({% latex %}X \cong Y{% endlatex %} znamená, že se chovají stejně)

{% math definition "plocha" %} kompaktní (uzavřená, omezená), souvislá (např. oblouková -- každé dva body můžu propojit obloukem), {% latex %}2{% endlatex %}-rozměrná varieta bez hranice (dostatečně malé okolí každého bodu je homeomorfní otevřenému okolí v {% latex %}\mathbb{R}^2{% endlatex %}).{% endmath %}
- např. sféra v {% latex %}\mathbb{R}^3{% endlatex %} nebo torus v {% latex %}\mathbb{R}^3{% endlatex %}
- není to např.
	- {% latex %}\mathbb{R}^2{% endlatex %}, jelikož není kompaktní (omezená)
	- čtverec s hranici, jelikož pro každý krajní body není homeomorfní {% latex %}\mathbb{R}^2{% endlatex %}

Operace s plochami, přes které umíme všechny zkonstruovat:


{:.rightFloatBox}
<div markdown="1">
{% xopp o1 %}
</div>
- přidání ucha (od hrnku)
	- vyříznu dva kruhy
	- vezmu plášť pálce bez dna a vrchu
	- ohnu a přílepím jej na díry po kruzích
	- (👀) -- teleport, do kterého když vejdeme, tak na druhé straně vyjdeme opačně („otočeně“)

{:.rightFloatBox}
<div markdown="1">
{% xopp o2 %}
</div>
- přidání křížítka (cross-cupu):
	- (👀) -- teleport, do kterého když vejdeme, tak nás to přesune naproti

Pro {% latex %}g \in \left\{0, 1, \ldots\right\}{% endlatex %} nechť {% latex %}\sum_g{% endlatex %} značí plochu zvniklou ze féry přidáním {% latex %}g{% endlatex %} uší, tak říkáme, že {% latex %}\sum g{% endlatex %} je **orientovatelná plocha** rodu {% latex %}g{% endlatex %}.

Pro {% latex %}g \in \left\{1, 2, \ldots\right\}{% endlatex %} nechť {% latex %}\prod_g{% endlatex %} značí plochu zvniklou ze féry přidáním {% latex %}g{% endlatex %} křížítek, tak říkáme, že {% latex %}\prod g{% endlatex %} je **neorientovatelná plocha** rodu {% latex %}g{% endlatex %}.

{% math fact %}Každá plocha je homeomorfní právě jedné z posloupností {% latex %}\sum_0, \prod_1, \sum_1, \prod_2,\ldots{% endlatex %}{% endmath %}
- máme tu skryté tvrzení, že žádné dvě z této posloupností nejsou homeomorfní.

{% math fact %}Přidám-li ke sféře {% latex %}k \ge 0{% endlatex %} uší a {% latex %}l \ge 1{% endlatex %} křížítek, vznikne neorientovatelná plocha homeomorfní {% latex %}\prod_{2k + l}{% endlatex %} ({% latex %}\approx{% endlatex %} „přidání dvou křížítek je jako přidání ucha,“ **pokud** už tam bylo {% latex %}\ge 1{% endlatex %} křížítko){% endmath %}

- {% latex %}\sum_0 \ldots{% endlatex %} sféra
- {% latex %}\prod_1 \ldots{% endlatex %} projektivní rovina
- {% latex %}\sum_1 \ldots{% endlatex %} torus
- {% latex %}\prod_2 \ldots{% endlatex %} kleinova láhev

### 5. přednáška
{% math definition "nakreslení grafu" %} {% latex %}G = (V, E){% endlatex %} na pllochu {% latex %}\Gamma{% endlatex %} je zobrazení {% latex %}\varphi{% endlatex %} t. ž.:
- každému vrcholu {% latex %}v \in V{% endlatex %} přiřadí bod {% latex %}\varphi(v) \in \Gamma{% endlatex %}
- každé hraně {% latex %}e \in E{% endlatex %} přiřadí prostou (neprotínající se) křivku {% latex %}\varphi(e) \in \Gamma{% endlatex %} spojující konce {% latex %}\varphi(x), \varphi(y){% endlatex %}
- {% latex %}x, y \in V: x \neq y \implies \varphi(x) \neq \varphi(y){% endlatex %}
- {% latex %}e, f \in E: e \neq f \implies \varphi(e) \cap \varphi(f) = \left\{\varphi(x) \mid x \in e \cap f\right\}{% endlatex %}
- {% latex %}e \in E, x \in V: x \in e \implies \varphi(x) \not\in \varphi(e){% endlatex %}
{% endmath %}

{% math definition "stěna nakreslení" %} souvislá komponenta {% latex %}\Gamma \setminus \left(\left(\bigcup_{e \in E}^{\varphi(e)}\right) \cup \left(\bigcup_{x \in V}^{\varphi(x)}\right)\right){% endlatex %}{% endmath %}
- prostě když odeberu všechna nakreslení hran a vrcholů

{% math definition "buňkové nakreslení" %} každá stěna je homeomorfní otevřenému kruhu v {% latex %}\mathbb{R}^2{% endlatex %}.{% endmath %}

{% xopp torus %}

{% math reminder %}{% latex %}G = (V, E){% endlatex %} souvislý {% latex %}\Rightarrow{% endlatex %} v každém rovinném nakreslení platí {% latex %}|V| - |E| + S = 2{% endlatex %} {% endmath %}
- využíváme faktu, že rovinné nakreslení {% latex %}G{% endlatex %} je buňkové {% latex %}\iff G{% endlatex %} je souvislé
- {% latex %}2{% endlatex %} je speciální pro rovinu

{% math definition "Eulerova charakteristika plochy" %} charakteristika plochy {% latex %}\Gamma{% endlatex %} je

{% latex display %}
\begin{aligned}
\Chi(\Gamma) &= \begin{cases} 2 - g & \Gamma \cong \prod (g \ge 1) \\ 2 - 2g & \Gamma \cong \sum (g \ge 0) \end{cases} \\
\            &= 2 - \text{\# křížítek} - 2 \cdot \text{\# uší}
\end{aligned}
{% endlatex %}
{% endmath %}

{% math theorem "zobecněná Eulerova formule" %}Nechť máme nakreslení grafu {% latex %}G = (V, E){% endlatex %} na ploše {% latex %}\Gamma{% endlatex %}, které má {% latex %}S{% endlatex %} stěn. Pak {% latex %}|V| - |E| + |S| \ge \Chi(\Gamma).{% endlatex %}. Pokud je buňkové, tak dokonce {% latex %}|V| - |E| + S = \Chi(\Gamma){% endlatex %}.{% endmath %} 

{% math proof "rovnosti" %}idea je indukce podle rodu {% latex %}\Gamma{% endlatex %}
- {% latex %}\Gamma \cong \sum_0{% endlatex %} platí

{:.rightFloatBox}
<div markdown="1">
{% xopp s1 %}
</div>
Mějme buňkové nakreslení {% latex %}G = (V, E){% endlatex %} na {% latex %}\Gamma{% endlatex %}
- {% latex %}v(G), e(G), s(G){% endlatex %} značíme počet vrcholů, hran a stěn

Nechť {% latex %}K{% endlatex %} je křížítko na {% latex %}\Gamma{% endlatex %}, {% latex %}x_1, \ldots, x_k{% endlatex %} jsou body {% latex %}K{% endlatex %} (ne nutně vrcholy grafu), kde hrany {% latex %}G{% endlatex %} kříží {% latex %}K{% endlatex %}
- (👀) {% latex %}k \ge 1{% endlatex %}, jinak by stěna obsahující {% latex %}K{% endlatex %} nebyla buňka

{:.rightFloatBox}
<div markdown="1">
{% xopp s2 %}
</div>
Vytvoříme {% latex %}G'{% endlatex %} přidáním dvou dělících vrcholů na každou hranu křížící {% latex %}K{% endlatex %} těsně vedle {% latex %}x_1, \ldots, x_k{% endlatex %} („před a za křížítkem“). Děláme to proto, že jedna hrana by mohla procházet křížítkem na více místech a bylo by to pak dost rozbitý
- {% latex %}v(G') = v(G) + 2k{% endlatex %}
- {% latex %}e(G') = e(G) + 2k{% endlatex %}
- {% latex %}s(G') = s(G){% endlatex %}
- {% latex %}L(G') = L(G){% endlatex %}

{:.rightFloatBox}
<div markdown="1">
{% xopp s3 %}
</div>
Vytvoříme {% latex %}G''{% endlatex %} přidaním cest délky {% latex %}2{% endlatex %} k sousedním vrcholům z předchozího kroku. Vznikne tím kružnice {% latex %}C{% endlatex %} obcházející {% latex %}K{% endlatex %}.
- {% latex %}v(G'') = v(G') + 2k{% endlatex %}
- {% latex %}e(G'') = e(G') + 4k{% endlatex %}
- {% latex %}s(G'') = s(G') + 2k{% endlatex %} (každou z {% latex %}k{% endlatex %} stěn dělím na {% latex %}3{% endlatex %} kusy)
- {% latex %}L(G'') = L(G'){% endlatex %}

{:.rightFloatBox}
<div markdown="1">
{% xopp s4 %}
</div>
Vytvoříme {% latex %}G'''{% endlatex %} odebráním všeho uvnitř {% latex %}C{% endlatex %}.
- {% latex %}v(G''') = v(G''){% endlatex %}
- {% latex %}e(G''') = e(G'') - k{% endlatex %} ({% latex %}k{% endlatex %} křížících-se hran uvnitř {% latex %}C{% endlatex %})
- {% latex %}s(G''') = s(G'') - k + 1{% endlatex %} („spojím“ {% latex %}k{% endlatex %} stěn do jedné)
- {% latex %}L(G''') = L(G'') + 1{% endlatex %}

{% latex display %}L(G''') = \Chi(\sum_{g - 1}) = \Chi(\Gamma) + 1 \qquad \mid \text{dle IP}{% endlatex %}
{% latex display %}\Chi(\Gamma) = L(G''') - 1 \qquad \mid \text{z výpočtu}{% endlatex %}

Tedy {% latex %}\Chi(\Gamma) = L(G''') - 1 = L(G'') = L(G') = L(G){% endlatex %}
{% endmath %}

{% math consequence %}Každý graf {% latex %}G{% endlatex %} nakreslitelný na plochu {% latex %}\Gamma{% endlatex %} splní {% latex %}|E| \le 3|V| - 3\Chi(\Gamma){% endlatex %}, pokud {% latex %}|V| \ge 4{% endlatex %}
- každý takový graf má průměrný stupeň {% latex %}\frac{2|E|}{|V|} \le 6 - \frac{6\Chi(\Gamma)}{|V|}{% endlatex %}
	- na žádnou zafixovanou plochu nelze nakreslit libovolně velký {% latex %}7{% endlatex %}-regulární graf
	- pro libovolně velký úplňák dokážeme vytvořit plochu, na kterou ho nakreslíme
{% endmath %}

{% math lemma %}Nechť {% latex %}\Gamma{% endlatex %} je plocha, {% latex %}\Gamma \neq \sum_0{% endlatex %}, nechť {% latex %}G{% endlatex %} je graf nakreslený na {% latex %}\Gamma{% endlatex %}, potom {% latex %}G{% endlatex %} obsahuje vrchol stupně {% latex %}\le \left\lfloor \frac{5 + \sqrt{49 - 24\Chi(\Gamma)}}{2} \right\rfloor{% endlatex %}{% endmath %}

{% math proof %}Mějme {% latex %}G{% endlatex %} podle předpokladu. Opět značíme {% latex %}v(G), e(G){% endlatex %} jako počet vrcholů a hran. ROzlišíme {% latex %}3{% endlatex %} případy:
- {% latex %}\Chi(\Gamma) = 1{% endlatex %} (t.j. {% latex %}\Gamma \cong \prod_1{% endlatex %}), dosazením do předchozího důsledku dostáváme průměrný stupeň {% latex %}< 6{% endlatex %}, tedy existuje vrchol stupně {% latex %}\le 5{% endlatex %}, což jsme chtěli
- {% latex %}\Chi(\Gamma) = 0{% endlatex %} (t.j. {% latex %}\Gamma \cong \prod_2{% endlatex %} nebo {% latex %}\Gamma \cong \sum_1{% endlatex %}), průměrný stupeň {% latex %}\le 6 \implies \exists{% endlatex %} vrchol stupně {% latex %}\le 6{% endlatex %}
- {% latex %}\Chi(\Gamma) < 0 \ldots \delta(G) = {% endlatex %} min. stupeň {% latex %}G{% endlatex %}; víme:
	- {% latex %}\delta(G) \le 6 - \frac{6 \Chi(\Gamma)}{v(G)}{% endlatex %}
	- {% latex %}\delta(G) \le v(G) - 1{% endlatex %} (žádný vrchol nemá víc než {% latex %}v(G) - 1{% endlatex %} sousedů)
	- chceme zjistit max. hodnotu {% latex %}\delta{% endlatex %}, což je řešení dvou rovnic výše; dosazením a vyřešením kvadratické rovnice vyjde přesně výraz, který dokazujeme
{% endmath %}

{% math consequence "Heawoodova formule, 1890" %} Pokud {% latex %}\Gamma \not\cong \sum_0{% endlatex %}, tak každý graf nakreslitelny na {% latex %}\Gamma{% endlatex %} je nejvýš {% latex %}H(\Gamma) = 1 + \left\lfloor \frac{5 + \sqrt{49 - 24 \Chi(\Gamma)}}{2} \right\rfloor = \left\lfloor \frac{7 + \sqrt{49 - 24 \Chi(\Gamma)}}{2} \right\rfloor{% endlatex %}-obarvitelný{% endmath %}
- vyplývá z předchozího důsledku -- pokud má graf stupeň nejvýše {% latex %}\delta{% endlatex %}, tak je {% latex %}\delta+1{% endlatex %}-obarvitelný
- platí i pro stéru: věta o {% latex %}4{% endlatex %}-barvách
- tento odhad je těsný pro všechny plochy kromě {% latex %}\prod_2{% endlatex %}
- na každou plochu {% latex %}\Gamma \not\cong \prod_2{% endlatex %} lze kreslit kliku velikosti {% latex %}H(\Gamma){% endlatex %}
	- (každý graf nakreslitelný na {% latex %}\prod_2{% endlatex %} je dokonce {% latex %}6{% endlatex %}-obarvitelný)

### 6. přednáška

#### Vrcholové barvení
- {% latex %}\Chi(G) = \text{barevnost } G = {% endlatex %} nejmenší počet barev, kterými lze (dobře) obarvit vrcholy {% latex %}G{% endlatex %}
- {% latex %}\Delta(G) = \text{max. stupeň } G = {% endlatex %}, {% latex %}\delta(G) = \text{min. stupeň } G{% endlatex %}

{% math definition %}{% latex %}G{% endlatex %} je {% latex %}d{% endlatex %}-degenerovaný {% latex %}\equiv{% endlatex %} každý podgraf {% latex %}H{% endlatex %} grafu {% latex %}G{% endlatex %} má {% latex %}\delta(H) \le d{% endlatex %}{% endmath %}
- {% latex %}\iff \exists{% endlatex %} pořadí vrcholů (eliminační) {% latex %}v_1, \ldots v_n{% endlatex %} t. ž. {% latex %}\forall i: G - \left\{v_1, \ldots, v_i\right\}: \delta(G_i) \le d{% endlatex %} a {% latex %}v_{i - 1}{% endlatex %} má {% latex %}\le d{% endlatex %} sousedů v {% latex %}G_i{% endlatex %}
	- {% math observation %}{% latex %}G{% endlatex %} je {% latex %}d{% endlatex %}-degenerovnaý {% latex %}\implies \Chi(G) \le d + 1{% endlatex %}{% endmath %} (barvím indukcí v pořadí {% latex %}v_n, v_{n - 1}, \ldots{% endlatex %}

- z minule: pokud {% latex %}G{% endlatex %} je nakreslitelný na {% latex %}\Gamma \implies G{% endlatex %} má vrchol stupně nejvýše {% latex %}H(\Gamma) - 1{% endlatex %} a {% latex %}G - v{% endlatex %} je stále nakreslitelný na {% latex %}\Gamma \implies G{% endlatex %} je {% latex %}\left(H(\Gamma) - 1\right){% endlatex %}-degenerovaný {% latex %}\implies{% endlatex %} je {% latex %}H(\Gamma){% endlatex %} obarvitelný

{% math observation %}{% latex %}G{% endlatex %} je {% latex %}\Delta(G){% endlatex %}-degenerovaný (triviálně) {% latex %}\implies \Chi(G) \le \Delta(G) + 1{% endlatex %} (z pozorování výše){% endmath %}

- s rovností platí např. pro úplné grafy a liché cykly

{% math lemma %}{% latex %}G{% endlatex %} souvislý graf a {% latex %}\delta(G) < \Delta(G){% endlatex %}, pak {% latex %}\Chi(G) \le \Delta(G){% endlatex %}{% endmath %}
- když nás zajímá předchozí otázka, tak se stačí zaměřit na nějaký regulární graf

{:.rightFloatBox}
<div markdown="1">
{% xopp a1 %}
</div>
{% math proof %}Tvrdím, že {% latex %}G{% endlatex %} je ({% latex %}\Delta(G) - 1{% endlatex %})-degenerovaný. Volme {% latex %}H{% endlatex %} neprázdný podgraf {% latex %}G{% endlatex %} a dokazujeme, že v {% latex %}H{% endlatex %} existuje {% latex %}v{% endlatex %} stupně {% latex %}\le \Delta(G) - 1{% endlatex %} 
- pokud {% latex %}H{% endlatex %} obsahuje všechny vrcholy {% latex %}\implies{% endlatex %} platí z předpokladu.
- jinak {% latex %}\exists e = \left\{x, y\right\} \in G{% endlatex %} t. ž. {% latex %}x \in H{% endlatex %} a {% latex %}y \not\in H{% endlatex %}
	- {% latex %}\mathrm{deg}_H(x) \le \mathrm{deg}_G(x) - 1 \le \Delta(G) - 1{% endlatex %}
{% endmath %}

{% math theorem "Brooks, 1941" %}Nechť {% latex %}G{% endlatex %} je souvislý graf který není úplný a není lichá kružnice. Pak je {% latex %}G \le \Delta(G){% endlatex %}-obarvitelný.{% endmath %}

{% math proof %}nechť {% latex %}\Chi = \Chi(G), \Delta = \Delta(G){% endlatex %} a navíc předpokládám, že {% latex %}G{% endlatex %} je {% latex %}\Delta{% endlatex %}-regulární (jinak viz. předchozí lemma.

- {% latex %}\Delta = 1{% endlatex %}
	- {% latex %}K_2{% endlatex %}: zakázané
- {% latex %}\Delta = 2{% endlatex %}
	- {% latex %}C_{2k}{% endlatex %}: {% latex %}\Chi = 2{% endlatex %}
	- {% latex %}C_{2k + 1}{% endlatex %}: zakázané
- {% latex %}\Delta \ge 3{% endlatex %}; označme {% latex %}k_V(G) = {% endlatex %} vrcholová souvislost {% latex %}G{% endlatex %}
	- {% latex %}k_V(G) = 1{% endlatex %} -- máme artikulaci; vrchol artikulace {% latex %}v{% endlatex %} měl souseda v obou částech grafu, proto {% latex %}\mathrm{deg}_{G_1}(v), \mathrm{deg}_{G_2}(V) < \Delta \implies{% endlatex %} podle lemmatu ({% latex %}G_1{% endlatex %} a {% latex %}G_2{% endlatex %} nejsou regulární) lze {% latex %}G_1{% endlatex %} i {% latex %}G_2{% endlatex %} {% latex %}\Delta{% endlatex %}-obarvit a stačí přepermutovat barvy, aby měl v obou obarveních stejnou
	- {% latex %}k_V(G) = 2{% endlatex %}
		- dobré případy (lze slepit)
			- {% latex %}b_1(x) = b_1(y){% endlatex %} a {% latex %}b_2(x) = b_2(y){% endlatex %} 
			- {% latex %}b_1(x) \neq b_1(y){% endlatex %} a {% latex %}b_2(x) \neq b_2(y){% endlatex %} 
		- těžší případ -- na jedné straně stejné, na druhé různé
			- {% latex %}b_1(x) = b_1(y){% endlatex %} a {% latex %}b_2(x) \neq b_2(y){% endlatex %} 
				- pokud {% latex %}\mathrm{deg}_{G_1}(x){% endlatex %} nebo {% latex %}\mathrm{deg}_{G_1}(y) \le \Delta - 2{% endlatex %}, tak po přidání hrany půjde použít lemma a vrcholy budou mít různou barvu a máme dobrý případ
				- {% latex %}\mathrm{deg}_{G_1}(x) = \mathrm{deg}_{G_1}(y) = \Delta - 1{% endlatex %}
					- {% latex %}\mathrm{deg}_{G_2}(x) = \mathrm{deg}_{G_2}(y) = 1{% endlatex %}; z předpokladu máme k použití alespoň {% latex %}3{% endlatex %} barvy, přebarvím jimi {% latex %}x{% endlatex %} a {% latex %}y{% endlatex %} a máme dobrý případ
	- {% latex %}k_V(G) \ge 3{% endlatex %} -- použiji lemma o třešničce (souvislý graf, který není klika, obsahuje třešničku)
		- seřadím vrcholy jako {% latex %}v_1 = x, v_2 = y, \ldots, v_n = z{% endlatex %} tak, aby {% latex %}\forall v_i: 3 \le i \le n - 1{% endlatex %} měl alespoň jednoho souseda napravo a barvím (hladově):
			- umíme získat jako BFS vrstvy od {% latex %}z{% endlatex %}, kromě {% latex %}x{% endlatex %} a {% latex %}y{% endlatex %}
			- {% latex %}b(x) = b(y) = 1{% endlatex %}
			- {% latex %}b(v_3)\ldots{% endlatex %} má {% latex %}\ge 1{% endlatex %} neobarveného souseda {% latex %}\implies{% endlatex %} je nějaká nepoužitá z {% latex %}\Delta{% endlatex %} barev
			- {% latex %}\ldots{% endlatex %}
			- {% latex %}b(v_n)\ldots{% endlatex %} všichni sousedé už obarvení, ale dva sousedé ({% latex %}x, y{% endlatex %}) mají stejnou barvu, tedy {% latex %}z{% endlatex %} vidí {% latex %}\le \Delta 1{% endlatex %} barev a jedna je volná

---

Obrázek případů pro {% latex %}k_V(G) = 2{% endlatex %}:

{% xopp cases %}

---

{% endmath %}

#### Pár poznámek

**Harwigerova domněnka:** {% latex %}K_t \not\preceq_m G{% endlatex %} (není minor){% latex %} \implies \Chi(G) < t{% endlatex %}
- {% latex %}t = 4 \ldots{% endlatex %} relativně jednoduché
- {% latex %}t = 5 \ldots{% endlatex %} zobecnění věty o {% latex %}4{% endlatex %} barvách
- {% latex %}t = 6 \ldots{% endlatex %} pomocí věty o {% latex %}4{% endlatex %} barvách + hodně práce
- {% latex %}t \ge 7 \ldots{% endlatex %} neví se

{% math claim %}{% latex %}G{% endlatex %} nakreslitelný na Kleinovu láhev {% latex %}\implies G{% endlatex %} je {% latex %}6{% endlatex %}-obarvitelný.{% endmath %}

{% math proof %}Z Eulerovy formule plyne, že platí jedno z následujících:
- {% latex %}\delta(G)\le 5 \implies \exists v: \mathrm{deg}(v) \le 5{% endlatex %}{% endmath %}
	- {% latex %}G - v \ldots{% endlatex %}  obarvím z indukce, přidám {% latex %}v{% endlatex %} a mám volnou barvu
- {% latex %}G{% endlatex %} je {% latex %}6{% endlatex %}-regulární:
	- {% latex %}G \cong K_7{% endlatex %} -- nesmí, protože nejde nakreslit (je potřeba si rozmyslet)
	- {% latex %}G \not\cong K_7{% endlatex %} -- přímo Brooksova věta

#### Hranové obarvení
{% math definition %}{% latex %}b: E \mapsto B{% endlatex %} (barvy) t. ž. {% latex %}\forall e \neq f \in E, e \cap f \neq \emptyset \implies b(e) \neq b(f){% endlatex %}. Hranová barevnost {% latex %}G{% endlatex %} ("chromatic index") {% latex %}\Chi'(G){% endlatex %} je min. počet barev pro hranové barvení {% latex %}G{% endlatex %}.{% endmath %}

### 7. přednáška

{% math theorem "Vizing, 1964" %}Pro každý graf {% latex %}G{% endlatex %} platí, že {% latex %}\Delta \le \Chi'(G) \le \Delta + 1{% endlatex %}{% endmath %}
- grafy Vizingovy třídy {% latex %}1{% endlatex %} jsou grafy {% latex %}\Chi'(G) = \Delta{% endlatex %}, třídy {% latex %}2{% endlatex %} jsou {% latex %}\Chi'(G) = \Delta + 1{% endlatex %}
- je NP-úplné rozhodnout, zda daný graf {% latex %}G{% endlatex %} má VIzingovu třídu {% latex %}1{% endlatex %} (i pro grafy s {% latex %}\Delta(G) = 3{% endlatex %})
- důkaz jsem zpracoval do [YouTube videa](https://www.youtube.com/watch?v=OZWZpQmGp0g)

#### Perfektní grafy

{% math theorem "Slabá věta o perfektních grafech, 1972" %}{% latex %}G{% endlatex %} je perfektní {% latex %}\iff{% endlatex %} {% latex %}\bar{G}{% endlatex %} je perfektní.{% endmath %}
- důkaz jsem zpracoval do [YouTube videa](https://www.youtube.com/watch?v=Koc63QhxPgk)

### 8. přednáška

#### Chordální grafy

{% math definition "chordální graf" %}Graf je chordální, pokud neobsahuje {% latex %}C_k, k \ge 4{% endlatex %} jako in. podgraf.{% endmath %}
- alternativní pohled vycházející ze jména: každá kružnice má _chordu_ (tětivu)

{% math definition %}Nechť {% latex %}x, y{% endlatex %} dva nesousední vrcholy {% latex %}G{% endlatex %}. {% latex %}R{% endlatex %} je {% latex %}x{\text -}y{% endlatex %}-řez, pokud je to řez takový, že {% latex %}x, y{% endlatex %} patří do různých komponent {% latex %}G \setminus R{% endlatex %}.{% endmath %}

{% math lemma %}{% latex %}G{% endlatex %} je chordální {% latex %}\iff{% endlatex %} pro každé dva nesousední vrcholy {% latex %}x, y \in V, x \neq y{% endlatex %} existuje {% latex %}x{\text -}y{% endlatex %}-řez, který je klika.{% endmath %}

{% math proof %} {% latex %}\Leftarrow{% endlatex %} nechť {% latex %}G{% endlatex %} není chordální, tedy obsahuje indukovanou kružnici {% latex %}C_4{% endlatex %}. Uvážíme-li dva její nesousední vrcholy, tak jakýkoliv řez musí obsahovat vrcholy z horní a dolní cesty mezi {% latex %}x{% endlatex %} a {% latex %}y{% endlatex %}. Ty nesousedí, tedy řez nebude klika.

{% latex %}\Rightarrow{% endlatex %} nechť {% latex %}G{% endlatex %} je chordální, {% latex %}x, y{% endlatex %} nesousední. Nechť {% latex %}R{% endlatex %} je {% latex %}x{\text -}y{% endlatex %}-řez s co nejméně vrcholy. Tvrdím, že {% latex %}R{% endlatex %} tvoří kliku.

Pro spor: {% latex %}R{% endlatex %} není klika {% latex %}\implies{% endlatex %} obsahuje {% latex %}u, v{% endlatex %} nesousedy. Protože {% latex %}R{% endlatex %} je nejmenší, má {% latex %}u{% endlatex %} i {% latex %}v{% endlatex %} sousedy na obou stranách. Jelikož jsou to komponenty souvislosti, tak tam bude existovat cesta. Vezmu nejkratší cesty {% latex %}P_x, P_y{% endlatex %} v komponentách {% latex %}G_x{% endlatex %}, {% latex %}G_y{% endlatex %}. Vrcholy {% latex %}P_x, P_y{% endlatex %} nesousedí (jinak by {% latex %}R{% endlatex %} nebyl řez), {% latex %}P_x-u-P_y-v{% endlatex %} tvoří indukovaný cyklus.

{% xopp another1 %}

{% endmath %}

{% math definition %}Vrchol {% latex %}x{% endlatex %} je v grafu {% latex %}G{% endlatex %} simpliciální, pokud jeho sousedství ({% latex %}N_G(x){% endlatex %} tvoří kliku {% latex %}G{% endlatex %}.{% endmath %}

{% math theorem %}Každý chordální graf (kromě prázdného) obsahuje simpliciální vrchol.{% endmath %}
- dokážeme pomocí silnějšího tvrzení

{% math theorem %}Každý chordální graf je buď úplný, nebo obsahuje dva nesousední simpliciální vrcholy.{% endmath %}

{% math proof %}indukcí podle {% latex %}|V(G)|{% endlatex %}
- základ: {% latex %}|V(G)| = 1{% endlatex %} platí
- pro více vrcholů
	- {% latex %}G{% endlatex %} je úplný, platí
	- nebo nechť {% latex %}x, y{% endlatex %} nesousedi v {% latex %}G{% endlatex %} a {% latex %}R{% endlatex %} je {% latex %}x{\text -}y{% endlatex %}-řez tvořící kliku
		- {% latex %}G_x^+ = \left(\text{komponenta $G \setminus R$ obsahující $x$}\right) \cup R{% endlatex %}, obdobně {% latex %}G_y^+{% endlatex %}
		- (👀) pokud {% latex %}G{% endlatex %} byl chordální, pak {% latex %}H \le G{% endlatex %} je také chordalní
		- použijeme IP na {% latex %}G_x^+{% endlatex %}
			- pokud {% latex %}G_x^+{% endlatex %} klika, vezmi jako {% latex %}s_x{% endlatex %} libovolný vrchol {% latex %}G_x{% endlatex %} (např. {% latex %}x{% endlatex %})
			- pokud {% latex %}G_x^+{% endlatex %} není klika, má dva simpliciální vrcholy; nejvýše jeden může ležet v {% latex %}R{% endlatex %}, jelikož je to klika a za {% latex %}s_x{% endlatex %} zvolím ten druhý; analogicky pro {% latex %}G_y^+{% endlatex %}
			- (👀) jelikož {% latex %}R{% endlatex %} je řez, tak se sousedství nezmění: {% latex %}N_{G_x^+}(s_x) = N_{G}(s_x){% endlatex %}

{% xopp another2 %}
{% endmath %}

{:.rightFloatBox}
<div markdown="1">
{:.center}
![](/assets/kombinatorika-a-grafy-ii/dog.svg)
</div>
{% math definition "PES" %} Perfektní eliminační schéma (PES) grafu {% latex %}G{% endlatex %} je pořadí vrcholů {% latex %}v_1, \ldots, v_n{% endlatex %} t. ž. {% latex %}\forall i \in [n]{% endlatex %} platí, že leví sousedé {% latex %}v_i{% endlatex %} ({% latex %}= \left\{v_j \mid j < i, v_jv_i \in E\right\}{% endlatex %}) tvoří kliku.{% endmath %}

{% math theorem %}G je chordální {% latex %}\iff{% endlatex %} G má PES.{% endmath %}

{% math proof %}{% latex %}\Rightarrow{% endlatex %} obměnou nechť {% latex %}G{% endlatex %} není chordální a má tedy indukovanou kružnici velikosti alespoň {% latex %}4{% endlatex %}. Pro spor nechť máme PES. Nejlevější vrchol špatné kružnice v PES nemá souseda na této kružnici, což je spor s definicí PES.

{% latex %}\Leftarrow{% endlatex %} nechť {% latex %}G{% endlatex %} je chordální. Má tedy simpliciální vrchol {% latex %}v_n{% endlatex %}. Jeho sousedé tvoří kliku a {% latex %}G - v_n{% endlatex %} je opět chordální (pozorování výše) a opakujeme, čímž vznikne PES pro {% latex %}G{% endlatex %}.
{% endmath %}

{% math consequence %}pro daný graf {% latex %}G{% endlatex %} lze v polynomiálním čase rozhodnout, zda je chordální.{% endmath %}

{% math consequence %}chordální grafy jsou perfektní.{% endmath %}

{% math definition %}{% latex %}G{% endlatex %} je hamiltonovský, pokud má kružnici na {% latex %}n{% endlatex %} vrcholech (jako podgraf).{% endmath %}

{% math theorem "Bondyho-Chvátalova" %}Nechť {% latex %}G{% endlatex %} je graf na {% latex %}\ge 3{% endlatex %} vrcholech. Nechť {% latex %}x,y{% endlatex %} jsou nesousedé t. ž. {% latex %}\mathrm{deg}_G(x) + \mathrm{deg}_G(y) \ge n{% endlatex %}. Nechť {% latex %}G^+ = (V, E \cup \left\{xy\right\}){% endlatex %}. Pak {% latex %}G{% endlatex %} je hamiltonovský {% latex %}\iff{% endlatex %} {% latex %}G^+{% endlatex %} je hamiltonovský.{% endmath %}

{% math proof %} {% latex %}\Rightarrow{% endlatex %} jasné

{% latex %}\Leftarrow{% endlatex %} nechť {% latex %}C{% endlatex %} je hamiltonovská kružnice {% latex %}G^+{% endlatex %} a {% latex %}x,y{% endlatex %} vrcholy splňující podmínku.
- pokud {% latex %}C{% endlatex %} neobsahuje {% latex %}xy{% endlatex %}, pak {% latex %}C{% endlatex %} je hamiltonovská kružnice {% latex %}G{% endlatex %}
- jinak {% latex %}v_1, \ldots, v_n{% endlatex %} očíslujeme vrcholy {% latex %}C{% endlatex %} a navíc {% latex %}v_1 = x, v_n = y{% endlatex %}
	- chceme {% latex %}C' := \left(C \setminus \left\{xy, v_iv_{i + 1}\right\}\right) \cup \left\{v_iy, v_{i + 1}x\right\}{% endlatex %} je ham. kružnice v {% latex %}G{% endlatex %}
	- {% latex %}I_1 := \left\{i \in \left\{2, \ldots, n - 2\right\}\ \text{t. ž. }\left\{x, v_{i + 1}\right\} \in E\right\}{% endlatex %} (vrcholy dobré pro {% latex %}x{% endlatex %})
		- povoluji vrcholy {% latex %}v_3, \ldots, v_{n-1}{% endlatex %}, viz. indexování
	- {% latex %}I_2 := \left\{i \in \left\{2, \ldots, n - 2\right\}\ \text{t. ž. }\left\{y, v_i\right\} \in E\right\}{% endlatex %} (vrcholy dobré pro {% latex %}y{% endlatex %})
		- povoluji vrcholy {% latex %}v_2, \ldots, v_{n - 2}{% endlatex %}, viz. indexování
	- {% latex %}|I_1 \cup I_2| \le n - 3{% endlatex %}
	- {% latex %}|I_1| = \mathrm{deg}_G(x) - 1{% endlatex %} (nesmím použít {% latex %}v_2{% endlatex %})
	- {% latex %}|I_2| = \mathrm{deg}_G(y) - 1{% endlatex %} (nesmím použít {% latex %}v_{n - 1}{% endlatex %})
	- {% latex %}|I_1| + |I_2| = \mathrm{deg}_G(x) - 1 + \mathrm{deg}_G(y) - 1 \ge n - 2{% endlatex %} (z předpokladu)
	- {% latex %}|I_1 \cup I_2| \le 3{% endlatex %} ale {% latex %}|I_1 + I_2| \ge n - 2{% endlatex %} znamená, že se překrývají

{% xopp another3 %}
{% endmath %}

{% math theorem "Divac" %}{% latex %}G{% endlatex %} graf na {% latex %}n \ge 3{% endlatex %} vrcholech s min. stupněm {% latex %}\ge n/2{% endlatex %} je hamiltonovský.{% endmath %}

{% math proof %}Z Bondy-Chvátalovy věty doplníme na {% latex %}K_n{% endlatex %}, který je hamiltonovský.{% endmath %}

### 9. přednáška

#### Tutteův polynom

{% math definition: "multigraf" %} {% latex %}G = (V, E){% endlatex %} kde {% latex %}V{% endlatex %} jsou vrcholy a {% latex %}E{% endlatex %} multimnožina prvků z {% latex %}V \cup \binom{V}{2}{% endlatex %}{% endmath %}
- odstranění a kontrakce fungují intuitivně -- kontrakce nezahazuje hrany, protože máme multigraf

{% math definition "most" %}hrana {% latex %}e \in E{% endlatex %} je most, v multigrafu {% latex %}G{% endlatex %}, pokud {% latex %}G - e{% endlatex %} má více komponent než {% latex %}G{% endlatex %}{% endmath %}
- {% latex %}k(G) = k(V, E) = \text{počet komponent}{% endlatex %}

{% math definition: "hodnost/rank" %}{% latex %}E{% endlatex %} je {% latex %}r(E) := |V| - k(G){% endlatex %}{% endmath %}
- intuice: {% latex %}\sim{% endlatex %} velikost největší „neredundantní“ podmnožiny {% latex %}F \subseteq E{% endlatex %} (t. ž. {% latex %}k(G) = k(V, F){% endlatex %})

{% math proof %}Chceme dokázat, že {% latex %}F{% endlatex %} neobsahuje cykly a že {% latex %}r(E) = r(F){% endlatex %}. Víme, že {% latex %}k(G) = k(V, F){% endlatex %}.

Postupné přidávání hran z {% latex %}F{% endlatex %}
- snižuje počet komponent, vždy o {% latex %}1{% endlatex %}, tedy {% latex %}k(V, F) = n - |F| = |V| - |F|{% endlatex %}
- zvyšuje {% latex %}\mathrm{r}{% endlatex %} vždy o {% latex %}1{% endlatex %} (nastává druhý případ z tabulky dole), tedy {% latex %}r(F) = |F|{% endlatex %}

Spojením dostáváme {% latex %}r(F) = |F| = |V| - k(V, F) = |V| - k(G){% endlatex %}.
{% endmath %}

{% math definition: "nulita" %}{% latex %}E{% endlatex %} je {% latex %}n(E) := |E| - r(E){% endlatex %}{% endmath %}
- intuice: velikost největší „redundantní“ podmnožiny {% latex %}F \subseteq E{% endlatex %} (t. ž. počet komponent se nezmění po jejím odebrání)

{% math example %}{% latex %}G = (V, \emptyset){% endlatex %}
- {% latex %}r(\emptyset) = 0{% endlatex %}
- {% latex %}n(\emptyset) = 0{% endlatex %}

| změna                                   | {% latex %}r(E){% endlatex %}     | {% latex %}n(E){% endlatex %}     |
| ---                                     | ---                               | ---                               |
| přidání hrany bez změny počtu komponent | {% latex %}r(E){% endlatex %}     | {% latex %}n(E) + 1{% endlatex %} |
| přidání hrany se změnou počtu komponent | {% latex %}r(E) + 1{% endlatex %} | {% latex %}n(E){% endlatex %}     |

- přidáním hrany se rank:
	- nezmění, pokud se nezmění počet komponent
	- zvětší o {% latex %}1{% endlatex %}, pokud se dvě komponenty spojily
{% endmath %}

{% math definition: "Tutteův polynom" %}multigrafu {% latex %}G = (V, E){% endlatex %} je polynom proměnných {% latex %}x, y{% endlatex %} definovaný jako {% latex display %}T_G(x, y) := \sum_{F \subseteq E} (x - 1)^{r(E) - r(F)} \cdot (y - 1)^{n(F)}{% endlatex %}{% endmath %}

{% math lemma %}pro {% latex %}G{% endlatex %} souvislý je {% latex %}T_G(1, 1){% endlatex %} počet koster {% latex %}G{% endlatex %}{% endmath %}

{% math proof %}Dosadím do polynomu a získám {% latex %}0^{r(E) - r(F)} 0^{n(F)}{% endlatex %}. Vím, že {% latex %}x^0 \equiv 1{% endlatex %}, tedy výraz bude počet {% latex %}F{% endlatex %} takových, že {% latex %}r(E) = r(F){% endlatex %} a {% latex %}n(F) = 0{% endlatex %}.
- z předpokladu souvislosti je počet komponent {% latex %}1{% endlatex %}
	- {% latex %}F{% endlatex %} musí mít také pouze {% latex %}1{% endlatex %}, protože {% latex %}r(E) = r(F){% endlatex %}
- {% latex %}n(F) = 0{% endlatex %} znamená, že {% latex %}0 = |F| - |V| - 1{% endlatex %}, tedy {% latex %}|F| = |V| - 1{% endlatex %}
- kombinace počtu hran a souvislosti dává, že je to strom a tedy kostra
{% endmath %}

{% math lemma %}Nechť {% latex %}G_1 = (V_1, E_1), G_2 = (V_2, G_2){% endlatex %} jsou multigrafy, t. ž. {% latex %}|V_1 \cap V_2| \le 1{% endlatex %}, {% latex %}|E_1 \cap E_2| = 0{% endlatex %} (protínají se nejvýše v jednom vrcholu a v žádné hraně). Definujeme {% latex %}G = (V, E){% endlatex %}, kde {% latex %}V = V_1 \cup V_2{% endlatex %} a {% latex %}E = E_1 \cup E_2{% endlatex %}. Potom {% latex %}T_G(x, y) = T_{G_1}(x, y) \cdot T_{G_2}(x, y){% endlatex %}
{% endmath %}

{% math proof %}V definici kvantifikuji přes podmnožiny hran. Ty ale můžu vždy rozdělit na disjunktní sjednocení podle {% latex %}E_1{% endlatex %} a {% latex %}E_2{% endlatex %}. Navíc:
- {% latex %}r(F) = r(F_1) + r(F_2){% endlatex %} (z pohledu jako největší neredundantní množina hran)
- {% latex %}n(F) = n(F_1) + n(F_2){% endlatex %} (analogicky, opět z intuice)

Pak rozepíšu:
{% latex display %}
\begin{aligned}
	T_G(x, y) &= \sum_{F \subseteq E} (x - 1)^{r(E) - r(F)} (y - 1)^{n(F)} \\
	          &= \sum_{F_1 \subseteq E_1} \sum_{F_2 \subseteq E_2} (x - 1)^{r(E_1 \cup E_2) - r(F_1 \cup F_2)} (y - 1)^{n(F_1 \cup F_2)} \\
	          &= \sum_{F_1 \subseteq E_1} \sum_{F_2 \subseteq E_2} (x - 1)^{r(E_1) - r(F_1) + r(E_2) - r(F_2)} (y - 1)^{n(F_1) +n(F_2) } \\
	          &= \sum_{F_1 \subseteq E_1} \sum_{F_2 \subseteq E_2} (x - 1)^{r(E_1) - r(F_1)} (x - 1)^{r(E_2) - r(F_2)} (y - 1)^{n(F_1)} (y - 1)^{n(F_2)} \\
	          &= \sum_{F_1 \subseteq E_1} (x - 1)^{r(E_1) - r(F_1)}(y - 1)^{n(F_1)}  \left(\sum_{F_2 \subseteq E_2} (x - 1)^{r(E_2) - r(F_2)} (y - 1)^{n(F_2)}\right) \\
	          &= T_{G_1}(x, y) \cdot T_{G_2}(x, y) \\
\end{aligned}
{% endlatex %}
{% endmath %}

{% math consequence %}dva grafy se stejným Tutteovým polynomem nemusí být stejné (neobsahuje informaci o počtu komponent či počtu vrcholů).{% endmath %}

{% math theorem %}Nechť {% latex %}G = (V, E){% endlatex %} je multigraf. Potom {% latex %}T_G(x, y){% endlatex %} je jednoznačně určen rekurencemi:
{% endmath %}
- {% latex %}E = \emptyset{% endlatex %}: {% latex %}T_G(x, y) = 1{% endlatex %}
- jinak pro {% latex %}e{% endlatex %}:

| most   | {% latex %}T_G(x, y) = x \cdot T_{G - e}(x, y)= x \cdot T_{G \setminus e}(x, y){% endlatex %}  |
|        | poslední rovnost: z důsledku výše                                                              |
| smyčka | {% latex %}T_G(x, y) = y \cdot T_{G - e}(x, y) = y \cdot T_{G \setminus e}(x, y){% endlatex %} |
|        | poslední rovnost: odstranění smyčky je to stejné jako její kontrakce                           |
| jindy  | {% latex %}T_G(x, y) = T_{G - e}(x, y) + \cdot T_{G \setminus e}(x, y){% endlatex %}           |

{% math proof %}Pro {% latex %}E = \emptyset{% endlatex %} jasné, všude je {% latex %}0{% endlatex %}. Jinak rozdělíme:

{% latex display %}T_G(x, y) = \underbrace{\sum_{F \subseteq E, e \not\in F} (x - 1)^{r(E) - r(F)} \cdot (y - 1)^{n(F)}}_{s_1} + \underbrace{\sum_{F \subseteq E, e \in F} (x - 1)^{r(E) - r(F)} \cdot (y - 1)^{n(F)}}_{s_2}{% endlatex %}

Stačí dokázat následující:
1. pokud {% latex %}e{% endlatex %} není most, tak {% latex %}s_1 = T_{G - e}(x, y){% endlatex %}
	- {% latex %}e{% endlatex %} není most, jeho odebráním se rank nezmění, jen dosadím...
2. pokud {% latex %}e{% endlatex %} je most, tak {% latex %}s_1 = (x - 1) \cdot T_{G - e}(x, y){% endlatex %}
	- {% latex %}e{% endlatex %} je most, jeho odebráním se rank zvětší o {% latex %}1{% endlatex %}, zase jen dosadím...
3. pokud {% latex %}e{% endlatex %} není smyčka, tak {% latex %}s_2 = T_{G \setminus e}(x, y){% endlatex %}
4. pokud {% latex %}e{% endlatex %} je smyčka, tak {% latex %}s_2 = (y - 1)T_{G \setminus e}(x, y){% endlatex %}

Poté pro větu stačí následující:
- {% latex %}e{% endlatex %} je most: (2) + (3)
- {% latex %}e{% endlatex %} je smyčka: (1) + (4)
- {% latex %}e{% endlatex %} není most ani smyčka: (1) + (3)

{% endmath %}

{% math definition: "chromatický polynom" %}multigrafu {% latex %}G = (V, E){% endlatex %} je funkce {% latex %}\mathrm{ch}_G(b): \mathbb{N}_0 \mapsto \mathbb{N}_0{% endlatex %}, kde pro {% latex %}b \in \mathbb{N}_0{% endlatex %} je {% latex %}\mathrm{ch}_G(b) := {% endlatex %} počet dobrých obarvení (posunutí udělá nové obarvení) {% latex %}G{% endlatex %} pomocí barev {% latex %}\left\{1, \ldots, b\right\}{% endlatex %}.
{% endmath %}
- pokud {% latex %}G{% endlatex %} má smyčku, pak {% latex %}\mathrm{ch}_G(b) = 0, \forall b{% endlatex %}

{% math theorem %}Pro každý multigraf {% latex %}G = (V, E){% endlatex %} platí
{% latex display %}\mathrm{ch}_G(b) = \left(-1\right)^{|V| + k(G)} \cdot b^{k(G)} \cdot T_G(1 - b, 0){% endlatex %}
{% endmath %}

### 10. přednáška

#### Formální mocniné řady
{% math definition %}Pro posloupnost reálných čísel {% latex %}a_0, a_1, \ldots{% endlatex %} je formální mocninná řada (FMŘ) zápis tvaru {% latex %}a_0 + a_1x^1 + a_2x^2 + \ldots = \sum_{i = 0}^{\infty} a_i x^i{% endlatex %}{% endmath %}
- {% latex %}\mathbb{R} \llbracket x \rrbracket \ldots{% endlatex %} všechny FMŘ nad {% latex %}x{% endlatex %}
- pro {% latex %}A(x) = a_0 + a_1 x + a_2x^2 + \ldots{% endlatex %} je {% latex %}[x^n]A(x) = a_n{% endlatex %}
- pro FMŘ {% latex %}A(x), B(x){% endlatex %} je
	- {% latex %}A(x) + B(x) = (a_0 + b_0) + (a_1 + b_1)x + (a_2 + b_2)x^2 + \ldots{% endlatex %}
	- {% latex %}A(x) \cdot B(x) = c_0 + c_1x + c_2x^2 + \ldots{% endlatex %}, kde {% latex %}c_n = a_0 b_n + a_1 b_{n - 1} + \ldots + a_{n - 1}b_1 + a_{n} b_0{% endlatex %} (konvoluce)

{% math fact %} {% latex %}\mathbb{R}\llbracket x \rrbracket{% endlatex %} tvoří (komutativní) okruh (máme {% latex %}+, \cdot, 0, 1{% endlatex %}{% endmath %}
- {% latex %}0 = A(x){% endlatex %} s nulovými koeficienty
- {% latex %}0 = A(x){% endlatex %} s {% latex %}a_0 = 1{% endlatex %} a zbytek nulové koeficienty

{% math fact %} {% latex %}\mathbb{R}\llbracket x \rrbracket{% endlatex %} tvoří vektorový postor (násobení konstantou je FMŘ pro {% latex %}a_0 = c{% endlatex %}{% endmath %}

{% math definition "převrácená hodnota" %} FMŘ {% latex %}A(x){% endlatex %} je taková FMŘ, že {% latex %}A(x) \cdot B(x) = 1{% endlatex %}{% endmath %}

- {% latex %}A(x) = c \ldots B(x) = \frac{1}{c}{% endlatex %}
- {% latex %}A(x) = x \ldots B(x){% endlatex %} není (muselo by být něco jako {% latex %}\frac{1}{x}{% endlatex %})
- {% latex %}A(x) = 1 - x \ldots B(x) = 1 + x + x^2 + \ldots{% endlatex %}
	- {% latex %}C(x) = A(x) \cdot B(x) = (1 + x + x^2 + \ldots) + (x + x^2 + x^3 + \ldots){% endlatex %}, kde {% latex %}[x^n]C(x){% endlatex %} bude nulové pro {% latex %}n \ge 1{% endlatex %} (požere se to)

{% math lemma %}Nechť {% latex %}A(x) = \sum_{n = 0}^{\infty} a_n x^n{% endlatex %} je FMŘ. Potom {% latex %}\frac{1}{A(x)}{% endlatex %} existuje, právě když {% latex %}a_0 \neq 0{% endlatex %} (a pak je jednoznačně určena).{% endmath %}

{% math proof %}Hledejme inverz. Rozepsáním {% latex %}A(x) \cdot B(x) = 1 + 0x + 0x^2 + \ldots{% endlatex %} nám dává soustavu takovýchto rovnic, které mají jednoznačné řešení:

{% latex display %}
\begin{aligned}
	a_0 b_0 = 1 &\qquad b_0 = \frac{1}{a_0} \\
	a_0 b_1 + a_1b_0 = 0 &\qquad b_1 = \frac{1}{a_0}(-a_1 b_0)\\
	a_0 b_2 + a_1b_1 + a_2b_0 = 0 &\qquad b_2 = \frac{1}{a_0} (-a_1 b_1 - a_2b_2) \\
	                          &\;\;\;\vdots \\
\end{aligned}
{% endlatex %}
{% endmath %}

TODO: od půlky

### 11. přednáška
TODO

### 12. přednáška
TODO

### 13. přednáška
TODO



### Zdroje/materiály
- [Stránky přednášky](https://research.koutecky.name/db/teaching:kg22021_prednaska).
- [Poznámky Václava Končického](https://kam.mff.cuni.cz/~koncicky/notes/kag2/pdf) z roku 2019.
