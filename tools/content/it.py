# -*- coding: utf-8 -*-
# Contenuti sito APEX — Italiano. Modifica qui, poi esegui tools/build.py.

LANG = "it"
PREFIX = "/it"
OTHER_PREFIX = ""

ROUTES = {
    "home": "/it/", "how": "/it/come-funziona", "reviews": "/it/recensioni", "product": "/it/prodotto",
    "guides": "/it/guide/", "faq": "/it/faq", "contact": "/it/contatti", "story": "/it/storia",
    "pro": "/it/pro", "early": "/it/accesso-anticipato",
    "terms": "/it/legal/termini", "privacy": "/it/legal/privacy", "warranty": "/it/legal/garanzia", "returns": "/it/legal/resi",
}
GUIDE_SLUGS = {
    "how-to-know-if-you-ride-well": "capire-se-guidi-bene-in-moto",
    "how-to-improve-cornering": "migliorare-in-curva-in-moto",
    "motorcycle-telemetry-road": "telemetria-moto-stradale",
    "riding-coach-cost": "quanto-costa-un-corso-di-guida-moto",
    "first-track-day-guide": "primo-track-day-come-prepararsi",
}

SITE = dict(name="APEX", tagline="Ogni giro diventa una review.", email="hello@apex-rider.com", company="APEX Srl · Milano")

NAV = [("how", "Come funziona"), ("reviews", "Recensioni"), ("guides", "Guide"), ("product", "Acquista")]
NAV_CTA = ("early", "Richiedi accesso anticipato")
FOOTER = {
    "product": ("Prodotto", [("product", "Kit APEX e pack"), ("how", "Come funziona"), ("reviews", "Recensioni"), ("faq", "FAQ")]),
    "company": ("Azienda", [("story", "La nostra storia"), ("pro", "Per istruttori e scuole"), ("guides", "Guide"), ("contact", "Contatti")]),
    "legal": ("Legale", [("terms", "Termini"), ("privacy", "Privacy"), ("warranty", "Garanzia"), ("returns", "Resi")]),
}
FOOT_BLURB = "Il coach di guida che lavora dopo il giro. Kit, montaggio e 12 mesi di review curva per curva, un solo prezzo."
NEWSLETTER = dict(label="Aggiornamenti dal primo lotto", placeholder="La tua email", button="Iscriviti", ok="Fatto. Scriviamo solo quando c'è qualcosa da dire.")
LANG_LABELS = dict(this="IT", other="EN")
COPYRIGHT = "© 2026 APEX Srl · Ogni giro diventa una review."
BACK_TO_TOP = "Torna su"

CTA_BAND = dict(
    eyebrow="Accesso anticipato aperto",
    h="Il tuo prossimo giro può già avere una review.",
    p="Nessun pagamento sul sito. Lasci i tuoi dati, confermiamo pack e moto, poi spediamo. L'accesso anticipato blocca il prezzo e la priorità di consegna sul primo lotto.",
    btn="Richiedi accesso anticipato", btn2="Vedi pack e prezzi",
)
TRUST = [
    ("Montaggio incluso", "Il kit arriva a casa e organizziamo noi il montaggio. Tu guidi e basta."),
    ("12 mesi di review inclusi", "Un prezzo, un anno. Nessun abbonamento, nessun rinnovo automatico."),
    ("Nessun pagamento finché non confermiamo la moto", "Prima verifichiamo la compatibilità con il tuo modello, poi parliamo di pagamento."),
]
REVIEW_CARD = dict(
    head="Review · Curva 4 · Giro di domenica", pill="Pronta",
    legend_you="La tua linea", legend_ideal="Linea ideale",
    metrics=[("Fluidità", 82), ("Frenata", 64), ("Linea", 88)],
    flags=[("warn", "Frenata", "Iniziata 15 m troppo presto"), ("warn", "Apex", "Toccato 4 m prima del punto ideale"), ("good", "Gas", "Riapertura fluida in uscita")],
    next_k="Da lavorare al prossimo giro",
    next="Porta la frenata più vicina alla curva 4 e rilasciala in ingresso. La linea è già buona: il tempo si perde prima dell'apex.",
)

PRESS = []
RESULTS = None
COMMUNITY = None
TESTIMONIALS = []
EMPTY_TESTIMONIALS = dict(
    b="I primi piloti sono in strada adesso.",
    p="APEX spedisce a piccole ondate. Le recensioni del primo lotto arrivano qui man mano: verificate, non ritoccate, con nome. Fino ad allora la cosa più onesta che possiamo mostrarti è il prodotto.",
    btn="Guarda come funziona una review",
)

HOME = dict(
    title="APEX — Il coach moto che lavora dopo il giro",
    description="Una review curva per curva dopo ogni giro: linea, frenata, gas e una cosa su cui lavorare. Kit, montaggio e 12 mesi di review da 49,90 €.",
    hero=dict(
        eyebrow="Ride review · Strada e pista",
        h="Guida meglio. A ogni singolo giro.",
        p="Smetti di chiederti cosa hai fatto in quella curva. APEX legge linea, frenata e gas mentre guidi e ti consegna la review prima che tu ti tolga il casco.",
        btn="Richiedi accesso anticipato", btn2="Guarda come funziona",
        note="Da 49,90 € · kit, montaggio e 12 mesi di review inclusi · nessun pagamento sul sito",
    ),
    sports=dict(
        eyebrow="Il problema",
        h="In ogni sport la review è normale. In moto non esiste.",
        rows=[
            ("Lo scacchista", "Analisi della partita dopo ogni match", True),
            ("Il tennista", "Rivede la partita colpo per colpo", True),
            ("Il calciatore", "Video-analisi il lunedì", True),
            ("Il motociclista", "Scende dalla moto. Fine.", False),
        ],
        apex=("Il motociclista con APEX", "Review pronta prima di togliere il casco"),
    ),
    meet=dict(
        eyebrow="Ecco APEX",
        h="Diventa un pilota migliore questa stagione in 3 passi.",
        steps=[
            ("Monta il kit", "Il kit arriva a casa e il montaggio è incluso. Vive sulla moto e si accende da solo. Niente da lanciare, niente da ricordare."),
            ("Guida come sempre", "Passo di montagna, tragitto quotidiano o pista: APEX legge linea, frenata e gas mentre tu tieni gli occhi sulla strada. Nessuno schermo in sella."),
            ("Leggi la review", "Scendi dalla moto ed è sul telefono: curva per curva, cosa ha funzionato, cosa correggere e l'unica cosa su cui lavorare la prossima volta."),
        ],
        btn="Scopri come funziona",
    ),
    changes=dict(
        eyebrow="Cosa cambia per te",
        h="Tre cose, dopo ogni giro.",
        items=[
            ("Sai cosa hai fatto bene", "Le curve pulite, la frenata giusta, i tratti in cui sei stato preciso. La review parte da ciò che funziona, così lo riconosci e lo ripeti."),
            ("Sai esattamente cosa correggere", "Non “rallenta”. Punti precisi: dove hai frenato troppo presto, dove hai riaperto il gas tardi, e una sola priorità per il prossimo giro."),
            ("Vedi i progressi, giro dopo giro", "Ogni sessione è confrontata con le precedenti sullo stesso tipo di strada. Fluidità, frenata, linea: numeri che salgono, non sensazioni vaghe."),
        ],
    ),
    riders=dict(
        eyebrow="Per chi è",
        h="Se ti riconosci, APEX è fatto per te.",
        items=[
            ("Neopatentato", "Patente fresca, o di nuovo in sella dopo anni", "Vuoi costruire le abitudini giuste prima che si fissino quelle sbagliate, e sentirti più sicuro senza che nessuno ti giudichi. Il pack Start a 49,90 € è per te."),
            ("Pilota del weekend", "Passi di montagna la domenica, curve che conosci a memoria", "E la sensazione di essere fermo allo stesso livello da anni. La review ti dà quello che un corso da qualche centinaio di euro ti dà una volta l'anno, a ogni giro."),
            ("Pilota da track day", "Track day amatoriali, a caccia di decimi", "Vuoi i dati della sessione prima di toglierti la tuta: dove freni, dove riapri, dove la linea si sporca. APEX Pro è fatto per te."),
        ],
    ),
    testimonials_h="Cosa dicono i piloti",
    testimonials_eyebrow="Recensioni",
)

HOW = dict(
    title="Come funziona APEX — monta, guida, review, migliora",
    description="Quattro passi dalla scatola a un pilota migliore: monta il kit, guida come sempre, leggi la review curva per curva, segui i progressi nel tempo.",
    hero=dict(eyebrow="Come funziona", h="Tu guidi. Al resto pensa APEX.", p="Nessuno schermo in sella, nessuna app da smanettare, nessun dato da interpretare. Quattro passi, e solo uno ti chiede qualcosa."),
    journey=[
        dict(k="1", eyebrow="Monta", h="Monta il kit una volta. Poi dimenticalo.",
             p="Il kit arriva a casa e il montaggio è incluso nel prezzo del pack. Si monta sulla moto senza toccare l'elettronica, si sveglia quando guidi e si addormenta quando ti fermi.",
             li=[("Montaggio incluso", "confermiamo la compatibilità con il tuo modello e lo organizziamo"), ("Nessun cablaggio", "non tocca l'elettronica della moto"), ("Nessuna routine", "si sveglia da solo, si ricarica di rado")],
             media="Foto: kit su una naked, primo piano"),
        dict(k="2", eyebrow="Guida", h="Guida come hai sempre fatto.",
             p="Strada, passo o pista. APEX legge linea, frenata e gas in ogni curva mentre tu pensi a guidare. Niente da guardare, niente da premere, zero distrazioni.",
             li=[("Ogni curva", "ingresso, apex, uscita"), ("Ogni comando", "punto di frenata, rilascio, riapertura del gas"), ("Ogni fondo", "riconosce strada e pista e adatta la review")],
             media="Foto: pilota in piega su strada di montagna"),
        dict(k="3", eyebrow="Review", h="Leggi la review prima di toglierti il casco.",
             p="Scendi dalla moto ed è sul telefono. La tua linea contro quella ideale, frenata e gas punto per punto, ciò che ha funzionato in verde — e una sola priorità per il prossimo giro.",
             li=[("La tua linea vs ideale", "la distanza tra le due è la lezione"), ("Cosa ha funzionato", "si migliora ripetendo le curve buone"), ("Una priorità", "un obiettivo alla volta, come un vero coach")],
             media="review"),
        dict(k="4", eyebrow="Migliora", h="Guardati migliorare.",
             p="Una review ti dice com'è andata oggi. Le review insieme ti dicono se stai davvero migliorando. Ogni sessione è confrontata con le precedenti sullo stesso tipo di strada, e i numeri non hanno opinioni.",
             li=[("Stessa strada, nel tempo", "confronta la curva, non la giornata"), ("Tre punteggi", "fluidità, frenata, linea"), ("Traguardi", "APEX segna i giri in cui qualcosa è scattato")],
             media="Schermate: progressi su sei giri"),
    ],
    skills=dict(
        eyebrow="Cosa migliora APEX",
        h="Le quattro cose che fanno una curva.",
        p="La maggior parte dei piloti pensa alla curva come a un gesto unico. È una sequenza di decisioni, e il problema è quasi sempre in una sola. APEX le valuta separatamente, così lavori su quella giusta.",
        items=[
            ("Frenata", "Dove inizi, come rilasci, se la porti dentro la curva o la molli prima.", 64),
            ("Linea", "Dove sei passato davvero rispetto alla linea che apre l'uscita e ti lascia margine.", 88),
            ("Gas", "Quando riapri e quanto progressivamente. Non quanto: quanto fluido.", 76),
            ("Fluidità", "Correzioni a metà curva, esitazioni, comandi bruschi. Il punteggio che mostra i fondamentali che si assestano.", 82),
        ],
    ),
    tech=dict(
        eyebrow="Sotto la carena",
        h="Come un giro diventa una review.",
        items=[
            ("Sensori di movimento", "Un'unità inerziale compatta sulla moto registra piega, accelerazione, frenata e comportamento del gas molte volte al secondo. Nessun collegamento alla centralina."),
            ("Ride AI", "Modelli addestrati su dati di guida dividono il giro in curve, trovano ogni punto di frenata, apex e riapertura, e li confrontano con l'ideale per quella curva."),
            ("Riconoscimento strada e pista", "APEX riconosce il tipo di strada — passo, urbano, circuito — e adatta ciò su cui ti valuta, così un tragitto quotidiano non è giudicato come un giro in pista."),
        ],
    ),
    not_=dict(
        eyebrow="Per essere chiari",
        h="Cosa APEX non è.",
        items=[
            ("Non è un cronometro", "Il cronometro ti dice quanto sei veloce. La review ti dice perché."),
            ("Non è un altro schermo", "Niente da guardare in sella. Tutto arriva dopo, casco tolto."),
            ("Non è un giudice", "Nessuna classifica pubblica. La review è tua e di nessun altro."),
        ],
    ),
    faq_h="Le domande dei piloti",
    faq=[
        ("APEX funziona sulla mia moto?", "APEX è pensato per qualsiasi moto, dalle naked alle grandi adventure. Quando richiedi l'accesso anticipato ti contattiamo e confermiamo la compatibilità con il tuo modello prima di qualsiasi pagamento."),
        ("Devo guardare qualcosa mentre guido?", "No. APEX non mostra nulla mentre guidi e non richiede alcuna interazione in sella. La review arriva sul telefono quando scendi dalla moto."),
        ("Funziona sia su strada che in pista?", "Sì. La review funziona su strada, sui passi e in pista. Per i track day con analisi giro per giro c'è il pack APEX Pro."),
        ("Devo essere un pilota esperto?", "No. APEX è fatto per ogni pilota, non solo per quelli veloci. Se guidi da solo su strada aperta, APEX troverà qualcosa di concreto su cui lavorare."),
        ("Cosa succede dopo i 12 mesi inclusi?", "Nessun rinnovo automatico: non conserviamo metodi di pagamento. Prima della scadenza ti presentiamo le opzioni e decidi tu se continuare."),
    ],
)

REVIEWS = dict(
    title="Recensioni APEX — cosa dicono i piloti",
    description="Recensioni verificate dei piloti che usano APEX, più le risposte per neopatentati, piloti del weekend, esperti e piloti da track day.",
    hero=dict(eyebrow="Recensioni", h="Chi guida meglio si diverte di più.", p="Non si tratta di essere il più veloce. Si tratta di essere migliore di domenica scorsa. Ecco cosa dicono i piloti, e le risposte oneste alle domande che riceviamo più spesso."),
    videos_h="I piloti in video",
    videos=[],
    faq_h="APEX è per me?",
    faq=[
        ("Ho appena preso la patente. Non è troppo presto?", "È il momento migliore. Le abitudini che costruisci nel primo anno sono quelle che restano. APEX parte da ciò che fai già bene e ti dà una cosa alla volta, senza giudizio. Il pack Start esiste proprio per questo."),
        ("Guido solo qualche weekend all'anno.", "Allora ogni giro vale doppio. Un corso ti dà feedback una volta l'anno; APEX te lo dà ogni volta che esci, sulle strade che fai davvero."),
        ("Sono un pilota esperto. Cosa può dirmi che non sento già?", "Dov'è davvero il tuo punto di frenata rispetto a dove pensi che sia. I piloti esperti di solito hanno ragione sulla linea e torto sulla frenata, e la sensazione in sella non distingue un punto dieci metri prima da uno perfetto."),
        ("Faccio track day. È un cronometro?", "No. Il cronometro ti dice quanto sei veloce. APEX ti dice perché: quale curva, quale fase, quale comando. APEX Pro aggiunge l'analisi giro per giro per i track day."),
        ("Guido un'adventure / uno scooter / una cruiser.", "Ad APEX non importa cosa guidi. Frenata, linea e gas funzionano allo stesso modo su qualsiasi due ruote; cambia solo il setup. Confermiamo la compatibilità con il tuo modello prima che tu paghi qualcosa."),
    ],
)

PRODUCT = dict(
    title="Kit APEX — pack e prezzi: kit, montaggio e 12 mesi di review",
    description="Scegli il pack: Start 49,90 € (under 25 o neopatentati), Rider 89,90 €, Pro 179,90 € per la pista. Kit, montaggio e 12 mesi di review in un solo prezzo.",
    eyebrow="Kit APEX · accesso anticipato",
    h="APEX. Il coach che ti aspetta a fine giro.",
    p="Kit, montaggio e 12 mesi di review curva per curva in un solo prezzo. Come un fitness tracker: paghi una volta, guidi tutto l'anno.",
    from_="Da", price_note="una tantum · tutto incluso",
    packs_h="Scegli il tuo pack",
    packs=[
        dict(id="Start", name="APEX Start", price="49,90 €", d="Under 25 o patente da meno di 12 mesi", tag="Accesso anticipato", soon=False),
        dict(id="Rider", name="APEX Rider", price="89,90 €", d="Per tutti, nessun requisito", tag="Accesso anticipato", soon=False),
        dict(id="Pro", name="APEX Pro", price="179,90 €", d="Pista e track day · analisi giro per giro", tag="Pre-ordine a breve", soon=True),
    ],
    buy_btn="Richiedi accesso anticipato",
    buy_meta=[
        "Nessun pagamento sul sito. Ti contattiamo, confermiamo la moto, poi gestiamo pagamento e consegna.",
        "Il primo lotto è limitato: l'accesso anticipato blocca prezzo e priorità di consegna.",
        "I tempi di consegna del primo lotto vengono confermati quando ti contattiamo.",
        "Montaggio incluso in ogni pack.",
    ],
    gallery=["Foto prodotto: kit, inquadratura principale", "Kit sulla moto", "App: review", "App: progressi", "Cosa c'è nella scatola"],
    tabs=[("tab-how", "Come funziona"), ("tab-packs", "Pack"), ("tab-specs", "Specifiche")],
    outcomes=dict(
        h="Cosa imparerai, in base a dove sei oggi",
        items=[
            ("Neopatentato", ["Dove inizia davvero la tua frenata", "Scegliere una linea che apre l'uscita", "Gas progressivo in uscita", "Sicurezza dai dati, non dalle sensazioni"]),
            ("Pilota del weekend", ["La fase di curva che ti frena", "Costanza curva dopo curva", "Portare la frenata al punto giusto", "Progressi misurati sulle strade che ami"]),
            ("Pilota da pista", ["Punto di frenata per curva, per giro", "Dove la linea si sporca sotto pressione", "Riapertura del gas vs ideale", "Confronto tra sessioni"]),
        ],
    ),
    tracking=dict(
        h="APEX registra ogni giro",
        items=[("Ogni curva", "ingresso, apex, uscita, con la tua linea disegnata contro l'ideale"), ("Ogni comando", "punto di frenata e rilascio, riapertura e progressività del gas"), ("Ogni fondo", "strada, passo o pista: la review si adatta"), ("Ogni sessione", "confrontata con le precedenti sullo stesso tipo di strada")],
    ),
    modes=dict(
        h="Tre modi in cui APEX ti allena",
        items=[
            ("Review post-giro", "Curva per curva", "Due minuti sul telefono quando scendi dalla moto: cosa ha funzionato, cosa correggere, una priorità."),
            ("Progressi", "Giro dopo giro", "Fluidità, frenata e linea nel tempo sullo stesso tipo di strada. Traguardi quando qualcosa scatta."),
            ("Modalità pista", "APEX Pro", "Analisi giro per giro per i track day: punto di frenata per curva per giro, confronto tra sessioni."),
        ],
    ),
    compare=dict(
        h="I pack, uno accanto all'altro",
        cols=["Start · 49,90 €", "Rider · 89,90 €", "Pro · 179,90 €"],
        rows=[
            ("Kit APEX", [1, 1, 1]), ("Montaggio incluso", [1, 1, 1]), ("12 mesi di review", [1, 1, 1]),
            ("Review curva per curva", [1, 1, 1]), ("Progressi tra sessioni", [1, 1, 1]), ("Analisi pista giro per giro", [0, 0, 1]),
            ("Requisiti", ["Under 25 o patente < 12 mesi", "nessuno", "nessuno"]), ("Disponibilità", ["Accesso anticipato", "Accesso anticipato", "Pre-ordine a breve"]),
        ],
        buying_h="Come funziona l'acquisto",
        buying=[
            ("30 secondi", "Compila il form rapido", "Nome, email, il pack che vuoi e cosa guidi. Fatto."),
            ("Ti scriviamo", "Ti contattiamo", "Dettagli del pack, tempi del primo lotto e qualsiasi domanda."),
            ("Insieme", "Confermiamo pack e moto", "Verifichiamo la compatibilità con il tuo modello, e i requisiti Start se ti riguardano."),
            ("Solo ora", "Pagamento e consegna", "Concordiamo pagamento, montaggio e consegna. Il prezzo dell'accesso anticipato resta bloccato."),
        ],
    ),
    specs=[
        ("Sensori", "Unità inerziale sulla moto: piega, accelerazione, comportamento di frenata e gas"),
        ("Collegamento alla moto", "Nessuno. Non tocca l'elettronica né la centralina"),
        ("Compatibilità", "Qualsiasi moto; confermata per modello prima dell'acquisto"),
        ("Montaggio", "Incluso in ogni pack, organizzato con te"),
        ("Consegna della review", "App APEX (iOS / Android) dopo ogni giro"),
        ("Cosa viene valutato", "Frenata, linea, gas, fluidità — per curva"),
        ("Riconoscimento strada", "Strada / passo / pista, automatico"),
        ("Periodo incluso", "12 mesi di review; nessun rinnovo automatico"),
        ("Nella scatola", "Kit APEX, supporto, cavo di ricarica, guida rapida"),
    ],
    specs_note="Le specifiche fisiche (dimensioni, peso, autonomia, resistenza all'acqua) vengono pubblicate con il primo lotto.",
)

GUIDES = dict(
    title="Guide APEX — guida meglio, curva per curva",
    description="Risposte dirette alle domande che i piloti fanno davvero: come capire se guidi bene, come pulire una curva, quanto vale un corso, cosa misura la telemetria, come prepararsi al primo track day.",
    hero=dict(eyebrow="Guide", h="Guida meglio, curva per curva.", p="Risposte dirette alle domande che ogni pilota si fa davvero. Filtra per dove sei oggi e per cosa vuoi migliorare."),
    level_lbl="Livello", topic_lbl="Argomento", all_="Tutti",
    levels=[("new", "Neopatentato"), ("weekend", "Pilota del weekend"), ("experienced", "Esperto"), ("track", "Track day")],
    topics=[("self-assessment", "Autovalutazione"), ("technique", "Tecnica"), ("data", "Dati e telemetria"), ("coaching", "Coaching e corsi"), ("track", "Pista")],
    read="min di lettura", by="Team APEX", featured="In evidenza",
    end=dict(h="Dalla lettura alla guida", p="Le guide ti dicono cosa guardare. APEX lo misura per te: ogni giro diventa una review, curva per curva, con una cosa concreta su cui lavorare."),
    prev="Precedente", next="Successiva", back="Tutte le guide", tip_k="Consiglio APEX", share="Condividi",
)
GUIDE_META = {
    "how-to-know-if-you-ride-well": (["new", "weekend", "experienced"], "APEX valuta separatamente frenata, linea, gas e fluidità dopo ogni giro, così “guido bene?” diventa quattro numeri e una priorità."),
    "how-to-improve-cornering": (["new", "weekend", "experienced", "track"], "Ogni review APEX disegna la tua linea contro quella ideale e segna il punto di frenata e la riapertura del gas. La distanza tra le due linee è la lezione."),
    "motorcycle-telemetry-road": (["weekend", "experienced", "track"], "APEX non tocca l'elettronica della moto: un'unità inerziale legge piega, frenata e gas e l'app li trasforma in una review leggibile."),
    "riding-coach-cost": (["new", "weekend"], "Un pack APEX costa quanto un solo giorno di corso, e fa la review di ogni giro per dodici mesi."),
    "first-track-day-guide": (["weekend", "track"], "APEX Pro aggiunge l'analisi giro per giro per i track day: punto di frenata per curva per giro, e un confronto tra sessioni leggibile nel paddock."),
}

FAQ = dict(
    title="FAQ APEX — prodotto, pack, acquisto, dati",
    description="Tutto ciò che i piloti chiedono su APEX: cos'è, quale pack scegliere, come funziona l'acquisto, come vengono trattati i dati di guida.",
    hero=dict(eyebrow="Centro assistenza", h="Domande, risposte.", p="Se la tua non c'è, scrivici. Risponde un founder."),
    groups=[
        ("Su APEX", [
            ("Cos'è APEX, in una frase?", "Un kit che vive sulla tua moto e trasforma ogni giro in una review curva per curva sul telefono: linea, frenata, gas, e una cosa su cui lavorare la prossima volta."),
            ("È un'app da guardare mentre guido?", "No. APEX non mostra nulla mentre guidi e non ti chiede nulla in sella. La review arriva dopo."),
            ("APEX funziona sulla mia moto?", "È pensato per qualsiasi moto. Confermiamo la compatibilità con il tuo modello specifico quando ti contattiamo, prima di qualsiasi pagamento."),
            ("Funziona su strada e in pista?", "Sì. Strada, passo e pista. L'analisi giro per giro per i track day è nel pack Pro."),
        ]),
        ("Pack e acquisto", [
            ("Cosa è incluso esattamente nel prezzo?", "Ogni pack include tre cose: il kit, il montaggio sulla tua moto e 12 mesi di review. Nessun abbonamento mensile, nessun costo nascosto."),
            ("Chi può acquistare APEX Start a 49,90 €?", "Piloti under 25 o con patente da meno di 12 mesi. Stesso kit e stesse review del pack Rider."),
            ("Come funziona il pagamento?", "Non c'è pagamento sul sito. Compili il form di accesso anticipato, ti contattiamo, confermiamo insieme pack e moto, e solo allora gestiamo pagamento e consegna."),
            ("Il prezzo dell'accesso anticipato è garantito?", "Sì. Richiedere l'accesso anticipato blocca il prezzo del pack e la priorità di consegna sul primo lotto, che è limitato."),
            ("Quando sarà disponibile APEX Pro?", "APEX Pro (179,90 €, pista e track day) apre al pre-ordine a breve. Lascia i tuoi dati nel form per essere avvisato."),
            ("Cosa succede dopo i 12 mesi inclusi?", "Nessun rinnovo automatico: non conserviamo metodi di pagamento. Prima della scadenza ti presentiamo le opzioni e decidi tu."),
        ]),
        ("Usare APEX", [
            ("Quanto ci vuole a leggere una review?", "Circa due minuti. Si apre sull'unica cosa su cui lavorare; il dettaglio curva per curva c'è se lo vuoi."),
            ("Devo ricaricarlo a ogni giro?", "No. Il kit si sveglia quando guidi e si addormenta quando ti fermi. Gli intervalli di ricarica vengono pubblicati con il primo lotto."),
            ("Posso usarlo su più di una moto?", "Il kit viene montato su una moto. Spostarlo su un'altra è possibile; scrivici e lo organizziamo."),
        ]),
        ("I tuoi dati", [
            ("Chi può vedere le mie review?", "Solo tu. Nessuna classifica pubblica obbligatoria, nessun punteggio visibile ad altri."),
            ("Quali dati raccoglie APEX?", "Dati di movimento dal kit, GPS dal telefono durante il giro e i dati del tuo account. Vedi l'informativa privacy per conservazione e diritti."),
            ("Posso cancellare i miei dati?", "Sì, in qualsiasi momento, dall'app o scrivendoci."),
        ]),
    ],
)

CONTACT = dict(
    title="Contatta APEX",
    description="Domande sul prodotto, sui pack o sulla tua moto: una email e risponde un founder.",
    hero=dict(eyebrow="Contatti", h="Una email. Risponde un founder.", p="Siamo un piccolo team a Milano e leggiamo tutto."),
    items=[
        ("Assistenza e domande", "Prodotto, pack, la tua moto, il tuo ordine.", "hello@apex-rider.com"),
        ("Istruttori e scuole", "Pro deal, partnership, demo day.", "hello@apex-rider.com"),
        ("Stampa e investitori", "Materiali, interviste, la storia.", "hello@apex-rider.com"),
    ],
    hours="Rispondiamo entro due giorni lavorativi, di solito prima.",
    faq_link="Molte risposte sono già nelle FAQ",
)

STORY = dict(
    title="La nostra storia — perché abbiamo costruito APEX",
    description="Migliaia di ore in moto, zero review. Come tre motociclisti a Milano hanno deciso di dare a ogni pilota ciò che ogni altro atleta ha già.",
    hero=dict(eyebrow="La nostra storia", h="Migliaia di ore in moto. Zero review.", p="Ogni atleta riceve un feedback strutturato sulla sua prestazione. I motociclisti finiscono il giro, scendono dalla moto e spesso non hanno idea di cosa hanno fatto bene o male. APEX esiste per colmare questo vuoto."),
    body=[
        ("Il vuoto", "Uno scacchista ha l'analisi della partita. Un tennista rivede il match. Un calciatore ha la video-analisi il lunedì. Un motociclista scende dalla moto, e basta. L'unico feedback è un corso una volta l'anno, o la sensazione in sella — che non distingue un punto di frenata dieci metri prima da uno perfetto."),
        ("L'idea", "E se la review semplicemente succedesse? Nessuno schermo da guardare, nessuna app da smanettare, nessun dato da interpretare. Un kit che vive sulla moto, legge come guidi e ti consegna due minuti di feedback chiaro quando ti togli il casco: cosa ha funzionato, cosa correggere, una cosa su cui lavorare."),
        ("Come lo costruiamo", "Un prezzo, tutto incluso, nessuna sorpresa da abbonamento. Nessuna classifica. Nessun giudizio. Una review che parte da ciò che fai già bene, perché è così che lavorano i veri coach — e perché i piloti che si sentono giudicati smettono di ascoltare."),
    ],
    founders_h="I founder",
    founders=[("Federico", "Co-founder"), ("Niccolò Bua Odetti", "Co-founder"), ("Giuseppe Pisante", "Co-founder")],
    where="APEX Srl ha sede a Milano.",
    milestones_h="Tappe",
    milestones=[],
)

PRO = dict(
    title="APEX per istruttori e scuole di guida",
    description="Dai a ogni allievo una review curva per curva tra una lezione e l'altra. Pro deal per istruttori, scuole, organizzatori di track day e club.",
    hero=dict(eyebrow="APEX Pro deal", h="Il tuo coaching, a ogni giro del tuo allievo.", p="Un corso dà feedback una volta. APEX continua a darlo tra le lezioni, nel tuo linguaggio: punto di frenata, linea, gas, una priorità. Per istruttori, scuole, organizzatori di track day e club."),
    who_h="Per chi è",
    who=[("Istruttori di guida", "Indipendenti o in una scuola"), ("Scuole e accademie", "Corsi stradali e avanzati"), ("Organizzatori di track day", "Coaching in paddock, gruppi"), ("Club e community", "Giri di gruppo con uno scopo")],
    benefits_h="Cosa ottieni",
    benefits=[
        ("Prezzo Pro", "Prezzo agevolato sui kit per te e per i tuoi allievi."),
        ("Referral", "Un codice per i tuoi piloti; vedi chi si è unito e su cosa sta lavorando (con il loro consenso)."),
        ("Demo day", "Veniamo da te con i kit per una giornata di giri montati e recensiti."),
        ("Voce nel prodotto", "Gli utenti Pro plasmano cosa dice la review. Costruiamo con te, non contro di te."),
    ],
    btn="Candidati per un Pro deal", note="Le candidature aprono con il primo lotto. Scrivici chi sei e cosa insegni.",
)

EARLY = dict(
    title="Richiedi accesso anticipato — APEX",
    description="Trenta secondi, sei campi, nessun pagamento ora. Ti contattiamo per confermare pack e moto.",
    hero=dict(eyebrow="Accesso anticipato · posti del primo lotto", h="Richiedi accesso anticipato.", p="Trenta secondi, nessun pagamento ora. Ti contattiamo per confermare il pack, verificare la compatibilità con la tua moto e gestire l'ordine. Il prezzo dell'accesso anticipato resta bloccato."),
    f=dict(name="Nome", email="Email", pack="Quale pack?", pack_ph="Scegli un pack",
           packs=[("Start €49,90", "APEX Start — 49,90 € (under 25 / patente < 12 mesi)"), ("Rider €89,90", "APEX Rider — 89,90 €"), ("Pro €179,90 (notify)", "APEX Pro — 179,90 € (avvisami al pre-ordine)")],
           bike="Cosa guidi?", bike_ph="es. Yamaha MT-07, 2021",
           usage="Come guidi di più?", usage_ph="Scegli",
           usages=[("road-weekend", "Weekend / strade di montagna"), ("commuting", "Tutti i giorni / pendolare"), ("track", "Track day"), ("mixed", "Un po' di tutto")],
           consent="Accetto di essere contattato da APEX per la mia richiesta di accesso anticipato", consent_link="informativa privacy",
           btn="Richiedi accesso anticipato", note="Nessun pagamento ora. Ti contattiamo per confermare il pack e gestire l'ordine."),
    ok=dict(h="Sei in lista.", p="Grazie per aver alzato la mano. Distribuiamo il primo lotto a piccole ondate e ti scriviamo appena si apre un posto per come e dove guidi."),
    steps=[("Compila il form", "Trenta secondi."), ("Ti scriviamo", "Dettagli del pack, tempi, le tue domande."), ("Pagamento e consegna", "Concordati insieme, dopo aver confermato la moto.")],
    direct_h="Preferisci scriverci direttamente?", direct_p="Domande sul prodotto, sui pack o sulla tua moto: una email e rispondiamo noi.",
)

LEGAL_NOTICE = "Bozza. Questa pagina è una struttura per i testi legali di APEX e deve essere rivista da un legale prima della pubblicazione."
LEGAL = {
    "terms": dict(title="Termini di servizio — APEX", h="Termini di servizio", updated="Ultimo aggiornamento: da impostare alla pubblicazione", sections=[
        ("1. Chi siamo", "APEX Srl, Milano (“APEX”, “noi”). Questi termini regolano il sito APEX, il kit APEX e l'app APEX."),
        ("2. Requisiti", "Devi essere titolare di una patente moto valida e maggiorenne per acquistare. APEX Start è riservato a piloti under 25 o con patente da meno di 12 mesi; i requisiti sono confermati prima dell'acquisto."),
        ("3. Sicurezza alla guida", "APEX fornisce feedback dopo il giro e non è un dispositivo di sicurezza. Resti l'unico responsabile di come guidi e del rispetto del codice della strada. Non interagire mai con il telefono mentre guidi."),
        ("4. Accesso anticipato e acquisto", "Richiedere l'accesso anticipato non è un acquisto. Prezzo e priorità di consegna sono bloccati al momento della richiesta. Il pagamento viene concordato dopo la conferma di compatibilità con la tua moto."),
        ("5. Periodo incluso", "Ogni pack include 12 mesi di review dall'attivazione. Nessun rinnovo automatico e nessuna conservazione dei metodi di pagamento."),
        ("6. Responsabilità", "Nei limiti di legge, la responsabilità di APEX è limitata al prezzo pagato per il pack."),
        ("7. Controversie", "Questi termini sono regolati dalla legge italiana. Foro competente Milano, fatte salve le tutele inderogabili del consumatore."),
    ]),
    "privacy": dict(title="Informativa privacy — APEX", h="Informativa privacy", updated="Ultimo aggiornamento: da impostare alla pubblicazione", sections=[
        ("1. Titolare del trattamento", "APEX Srl, Milano. Contatto: hello@apex-rider.com."),
        ("2. Dati raccolti", "Dati dell'account (nome, email); dati del form di accesso anticipato (pack, moto, abitudini di guida); dati di movimento dal kit; dati GPS dal telefono durante i giri; dati di utilizzo dell'app."),
        ("3. Finalità", "Fornire il servizio di review, contattarti per la richiesta di accesso anticipato, migliorare i modelli di analisi e adempiere agli obblighi di legge."),
        ("4. Trattamento con AI", "I dati di guida sono elaborati dai modelli APEX per produrre le review. I dati usati per migliorare i modelli sono pseudonimizzati."),
        ("5. Condivisione", "Utilizziamo responsabili del trattamento per hosting, invio email e analytics con accordi di trattamento dati. Non vendiamo i tuoi dati. Le review sono private."),
        ("6. Conservazione", "Le richieste di accesso anticipato sono conservate fino all'evasione del primo lotto o finché non chiedi la cancellazione. I dati di guida sono conservati finché l'account è attivo."),
        ("7. I tuoi diritti", "Accesso, rettifica, cancellazione, portabilità, opposizione e reclamo al Garante per la protezione dei dati personali. Scrivi a hello@apex-rider.com."),
    ]),
    "warranty": dict(title="Garanzia — APEX", h="Garanzia", updated="Ultimo aggiornamento: da impostare alla pubblicazione", sections=[
        ("Hardware", "Il kit APEX è coperto dalla garanzia legale di conformità di due anni prevista per i consumatori nell'UE."),
        ("Cosa copre", "Difetti di fabbricazione e guasti in condizioni d'uso normali."),
        ("Cosa non copre", "Danni da caduta, montaggio improprio non eseguito da APEX o dai suoi partner, infiltrazioni d'acqua oltre il grado dichiarato, modifiche al kit."),
        ("Come richiederla", "Scrivi a hello@apex-rider.com con i dettagli dell'ordine e una descrizione del problema."),
    ]),
    "returns": dict(title="Resi — APEX", h="Resi", updated="Ultimo aggiornamento: da impostare alla pubblicazione", sections=[
        ("Diritto di recesso", "Come consumatore UE puoi recedere entro 14 giorni dalla consegna senza motivazione. Il kit deve essere restituito completo e integro."),
        ("Pre-ordini", "I pre-ordini possono essere annullati con rimborso completo in qualsiasi momento prima della spedizione."),
        ("Procedura di rimborso", "Scrivi a hello@apex-rider.com. I rimborsi vengono emessi sul metodo di pagamento originale entro 14 giorni dal ricevimento del reso."),
    ]),
}
