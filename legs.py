# -*- coding: utf-8 -*-
# The eight journeys. Nothing else — the stays are not legs, they are just
# the gaps in between, and the app is for working out what goes in which bag
# on the days you actually move.
#
# Each leg holds a list of bags. Every bag has a mode, which is what the sash
# on the tile says and the only thing that really matters at the airport:
#
#   cabin    comes on board with you
#   checked  goes in the hold
#   with     surface leg, no airline — it is simply with you
#   worn     on your body, not in a bag
#   left     not on this leg at all (in storage, or handed over)
#
# key=1     a leg where the bags genuinely change hands
# stored=1  the suitcases are in Smilelugg for this leg, so anything with
#           fate="store" is filtered out of the available pool.


def P(n, note="", add=False):
    d = dict(n=n)
    if note:
        d["note"] = note
    if add:
        d["add"] = True
    return d


def B(bag, mode, items, note=""):
    return dict(bag=bag, mode=mode, items=items, note=note)


LEGS = [
    dict(
        id="lon-per",
        name="London – Perth",
        dates="19–20 Nov",
        where="LGW → DOH → PER",
        via="QR 330 · QR 900 · Qatar Business",
        key=1,
        note=(
            "About 26 hours door to door, and it starts at the Gatwick hotel on the 18th — "
            "so the cabin bag has to cover that night without opening a suitcase. Qatar "
            "Business gives you 40 kg checked and two cabin pieces at 15 kg plus a personal "
            "item, so all three carry-ons travel with you. Qsuite: pyjamas and bedding provided."
        ),
        do=[
            P("Erase the MacBook Pro and iPad mini", "Sign out of your Apple ID, erase, remove from Find My. An activation-locked device is useless to whoever gets it, and doing this on Phuket hotel wifi with someone waiting is miserable."),
            P("Collect the Sainsbury's travel money", "Order STM30429677 — THB 25,000 and AUD 200, £707.30, already paid. Count it at the counter."),
            P("Buy the small dry bag and the goggles", "The last two outstanding items."),
            P("Check passport validity", "Six months beyond 24 Jan 2027."),
            P("Download offline maps", "Perth, Bangkok, Samui, Krabi. Plus WhatsApp, Line, GetYourGuide and Bolt on your apps page."),
            P("AirTags in both cases", "They sit in third-party storage for 13 days later on."),
        ],
        bags=[
            B("SL", "cabin", [
                P("Passport holder"), P("Wallet and cards"),
                P("Cash", "GBP float plus the Sainsbury's order: THB 25,000 and AUD 200. Split the baht between the sling and a case — not 25,000 in one pocket. Nothing to declare at either end."),
                P("Phone"), P("Sunglasses — daily pair"), P("AirPods Pro"),
                P("Fold-up 3-in-1 charger"), P("Extendable USB-C cable"),
                P("Mini charger brick", "Cabin only, never checked."),
                P("Earplugs"), P("Eye mask"), P("Mouth tape"),
                P("Prescription medication", "Hand luggage, original packaging."),
                P("Clear 1L liquids bag", "Cleared twice — Gatwick and Doha."),
            ], "Everything you cannot replace. It never leaves you."),
            B("BP", "cabin", [
                P("iPad Air", "The main one, not the one being handed over in Phuket."),
                P("Sony over-ear headphones", "The flight you bought them for."),
                P("USB-C dongle"), P("HDMI cable"),
                P("Compression socks", "Worth it on a 26-hour door to door."),
                P("Larq bottle, empty", "Fill it after security."),
            ], "The in-flight bag. Under the seat, not in the bin."),
            B("CB", "cabin", [
                P("Mini washbag", "Electric toothbrush, mini toothpaste, travel face wash, roll-on deodorant, aftershave atomiser. Covers the Gatwick night and the Doha spa at 23:30."),
                P("Electric shaver and its cable", "Cabin, not hold — lithium batteries belong in the cabin anyway, and you land in Perth at 18:45 after 26 hours."),
                P("Mini shaving foam", "Under 100 ml, so it travels in the clear liquids bag."),
                P("Moisturiser", "Three long-haul sectors of dry cabin air, and a shave at the end of it."),
                P("2 boxers, 2 socks, 2 T-shirts"),
                P("1 gym top, 1 gym shorts, 1 gym socks"),
                P("1 swim shorts"), P("Running shoes"), P("MacBook Air"),
            ], "This bag alone has to get you through the Gatwick night."),
            B("L1", "checked", [
                P("The clothing bulk", "Shirts, tees, shorts, trousers, boxers, socks — seven weeks of Perth."),
                P("Hoodie and tracksuit bottoms", "Not worn. You want them for the flight home, not this one."),
                P("Windbreaker"), P("Travel adapter"),
                P("4-pair sunglasses case"), P("Sliders, sandals, old trainers"),
            ]),
            B("L2", "checked", [
                P("Full-size toiletries and the big washbag"),
                P("Towels"),
                P("MacBook Pro and iPad mini", "For the Phuket handover. Already erased and signed out."),
                P("Switch, PS5 controller and the HDMI cable"),
                P("Room left deliberately", "You are buying suncream, protein powder and the rest in Perth."),
            ]),
            B("worn", "worn", [
                P("Nice trainers", "Wear the bulkiest footwear rather than packing it."),
                P("T-shirt and light trousers", "Qatar hand you pyjamas, so do not overthink this."),
            ]),
        ],
    ),
    dict(
        id="per-hkt",
        name="Perth – Phuket",
        dates="7 Jan",
        where="PER → HKT",
        via="JQ 71 · Jetstar · 07:25",
        key=1,
        note=(
            "Very early start from Scarborough. You have 40 kg of hold baggage prepaid across "
            "as many bags as you like, so check all three — both cases AND the cabin bag — and "
            "walk on with just the backpack and sling. Jetstar cabin is two items, 7 kg combined, "
            "and they weigh it at the gate."
        ),
        do=[
            P("Pack the night of the 5th", "Not the morning of the 7th. The flight is at 07:25."),
            P("Pre-pack the three cubes", "Cube 1 clothing, Cube 2 gym and footwear, Cube 3 kit. This is what makes the Phuket repack ten minutes instead of an hour."),
            P("Spend or leave the AUD", "Australia is behind you. Any Australian cash is dead weight from here."),
        ],
        bags=[
            B("SL", "cabin", [
                P("Passport, phone, cards, daily sunglasses, AirPods, mini charger brick"),
                P("The baht", "All three bags are checked on this leg. Cash does not go in the hold."),
                P("Prescriptions and the liquids bag", "Never in the hold."),
            ]),
            B("BP", "cabin", [
                P("iPad Air, chargers, Larq"),
                P("Anything you want in the air", "Five and a half hours, no seat-back entertainment worth the name."),
            ]),
            B("CB", "checked", [
                P("Packed as normal", "It goes in the hold here — there is nothing in it you need for five hours, and the prepaid 40 kg covers it."),
            ], "In the hold on this leg only."),
            B("L1", "checked", [P("Cubes 1, 2 and 3 near the top", "You open this case once, in Phuket, and you want the cubes to be the first thing you see.")]),
            B("L2", "checked", [P("Everything else"), P("The Perth surplus", "Whatever you bought and are keeping.")]),
            B("worn", "worn", [P("Trainers and a layer", "The plane is cold, Phuket is not.")]),
        ],
    ),
    dict(
        id="hkt-bkk",
        name="Phuket – Bangkok",
        dates="10 Jan",
        where="HKT → BKK",
        via="TG 206 · Thai Airways · 11:50",
        key=1,
        stored=1,
        note=(
            "The tightest leg of the trip. Thai Economy gives you ONE cabin piece at 7 kg, and "
            "both checked allowances are taken by the suitcases — so the cabin bag has to come "
            "down under 7 kg before you leave the Courtyard. Land 13:20, then straight to "
            "Smilelugg on B Floor: lift the three cubes out of the cases into the cabin bag, "
            "lock the cases, hand them over. Ref 14XIWBX4, paid, 10–23 Jan."
        ),
        do=[
            P("Hand over the MacBook Pro and iPad mini", "Early in the three days, not on the morning you leave."),
            P("Decant the suncream", "Fill the 100 ml bottles before the full-size goes into storage for a fortnight."),
            P("Weigh the cabin bag before you leave the room", "Under 7 kg. The only number that matters today."),
            P("Photograph the Smilelugg receipt", "Your taxi waits 45 minutes, so this is not a rush."),
        ],
        bags=[
            B("SL", "cabin", [P("As always", "Passport, phone, cards, cash, sunglasses, prescriptions, liquids.")]),
            B("BP", "cabin", [P("Your personal item", "Thai allow a handbag under 1.5 kg alongside the one cabin piece. Keep it genuinely small today.")]),
            B("CB", "cabin", [
                P("Toiletries — both mini washbags and the decant bottles", "About 1.3 kg."),
                P("Full health kit", "About 0.5 kg."),
                P("iPad Air, chargers, power bank, shaver and cable", "About 1.7 kg."),
                P("One change of clothes", "Insurance only — you are back into the cases three hours later."),
                P("TARGET: under 7 kg", "Weigh it. Everything else waits in the cubes."),
            ], "Has to be under 7 kg to board. Then it swallows the cubes at BKK."),
            B("L1", "checked", [
                P("CUBE 1 — clothing", "5 tees, 3 shorts, 2 nice shirts, 1 trousers, 5 boxers, 3 socks, 2 swim shorts. About 4 kg."),
                P("CUBE 2 — gym and footwear", "Gym top, shorts, socks, running shoes, sandals, sliders. About 2.5 kg. Shoes in a bin bag inside the cube."),
                P("CUBE 3 — kit", "Mini towel, dry bag, laundry and bin bags, goggles, daypack, locks. About 1.4 kg."),
                P("Larq bottle, loose", "Too awkward for a cube. Keep it near the top with them."),
            ], "Checked to BKK, then straight into storage — but the cubes come out first."),
            B("L2", "checked", [
                P("Staying behind for 13 days", "MacBook Air and its kit, Sony over-ears, Switch, PS5 pad, 4-pair sunglasses case, the Perth clothing surplus, old trainers, hoodie, tracksuit, large washbag, full-size suncream, large towel, driving licence. About 9 kg between the two cases."),
            ], "Checked to BKK, then locked and left at Smilelugg."),
        ],
    ),
    dict(
        id="bkk-usm",
        name="Bangkok – Koh Samui",
        dates="13 Jan",
        where="BKK → USM",
        via="PG 133 · Bangkok Airways",
        stored=1,
        note=(
            "Bangkok Airways allow only 5 kg in the cabin, but 20 kg checked is included — so "
            "the cabin bag goes in the hold on this one and you keep the backpack and sling. "
            "Leave Theatre Residence by 08:00: check-out is 12:00 but PG 133 does not wait."
        ),
        do=[
            P("Buy DEET before you leave Bangkok", "Stronger and cheaper here than anything you would have carried from home."),
            P("Take a motion sickness tablet the night before the 17th", "Not for this flight — for the 06:00 Donsak ferry four days later. Easy to forget once you are on the beach."),
        ],
        bags=[
            B("SL", "cabin", [P("As always")]),
            B("BP", "cabin", [P("Day kit", "Dry bag, mini towel, daily sunglasses, suncream, Larq."), P("iPad and chargers", "The cabin bag is in the hold, so anything you want on the way travels here.")]),
            B("CB", "checked", [P("Packed as it is", "5 kg cabin is not worth fighting. It goes in the hold and comes back to you at Samui.")], "In the hold — cabin is only 5 kg on this airline."),
            B("L1", "left", [P("At Smilelugg, Bangkok", "Collected 23 Jan.")]),
            B("L2", "left", [P("At Smilelugg, Bangkok", "Collected 23 Jan.")]),
        ],
    ),
    dict(
        id="usm-kha",
        name="Koh Samui – Khao Sok",
        dates="17 Jan",
        where="Lipa Noi → Donsak → Cheow Lan Lake",
        via="06:00 ferry · 2h15 road · boat in",
        key=1,
        stored=1,
        note=(
            "No airline, so no weight limits — but two water crossings, and the second one is "
            "an open longtail onto the lake. Everything that must stay dry needs to be in the "
            "dry bag before you step on the boat, not after. 500 Rai is a raft house: there is "
            "no shop, no ATM and no card machine."
        ),
        do=[
            P("BOOK THE DONSAK FERRY", "Still outstanding. The 06:00 sailing docks 07:30 and leaves real margin; the 07:00 leaves you 25 minutes."),
            P("Confirm the 500 Rai pick-up time", "Do this before you book the ferry, not after."),
            P("Warn Hansar about the early start", "You are leaving before any normal breakfast."),
            P("Take baht for the park fee", "THB 340 at the pier. The stay itself is fully prepaid, so this and any drinks are the only cash you need on the lake — but there is no card machine, so it has to be in your pocket."),
        ],
        bags=[
            B("SL", "with", [P("On you for both crossings", "Passport, cash, phone. Inside the dry bag for the lake boat.")]),
            B("BP", "with", [P("Dry bag, packed before the boat", "Phone, wallet, iPad. The lake transfer is open water both ways."), P("Mini towel, suncream, DEET, Larq, power bank")]),
            B("CB", "with", [P("Can stay packed", "You are on the raft for two nights. There is nothing to lay out.")]),
            B("L1", "left", [P("At Smilelugg, Bangkok")]),
            B("L2", "left", [P("At Smilelugg, Bangkok")]),
        ],
    ),
    dict(
        id="kha-kbv",
        name="Khao Sok – Krabi",
        dates="19 Jan",
        where="Cheow Lan Lake → Ao Nang",
        via="10:00 boat · 2.5–3 hrs road",
        stored=1,
        note=(
            "Check-out is 09:30 and the boat off the lake is 10:00, with a morning massage "
            "booked at 07:30 — so the bag has to be packed the night before. Then two and a "
            "half to three hours by road to Ao Nang."
        ),
        do=[
            P("Pack the night of the 18th", "The morning is massage, breakfast, boat, in that order, with no slack in it."),
            P("Settle the 500 Rai extras in cash", "Drinks and the park fees. No card machine on the lake."),
            P("Dry bag again for the boat out", "Same crossing, same water."),
        ],
        bags=[
            B("SL", "with", [P("On you")]),
            B("BP", "with", [P("Dry bag with the phone and iPad", "Open boat off the lake.")]),
            B("CB", "with", [P("Packed the night before", "Not on the morning.")]),
            B("L1", "left", [P("At Smilelugg, Bangkok")]),
            B("L2", "left", [P("At Smilelugg, Bangkok")]),
        ],
    ),
    dict(
        id="kbv-bkk",
        name="Krabi – Bangkok",
        dates="23 Jan",
        where="KBV → BKK",
        via="TG 246 · Thai Airways · 12:45",
        stored=1,
        note=(
            "Check-out is 12:00 and the flight is at 12:45, so leave Ao Nang around 10:00. "
            "One checked bag included, which is the cabin bag — take the pressure off and put "
            "it in the hold, because you are collecting two suitcases at the other end anyway."
        ),
        do=[
            P("Repack the night of the 22nd", "Storage collection and a long-haul on the same day. Do not start this at breakfast."),
            P("Keep the Smilelugg ref to hand", "14XIWBX4. The counter is landside on B Floor, so you clear arrivals first."),
        ],
        bags=[
            B("SL", "cabin", [P("As always")]),
            B("BP", "cabin", [P("iPad, chargers, Larq")]),
            B("CB", "checked", [P("In the hold", "One checked bag is included and you have a 4h45 connection to use.")]),
            B("L1", "left", [P("Collected at BKK", "Not on this flight — you pick it up at Smilelugg after you land.")]),
            B("L2", "left", [P("Collected at BKK")]),
        ],
    ),
    dict(
        id="bkk-lon",
        name="Bangkok – London",
        dates="23–24 Jan",
        where="BKK → DOH → LHR",
        via="QR 835 · QR 107 · Qatar Business",
        key=1,
        note=(
            "TG 246 lands 14:10, QR 835 leaves 18:55 — 4h45 to clear arrivals, collect both "
            "cases from Smilelugg on B Floor and re-check everything. Qatar give you 40 kg "
            "across any number of bags, so weight is not the problem; time is. Lands Heathrow "
            "06:35 on the 24th, in January, straight off a plane from 30°C."
        ),
        do=[
            P("Collect from Smilelugg first", "Ref 14XIWBX4. B Floor, landside, about 50 m past the ticket kiosk from the SA City Line entrance."),
            P("Pull the hoodie and tracksuit out before you re-check", "Heathrow at 06:35 in January. This is the whole reason they came."),
            P("Keep the shaver, foam and moisturiser in the cabin bag", "Thirteen hours to London and a 06:35 landing — you will want a shave in the Doha lounge."),
        ],
        bags=[
            B("SL", "cabin", [P("As always"), P("Any leftover baht", "Spend it airside or keep it for next time.")]),
            B("BP", "cabin", [
                P("Sony over-ears", "Back in your hands after 13 days in storage."),
                P("iPad Air, chargers, Larq"),
                P("Compression socks"),
            ]),
            B("CB", "cabin", [
                P("Switch, PS5 controller and HDMI", "Thirteen hours Bangkok to Doha to London. This is what they are for."),
                P("Shaver, shaving foam and moisturiser", "Do NOT let these go into the cases when you re-check."),
                P("Shaving foam into the liquids bag", "You clear security again at Bangkok and at Doha."),
                P("One change of clothes"),
            ]),
            B("L1", "checked", [P("Re-checked to London", "Collected from storage, repacked, straight back in the hold.")]),
            B("L2", "checked", [P("Re-checked to London", "Everything you are not using on the flight.")]),
            B("worn", "worn", [P("Hoodie and tracksuit bottoms", "Out of the case before you re-check, not after you land.")]),
        ],
    ),
]
