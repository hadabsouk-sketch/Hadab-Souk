"""Product catalog for Hadab Souk."""

CATEGORIES = [
    {"slug": "smartphones", "name_en": "Smartphones", "name_ar": "الهواتف الذكية", "icon": "📱"},
    {"slug": "laptops", "name_en": "Laptops", "name_ar": "أجهزة اللابتوب", "icon": "💻"},
    {"slug": "tablets", "name_en": "Tablets", "name_ar": "الأجهزة اللوحية", "icon": "📲"},
    {"slug": "smartwatches", "name_en": "Smart Watches", "name_ar": "الساعات الذكية", "icon": "⌚"},
    {"slug": "accessories", "name_en": "Accessories", "name_ar": "الإكسسوارات", "icon": "🎧"},
    {"slug": "gaming", "name_en": "Gaming", "name_ar": "الألعاب", "icon": "🎮"},
    {"slug": "cameras", "name_en": "Cameras", "name_ar": "الكاميرات", "icon": "📷"},
    {"slug": "appliances", "name_en": "Home Appliances", "name_ar": "الأجهزة المنزلية", "icon": "🏠"},
]


def _img(uid, w=800):
    return f"https://images.unsplash.com/{uid}?auto=format&fit=crop&w={w}&q=80"


PRODUCTS = [
    {
        "id": "p1", "slug": "iphone-15-pro-max",
        "name_en": "iPhone 15 Pro Max 256GB", "name_ar": "آيفون 15 برو ماكس 256 جيجا",
        "brand": "Apple", "category": "smartphones", "price": 4799, "old_price": 5499,
        "rating": 4.9, "reviews": 1284, "badge": "hot",
        "image": _img("photo-1696446702183-cbd13d4d4ac8"),
        "desc_en": "Titanium design, A17 Pro chip, breakthrough camera system.",
        "desc_ar": "تصميم تيتانيوم، شريحة A17 Pro، نظام كاميرا متطور.",
        "featured": True, "best_seller": True,
    },
    {
        "id": "p2", "slug": "samsung-galaxy-s24-ultra",
        "name_en": "Samsung Galaxy S24 Ultra", "name_ar": "سامسونج جالاكسي S24 الترا",
        "brand": "Samsung", "category": "smartphones", "price": 4299, "old_price": 4999,
        "rating": 4.8, "reviews": 892, "badge": "deal",
        "image": _img("photo-1610945265064-0e34e5519bbf"),
        "desc_en": "Galaxy AI, 200MP camera, titanium frame, S Pen included.",
        "desc_ar": "ذكاء اصطناعي، كاميرا 200 ميجا، إطار تيتانيوم.",
        "featured": True, "best_seller": True,
    },
    {
        "id": "p3", "slug": "macbook-pro-14-m3",
        "name_en": 'MacBook Pro 14" M3', "name_ar": "ماك بوك برو 14 إنش M3",
        "brand": "Apple", "category": "laptops", "price": 7499, "old_price": 7999,
        "rating": 4.9, "reviews": 421, "badge": "top",
        "image": _img("photo-1517336714731-489689fd1ca8"),
        "desc_en": "M3 chip, Liquid Retina XDR display, all-day battery.",
        "desc_ar": "شريحة M3، شاشة Liquid Retina XDR.",
        "featured": True, "best_seller": True,
    },
    {
        "id": "p4", "slug": "dell-xps-15",
        "name_en": "Dell XPS 15 OLED", "name_ar": "ديل XPS 15 OLED",
        "brand": "Dell", "category": "laptops", "price": 6299, "old_price": None,
        "rating": 4.6, "reviews": 256, "badge": None,
        "image": _img("photo-1593642632559-0c6d3fc62b89"),
        "desc_en": "Intel Core i9, RTX 4070, stunning OLED display.",
        "desc_ar": "معالج i9، كرت RTX 4070، شاشة OLED.",
    },
    {
        "id": "p5", "slug": "ipad-pro-m4",
        "name_en": 'iPad Pro 13" M4', "name_ar": "آيباد برو 13 إنش M4",
        "brand": "Apple", "category": "tablets", "price": 5199, "old_price": 5799,
        "rating": 4.8, "reviews": 312, "badge": "new",
        "image": _img("photo-1561154464-82e9adf32764"),
        "desc_en": "Tandem OLED, M4 chip, thinnest iPad ever.",
        "desc_ar": "شاشة OLED مزدوجة، شريحة M4.",
        "featured": True,
    },
    {
        "id": "p6", "slug": "galaxy-tab-s9",
        "name_en": "Galaxy Tab S9+", "name_ar": "جالاكسي تاب S9+",
        "brand": "Samsung", "category": "tablets", "price": 3299, "old_price": None,
        "rating": 4.5, "reviews": 188, "badge": None,
        "image": _img("photo-1585790050230-5dd28404ccb9"),
        "desc_en": "12.4\" AMOLED, IP68 water resistant, S Pen included.",
        "desc_ar": "شاشة AMOLED مقاومة للماء IP68.",
    },
    {
        "id": "p7", "slug": "apple-watch-ultra-2",
        "name_en": "Apple Watch Ultra 2", "name_ar": "ساعة آبل ألترا 2",
        "brand": "Apple", "category": "smartwatches", "price": 3199, "old_price": 3499,
        "rating": 4.9, "reviews": 642, "badge": "hot",
        "image": _img("photo-1551816230-ef5deaed4a26"),
        "desc_en": "Most rugged Apple Watch. 49mm titanium case, 36-hour battery.",
        "desc_ar": "الأقوى من آبل. إطار تيتانيوم 49ملم.",
        "featured": True, "best_seller": True,
    },
    {
        "id": "p8", "slug": "galaxy-watch-6-classic",
        "name_en": "Galaxy Watch 6 Classic", "name_ar": "جالاكسي ووتش 6 كلاسيك",
        "brand": "Samsung", "category": "smartwatches", "price": 1499, "old_price": 1799,
        "rating": 4.6, "reviews": 318, "badge": None,
        "image": _img("photo-1617043786394-f977fa12eddf"),
        "desc_en": "Rotating bezel returns. Advanced health tracking.",
        "desc_ar": "إطار دوّار. تتبع صحي متقدم.",
    },
    {
        "id": "p9", "slug": "airpods-pro-2",
        "name_en": "AirPods Pro (2nd Gen) USB-C", "name_ar": "إيربودز برو الجيل الثاني",
        "brand": "Apple", "category": "accessories", "price": 949, "old_price": 1099,
        "rating": 4.8, "reviews": 2114, "badge": "hot",
        "image": _img("photo-1606220588913-b3aacb4d2f46"),
        "desc_en": "Adaptive Audio, USB-C MagSafe case, double battery life.",
        "desc_ar": "صوت تكيفي، علبة MagSafe بـ USB-C.",
        "best_seller": True,
    },
    {
        "id": "p10", "slug": "sony-wh1000xm5",
        "name_en": "Sony WH-1000XM5", "name_ar": "سوني WH-1000XM5",
        "brand": "Sony", "category": "accessories", "price": 1399, "old_price": 1599,
        "rating": 4.8, "reviews": 1422, "badge": None,
        "image": _img("photo-1583394838336-acd977736f90"),
        "desc_en": "Industry-leading noise cancellation, 30-hour battery.",
        "desc_ar": "أفضل عزل للضوضاء، بطارية 30 ساعة.",
        "featured": True,
    },
    {
        "id": "p11", "slug": "playstation-5-slim",
        "name_en": "PlayStation 5 Slim", "name_ar": "بلايستيشن 5 سليم",
        "brand": "Sony", "category": "gaming", "price": 2199, "old_price": None,
        "rating": 4.9, "reviews": 988, "badge": "top",
        "image": _img("photo-1606813907291-d86efa9b94db"),
        "desc_en": "Slimmer design, 1TB SSD, 4K HDR gaming.",
        "desc_ar": "تصميم نحيف، تخزين 1TB.",
        "best_seller": True,
    },
    {
        "id": "p12", "slug": "xbox-series-x",
        "name_en": "Xbox Series X", "name_ar": "إكس بوكس سيريس X",
        "brand": "Microsoft", "category": "gaming", "price": 2099, "old_price": None,
        "rating": 4.8, "reviews": 624, "badge": None,
        "image": _img("photo-1621259182978-fbf93132d53d"),
        "desc_en": "True 4K, 120 FPS, Quick Resume.",
        "desc_ar": "دقة 4K حقيقية، 120 إطار/ث.",
    },
    {
        "id": "p13", "slug": "canon-r6-mark-ii",
        "name_en": "Canon EOS R6 Mark II", "name_ar": "كانون EOS R6 مارك II",
        "brand": "Canon", "category": "cameras", "price": 9899, "old_price": None,
        "rating": 4.9, "reviews": 142, "badge": "top",
        "image": _img("photo-1502920917128-1aa500764cbd"),
        "desc_en": "Full-frame mirrorless, 24MP, 40fps electronic shutter.",
        "desc_ar": "كاميرا كاملة الإطار، 24 ميجا.",
    },
    {
        "id": "p14", "slug": "dji-mini-4-pro",
        "name_en": "DJI Mini 4 Pro Drone", "name_ar": "درون DJI ميني 4 برو",
        "brand": "DJI", "category": "cameras", "price": 3499, "old_price": 3799,
        "rating": 4.7, "reviews": 287, "badge": None,
        "image": _img("photo-1473968512647-3e447244af8f"),
        "desc_en": "Under 249g, 4K/100fps HDR, omnidirectional sensing.",
        "desc_ar": "أقل من 249 جرام، تصوير 4K HDR.",
        "featured": True,
    },
    {
        "id": "p15", "slug": "dyson-v15-detect",
        "name_en": "Dyson V15 Detect Vacuum", "name_ar": "مكنسة دايسون V15 ديتكت",
        "brand": "Dyson", "category": "appliances", "price": 2799, "old_price": 3199,
        "rating": 4.7, "reviews": 519, "badge": "deal",
        "image": _img("photo-1558317374-067fb5f30001"),
        "desc_en": "Laser dust detection, 60-min runtime, LCD screen.",
        "desc_ar": "كشف الغبار بالليزر، 60 دقيقة.",
    },
    {
        "id": "p16", "slug": "samsung-bespoke-fridge",
        "name_en": "Samsung Bespoke Smart Fridge", "name_ar": "ثلاجة سامسونج Bespoke الذكية",
        "brand": "Samsung", "category": "appliances", "price": 8999, "old_price": None,
        "rating": 4.5, "reviews": 96, "badge": None,
        "image": _img("photo-1571175443880-49e1d25b2bc5"),
        "desc_en": "Family Hub, customizable panels, AI-powered cooling.",
        "desc_ar": "Family Hub، ألواح قابلة للتخصيص، تبريد ذكي.",
    },
]


def get_product(slug):
    return next((p for p in PRODUCTS if p["slug"] == slug), None)


def get_category(slug):
    return next((c for c in CATEGORIES if c["slug"] == slug), None)


def by_category(slug):
    return [p for p in PRODUCTS if p["category"] == slug]


def related(product, n=4):
    return [p for p in PRODUCTS if p["category"] == product["category"] and p["id"] != product["id"]][:n]
