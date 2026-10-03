# -*- coding: utf-8 -*-
# Every stage of the trip, with a per-bag plan you can tick off.
#
# plan keys:  do · worn · SL · BP · CB · L1 · checked
# key=1       highlights a leg where bags actually change hands

def P(n, note="", add=False):
    d = dict(n=n)
    if note: d["note"] = note
    if add: d["add"] = True
    return d

LEGS = [

 dict(id="prep", name="Before you go", dates="Nov", where="Home", bags="L1 L2 CB BP SL",
  note="The only stage where forgetting something is fixable. Most of this is admin, not packing.",
  plan=dict(
    do=[
      P("Erase the MacBook Pro and iPad mini", "Sign out of your Apple ID, erase, and remove them from Find My. An activation-locked device is useless to whoever gets it, and doing this on Phuket hotel wifi with someone waiting is miserable."),
      P("Buy the small dry bag", "The last outstanding item. Khao Sok arrives by boat and Krabi longtails soak everything."),
      P("Buy swimming goggles", "The Sebel and the office both have gyms."),
      P("Check passport validity", "Six months beyond 24 Jan 2027."),
      P("Download offline maps", "Perth, Bangkok, Samui, Krabi. Plus add WhatsApp, Line, GetYourGuide and Bolt to your apps page."),
      P("Pre-pack the three cubes", "Cube 1 clothing, Cube 2 gym and footwear, Cube 3 kit. Doing this now is what makes the Phuket repack ten minutes."),
      P("AirTags in both cases", "They sit in third-party storage for 13 days."),
    ],
  )),

 dict(id="out", name="Outbound long-haul", dates="19–20 Nov", where="LGW → DOH → PER", bags="L1 L2 CB BP SL", key=1,
  note="Gatwick hotel on the 18th — the cabin bag has to cover that night without opening a suitcase. QR330 08:40, QR900 out of Doha at 02:40, into Perth 18:45. About 26 hrs door to door. Qsuite, so pyjamas and bedding are provided. Qatar Business allows two cabin pieces at 15 kg plus a personal item, so all three travel with you.",
  plan=dict(
    worn=[
      P("Nice trainers", "Wear the bulkiest footwear rather than packing it."),
      P("T-shirt and light trousers", "Hoodie and tracksuit are in the suitcase; Qatar hand you pyjamas anyway."),
    ],
    SL=[
      P("Wallet and cards"), P("Passport holder"), P("Cash"), P("Sunglasses — daily pair"),
      P("AirPods Pro"), P("Fold-up 3-in-1 charger"), P("Extendable USB-C cable"),
      P("Earplugs"), P("Eye mask"), P("Mouth tape"), P("Phone"),
      P("Mini charger brick", "Cabin only, never checked."),
      P("Prescription medication", "Hand luggage, original packaging."),
      P("Clear 1L liquids bag", "Cleared twice — Gatwick and Doha."),
    ],
    BP=[
      P("iPad Air", "The main one, not the one being handed over in Phuket."),
      P("USB-C dongle"), P("HDMI cable"), P("Compression socks"), P("Larq bottle, empty"),
      P("Sony over-ear headphones", "The flight you bought them for."),
    ],
    CB=[
      P("2 boxers, 2 socks, 2 T-shirts"), P("1 gym top, 1 gym shorts, 1 gym socks"),
      P("Running shoes"), P("1 swim shorts"), P("MacBook Air"),
      P("Mini washbag", "Electric toothbrush, mini toothpaste, travel face wash, roll-on deodorant, aftershave atomiser. Covers the Gatwick night and the Doha spa at 23:30."),
    ],
    L1=[P("Everything else", "Hoodie, tracksuit, windbreaker, travel adapter, the 4-pair sunglasses case, the clothing bulk, MacBook Pro and iPad mini for the handover.")],
  )),

 dict(id="perth", name="Perth — the long stay", dates="20 Nov–18 Dec", where="The Sebel West Perth", bags="L1 L2 CB BP SL",
  note="Four weeks. Working from the Fern office, gym at both. Self-service laundry, so wash weekly and live out of the wardrobe. Peak summer, 30–40°C.",
  plan=dict(
    do=[
      P("Unpack properly", "Four weeks. Empty both cases into the wardrobe rather than living out of them."),
      P("Do the big shop", "See Buy on arrival — suncream, protein powder, toothpaste, milk, eggs, laundry pods."),
      P("Check the suncream is reef-safe", "It is also what you decant for Thailand, and Thai marine parks fine the banned ingredients up to 100,000 baht."),
      P("Sort the office", "Fern, 79 St Georges Terrace, from 23 Nov. AUD 500 still to pay."),
    ],
    SL=[P("Daily carry", "Phone, cards, daily sunglasses, mini charger brick.")],
  )),

 dict(id="perth2", name="Perth — Calum's", dates="18–29 Dec", where="37 Sackville Terrace", bags="L1 L2 CB BP SL",
  note="Eleven nights at your cousin's. Nothing flies, so this is a repack across town rather than a real transition. Office runs to 23 Dec, so five days of commuting in from Scarborough.",
  plan=dict(
    do=[
      P("Repack the cases to move", "Short hop, so no need to be clever about it."),
      P("Boxing Day cricket", "26 Dec, Optus Stadium, 18:15. See the day bag — sling only, bags capped at 40 x 30 cm."),
    ],
  )),

 dict(id="scar", name="Scarborough — Christmas", dates="29 Dec–7 Jan", where="7 Stanley Street", bags="L1 L2 CB BP SL",
  note="Christmas and New Year at the rented house. Avis hire car from the 29th — you need the physical licence, no IDP required. Beach Christmas, one smart evening.",
  plan=dict(
    do=[
      P("Collect the hire car", "29 Dec, 13:30. Physical licence only — photos and photocopies are refused."),
      P("Rottnest on 2 Jan", "Ferry 09:00, e-bikes 09:30–15:30, ferry back 16:00. See the day bag."),
      P("Start consolidating", "You fly out at 07:25 on the 7th. Pack the night of the 5th, not the morning of the 7th."),
      P("Book the Jetstar bags if not already", "40 kg prepaid, GBP 72.27, ref DMF5N5."),
    ],
    L1=[P("Pack for the 7th", "Everything back in the cases. Cubes 1, 2 and 3 packed and near the top — that is what makes Phuket quick.")],
  )),

 dict(id="jet", name="Jetstar to Phuket", dates="7 Jan", where="PER → HKT, JQ71", bags="BP SL", key=1,
  note="07:25 departure, so a very early start from Scarborough. 40 kg prepaid across as many bags as you like, so check all three — both cases AND the cabin bag — and walk on with just the backpack and sling. Jetstar cabin is two items at 7 kg combined, weighed at the gate.",
  plan=dict(
    checked=[
      P("Suitcase 1"), P("Suitcase 2"),
      P("Cabin bag", "In the hold here. Nothing in it you need for five hours."),
    ],
    BP=[P("iPad Air, chargers, Larq"), P("Anything you want in the air")],
    SL=[
      P("Passport, phone, cards, cash, daily sunglasses, AirPods, mini charger brick"),
      P("Prescriptions and the liquids bag", "Never in the hold."),
    ],
  )),

 dict(id="phu", name="Phuket", dates="7–10 Jan", where="Courtyard by Marriott Phuket Town", bags="L1 L2 CB BP SL",
  note="Three nights with everything still in tow, and the last leg where the cases are open.",
  plan=dict(
    do=[
      P("Hand over the MacBook Pro and iPad mini", "Already erased and signed out before you flew. Hand them over early in the three days, not on the morning you leave."),
      P("Complete the TDAC if you have not", "Mandatory, online, within 3 days of arrival."),
      P("Decant the suncream", "Fill the 100 ml bottles from the full-size before it goes into storage."),
    ],
  )),

 dict(id="repack", name="The repack — Phuket", dates="10 Jan, morning", where="Courtyard, before TG206", bags="L1 L2 CB BP SL", key=1,
  note="The cabin bag has to be UNDER 7 kg to board TG206 — Thai Economy allows one cabin piece at that weight and both checked allowances are taken by the suitcases. So pack it light, and leave the rest in cubes near the top of the cases. TG206 departs 11:50; start after breakfast.",
  plan=dict(
    CB=[
      P("Toiletries — both mini washbags and the decant bottles", "1.3 kg."),
      P("Full health kit", "0.5 kg."),
      P("iPad Air, chargers, power bank, shaver and cable", "1.7 kg."),
      P("One change of clothes", "Insurance only — you are back in the cases three hours later."),
      P("TARGET: under 7 kg", "Weigh it with the scales before you leave the room. The only number that matters today."),
    ],
    L1=[
      P("CUBE 1 — clothing", "5 tees, 3 shorts, 2 nice shirts, 1 trousers, 5 boxers, 3 socks, 2 swim shorts. About 4 kg."),
      P("CUBE 2 — gym and footwear", "Gym top, shorts, socks, running shoes, sandals, sliders. About 2.5 kg. Shoes in a bin bag inside the cube."),
      P("CUBE 3 — kit", "Mini towel, dry bag, laundry and bin bags, goggles, daypack, locks. About 1.4 kg."),
      P("LOOSE — Larq bottle", "Too awkward for a cube. Near the top with the others."),
      P("Staying behind", "MacBook Air and its kit, Sony over-ears, Switch, PS5 pad, 4-pair sunglasses case, Perth clothing surplus, old trainers, hoodie, tracksuit, large washbag, full-size suncream, large towel, driving licence, Apple Watch. About 9 kg."),
    ],
  )),

 dict(id="drop", name="Land and dump", dates="10 Jan, 13:20", where="Suvarnabhumi, B Floor", bags="CB BP SL", key=1,
  note="Ten minutes if the cubes are packed. Collect the cases, go to Smilelugg on B Floor — the Airport Rail Link level, about 50 m past the ticket kiosk from the SA City Line entrance. Lift the cubes across, lock up, hand over. Ref 14XIWBX4, paid, 10–23 Jan. Your taxi waits 45 min.",
  plan=dict(
    CB=[
      P("Lift in Cube 1, Cube 2, Cube 3", "No sorting — you did that in Phuket."),
      P("Plus the Larq bottle", "Takes the cabin bag to about 11.9 kg. Your only bag until the 23rd."),
    ],
    L1=[
      P("Lock both cases, photograph the receipt"),
      P("Hand to Smilelugg", "About 9 kg between them, collected during the 4h45 connection on the way home."),
    ],
  )),

 dict(id="bkk1", name="Bangkok", dates="10–13 Jan", where="Theatre Residence", bags="CB BP SL",
  note="Cabin bag only from here. Private taxi booked, driver contacts you on WhatsApp at +44 7951 592634. Two dress-code nights.",
  plan=dict(
    do=[
      P("Buy elephant pants", "Before the Grand Palace on the 11th — the dress code is enforced at the gate."),
      P("Vertigo on the 11th, 19:00", "Long trousers required. Trainers are fine, you have been before."),
      P("A Chef's Tour on the 12th, 16:00", "Outside Shanghai Mansion, Yaowarat."),
      P("Buy DEET", "Stronger and cheaper here than anything you would have carried."),
    ],
    CB=[P("Trousers and a nice shirt out", "The two dress-code nights are both in this leg.")],
  )),

 dict(id="sam", name="Koh Samui", dates="13–17 Jan", where="Hansar Samui Resort", bags="CB BP SL",
  note="Beach and resort, with a gym. The cabin bag goes in the hold on PG133 — Bangkok Airways cabin is only 5 kg, and 20 kg checked is included.",
  plan=dict(
    do=[
      P("BOOK THE DONSAK FERRY", "Still outstanding. 17 Jan, the 06:00 sailing — it docks 07:30 and leaves real margin. The 07:00 leaves 25 minutes."),
      P("Confirm the 500 Rai pick-up time", "Do this before booking the ferry, not after."),
      P("Choose a cooking class", "Still on your to-do list."),
      P("Take a motion sickness tablet the night before", "1h30 of open water at 06:00."),
    ],
    BP=[P("Day kit", "Dry bag, mini towel, daily sunglasses, suncream, Larq.")],
  )),

 dict(id="kha", name="Khao Sok", dates="17–19 Jan", where="500 Rai Floating Resort", bags="CB BP SL",
  note="06:00 ferry from Lipa Noi, 2h15 by road, then in by boat. A floating raft house on the lake. Check-out 09:30 on the 19th, then 2.5–3 hrs by road to Krabi.",
  plan=dict(
    do=[
      P("Dry bag packed before the boat", "Phone, wallet and the iPad. The transfer is open water both ways."),
      P("DEET on at dusk", "Jungle on water. This is the worst spot on the trip for it."),
      P("Cash", "The least card-friendly place you will stay."),
    ],
    BP=[P("Onto the boat", "Dry bag, mini towel, suncream, DEET, Larq, phone, power bank. The cabin bag can stay packed.")],
  )),

 dict(id="kra", name="Ao Nang, Krabi", dates="19–23 Jan", where="Krabi La Playa Resort", bags="CB BP SL",
  note="Four nights, already paid in full. Longtails to the beaches soak everything. Railay on the 20th, the Dragon Crest hike on the 21st, Kodam Kitchen on the 22nd.",
  plan=dict(
    do=[
      P("Dragon Crest hike, 21 Jan", "Steep and early. Walking shoes, two litres of water, suncream."),
      P("Reef-safe suncream only", "Krabi marine parks enforce the ban."),
      P("Repack the night of the 22nd", "TG246 leaves at 12:45 and you have a storage collection and a long-haul the same day."),
    ],
    BP=[P("Beach days", "Dry bag for the longtails — they are wet boats, every time.")],
  )),

 dict(id="ret", name="Collect and fly home", dates="23–24 Jan", where="KBV → BKK → DOH → LHR", bags="L1 L2 CB BP SL", key=1,
  note="TG246 lands 14:10, QR835 departs 18:55 — 4h45 to clear arrivals, collect both cases from Smilelugg on B Floor (ref 14XIWBX4) and re-check. The counter is landside, so you come out first. Lands Heathrow 06:35 on the 24th, in January.",
  plan=dict(
    CB=[
      P("Switch, PS5 pad and HDMI out of the cases", "Thirteen hours Bangkok to Doha to London. This is what they are for."),
      P("Sony over-ears back out", "In storage since the 10th."),
      P("Hoodie and tracksuit within reach", "Heathrow at 06:35 in January, straight off a plane from 30°C."),
    ],
    L1=[P("Re-check both cases to London", "Qatar allows 40 kg across any number of bags, so weight is not a concern.")],
  )),
]
