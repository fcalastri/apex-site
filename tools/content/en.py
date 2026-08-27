# -*- coding: utf-8 -*-
# APEX site content — English. Edit copy here, then run tools/build.py.
# Sections that depend on data APEX does not have yet (press, survey numbers,
# testimonials) are lists left empty on purpose: the build renders an honest
# fallback until real entries are added. See CONTENT-TODO.md.

LANG = "en"
PREFIX = ""            # URL prefix for this language
OTHER_PREFIX = "/it"   # URL prefix of the other language

# ---- routes (slug per page id) --------------------------------------------
ROUTES = {
    "home": "/", "how": "/how-it-works", "reviews": "/reviews", "product": "/product",
    "guides": "/guides/", "faq": "/faq", "contact": "/contact", "story": "/our-story",
    "pro": "/pro", "early": "/early-access",
    "terms": "/legal/terms", "privacy": "/legal/privacy", "warranty": "/legal/warranty", "returns": "/legal/returns",
}
GUIDE_SLUGS = {   # article id -> slug
    "how-to-know-if-you-ride-well": "how-to-know-if-you-ride-well",
    "how-to-improve-cornering": "how-to-improve-cornering",
    "motorcycle-telemetry-road": "motorcycle-telemetry-road",
    "riding-coach-cost": "riding-coach-cost",
    "first-track-day-guide": "first-track-day-guide",
}

SITE = dict(
    name="APEX", tagline="Every ride becomes a review.",
    email="hello@apex-rider.com",
    company="APEX Srl · Milan, Italy",
)

NAV = [("how", "How it works"), ("reviews", "Reviews"), ("guides", "Guides"), ("product", "Buy")]
NAV_CTA = ("early", "Request early access")
FOOTER = {
    "product": ("Product", [("product", "APEX kit & packs"), ("how", "How it works"), ("reviews", "Reviews"), ("faq", "FAQ")]),
    "company": ("Company", [("story", "Our story"), ("pro", "For instructors & schools"), ("guides", "Guides"), ("contact", "Contact")]),
    "legal": ("Legal", [("terms", "Terms"), ("privacy", "Privacy"), ("warranty", "Warranty"), ("returns", "Returns")]),
}
FOOT_BLURB = "The riding coach that works after the ride. Kit, fitting and 12 months of corner-by-corner reviews, one price."
NEWSLETTER = dict(label="Updates from the first run", placeholder="Your email", button="Subscribe", ok="You're in. We only write when there's something to say.")
LANG_LABELS = dict(this="EN", other="IT")
COPYRIGHT = "© 2026 APEX Srl · Every ride becomes a review."
BACK_TO_TOP = "Back to top"

# ---- shared blocks ----------------------------------------------------------
CTA_BAND = dict(
    eyebrow="Early access open",
    h="Your next ride can already have a review.",
    p="No payment on the site. Leave your details, we confirm the pack and your bike, then we ship. Early access locks your price and delivery priority on the first run.",
    btn="Request early access", btn2="See packs & prices",
)
TRUST = [
    ("Fitting included", "The kit ships to you and we arrange the fitting. You just ride."),
    ("12 months of reviews included", "One price, one year. No subscription, no auto-renewal."),
    ("No payment until your bike is confirmed", "We check compatibility with your model first, then talk payment."),
]
REVIEW_CARD = dict(
    head="Review · Turn 4 · Sunday ride", pill="Ready",
    legend_you="Your line", legend_ideal="Ideal line",
    metrics=[("Smoothness", 82), ("Braking", 64), ("Line", 88)],
    flags=[("warn", "Braking", "Started 15 m too early"), ("warn", "Apex", "Touched 4 m before the ideal point"), ("good", "Throttle", "Smooth pick-up on exit")],
    next_k="Work on next ride",
    next="Carry your braking closer to turn 4 and release it on entry. The line is already good — the time is lost before the apex.",
)

# ---- lists that need real data (kept empty on purpose) ---------------------
PRESS = []            # [("“Quote under 15 words”", "Outlet")]
RESULTS = None        # dict(intro="From a survey of N riders", items=[("87%", "Improved their cornering"), ...])
COMMUNITY = None      # dict(h="One community, over N riders", p="It's not about being fast. It's about being better.")
TESTIMONIALS = []     # [dict(q="...", name="...", role="...")]
EMPTY_TESTIMONIALS = dict(
    b="The first riders are on the road now.",
    p="APEX ships in small waves. Reviews from the first run go here as they come in — verified, unedited, named. Until then, the fairest thing we can show you is the product itself.",
    btn="See how a review works",
)

# ---- HOME -------------------------------------------------------------------
HOME = dict(
    title="APEX — The motorcycle coach that works after the ride",
    description="A corner-by-corner review after every ride: line, braking, throttle and one thing to work on. Kit, fitting and 12 months of reviews from €49.90.",
    hero=dict(
        eyebrow="Ride review · Road & track",
        h="Ride better. Every single ride.",
        p="Stop guessing what you did in that corner. APEX reads your line, braking and throttle while you ride, and hands you a review before your helmet is off.",
        btn="Request early access", btn2="See how it works",
        note="From €49.90 · kit, fitting and 12 months of reviews included · no payment on the site",
    ),
    sports=dict(
        eyebrow="The problem",
        h="In every sport the review is normal. On a motorcycle it doesn't exist.",
        rows=[
            ("The chess player", "Game review after every match", True),
            ("The tennis player", "Replays the match shot by shot", True),
            ("The footballer", "Video analysis on Monday", True),
            ("The rider", "Gets off the bike. That's it.", False),
        ],
        apex=("The rider with APEX", "Review ready before the helmet comes off"),
    ),
    meet=dict(
        eyebrow="Meet APEX",
        h="Become a better rider this season in 3 steps.",
        steps=[
            ("Fit the kit", "The kit ships to your door and fitting is included. It lives on the bike and switches itself on. Nothing to launch, nothing to remember."),
            ("Ride like you always do", "Mountain pass, commute or track: APEX reads your line, braking and throttle while you keep your eyes on the road. No screen in the saddle."),
            ("Read your review", "Get off the bike and it's on your phone: corner by corner, what worked, what to fix, and the one thing to work on next time out."),
        ],
        btn="Explore how it works",
    ),
    changes=dict(
        eyebrow="What changes for you",
        h="Three things, after every ride.",
        items=[
            ("Know what you did right", "The clean corners, the well-judged braking, the sections where you were precise. The review starts from what works, so you can recognise it and repeat it."),
            ("Know exactly what to fix", "Not “slow down”. Precise points: where you braked too early, where you got on the throttle late, and a single priority for your next ride."),
            ("See progress, ride after ride", "Every session is compared with the ones before it on the same kind of road. Smoothness, braking, line: numbers going up, not vague feelings."),
        ],
    ),
    riders=dict(
        eyebrow="Who it's for",
        h="If this sounds like you, APEX was built for you.",
        items=[
            ("New rider", "Fresh licence, or back in the saddle after years away", "You want to build the right habits before the bad ones stick, and feel more confident without anyone judging you. The Start pack at €49.90 is for you."),
            ("Weekend rider", "Mountain passes on Sunday, corners you know by heart", "And the feeling you've been stuck at the same level for years. The review gives you what a few-hundred-euro course gives you once a year, on every ride."),
            ("Track day rider", "Amateur track days, chasing tenths", "You want the session data before your leathers are off: where you brake, where you open up, where the line gets scrappy. APEX Pro is built for you."),
        ],
    ),
    testimonials_h="What riders say",
    testimonials_eyebrow="Reviews",
)

# ---- HOW IT WORKS -----------------------------------------------------------
HOW = dict(
    title="How APEX works — fit, ride, review, improve",
    description="Four steps from the box to a better rider: fit the kit, ride as usual, read the corner-by-corner review, track your progress over time.",
    hero=dict(eyebrow="How it works", h="You ride. APEX does the rest.", p="No screen in the saddle, no app to fiddle with, no data to interpret. Four steps, and only one of them asks anything of you."),
    journey=[
        dict(k="1", eyebrow="Fit", h="Fit the kit once. Forget it.",
             p="The kit ships to your door and fitting is included in the pack price. It mounts on the bike without touching its electronics, wakes when you ride and sleeps when you stop.",
             li=[("Fitting included", "we confirm compatibility with your model and arrange it"), ("No wiring", "it doesn't touch the bike's electronics"), ("No routine", "wakes on its own, charges rarely")],
             media="Photo: kit on a naked bike, close-up"),
        dict(k="2", eyebrow="Ride", h="Ride like you always do.",
             p="Road, mountain pass or track. APEX reads your line, braking and throttle in every corner while you focus on riding. Nothing to look at, nothing to press, zero distractions.",
             li=[("Every corner", "entry, apex, exit"), ("Every input", "braking point, release, throttle pick-up"), ("Every surface", "recognises road vs track and adjusts the review")],
             media="Photo: rider mid-corner on a mountain road"),
        dict(k="3", eyebrow="Review", h="Read the review before the helmet is off.",
             p="Get off the bike and it's on your phone. Your line against the ideal line, your braking and throttle point by point, what worked highlighted in green — and one single priority for your next ride.",
             li=[("Your line vs ideal", "the gap is your lesson"), ("What worked", "improving starts from repeating the good corners"), ("One priority", "one goal at a time, like a real coach")],
             media="review"),
        dict(k="4", eyebrow="Improve", h="See yourself getting better.",
             p="One review tells you how today went. Reviews together tell you whether you're actually improving. Every session is compared with the previous ones on the same kind of road, and numbers don't have opinions.",
             li=[("Same road, over time", "compare the corner, not the day"), ("Three scores", "smoothness, braking, line"), ("Milestones", "APEX marks the rides where something clicked")],
             media="Screens: progress over six rides"),
    ],
    skills=dict(
        eyebrow="What APEX improves",
        h="The four things that make a corner.",
        p="Most riders think of a corner as one fluid action. It's a sequence of decisions, and the problem is almost always in just one of them. APEX scores each separately so you work on the right one.",
        items=[
            ("Braking", "Where you start, how you release, whether you're carrying it into the corner or dumping it before.", 64),
            ("Line", "Where you actually went versus the line that opens the exit and keeps your options open.", 88),
            ("Throttle", "When you pick it up and how progressively. Not how much: how smooth.", 76),
            ("Smoothness", "Mid-corner corrections, hesitation, abrupt inputs. The score that shows fundamentals settling in.", 82),
        ],
    ),
    tech=dict(
        eyebrow="Under the fairing",
        h="How a ride becomes a review.",
        items=[
            ("Motion sensing", "A compact inertial unit on the bike records lean, acceleration, braking and throttle behaviour many times a second. No connection to the bike's ECU."),
            ("Ride AI", "Models trained on riding data split the ride into corners, find each braking point, apex and throttle pick-up, and compare them to the ideal for that corner."),
            ("Road & track detection", "APEX recognises the kind of road you're on — pass, urban, circuit — and adjusts what it scores you on, so a commute isn't judged like a track lap."),
        ],
    ),
    not_=dict(
        eyebrow="To be clear",
        h="What APEX is not.",
        items=[
            ("Not a lap timer", "The stopwatch tells you how fast. The review tells you why."),
            ("Not another screen", "Nothing to look at in the saddle. Everything arrives after, helmet off."),
            ("Not a judge", "No public leaderboard. The review is yours and no one else's."),
        ],
    ),
    faq_h="Questions riders ask",
    faq=[
        ("Does APEX work on my motorcycle?", "APEX is designed for any motorcycle, from nakeds to big adventure bikes. When you request early access we contact you and confirm compatibility with your model before any payment."),
        ("Do I have to look at anything while riding?", "No. APEX shows nothing while you ride and requires no interaction in the saddle. The review lands on your phone when you get off the bike."),
        ("Does it work on both road and track?", "Yes. The review works on the road, on mountain passes and on track. For track days with lap-by-lap analysis there is the APEX Pro pack."),
        ("Do I need to be an experienced rider?", "No. APEX is built for every rider, not just fast ones. If you ride on your own on open roads, APEX will find something concrete for you to work on."),
        ("What happens after the 12 included months?", "There is no automatic renewal: we do not store payment methods. Before the end we present your options and you decide whether to continue."),
    ],
)

# ---- REVIEWS ----------------------------------------------------------------
REVIEWS = dict(
    title="APEX reviews — what riders say",
    description="Verified reviews from riders using APEX, plus answers for new riders, weekend riders, experienced riders and track day riders.",
    hero=dict(eyebrow="Reviews", h="Better riders have more fun.", p="It's not about being the fastest. It's about being better than last Sunday. Here is what riders say, and the honest answers to the questions we get most."),
    videos_h="Riders on camera",
    videos=[],   # [("Video title", "youtube_id")]
    faq_h="Is APEX for me?",
    faq=[
        ("I've just got my licence. Isn't it too early?", "It's the best moment. The habits you build in the first year are the ones that stick. APEX starts from what you already do well and gives you one thing at a time, without judgement. The Start pack exists for exactly this."),
        ("I only ride a few weekends a year.", "Then every ride counts double. A course gives you feedback once a year; APEX gives it to you every time you go out, on the roads you actually ride."),
        ("I'm an experienced rider. What can it tell me that I don't already feel?", "Where your braking point really is versus where you think it is. Experienced riders are usually right about the line and wrong about braking, and the feeling in the saddle can't tell a point ten metres early from a perfect one."),
        ("I do track days. Is this a lap timer?", "No. A lap timer tells you how fast. APEX tells you why: which corner, which phase, which input. APEX Pro adds lap-by-lap analysis for track days."),
        ("I ride an adventure bike / a scooter / a cruiser.", "APEX doesn't care what you ride. Braking, line and throttle work the same way on any two wheels; only the setup changes. We confirm compatibility with your model before you pay anything."),
    ],
)

# ---- PRODUCT ----------------------------------------------------------------
PRODUCT = dict(
    title="APEX kit — packs & prices: kit, fitting and 12 months of reviews",
    description="Choose your pack: Start €49.90 (under 25 or new licence), Rider €89.90, Pro €179.90 for track. Kit, fitting and 12 months of reviews in one price.",
    eyebrow="APEX kit · early access",
    h="APEX. The coach that waits for you at the end of the ride.",
    p="Kit, fitting and 12 months of corner-by-corner reviews in one price. Like a fitness tracker: pay once, ride all year.",
    from_="From", price_note="one-time · everything included",
    packs_h="Choose your pack",
    packs=[
        dict(id="Start", name="APEX Start", price="€49.90", d="Under 25 or licensed less than 12 months", tag="Early access", soon=False),
        dict(id="Rider", name="APEX Rider", price="€89.90", d="For everyone, no requirements", tag="Early access", soon=False),
        dict(id="Pro", name="APEX Pro", price="€179.90", d="Track & track days · lap-by-lap analysis", tag="Pre-order soon", soon=True),
    ],
    buy_btn="Request early access",
    buy_meta=[
        "No payment on the site. We contact you, confirm your bike, then handle payment and delivery.",
        "First run is limited: early access locks your price and delivery priority.",
        "Delivery timing for the first run is confirmed when we contact you.",
        "Fitting included in every pack.",
    ],
    gallery=["Product photo: kit, hero angle", "Kit on bike", "App: review", "App: progress", "What's in the box"],
    tabs=[("tab-how", "How it works"), ("tab-packs", "Packs"), ("tab-specs", "Tech specs")],
    outcomes=dict(
        h="What you'll learn, by where you are today",
        items=[
            ("New rider", ["Where your braking really starts", "Choosing a line that opens the exit", "Progressive throttle on exit", "Confidence from data, not guesswork"]),
            ("Weekend rider", ["The corner phase that's holding you back", "Consistency corner after corner", "Carrying braking to the right point", "Measured progress on the roads you love"]),
            ("Track rider", ["Braking point per corner, per lap", "Where the line gets scrappy under pressure", "Throttle pick-up vs ideal", "Session-to-session comparison"]),
        ],
    ),
    tracking=dict(
        h="APEX tracks every ride",
        items=[("Every corner", "entry, apex, exit, with your line drawn against the ideal"), ("Every input", "braking point and release, throttle pick-up and progressiveness"), ("Every surface", "road, pass or track — the review adapts"), ("Every session", "compared with the previous ones on the same kind of road")],
    ),
    modes=dict(
        h="Three ways APEX coaches you",
        items=[
            ("Post-ride review", "Corner by corner", "Two minutes on your phone when you get off the bike: what worked, what to fix, one priority."),
            ("Progress tracking", "Ride after ride", "Smoothness, braking and line over time on the same kind of road. Milestones when something clicks."),
            ("Track mode", "APEX Pro", "Lap-by-lap analysis for track days: braking point per corner per lap, session comparison."),
        ],
    ),
    compare=dict(
        h="The packs, side by side",
        cols=["Start · €49.90", "Rider · €89.90", "Pro · €179.90"],
        rows=[
            ("APEX kit", [1, 1, 1]), ("Fitting included", [1, 1, 1]), ("12 months of reviews", [1, 1, 1]),
            ("Corner-by-corner review", [1, 1, 1]), ("Progress across sessions", [1, 1, 1]), ("Lap-by-lap track analysis", [0, 0, 1]),
            ("Requirements", ["Under 25 or licence < 12 months", "none", "none"]), ("Availability", ["Early access", "Early access", "Pre-order soon"]),
        ],
        buying_h="How buying works",
        buying=[
            ("30 seconds", "Fill in the quick form", "Name, email, the pack you want and what you ride. Done."),
            ("We write to you", "We contact you", "Pack details, first-run timing and any question you have."),
            ("Together", "We confirm pack and bike", "We verify compatibility with your model, and Start eligibility if it applies."),
            ("Only now", "Payment and delivery", "We agree on payment, fitting and delivery. Your early access price stays locked."),
        ],
    ),
    specs=[
        ("Sensing", "Inertial motion unit on the bike: lean, acceleration, braking and throttle behaviour"),
        ("Bike connection", "None. Does not touch the bike's electronics or ECU"),
        ("Compatibility", "Any motorcycle; confirmed per model before purchase"),
        ("Fitting", "Included in every pack, arranged with you"),
        ("Review delivery", "APEX app (iOS / Android) after each ride"),
        ("What's scored", "Braking, line, throttle, smoothness — per corner"),
        ("Road detection", "Road / mountain pass / track, automatic"),
        ("Included period", "12 months of reviews; no auto-renewal"),
        ("In the box", "APEX kit, mount, charging cable, quick start"),
    ],
    specs_note="Physical specifications (dimensions, weight, battery life, water resistance) are published with the first run.",
)

# ---- GUIDES -----------------------------------------------------------------
GUIDES = dict(
    title="APEX Guides — ride better, corner by corner",
    description="Straight answers to the questions riders actually ask: how to tell if you ride well, how to clean up a corner, what a course is worth, what telemetry measures, how to prepare for a track day.",
    hero=dict(eyebrow="Guides", h="Ride better, corner by corner.", p="Straight answers to the questions every rider actually asks. Filter by where you are today and by what you want to work on."),
    level_lbl="Rider level", topic_lbl="Topic", all_="All",
    levels=[("new", "New rider"), ("weekend", "Weekend rider"), ("experienced", "Experienced"), ("track", "Track day")],
    topics=[("self-assessment", "Self-assessment"), ("technique", "Technique"), ("data", "Data & telemetry"), ("coaching", "Coaching & courses"), ("track", "Track")],
    read="min read", by="APEX team", featured="Featured",
    end=dict(h="From reading to riding", p="The guides tell you what to look for. APEX measures it for you: every ride becomes a review, corner by corner, with one concrete thing to work on."),
    prev="Previous", next="Next", back="All guides", tip_k="APEX tip", share="Share",
)
GUIDE_META = {  # id -> (levels, tip)
    "how-to-know-if-you-ride-well": (["new", "weekend", "experienced"], "APEX scores braking, line, throttle and smoothness separately after every ride, so “do I ride well?” becomes four numbers and one priority."),
    "how-to-improve-cornering": (["new", "weekend", "experienced", "track"], "Every APEX review draws your line against the ideal and marks the braking point and throttle pick-up. The gap between the two lines is your lesson."),
    "motorcycle-telemetry-road": (["weekend", "experienced", "track"], "APEX doesn't touch the bike's electronics: an inertial unit reads lean, braking and throttle behaviour and the app turns it into a readable review."),
    "riding-coach-cost": (["new", "weekend"], "An APEX pack is the price of a single day's course, and it reviews every ride for twelve months."),
    "first-track-day-guide": (["weekend", "track"], "APEX Pro adds lap-by-lap analysis for track days: braking point per corner per lap, and a session comparison you can read in the paddock."),
}

# ---- FAQ --------------------------------------------------------------------
FAQ = dict(
    title="APEX FAQ — product, packs, buying, data",
    description="Everything riders ask about APEX: what it is, which pack to choose, how buying works, how your ride data is handled.",
    hero=dict(eyebrow="Help centre", h="Questions, answered.", p="If yours isn't here, write to us. A founder replies."),
    groups=[
        ("About APEX", [
            ("What is APEX, in one sentence?", "A kit that lives on your motorcycle and turns every ride into a corner-by-corner review on your phone: line, braking, throttle, and one thing to work on next time."),
            ("Is it an app I look at while riding?", "No. APEX shows nothing while you ride and asks nothing of you in the saddle. The review arrives after."),
            ("Does APEX work on my motorcycle?", "It is designed for any motorcycle. We confirm compatibility with your specific model when we contact you, before any payment."),
            ("Does it work on road and track?", "Yes. Road, mountain pass and track. Lap-by-lap analysis for track days is in the Pro pack."),
        ]),
        ("Packs & buying", [
            ("What exactly is included in the price?", "Every pack includes three things: the kit, fitting on your bike and 12 months of reviews. No monthly subscription, no hidden costs."),
            ("Who can buy APEX Start at €49.90?", "Riders under 25 or licensed for less than 12 months. Same kit and same reviews as the Rider pack."),
            ("How does payment work?", "There is no payment on the site. Fill in the early access form, we contact you, we confirm pack and bike together, and only then do we handle payment and delivery."),
            ("Is the early access price guaranteed?", "Yes. Requesting early access locks your pack price and your delivery priority on the first run, which is limited."),
            ("When will APEX Pro be available?", "APEX Pro (€179.90, track and track days) opens for pre-order soon. Leave your details in the early access form to be notified."),
            ("What happens after the 12 included months?", "No automatic renewal: we don't store payment methods. Before the end we present your options and you decide."),
        ]),
        ("Using APEX", [
            ("How long does a review take to read?", "About two minutes. It opens on the one thing to work on; the corner-by-corner detail is there if you want it."),
            ("Do I need to charge it every ride?", "No. The kit wakes when you ride and sleeps when you stop. Charging intervals are published with the first run."),
            ("Can I use it on more than one bike?", "The kit is fitted to one bike. Moving it to another is possible; write to us and we'll arrange it."),
        ]),
        ("Your data", [
            ("Who can see my reviews?", "Only you. No mandatory public leaderboard, no score visible to others."),
            ("What data does APEX collect?", "Motion data from the kit, GPS from your phone during the ride, and your account details. See the privacy notice for retention and your rights."),
            ("Can I delete my data?", "Yes, at any time, from the app or by writing to us."),
        ]),
    ],
)

# ---- CONTACT ----------------------------------------------------------------
CONTACT = dict(
    title="Contact APEX",
    description="Questions about the product, the packs or your bike: one email and a founder replies.",
    hero=dict(eyebrow="Contact", h="One email. A founder replies.", p="We're a small team in Milan and we read everything."),
    items=[
        ("Support & questions", "Product, packs, your bike, your order.", "hello@apex-rider.com"),
        ("Instructors & schools", "Pro deals, partnerships, demo days.", "hello@apex-rider.com"),
        ("Press & investors", "Material, interviews, the story.", "hello@apex-rider.com"),
    ],
    hours="We reply within two working days, usually faster.",
    faq_link="Many answers are already in the FAQ",
)

# ---- OUR STORY --------------------------------------------------------------
STORY = dict(
    title="Our story — why we built APEX",
    description="Thousands of hours on the bike, zero reviews. How three riders in Milan set out to give every rider what every other athlete already has.",
    hero=dict(eyebrow="Our story", h="Thousands of hours on the bike. Zero reviews.", p="Every athlete gets structured feedback on their game. Riders finish the session, get off the bike, and often have no idea what they did right or wrong. That gap is why APEX exists."),
    body=[
        ("The gap", "A chess player gets a game review. A tennis player replays the match. A footballer has video analysis on Monday. A rider gets off the bike, and that's it. The only feedback is a course once a year, or the feeling in the saddle — which can't tell a braking point ten metres early from a perfect one."),
        ("The idea", "What if the review just happened? No screen to watch, no app to fiddle with, no data to interpret. A kit that lives on the bike, reads how you ride, and hands you two minutes of clear feedback when the helmet comes off: what worked, what to fix, one thing to work on."),
        ("The way we build it", "One price, everything included, no subscription surprises. No leaderboard. No judgement. A review that starts from what you already do well, because that's how real coaches work — and because riders who feel judged stop listening."),
    ],
    founders_h="The founders",
    founders=[("Federico", "Co-founder"), ("Niccolò Bua Odetti", "Co-founder"), ("Giuseppe Pisante", "Co-founder")],
    where="APEX Srl is based in Milan, Italy.",
    milestones_h="Milestones",
    milestones=[],   # [("2025", "Title", "Text")]
)

# ---- PRO --------------------------------------------------------------------
PRO = dict(
    title="APEX for instructors & riding schools",
    description="Give every student a corner-by-corner review between lessons. Pro deals for instructors, schools, track day organisers and clubs.",
    hero=dict(eyebrow="APEX Pro deal", h="Your coaching, every ride your student takes.", p="A course gives a rider feedback once. APEX keeps giving it between lessons, in your language: braking point, line, throttle, one priority. Built for instructors, schools, track day organisers and clubs."),
    who_h="Who it's for",
    who=[("Riding instructors", "Independent or in a school"), ("Riding schools & academies", "Road and advanced courses"), ("Track day organisers", "Paddock coaching, groups"), ("Clubs & communities", "Group rides with a purpose")],
    benefits_h="What you get",
    benefits=[
        ("Pro pricing", "Preferential pricing on kits for you and for your students."),
        ("Referral", "A code for your riders; you see who joined and what they're working on (with their consent)."),
        ("Demo days", "We come to you with kits for a day of fitted, reviewed rides."),
        ("A voice in the product", "Pro users shape what the review says. We build with you, not at you."),
    ],
    btn="Apply for a Pro deal", note="Applications open with the first run. Write to us with who you are and what you teach.",
)

# ---- EARLY ACCESS -----------------------------------------------------------
EARLY = dict(
    title="Request early access — APEX",
    description="Thirty seconds, six fields, no payment now. We contact you to confirm your pack and your bike.",
    hero=dict(eyebrow="Early access · first-run spots", h="Request early access.", p="Thirty seconds, no payment now. We contact you to confirm your pack, check compatibility with your bike and handle the order. Your early access price stays locked."),
    f=dict(name="Name", email="Email", pack="Which pack?", pack_ph="Choose a pack",
           packs=[("Start €49,90", "APEX Start — €49.90 (under 25 / licence < 12 months)"), ("Rider €89,90", "APEX Rider — €89.90"), ("Pro €179,90 (notify)", "APEX Pro — €179.90 (notify me at pre-order)")],
           bike="What do you ride?", bike_ph="e.g. Yamaha MT-07, 2021",
           usage="How do you ride most?", usage_ph="Pick one",
           usages=[("road-weekend", "Weekend / mountain roads"), ("commuting", "Everyday / commuting"), ("track", "Track days"), ("mixed", "A bit of everything")],
           consent="I agree to being contacted by APEX about my early access request", consent_link="privacy notice",
           btn="Request early access", note="No payment now. We'll contact you to confirm your pack and handle the order."),
    ok=dict(h="You're on the list.", p="Thanks for raising your hand. We roll out the first run in small waves and we'll email you the moment a spot opens for how and where you ride."),
    steps=[("Fill in the form", "Thirty seconds."), ("We write to you", "Pack details, timing, your questions."), ("Payment and delivery", "Agreed together, after we confirm your bike.")],
    direct_h="Prefer to write to us directly?", direct_p="Questions about the product, the packs or your bike: one email and we reply ourselves.",
)

# ---- LEGAL (drafts — see notice) -------------------------------------------
LEGAL_NOTICE = "Draft. This page is a structure for APEX's legal text and must be reviewed by counsel before publication."
LEGAL = {
    "terms": dict(title="Terms of service — APEX", h="Terms of service", updated="Last updated: to be set at publication", sections=[
        ("1. Who we are", "APEX Srl, Milan, Italy (“APEX”, “we”). These terms govern the APEX website, the APEX kit and the APEX app."),
        ("2. Eligibility", "You must hold a valid motorcycle licence and be of legal age to purchase. APEX Start is reserved for riders under 25 or licensed for less than 12 months; eligibility is confirmed before purchase."),
        ("3. Riding safety", "APEX provides feedback after the ride and is not a safety device. You remain solely responsible for how you ride and for complying with the law. Never interact with your phone while riding."),
        ("4. Early access and purchase", "Requesting early access is not a purchase. Price and delivery priority are locked at the time of request. Payment is agreed after we confirm compatibility with your motorcycle."),
        ("5. Included period", "Each pack includes 12 months of reviews from activation. There is no automatic renewal and we do not store payment methods."),
        ("6. Liability", "To the extent permitted by law, APEX's liability is limited to the price paid for the pack."),
        ("7. Disputes", "These terms are governed by Italian law. The courts of Milan have jurisdiction, without prejudice to mandatory consumer protections."),
    ]),
    "privacy": dict(title="Privacy notice — APEX", h="Privacy notice", updated="Last updated: to be set at publication", sections=[
        ("1. Data controller", "APEX Srl, Milan, Italy. Contact: hello@apex-rider.com."),
        ("2. Data we collect", "Account details (name, email); early access form data (pack, motorcycle, riding habits); motion data from the kit; GPS data from your phone during rides; app usage data."),
        ("3. Why", "To provide the review service, to contact you about your early access request, to improve the analysis models, and to meet legal obligations."),
        ("4. AI processing", "Ride data is processed by APEX's models to produce reviews. Data used to improve models is pseudonymised."),
        ("5. Sharing", "We use processors for hosting, email delivery and analytics under data processing agreements. We do not sell your data. Reviews are private to you."),
        ("6. Retention", "Early access requests are kept until the first run is fulfilled or you ask us to delete them. Ride data is kept while your account is active."),
        ("7. Your rights", "Access, rectification, erasure, portability, objection, and complaint to the Garante per la protezione dei dati personali. Write to hello@apex-rider.com."),
    ]),
    "warranty": dict(title="Warranty — APEX", h="Warranty", updated="Last updated: to be set at publication", sections=[
        ("Hardware", "The APEX kit is covered by the statutory two-year legal guarantee for consumers in the EU."),
        ("What's covered", "Manufacturing defects and failures under normal use."),
        ("What's not", "Damage from crashes, improper fitting not carried out by APEX or its partners, water ingress beyond the stated rating, or modification of the kit."),
        ("How to claim", "Write to hello@apex-rider.com with your order details and a description of the issue."),
    ]),
    "returns": dict(title="Returns — APEX", h="Returns", updated="Last updated: to be set at publication", sections=[
        ("Right of withdrawal", "As an EU consumer you may withdraw within 14 days of delivery without giving a reason. The kit must be returned complete and undamaged."),
        ("Pre-orders", "Pre-orders can be cancelled for a full refund at any time before shipment."),
        ("Refund process", "Write to hello@apex-rider.com. Refunds are issued to the original payment method within 14 days of receiving the return."),
    ]),
}
