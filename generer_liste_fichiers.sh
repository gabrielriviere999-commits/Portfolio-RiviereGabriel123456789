#!/bin/bash

generate_index() {
    local dir="$1"
    local output="$dir/liste_fichiers.html"

    echo "Génération : $output"

    # Début du fichier HTML
    {
        echo "<!DOCTYPE html>"
        echo "<html><head><meta charset='utf-8'>"
        echo "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        echo "<title>Liste des fichiers - ${dir}</title>"
        echo "<style>"
        echo "body { background:white; color:black; font-family:sans-serif; font-size:18px; line-height:1.5; }"
        echo "a { 
          color:blue;
          display:inline;            /* pas inline-block → permet le retrait suspendu */
          overflow-wrap:anywhere;
          word-break:normal; 
          white-space:normal; 
          max-width:100%; 
          font-size:18px; 
        }"
        echo "a:visited { color:purple; }"
        echo "ul { margin:0; padding-left:1.2em; list-style-position:outside; }"
        echo "li { margin:4px 0; font-size:18px; }"
        echo "h1 { font-size:22px; }"
        echo "</style>"
        echo "</head><body>"
        echo "<h1>Contenu de : ${dir}</h1>"
        echo "<ul>"
    } > "$output"

    # Lien vers le dossier parent (sauf racine)
    if [ "$dir" != "." ]; then
        echo "<li><a href=\"../liste_fichiers.html\">← Retour</a></li>" >> "$output"
    fi

    # Parcours des fichiers et dossiers
    for item in "$dir"/*; do
        name=$(basename "$item")

        # Ignorer le fichier généré
        if [ "$name" = "liste_fichiers.html" ]; then
            continue
        fi

        if [ -d "$item" ]; then
            echo "<li>[Dossier] <a href=\"$name/liste_fichiers.html\">$name</a></li>" >> "$output"
            generate_index "$item"   # Récursion
        else
            echo "<li><a href=\"$name\">$name</a></li>" >> "$output"
        fi
    done

    # Fin du fichier HTML
    {
        echo "</ul>"
        echo "</body></html>"
    } >> "$output"
}

# Lancer depuis la racine
generate_index "."
