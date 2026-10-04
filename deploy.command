#!/bin/bash
# Double-click to deploy the packing list.
# First run will ask you to link it to a Vercel project — choose "new project"
# and name it something like semmence-packing.

cd "$(dirname "$0")" || exit 1

echo "──────────────────────────────────────────────"
echo " Deploying the packing list"
echo " Folder: $(pwd)"
echo "──────────────────────────────────────────────"
echo

# Rebuild index.html from the data modules so a deploy can never ship stale output.
if [ -f build.py ]; then
  echo "Rebuilding index.html from items.py / legs.py / bags.py / daybags.py / shopping.py ..."
  python3 build.py || { echo "Build failed - nothing deployed."; read -r -p "Press return to close."; exit 1; }
  echo
fi

echo "Files that will ship:"
ls -1 index.html sw.js manifest.webmanifest icon-*.png img/* 2>/dev/null | sed 's/^/  /'
echo

if [ ! -d .vercel ]; then
  echo "Not linked to a Vercel project yet."
  echo "You'll be asked a few questions — choose to create a NEW project."
  echo
  read -r -p "Continue? [y/N] " go
  case "$go" in [yY]|[yY][eE][sS]) ;; *) echo "Cancelled."; read -r -p "Press return to close."; exit 0 ;; esac
  npx vercel link || { echo "Link failed."; read -r -p "Press return to close."; exit 1; }
fi

read -r -p "Deploy to PRODUCTION? [y/N] " reply
case "$reply" in
  [yY]|[yY][eE][sS]) ;;
  *) echo "Cancelled. Nothing deployed."; echo; read -r -p "Press return to close."; exit 0 ;;
esac

echo
npx vercel deploy --prod
status=$?

echo
if [ $status -eq 0 ]; then
  echo "✓ Deployed. Open it on your phone and Add to Home Screen."
else
  echo "✗ Deploy failed (exit $status)."
  echo "  If it asked you to log in, run 'npx vercel login' and try again."
fi

echo
read -r -p "Press return to close."
