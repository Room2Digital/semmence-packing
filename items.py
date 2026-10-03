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
it("cash-thb","Cash — 50,000 THB","docs","SL",1,120,"always",
   "About GBP 1,150. Well under Thailand's declaration threshold, which is USD 20,000 equivalent, so nothing to declare. Split it: some in the sling, some in a case, some in the hotel safe — do not carry the lot in one place for 67 days. It funds the ferries, longtails, Khao Sok and the 500 Rai extras, which is where cards stop working.",True)
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
it("hdmi","HDMI cable","tech","CB",1,90,"store","General purpose — hotel TVs, the MacBook. Stores at Phuket.")
it("hdmi-switch","Nintendo Switch HDMI cable","tech","CB",1,80,"always",
   "Stays with the Switch. Theatre Residence, Hansar and Krabi La Playa all have TVs.")
it("ps5-pad","PS5 controller","tech","CB",1,280,"always",
   "For Remote Play. Qatar's Starlink should genuinely carry it — the bandwidth is there and satellite latency is usually workable. Worth testing on the Gatwick to Doha leg before you count on it for the 14 hours to Perth. Pairs natively with the iPad Air as the fallback.")
it("switch","Nintendo Switch","tech","CB",1,400,"always","Long transits and the Khao Sok evenings.")
it("charger-mac","MacBook charger — high wattage","tech","CB",1,300,"store",
   "Check the wattage covers the Air. The fold-up 3-in-1 will not charge a laptop.",True)
it("plug-uk","Mains plug — UK","tech","CB",1,90,"always","")
it("adapter-universal","Travel adapter with USB-C","tech","CB",1,180,"always",
   "UK Type G, Australia Type I, Thailand A/C. Check it is rated for the laptop charger, not just phones.",True)
it("charger-3in1","Fold-up 3-in-1 charger","tech","SL",1,180,"always",
   "Watch, phone and AirPods from one plug. The best single item in the sling.")
it("cable-ext","Extendable USB-C cable","tech","SL",1,70,"always","")
it("cable-shaver","Shaver cable","tech","CB",1,40,"always",
   "Not USB-C at both ends, so nothing else in the bag will charge it. The one cable with no substitute — pack it with the shaver, not loose.",True)
it("brick-sm","Power bank — small","tech","SL",1,200,"always",
   "The only one you are taking — the large one is out. Cabin baggage only, never checked.",True)
it("esim","Global SIM — 2 months","tech","SL",1,0,"always",
   "Already organised. Covers both countries for the whole trip, so no Australian or Thai eSIM needed on arrival.")
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
it("shaver","Electric shaver","toiletries","CB",1,220,"always",
   "Check how it charges — if it's a proprietary barrel plug rather than USB-C, that charger has to come too and it's easy to leave behind.",True)
it("shave-foam","Mini shaving foam","toiletries","CB",1,100,"always","Under 100 ml so it clears cabin security.")
it("etoothbrush","Electric toothbrush","toiletries","CB",1,180,"always",
   "Toothpaste bought on arrival; Qatar give you a travel one for the flight. Check the charger — most are an inductive base with a fixed plug, which needs the travel adapter.",True)
it("deodorant","Deodorant","toiletries","CB",1,100,"always",
   "Not on your list either. Solid or stick travels better than aerosol and does not count as a liquid.",True)
it("lipbalm","Lip balm with SPF","toiletries","SL",1,15,"always",
   "Six hours cycling at Rottnest, a lot of beach, and three long-haul sectors of dry cabin air.")
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
it("laundry-bag","Dirty laundry bags","kit","CB",2,110,"always",
   "Two, so dirty and damp stay apart from clean. Thai laundry charges by the kilo and bagged is faster to drop off.")
it("binbags","Bin bags","kit","CB",5,60,"always",
   "Wet swimwear, sandy shoes, the shirt you sweated through on the ferry. Weigh nothing and solve a problem every few days.")
it("goggles","Swimming goggles","kit","CB",1,80,"buy",
   "Worth having — the Sebel and the office both have gyms, and there is a lot of sea between Scarborough, Samui and Krabi.")
it("apps","Phone apps page","docs","SL",1,0,"always",
   "Airlines, TripIt, Avios, Amex, Monzo, Booking.com, Grab, Uber, Uber Eats, Ticketmaster. Add WhatsApp — the Bangkok driver contacts you on it — plus Line, which is how Thai businesses actually communicate, and GetYourGuide for the Rottnest ferry booking.")
it("notepad","Thai notepad","kit","SL",1,90,"always","")
it("daypack","Lockable daypack","kit","CB",1,320,"always",
   "Rottnest, the ferries and Bangkok. Lockable zips and a slash-resistant strap.",True)

# ───────────────────────────── FOOTWEAR ─────────────────────────────
it("trainers-nice","Nice trainers","footwear","CB",1,780,"always",
   "Your smart-casual pair. Fine at Vertigo and Blue Elephant — long trousers are the part they actually care about.")
it("trainers-old","Old trainers","footwear","L1",1,750,"store",
   "The pair you don't mind ruining. Perth beaches and anything messy.")
it("running","Running shoes","footwear","CB",1,720,"always","Gym the whole trip, so these travel onward.")
it("sandals","Sandals","footwear","CB",1,400,"always",
   "The ones you can walk miles in and get wet — Khao Sok, the piers, Krabi.",True)
it("sliders","Sliders","footwear","CB",1,280,"always","Beach, pool, hotel bathrooms.")

# ───────────────────────────── CLOTHING ─────────────────────────────
it("shirts-nice","Nice shirts","clothing","CB",7,1400,"always","Dinners, Christmas, Bangkok, and sun cover that still reads as clothing.")
it("tees","T-shirts","clothing","CB",10,1500,"always","")
it("shorts","Shorts","clothing","CB",5,1000,"always","")
it("trousers","Trousers","clothing","CB",1,450,"always",
   "For the two or three nights out — Vertigo, Blue Elephant, Christmas dinner. Elephant pants bought in Thailand cover the temples; shorts cover everything else.",True)
it("swim","Swim shorts","clothing","CB",2,200,"always","Two, so one is always dry.",True)
it("boxers","Boxers","clothing","CB",8,270,"always","")
it("socks-white","White socks","clothing","CB",8,320,"always","")
it("socks-gym","Gym socks","clothing","CB",3,120,"always","")
it("compression","Compression socks","clothing","BP",1,90,"always",
   "For the long-haul. Worth it on a 26-hour door-to-door and again on the way back.",True)
it("gym-tops","Gym tops","clothing","CB",3,300,"always","")
it("gym-shorts","Gym shorts","clothing","CB",2,300,"always","")
it("belt","Belt","clothing","CB",1,150,"always","")
it("hoodie","Hoodie","clothing","CB",1,520,"always",
   "Worn on the flight out with the tracksuit bottoms. Also the layer for aircraft air con, the 06:00 Donsak ferry and nights on the lake.",True)
it("windbreaker","Windbreaker","clothing","CB",1,280,"always",
   "Packs to nothing. The one thing between you and a British 06:35 landing on 24 January.",True)
it("tracksuit","Tracksuit bottoms","clothing","CB",1,420,"always",
   "Worn on the long-haul with the hoodie. Doubles as something to sleep in and to throw on at Khao Sok.")
it("pyjamas","Qatar pyjamas","clothing","CB",1,250,"always",
   "They don't take them back, so you have them from 19 Nov. Covers sleepwear for the rest of the trip.")
it("hats","Hats","clothing","CB",3,300,"always","")
it("hat-gym","Gym hat","clothing","CB",1,100,"always","")
