from app.models import db, Tag


def seed_tags():
    acai_bowls = Tag(tag='Acai Bowls')
    bagels = Tag(tag='Bagels')
    bakeries = Tag(tag='Bakeries')
    beer_wine_spirits = Tag(tag='Beer, Wine & Spirits')
    breweries = Tag(tag='Breweries')
    bubble_tea = Tag(tag='Bubble Tea')
    butcher = Tag(tag='Butcher')
    coffee_tea = Tag(tag='Coffee & Tea')
    convenience_store = Tag(tag='Convenience Store')
    delicatessen = Tag(tag='Delicatessen')
    desserts = Tag(tag='Desserts')
    donuts = Tag(tag='Donuts')
    farmers_market = Tag(tag='Famers Market')
    food_deliever_services = Tag(tag='Food Delivery Services')
    food_trucks = Tag(tag='Food Trucks')
    gelato = Tag(tag='Gelato')
    grocery = Tag(tag='Grocery')
    honey = Tag(tag='Honey')
    ice_cream_frozen_yogurt = Tag(tag='Ice Cream & Frozen Yogurt')
    internet_cafes = Tag(tag='Internet Cafes')
    juice_bars_smoothies = Tag(tag='Juice Bars & Smoothies')
    poke = Tag(tag='Poke')
    shaved_ice = Tag(tag='Shaved Ice')
    tortillas = Tag(tag='Tortillas')
    afghan = Tag(tag='Afghan')
    african = Tag(tag='African')
    american = Tag(tag='American')
    asian_fusion = Tag(tag='Asian Fusion')
    barbeque = Tag(tag='Barbeque')
    bistros = Tag(tag='Bistros')
    brazillian = Tag(tag='Brazillian')
    breakfast_brunch = Tag(tag='Breakfast & Brunch')
    buffets = Tag(tag='Buffets')
    burgers = Tag(tag='Burgers')
    cafes = Tag(tag='Cafes')
    cajun_creole = Tag(tag='Cajun/Creole')
    caribbean = Tag(tag='Caribbean')
    chicken_wings = Tag(tag='Chicken Wings')
    chinese = Tag(tag='Chinese')
    comfort_food = Tag(tag='Comfort Food')
    cuban = Tag(tag='Cuban')
    danish = Tag(tag='Danish')
    diners = Tag(tag='Diners')
    dim_sum = Tag(tag='Dim Sum')
    dumplings = Tag(tag='Dumplings')
    eastern_european = Tag(tag='Eastern European')
    filipino = Tag(tag='Filipino')
    fish_chips = Tag(tag='Fish & Chips')
    food_court = Tag(tag='Food Court')
    french = Tag(tag='French')
    gastropubs = Tag(tag='Gastropubs')
    german = Tag(tag='German')
    gluten_free = Tag(tag='Gluten-Free')
    greek = Tag(tag='Greek')
    halal = Tag(tag='Halal')
    hawaiian = Tag(tag='Hawaiian')
    hong_kong_style_cafe = Tag(tag='Hong Kong Style Cafe')
    fast_food = Tag(tag='Fast Food')
    hot_pot = Tag(tag='Hot Pot')
    indian = Tag(tag='Indian')
    italian = Tag(tag='Italian')
    japanese = Tag(tag='Japanese')
    kebab = Tag(tag='Kebab')
    korean = Tag(tag='Korean')
    kosher = Tag(tag='Kosher')
    raw_food = Tag(tag='Raw Food')
    mediterranean = Tag(tag='Mediterranean')
    mexican = Tag(tag='Mexican')
    middle_eastern = Tag(tag='Middle Eastern')
    noodles = Tag(tag='Noodles')
    pizza = Tag(tag='Pizza')
    salad = Tag(tag='Salad')
    seafood = Tag(tag='Seafood')
    soul_food = Tag(tag='Soul Food')
    soup = Tag(tag='Soup')
    steakhouse = Tag(tag='Steakhouse')
    sushi = Tag(tag='Sushi')
    tapas = Tag(tag='Tapas')
    fusion = Tag(tag='Fusion')
    thai = Tag(tag='Thai')
    vegan = Tag(tag='Vegan')
    vegetarian = Tag(tag='Vegetarian')
    vietnamese = Tag(tag='Vietnamese')

    db.session.add(acai_bowls)
    db.session.add(bagels)
    db.session.add(bakeries)
    db.session.add(beer_wine_spirits)
    db.session.add(breweries)
    db.session.add(bubble_tea)
    db.session.add(butcher)
    db.session.add(coffee_tea)
    db.session.add(convenience_store)
    db.session.add(delicatessen)
    db.session.add(desserts)
    db.session.add(donuts)
    db.session.add(farmers_market)
    db.session.add(food_deliever_services)
    db.session.add(food_trucks)
    db.session.add(gelato)
    db.session.add(grocery)
    db.session.add(honey)
    db.session.add(ice_cream_frozen_yogurt)
    db.session.add(internet_cafes)
    db.session.add(juice_bars_smoothies)
    db.session.add(poke)
    db.session.add(shaved_ice)
    db.session.add(tortillas)
    db.session.add(afghan)
    db.session.add(african)
    db.session.add(american)
    db.session.add(asian_fusion)
    db.session.add(barbeque)
    db.session.add(bistros)
    db.session.add(brazillian)
    db.session.add(breakfast_brunch)
    db.session.add(buffets)
    db.session.add(burgers)
    db.session.add(cafes)
    db.session.add(cajun_creole)
    db.session.add(caribbean)
    db.session.add(chicken_wings)
    db.session.add(chinese)
    db.session.add(comfort_food)
    db.session.add(cuban)
    db.session.add(danish)
    db.session.add(diners)
    db.session.add(dim_sum)
    db.session.add(dumplings)
    db.session.add(eastern_european)
    db.session.add(filipino)
    db.session.add(fish_chips)
    db.session.add(food_court)
    db.session.add(french)
    db.session.add(gastropubs)
    db.session.add(german)
    db.session.add(gluten_free)
    db.session.add(greek)
    db.session.add(halal)
    db.session.add(hawaiian)
    db.session.add(hong_kong_style_cafe)
    db.session.add(fast_food)
    db.session.add(hot_pot)
    db.session.add(indian)
    db.session.add(italian)
    db.session.add(japanese)
    db.session.add(kebab)
    db.session.add(korean)
    db.session.add(kosher)
    db.session.add(raw_food)
    db.session.add(mediterranean)
    db.session.add(mexican)
    db.session.add(middle_eastern)
    db.session.add(noodles)
    db.session.add(pizza)
    db.session.add(salad)
    db.session.add(seafood)
    db.session.add(soul_food)
    db.session.add(soup)
    db.session.add(steakhouse)
    db.session.add(sushi)
    db.session.add(tapas)
    db.session.add(fusion)
    db.session.add(thai)
    db.session.add(vegan)
    db.session.add(vegetarian)
    db.session.add(vietnamese)
    db.session.commit()


def undo_tags():
    db.session.execute('TRUNCATE tags RESTART IDENTITY CASCADE;')
    db.session.commit()