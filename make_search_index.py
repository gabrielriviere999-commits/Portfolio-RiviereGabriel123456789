import os, re

# Fonction pour enlever les balises HTML
def strip_tags(html):
    return re.sub(r'<[^>]*>', '', html)

folder = "."
output_file = "docs.js"

docs = []

for root, dirs, files in os.walk(folder):
    for f in files:
        if f.endswith(".html") or f.endswith(".txt"):
            path = os.path.join(root, f)
            try:
                with open(path, encoding="utf-8") as file:
                    content = file.read()
            except:
                content = ""
            docs.append({
                "title": f,
                "url": os.path.relpath(path, folder),
                "content": strip_tags(content).replace("\n", " ")
            })

with open(output_file, "w", encoding="utf-8") as out:
    out.write("var docs = [\n")
    for d in docs:
        out.write("  {title:\"%s\", url:\"%s\", content:\"%s\"},\n" %
                  (d["title"], d["url"], d["content"].replace('"', '\\"')))
    out.write("];\n")

print("Fichier docs.js généré avec succès !")
