import os, re

# Fonction pour enlever les balises HTML
def strip_tags(html):
    return re.sub(r'<[^>]*>', '', html)

folder = "."
output_file = "docs.js"

docs = []

for root, dirs, files in os.walk(folder):
    for f in files:
        path = os.path.join(root, f)
        content = ""

        # Si c'est du HTML ou TXT → on extrait le texte
        if f.endswith(".html") or f.endswith(".txt"):
            try:
                with open(path, encoding="utf-8") as file:
                    content = file.read()
                content = strip_tags(content)
            except:
                content = ""

        # Pour les autres fichiers (PDF, images, etc.) → pas de contenu, juste le nom
        else:
            content = ""   # on laisse vide pour rester léger

        docs.append({
            "title": f,
            "url": os.path.relpath(path, folder),
            # On indexe aussi le nom du fichier dans "content" pour que la recherche marche dessus
            "content": (f + " " + content).replace("\n", " ")
        })

# Écriture directe dans docs.js
with open(output_file, "w", encoding="utf-8") as out:
    out.write("var docs = [\n")
    for d in docs:
        out.write("  {title:\"%s\", url:\"%s\", content:\"%s\"},\n" %
                  (d["title"], d["url"], d["content"].replace('"', '\\"')))
    out.write("];\n")

print("Fichier docs.js généré avec succès !")
