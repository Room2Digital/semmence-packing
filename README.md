# semmence-packing — retired

The packing list is a tab in the trip app. This site now serves a single
page pointing there.

Everything that used to live here moved into
[semmence-trip](https://github.com/Room2Digital/semmence-trip):

| Was here | Is now |
|---|---|
| `items.py`, `legs.py`, `bags.py`, `daybags.py`, `shopping.py` | `packdata/` |
| `template.html` | `src/pack.js` and `src/pack.css` |
| `build.py` | folded into the trip app's `build.py` |

The source files were deleted here rather than left behind, because two
copies of the same lists is how they quietly stop matching.

Supabase is unchanged: `pack_state` and `pack_items` in the same project,
so ticks and custom items carried over.
