# -*- coding: utf-8 -*-
# Robbie — Australia & Thailand, 19 Nov 2026 – 24 Jan 2027
#
# bag:  L1/L2 large cases · CB cabin bag · BP backpack · SL sling
# fate: always   with you the whole way
#       store    parked in the Bangkok cases, 10–23 Jan
#       handover given away in Phuket, 7–10 Jan
#       buy      bought en route
I = []
def it(id, name, cat, bag, qty=1, g=0, fate="always", note="", crit=False):
    I.append(dict(id=id, name=name, cat=cat, bag=bag, qty=qty, g=g,
                  fate=fate, note=note, crit=crit))

# ───────────────────────── DOCUMENTS & MONEY ─────────────────────────
it("passport","Passport — trackable holder","docs","SL",1,60,"always",
   "Six months' validity beyond 24 Jan 2027. The holder is tracked, so it shows in Find My.",True)
it("tdac","Thailand Digital Arrival Card","docs","SL",1,0,"always",
   "Mandatory for every foreign national. Complete it online 4–6 Jan, within 3 days of landing in Phuket on the 7th. Needs flight number, the Courtyard's address and a contact mobile. Save the QR offline.",True)
it("eta-aus","Australian ETA","docs","SL",1,0,"always",
   "Approved before you fly — the airline checks it at Gatwick.",True)
it("licence","Driving licence — the physical card","docs","SL",1,10,"store",
   "Avis from 29 Dec. No International Driving Permit needed, a UK licence is already in English — but hire firms will not accept a photo or a photocopy. Into the stored case at the Phuket repack; you don't drive again.",True)
it("insurance","Travel insurance — policy and 24hr number","docs","SL",1,10,"always",
   "Check the single-article limit before you fly. You are carrying roughly four thousand pounds of Apple hardware and most policies cap any one item at £300–500.",True)
it("cards","Bank cards — two providers","docs","SL",2,20,"always",
   "Tracker card in the wallet. Split across two bags so one loss isn't total.",True)
it("cash-gbp","Cash — GBP float","docs","SL",1,20,"always","Gatwick, and the taxi home on the 24th.")
it("cash-aud","Cash — AUD","docs","SL",1,20,"buy","Withdraw on arrival. Perth is near-cashless but markets aren't.")
it("cash-thb","Cash — THB","docs","SL",1,20,"buy",
   "Ferries, longtails, the Khao Sok transfers and 500 Rai extras. The lake is the least card-friendly place on the trip.",True)
it("flights-off","All 8 flight confirmations — offline","docs","SL",1,0,"always",
   "Saved offline. Phuket and Khao Sok have patchy signal.",True)
it("hotels-off","Accommodation confirmations — offline","docs","SL",1,0,"always",
   "Theatre Residence and the 500 Rai transfer details especially.")
it("bag-conf","Baggage receipts — JQ71 and TG206","docs","SL",1,0,"always",
   "JQ71: 40 kg prepaid, GBP 72.27, ref DMF5N5. TG206: 2 × 23 kg, second bag GBP 15.05, PNR FV844G. Have both at the bag drops.",True)
it("storage-receipt","Smilelugg receipt — 14XIWBX4","docs","SL",1,5,"always",
   "Paid, GBP 90.26, two cases, 10–23 Jan. B Floor at Suvarnabhumi, the Airport Rail Link level. Without it you are not getting the cases back.",True)
it("taxi-conf","Bangkok taxi — booking 911245279","docs","SL",1,0,"always",
   "Driver contacts you on WhatsApp at +44 7951 592634. Check WhatsApp works on landing.",True)

# ───────────────────────────── TECH ─────────────────────────────
it("phone","Phone","tech","SL",1,220,"always","",True)
it("watch","Apple Watch","tech","SL",1,50,"always","")
it("airpods","AirPods Pro","tech","SL",1,60,"always","Your everyday set once the over-ears are parked.")
it("sony","Sony over-ear headphones","tech","SL",1,250,"store",
   "Earn their place over the 26 hours out. Into the stored case at the Phuket repack, collected on the 23rd for the flight home.")
it("ipad-air","iPad Air","tech","CB",1,460,"always","Reading and films. Comes everywhere.")
it("mba","MacBook Air","tech","CB",1,1240,"store",
   "You work from Perth and stop in Thailand. Into the stored case at the Phuket repack — it does not need to see Samui or the lake.",True)
it("dongle","USB-C dongle","tech","CB",1,40,"store","Stores with the Air.")
it("mouse","Mouse","tech","CB",1,80,"store","Seven weeks of work earns it. Stores with the Air.")
it("hdmi","HDMI cable","tech","CB",1,90,"store","Hotel TVs and the Switch. Stores at Phuket.")
it("switch","Nintendo Switch","tech","CB",1,400,"always","Long transits and the Khao Sok evenings.")
it("charger-mac","MacBook charger — high wattage","tech","CB",1,300,"store",
   "Check the wattage covers the Air. The fold-up 3-in-1 will not charge a laptop.",True)
it("plug-uk","Mains plug — UK","tech","CB",1,90,"always","")
it("adapter-universal","Travel adapter with USB-C","tech","CB",1,180,"always",
   "UK Type G, Australia Type I, Thailand A/C. Check it is rated for the laptop charger, not just phones.",True)
it("charger-3in1","Fold-up 3-in-1 charger","tech","SL",1,180,"always",
   "Watch, phone and AirPods from one plug. The best single item in the sling.")
it("cable-ext","Extendable USB-C cable","tech","SL",1,70,"always","")
it("brick-lg","Power bank — large","tech","SL",1,500,"always",
   "CABIN ONLY, never checked, on every airline. Check the watt-hour rating on the casing: anything over 100 Wh needs airline approval and over 160 Wh is refused outright.",True)
it("brick-sm","Power bank — small","tech","SL",1,200,"always","Cabin only, same rule.")
it("airtags","AirTags","tech","CB",5,55,"always",
   "On the tech bag, sling, backpack and both cases. Get the fifth so suitcase 2 is covered — it sits in third-party storage for 13 days.",True)

# ─────────────────────────── SLEEP & FLIGHT ───────────────────────────
it("mouthtape","Mouth tape","flight","SL",1,20,"always","")
it("eyemask","Eye mask","flight","SL",1,30,"always","QR835 is an overnight and QR107 lands at 06:35.")
it("earplugs","Earplugs","flight","SL",1,10,"always","")
it("snacks","Snacks for travel days","flight","SL",1,150,"always","")

# ───────────────────────────── TOILETRIES ─────────────────────────────
it("washbag-lg","Fold-out washbag — large","toiletries","L2",1,260,"store",
   "Lives in the suitcase. Into storage at the Phuket repack.")
it("washbag-mini","Mini washbags","toiletries","CB",2,80,"always",
   "The hand-luggage pair. These are what you actually use on travel days and at the lake.",True)
it("liquids-bag","Clear 1L liquids bag","toiletries","SL",1,20,"always",
   "Re-cleared at Perth, Phuket, Bangkok and Krabi. Keep it reachable.",True)
it("decant","Decant bottles, 100 ml","toiletries","CB",5,150,"always",
   "Fill these at the Phuket repack. For the lake you really only need suncream and the basics — Hansar, Krabi La Playa and Theatre Residence all provide the rest.",True)
it("suncream","Suncream — full size","toiletries","L2",1,200,"always",
   "Australian suncream is the best there is and cheap. Decant 100 ml for the onward leg.",True)
it("suncream-tr","Travel suncream","toiletries","SL",1,80,"always","For the plane and the first day before you buy properly.")
it("facewash","Travel facewash","toiletries","CB",1,90,"always","")
it("moisturiser","Moisturiser","toiletries","CB",1,100,"always","")
it("eyecream","Eye cream","toiletries","CB",1,40,"always","")
it("sanitiser","Hand sanitiser","toiletries","SL",1,60,"always","")
it("mozzie","Mosquito spray","toiletries","CB",1,120,"always",
   "Khao Sok is jungle on water and the lake is worst at dusk. Top up with stronger DEET in Thailand if yours is mild.",True)
it("nail","Nail clippers","toiletries","CB",1,40,"always","Fine in checked. Cabin rules on clippers vary by airport.")

# ────────────────────────────── HEALTH ──────────────────────────────
it("medkit","Small medical pouch","health","CB",1,60,"always","")
it("imodium","Imodium","health","CB",1,20,"always",
   "The 06:00 ferry on the 17th, then 2h15 by road to the lake. You cannot buy this at 5am on a pier.",True)
it("motion","Motion sickness tablets","health","CB",1,20,"always",
   "Samui to Donsak is 1h30 of open water. Take one before boarding, not when you feel it.",True)
it("paracetamol","Paracetamol","health","CB",1,40,"always","")
it("ibuprofen","Ibuprofen","health","CB",1,40,"always","")
it("antihistamine","Antihistamine","health","CB",1,20,"always","Bites, heat rash, unfamiliar food.")
it("antiseptic","Antiseptic cream","health","CB",1,40,"always",
   "Coral and scooter scrapes infect fast in the tropics.",True)
it("plasters","Plasters + blister plasters","health","CB",1,50,"always",
   "Blister plasters specifically — new sandals and a lot of walking.",True)
it("rehydration","Rehydration sachets","health","CB",6,60,"always","Heat, beer and stomach trouble. Tiny and cheap.")
it("athletes","Athlete's foot cream","health","CB",1,50,"always","Humidity, flip-flops, wet bathrooms.")
it("prescriptions","Prescription medication","health","SL",1,100,"always",
   "Enough for 67 days plus buffer, in original packaging, in hand luggage.",True)

# ─────────────────────── HANDOVER — leaves in Phuket ───────────────────────
it("mbp","MacBook Pro — for handover","tech","CB",1,1600,"handover",
   "Given away in Phuket, 7–10 Jan. Sign out of your Apple ID and erase it BEFORE you fly — doing that over hotel wifi with a deadline is miserable. Remove it from Find My or it stays activation-locked and useless to them.",True)
it("ipad-mini","iPad mini — for handover","tech","CB",1,300,"handover",
   "Same: signed out, erased and removed from Find My before you fly.",True)

# ─────────────────────────────── KIT ───────────────────────────────
it("larq","Larq bottle, 1L","kit","BP",1,500,"always",
   "Self-cleaning, so it earns itself in Thailand. Empty through security, fill after.",True)
it("towel-lg","Microfibre towel — large","kit","L1",1,300,"store","Beach days in Perth. Stores at Phuket.")
it("towel-sm","Microfibre towel — mini","kit","CB",1,120,"always",
   "The one that matters onward — ferries, the lake, Krabi longtails.",True)
it("drybag","Dry bag, small — TO BUY","kit","BP",1,120,"buy",
   "Not owned yet. Khao Sok arrives by boat, the ferry deck is wet and Krabi longtails soak everything. Phone, wallet and the Switch while you're on the water.",True)
it("cubes","Packing cubes","kit","CB",4,220,"always",
   "What makes the Phuket repack take twenty minutes instead of two hours.",True)
it("sunglasses","Sunglasses — 4 pairs, one case","kit","CB",4,400,"always",
   "Trimmed from eight. Keep one cheap pair for the water and the longtails — that is the pair that gets lost.",True)
it("locks","TSA padlocks","kit","CB",3,150,"always",
   "Three bags go in the Jetstar hold and two sit in storage for 13 days.",True)
it("scales","Luggage scales","kit","CB",1,100,"always",
   "You have a live 7 kg problem on TG206. Pays for itself once.",True)
it("laundry-bag","Laundry bag","kit","CB",1,80,"always","Thai laundry charges by the kilo; bagged is faster to drop off.")
it("notepad","Thai notepad","kit","SL",1,90,"always","")
it("daypack","Lockable daypack","kit","CB",1,320,"always",
   "Rottnest, the ferries and Bangkok. Lockable zips and a slash-resistant strap.",True)

# ───────────────────────────── FOOTWEAR ─────────────────────────────
it("trainers","Trainers — running and gym","footwear","CB",1,800,"always",
   "Gym the whole trip, so these come onward. Bulkiest single item in the cabin bag — wear them on travel days.",True)
it("walking","Walking shoes","footwear","CB",1,700,"always",
   "Khao Sok and the Perth hills. Wear them rather than pack them.",True)
it("sandals","Sandals with a real sole","footwear","CB",1,400,"always",
   "Not flip-flops — something you can walk miles in and get wet.",True)
it("flipflops","Flip-flops","footwear","CB",1,200,"always","Beach, pool, questionable shower floors.")
it("smart-shoes","Smart shoes — closed, dark","footwear","CB",1,600,"always",
   "Christmas dinner, and Vertigo and Blue Elephant both enforce closed shoes. Bangkok is after the cases are parked, so these stay with you.",True)

# ───────────────────────────── CLOTHING ─────────────────────────────
it("tees","T-shirts","clothing","L1",10,1500,"store","Ten for Perth, where you wash your own. Four come onward.")
it("tees-on","T-shirts — onward","clothing","CB",4,600,"always","Quick-dry or merino. Thai laundry is cheap and same-day.")
it("shorts","Shorts","clothing","L1",4,800,"store","Two come onward.")
it("shorts-on","Shorts — onward","clothing","CB",2,400,"always","")
it("underwear","Underwear","clothing","L1",12,400,"store","Seven come onward.")
it("underwear-on","Underwear — onward","clothing","CB",7,250,"always","")
it("socks","Socks","clothing","L1",10,400,"store","Three pairs come onward — you'll be in sandals most days.")
it("socks-on","Socks — onward","clothing","CB",3,120,"always","")
it("gym-kit","Gym shorts + technical tees","clothing","CB",3,500,"always",
   "Gym the whole trip. Quick-dry, so they wash in a sink and are dry by morning.")
it("trousers-light","Light trousers or chinos","clothing","CB",1,400,"always",
   "Temples, Bangkok restaurants, mosquitoes at dusk, and the cold landing on the 24th.",True)
it("shirt-casual","Casual shirts — linen","clothing","CB",2,400,"always","Sun cover that still reads as clothing.")
it("midlayer","Packable midlayer","clothing","CB",1,350,"always",
   "Aircraft air con, the 06:00 ferry, and Heathrow in January.",True)
it("sleepwear","Sleepwear","clothing","CB",1,200,"always","Qatar provide pyjamas on the long-haul; there are 65 other nights.")
it("cap","Cap or hat","clothing","BP",1,100,"always","Perth sun in December is genuinely dangerous.",True)
it("smart-shirt","Smart shirts — collared","clothing","CB",2,400,"always",
   "One for Christmas, one for Bangkok. Bangkok is after the drop, so they stay with you.",True)
it("smart-trousers","Smart trousers — dark, long","clothing","CB",1,450,"always",
   "Required at Vertigo and Blue Elephant.",True)
it("belt","Belt","clothing","CB",1,150,"always","")
it("swim","Swim shorts","clothing","L1",3,300,"store","Two come onward.")
it("swim-on","Swim shorts — onward","clothing","CB",2,200,"always","Two, so one is always dry.",True)
it("rashvest","Rash vest","clothing","CB",1,200,"always",
   "Snorkelling with a bare back in Thai sun ruins a week. Also the Rottnest bike day.",True)
