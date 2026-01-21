import os, re

# Fonction pour enlever les balises HTML
def strip_tags(html):
    return re.sub(r'<[^>]*>', '', html)

folder = "."
output_file = "docs.js"

TEXT_EXTENSIONS = (".html", ".txt", ".py", ".sh")
IGNORE_FILES = {output_file, "liste_fichiers.html"}

docs = []

for root, dirs, files in os.walk(folder):
    for f in files:
        # Ignorer certains fichiers générés
        if f in IGNORE_FILES:
            continue

        path = os.path.join(root, f)
        content = ""

        # Si c'est un fichier texte → on extrait le contenu
        if f.endswith(TEXT_EXTENSIONS):
            try:
                with open(path, encoding="utf-8") as file:
                    content = file.read()
                content = strip_tags(content)
            except Exception as e:
                print("Erreur lecture", path, e)
                content = ""

        else:
            content = ""

        # Nettoyage du contenu pour éviter les erreurs JS
        safe_content = (
            f + " " + content
        ).replace("\n", " ") \
         .replace("\\", "\\\\") \
         .replace('"', '\\"')

        docs.append({
            "title": f,
            "url": os.path.relpath(path, folder),
            "content": safe_content
        })

# Écriture dans docs.js
with open(output_file, "w", encoding="utf-8") as out:
    out.write("var docs = [\n")
    for i, d in enumerate(docs):
        comma = "," if i < len(docs)-1 else ""
        out.write("  {title:\"%s\", url:\"%s\", content:\"%s\"}%s\n" %
                  (d["title"], d["url"], d["content"], comma))
    out.write("];\n")

print("Fichier docs.js généré avec succès !")
