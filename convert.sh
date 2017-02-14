einfo -p "$1" | html2text -b0 --ignore-emphasis  --ignore-images --ignore-links | sed 's/. . ./.../g'
