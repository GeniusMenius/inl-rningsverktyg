#!/usr/bin/env python3
"""
skapa_modul.py — Konverterar CSV till inlärningsverktygets JSON-format

QUIZ-CSV (quiz.csv):
  Kategori,Fråga,Alt1,Alt2,Alt3,Alt4,Rätt(0-3),Förklaring

FLASHKORT-CSV (flashkort.csv):
  Kategori,Framsida,Baksida

Användning:
  python3 skapa_modul.py --namn "Min modul" --icon "📚" --quiz quiz.csv --fc flashkort.csv --ut min_modul.json
"""

import csv, json, argparse, sys, os

def load_quiz(path):
    items = []
    with open(path, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 2):
            try:
                o = [row['Alt1'].strip(), row['Alt2'].strip(), row['Alt3'].strip(), row['Alt4'].strip()]
                a = int(row['Rätt(0-3)'].strip())
                assert 0 <= a <= 3, f"Rätt måste vara 0–3, rad {i}"
                assert all(o), f"Tomma alternativ på rad {i}"
                items.append({
                    "c": row['Kategori'].strip(),
                    "q": row['Fråga'].strip(),
                    "o": o,
                    "a": a,
                    "e": row.get('Förklaring','').strip()
                })
            except (KeyError, ValueError) as e:
                print(f"⚠️  Rad {i} i quiz: {e}")
    return items

def load_fc(path):
    items = []
    with open(path, encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, 2):
            try:
                items.append({
                    "c": row['Kategori'].strip(),
                    "t": row['Framsida'].strip(),
                    "d": row['Baksida'].strip()
                })
            except KeyError as e:
                print(f"⚠️  Rad {i} i flashkort: {e}")
    return items

def build_categories(quiz, fc):
    seen = {}
    colors = ["#4f46e5","#7c3aed","#059669","#d97706","#dc2626","#0891b2","#be185d","#16a34a"]
    icons  = ["📚","⚙️","🔩","📡","🔧","🖥️","🚨","🏭"]
    for item in quiz + fc:
        cat = item['c']
        if cat not in seen:
            idx = len(seen)
            seen[cat] = {
                "name": cat,
                "color": colors[idx % len(colors)],
                "icon": icons[idx % len(icons)]
            }
    return list(seen.values())

def main():
    p = argparse.ArgumentParser(description='CSV → JSON modulkonverterare')
    p.add_argument('--namn',  default='Min modul',    help='Modulnamn')
    p.add_argument('--icon',  default='📚',           help='Emoji-ikon')
    p.add_argument('--quiz',  default=None,            help='Sökväg till quiz.csv')
    p.add_argument('--fc',    default=None,            help='Sökväg till flashkort.csv')
    p.add_argument('--ut',    default='modul.json',    help='Utdatafil')
    p.add_argument('--version', default='1.0',         help='Versionsnummer')
    args = p.parse_args()

    quiz, fc = [], []
    if args.quiz:
        if not os.path.exists(args.quiz):
            print(f"❌ Hittar inte: {args.quiz}"); sys.exit(1)
        quiz = load_quiz(args.quiz)
        print(f"✅ Quiz:      {len(quiz)} frågor laddade")
    if args.fc:
        if not os.path.exists(args.fc):
            print(f"❌ Hittar inte: {args.fc}"); sys.exit(1)
        fc = load_fc(args.fc)
        print(f"✅ Flashkort: {len(fc)} kort laddade")

    if not quiz and not fc:
        print("❌ Ange minst --quiz eller --fc"); sys.exit(1)

    cats = build_categories(quiz, fc)
    print(f"✅ Kategorier: {[c['name'] for c in cats]}")

    module = {
        "name": args.namn,
        "icon": args.icon,
        "version": args.version,
        "categories": cats,
        "quiz": quiz,
        "flashcards": fc,
        "comparison": "",
        "srData": {}
    }

    with open(args.ut, 'w', encoding='utf-8') as f:
        json.dump(module, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Sparad: {args.ut}")
    print(f"   {len(quiz)} quiz · {len(fc)} flashkort · {len(cats)} kategorier")

if __name__ == '__main__':
    main()
