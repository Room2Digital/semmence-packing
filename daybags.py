# -*- coding: utf-8 -*-
# Day bags — what comes off the main pack for a specific day out.
# Each item is either a reference to something already on the main list (ref=id)
# or a one-off for that day.

DAYBAGS = [
 dict(
  id="rottnest",
  name="Rottnest Island",
  date="2027-01-02",
  dates="Sat 2 Jan",
  bag="Lockable daypack",
  where="Fremantle → Thomson Bay",
  note=("Ferry out 09:00 from O'Connor Landing, e-bikes 09:30–15:30 from Pedal & Flipper, "
        "ferry back 16:00. Booking 2G6JZV, 3 adults, same-day return — the fare includes the "
        "island admission. Be at the terminal by 08:30; boarding closes 08:50."),
  warn=("Six hours on a bike in peak Australian summer with almost no shade, and you're "
        "drinking. This is the single most sunburn-and-dehydration-prone day of the whole trip. "
        "The bikes are due back at 15:30 and the last ferry is 16:00 — that is 30 minutes of "
        "margin, so do the drinking at Hotel Rottnest at the end, near the jetty, not at a "
        "far bay."),
  items=[
   # --- the non-negotiables ---
   dict(name="Water, 2 litres minimum", ref=None, g=2000, crit=True,
        note="There are filling stations at Thomson Bay, Geordie Bay and The Basin, but long "
             "stretches between them with nothing. Freeze one bottle the night before."),
   dict(name="Suncream SPF50", ref="suncream", g=200, crit=True,
        note="Apply before you leave the ferry, then again at every beach stop. Australian "
             "summer UV is genuinely different — this is not the place to ration it."),
   dict(name="Hat", ref="cap", g=100, crit=True,
        note="Has to stay on at bike speed. A cap with a strap, or wear it backwards."),
   dict(name="Sunglasses", ref="sunglasses", g=40, crit=True),
   dict(name="Swim shorts — worn under", ref="swim-is", g=100, crit=True,
        note="Wear them rather than pack them. You'll stop at The Basin, Little Salmon and "
             "Parakeet, and changing facilities are thin away from the settlement."),
   dict(name="Quick-dry towel", ref="quick-towel", g=180, crit=True),
   dict(name="Dry bag, 10L", ref="drybag", g=150, crit=True,
        note="Phone, wallet and keys while you swim. Bags are not watched at the bays."),

   # --- the ones people regret skipping ---
   dict(name="Rash vest or light long sleeve", ref="rashvest", g=200,
        note="Your back and shoulders are pointed at the sun for six hours on a bike. "
             "This is the difference between a good evening and a ruined one."),
   dict(name="Power bank", ref="powerbank", g=300,
        note="Maps, photos and the return ferry QR all live on your phone."),
   dict(name="Card and some cash", ref="cards", g=20,
        note="Hotel Rottnest and the Thomson Bay bakery take cards. Carry a little cash anyway."),
   dict(name="Snacks", ref=None, g=200,
        note="Food away from Thomson Bay is essentially nothing. Even with lunch booked, "
             "carry something for the middle of the island."),
   dict(name="Plasters", ref="plasters", g=30,
        note="Saddle soreness and a blister from wet feet in dry shoes are the two likely ones."),
   dict(name="Dry shirt for the ferry home", ref=None, g=150,
        note="You'll be salty, sunburnt and damp at 16:00. The air con on the boat is cold."),
   dict(name="Ferry booking 2G6JZV", ref=None, g=0, crit=True,
        note="Saved offline. Show the barcode to the crew at the vessel."),
  ],
 ),
]
