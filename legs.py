# Pack legs — Robbie's real route
LEGS = [
 dict(id="prep",   name="Before you go",      dates="Nov",             where="Home",            bags="L1 L2 CB BP SL", note="Everything assembled. The only leg where forgetting something is fixable."),
 dict(id="out",    name="Outbound long-haul", dates="19–20 Nov",       where="LGW→DOH→PER",     bags="L1 L2 CB BP SL",
      note="QR330 08:40 from Gatwick, QR900 out of Doha at 02:40, into Perth 18:45 on the 20th. About 26 hrs door to door with an 8h25 layover. Qsuite, so pyjamas and bedding are provided. Qatar Business gives you two cabin pieces at 15 kg plus a personal item, so the sling, backpack and cabin bag all travel with you — the cabin bag is your lost-luggage insurance.",
      plan=dict(
        worn=[
          dict(n="Nice trainers", note="Wear the bulkiest footwear rather than packing it."),
          dict(n="T-shirt and light trousers", note="Hoodie and tracksuit are in the suitcase now, and Qatar hand you pyjamas anyway."),
        ],
        SL=[
          dict(n="Wallet and cards"), dict(n="Passport holder"), dict(n="Cash"),
          dict(n="AirPods Pro"), dict(n="Fold-up 3-in-1 charger"), dict(n="Extendable USB-C cable"),
          dict(n="Earplugs"), dict(n="Eye mask"), dict(n="Mouth tape"),
          dict(n="Phone"),
          dict(n="Mini charger brick", note="Cabin only, never checked."),
          dict(n="Prescription medication", add=True, note="Has to be hand luggage, in original packaging. Not in a hold bag."),
          dict(n="Clear 1L liquids bag", add=True, note="Travel suncream, sanitiser, lip balm. Needed at Gatwick and again at Doha."),
          dict(n="Australian ETA + insurance details", add=True, note="The airline checks the ETA at Gatwick."),
        ],
        BP=[
          dict(n="iPad Air", note="The main one — not the one being handed over in Phuket."),
          dict(n="USB-C dongle"), dict(n="HDMI cable"), dict(n="Compression socks"), dict(n="Larq bottle"),
          dict(n="Sony over-ear headphones", note="The flight you bought them for."),
          dict(n="Travel adapter", add=True, note="Perth is Type I. Doha is Type G like the UK, so the layover is fine, but you want this reachable on landing."),
        ],
        CB=[
          dict(n="2 boxers"), dict(n="2 socks"), dict(n="2 T-shirts"),
          dict(n="1 gym shirt"), dict(n="1 gym shorts"), dict(n="1 gym socks"),
          dict(n="Running shoes"), dict(n="1 swim shorts"), dict(n="MacBook Air"),
          dict(n="Mini washbag", note="Electric toothbrush, mini toothpaste, travel face wash, roll-on deodorant, aftershave atomiser. Covers the Gatwick night, the 26 hours and the Doha spa at 23:30."),
          dict(n="Windbreaker", add=True, note="Not worn, so it needs a home. Perth at 18:45 in November is warm — you do not actually need this again until Heathrow on 24 January, so a suitcase would do just as well."),
        ],
      )),
 dict(id="perth",  name="Perth — the long stay", dates="20 Nov–18 Dec", where="The Sebel West Perth", bags="L1 L2 CB BP SL", note="Four weeks. Working. Self-service laundry, so wash weekly and live out of the cases. Peak summer — 30–40°C."),
 dict(id="perth2", name="Perth — interim",     dates="18–29 Dec",       where="Not booked",      bags="L1 L2 CB BP SL", note="11 nights still unbooked. Same kit as the Sebel stay."),
 dict(id="scar",   name="Scarborough — Christmas", dates="29 Dec–7 Jan", where="Scarborough house", bags="L1 L2 CB BP SL", note="Christmas and New Year with everyone. Hire car from the 29th. Beach Christmas, but one smart evening."),
 dict(id="jet",    name="Jetstar to Phuket",   dates="7 Jan",           where="PER→HKT, JQ71",   bags="BP SL", note="07:25 departure. 40 kg prepaid across as many bags as you like, so check all three — both cases AND the cabin bag — and walk on with just the backpack and sling. Short flight, nothing on your person. Jetstar cabin is two items at 7 kg combined, weighed at the gate, and backpack plus sling is comfortably inside that.",
      plan=dict(
        checked=[dict(n="Suitcase 1"),dict(n="Suitcase 2"),dict(n="Cabin bag", note="Goes in the hold here. Nothing in it you need for five hours.")],
        BP=[dict(n="iPad Air, chargers, Larq, both sunglasses cases"),dict(n="Anything you want in the air")],
        SL=[dict(n="Passport, phone, cards, cash, AirPods, power bank"),
            dict(n="Prescriptions and the liquids bag", note="Never in the hold.")],
      )),
 dict(id="phu",    name="Phuket",              dates="7–10 Jan",        where="Courtyard by Marriott Phuket Town", bags="L1 L2 CB BP SL", note="Three nights with everything still in tow. The last leg where you have the cases open."),
 dict(id="repack", name="THE REPACK — Phuket",   dates="10 Jan, morning",  where="Courtyard, before TG206", bags="L1 L2 CB BP SL", note="Stage one of two, and the one that does the work. The cabin bag has to be UNDER 7 kg to board TG206 — Thai Economy allows one cabin piece at that weight, and both checked allowances are taken by the suitcases. So pack the cabin bag light, and put everything else onward into packing cubes near the top of the cases. At Bangkok you lift the cubes across and you are done. TG206 departs 11:50 — start after breakfast.",
      plan=dict(
        CB=[
          dict(n="Toiletries — both mini washbags and the decant bottles", note="1.3 kg. Refill the 100 ml bottles from the full-size first."),
          dict(n="Full health kit", note="0.5 kg."),
          dict(n="iPad Air, chargers, power bank, shaver and cable", note="About 1.5 kg of small tech."),
          dict(n="One change of clothes", note="Insurance only — you are back in the cases three hours later."),
          dict(n="TARGET: under 7 kg", note="Weigh it with the scales before you leave the room. This is the only number that matters today."),
        ],
        L1=[
          dict(n="CUBE 1 — clothing", note="5 tees, 3 shorts, 2 nice shirts, 1 trousers, 5 boxers, 3 socks, 2 swim shorts. About 4 kg."),
          dict(n="CUBE 2 — gym and footwear", note="Gym top, shorts, socks, running shoes, sandals, sliders. About 2.5 kg. Shoes in a bin bag inside the cube."),
          dict(n="CUBE 3 — kit", note="Mini towel, dry bag, laundry and bin bags, goggles, daypack, locks. About 1.4 kg. Sunglasses stay in the backpack throughout."),
          dict(n="LOOSE — Larq bottle", note="Too awkward for a cube. Near the top with the cubes."),
          dict(n="Pack all four near the top", note="The whole point is that Bangkok is lifting, not sorting."),
          dict(n="Genuinely staying behind", note="MacBook Air and its kit, Sony over-ears, Switch, PS5 pad, Perth clothing surplus, old trainers, hoodie, tracksuit, large washbag, full-size suncream, large towel, driving licence, Apple Watch. About 8.8 kg, not seen again until the 23rd."),
        ],
      )),

 dict(id="drop",   name="Land and dump",       dates="10 Jan, 13:20",   where="Suvarnabhumi",    bags="CB BP SL", note="Stage two, and it should take ten minutes. Land 13:20, collect the cases, go to Smilelugg on B Floor — the Airport Rail Link level, about 50 m past the ticket kiosk from the SA City Line entrance. Open the cases, lift the three cubes and the loose tech into the cabin bag, lock up and hand them over. Ref 14XIWBX4, paid, 10–23 Jan. Your taxi waits 45 min, which is plenty for this.",
      plan=dict(
        CB=[
          dict(n="Lift in Cube 1, Cube 2, Cube 3", note="No sorting, no decisions — you did that in Phuket."),
          dict(n="Plus the Larq bottle", note="Takes the cabin bag to about 11.9 kg. Your only bag until the 23rd."),
        ],
        L1=[
          dict(n="Lock both cases and photograph the receipt", note="About 8 kg between them."),
          dict(n="Hand to Smilelugg", note="Collected during the 4h45 connection on the way home."),
        ],
      )),
 dict(id="bkk1",   name="Bangkok",             dates="10–13 Jan",       where="Theatre Residence", bags="CB BP SL", note="Cabin bag only from here. Smart dress nights — Blue Elephant and the rooftops enforce long trousers and closed shoes, so that kit has to be in the cabin bag, not the cases."),
 dict(id="sam",    name="Koh Samui",           dates="13–17 Jan",       where="Hansar Samui Resort", bags="CB BP SL", note="Beach and resort. Light kit from here on."),
 dict(id="kha",    name="Khao Sok",            dates="17–19 Jan",       where="500 Rai Floating Resort", bags="CB BP SL", note="06:00 ferry from Lipa Noi, 2h15 by road, then in by boat. Floating raft house — limited power, properly dark, everything stays damp. Check-out 09:30 on the 19th."),
 dict(id="kra",    name="Ao Nang, Krabi",      dates="19–23 Jan",       where="Krabi La Playa Resort", bags="CB BP SL", note="Longtails to the beaches soak everything. Free cancellation ended 4 Jan — already paid."),
 dict(id="ret",    name="Collect and fly home", dates="23–24 Jan",      where="KBV→BKK→DOH→LHR", bags="L1 L2 CB BP SL", note="TG246 lands 14:10, QR835 departs 18:55 — 4h45 to clear arrivals, collect both cases from Smilelugg on B Floor (ref 14XIWBX4) and re-check. The counter is landside, so you come out first. Lands Heathrow 06:35 on the 24th, in January.",
      plan=dict(
        CB=[
          dict(n="Switch, PS5 pad and HDMI out of the cases", note="Thirteen hours Bangkok to Doha to London. This is what they are for."),
          dict(n="Sony over-ears back out too", note="Same reason. They have been in storage since the 10th."),
          dict(n="Hoodie and tracksuit within reach", note="Heathrow at 06:35 in January, straight off a plane from 30°C."),
        ],
        L1=[dict(n="Re-check both cases to London", note="Qatar allows 40 kg across any number of bags, so weight is not a concern here.")],
      )),
]
