#!/usr/bin/env python3
import subprocess
import sys
import platform

def get_clipboard():
    try:
        return subprocess.check_output(
            ["powershell", "-Command", "Get-Clipboard"],
            text=True
        )
    except subprocess.CalledProcessError:
        print("⚠️ Presse-papier vide ou inaccessible.")
        sys.exit(1)

def set_clipboard(text):
    try:
        subprocess.run(
            ["powershell", "-Command", f'Set-Clipboard -Value @"{text}"@'],
            check=True
        )
    except Exception as e:
        print(f"❌ Impossible de copier dans le presse-papier : {e}")
        sys.exit(1)

if platform.system() != "Windows":
    print("❌ Ce script est destiné à Windows.")
    sys.exit(1)

texte = get_clipboard()

if not texte.strip():
    print("⚠️ Presse-papier vide.")
    sys.exit(1)

set_clipboard(texte.upper())
print("✅ Texte en MAJUSCULES.")
