#!/bin/bash

generate_index() {
    local dir="$1"
    local output="$dir/liste_fichiers.html"

    echo "Génération : $output"

    {
        echo "<!DOCTYPE html>"
        echo "<html><head><meta charset='utf-8'>"
        echo "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        echo "<title>Liste des fichiers - ${dir}</title>"
        echo "<style>"
        echo "body { background:white; color:black; font-family:sans-serif; font-size:18px; line-height:1.5; }"

        # Liens : inline pour retrait suspendu, compatible 3DS
        echo "a {"
        echo "  color:blue;"
        echo "  display:inline;"
        echo "  word-wrap:break-word;"   # compatible 3DS
        echo "  white-space:normal;"
        echo "  max-width:100%;"
        echo "  font-size:18px;"
        echo "}"

        echo "a:visited { color:purple; }"

        # Puces propres
        echo "ul { margin:0; padding-left:1.2em; list-style-position:outside; }"
        echo "li { margin:4px 0; font-size:18px; }"

        # Ajout du label [Dossier] via CSS → solution parfaite
        echo "li.folder::before { content:'[Dossier] '; color:#555; }"

        echo "h1 { font-size:22px; }"
        echo "</style>"
        echo "</head><body>"
        echo "<h1>Contenu de : ${dir}</h1>"
        echo "<ul>"
    } > "$output"

    # Lien retour
    if [ "$dir" != "." ]; then
        echo "<li><a href=\"../liste_fichiers.html\">← Retour</a></li>" >> "$output"
    fi

    # Parcours
    for item in "$dir"/*; do
        name=$(basename "$item")

        # Ignorer le fichier généré
        if [ "$name" = "liste_fichiers.html" ]; then
            continue
        fi

        if [ -d "$item" ]; then
            # Dossier → classe spéciale
            echo "<li><a href=\"$name/liste_fichiers.html\">[Dossier]&nbsp;$name</a></li>" >> "$output"
            generate_index "$item"
        else
            # Fichier normal
            echo "<li><a href=\"$name\">$name</a></li>" >> "$output"
        fi
    done

    {
        echo "</ul>"
        echo "</body></html>"
    } >> "$output"
}

generate_index "."
