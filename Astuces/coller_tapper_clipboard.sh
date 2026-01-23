#!/bin/bash
# coller_tapper_clipboard.sh

echo "Clique sur la fenêtre cible (xdotool attend ton clic, 5s max)..."
# timeout de 5 secondes
win_id=$(timeout 5 xdotool selectwindow)

# Vérifier si une fenêtre a été sélectionnée
if [ -z "$win_id" ]; then
    echo "Aucune fenêtre sélectionnée dans le délai imparti."
    exit 1
fi

sleep 1
xdotool windowfocus "$win_id"

# Lire le presse-papiers (xclip ou xsel)
if command -v xclip >/dev/null 2>&1; then
    clipboard=$(xclip -o -selection clipboard)
elif command -v xsel >/dev/null 2>&1; then
    clipboard=$(xsel --clipboard)
else
    echo "Ni xclip ni xsel n'est installé."
    exit 1
fi

# Lecture ligne par ligne et frappe
while IFS= read -r ligne || [ -n "$ligne" ]; do
    xdotool type --window "$win_id" --clearmodifiers --delay 50 -- "$ligne"
    xdotool key --window "$win_id" Return
done <<< "$clipboard"
