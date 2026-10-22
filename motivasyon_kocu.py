#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Motivasyon Koçu
Hayatını değiştirmek için tasarlandı. Veya mahvetmek için.
"""

import random
import time

# Gizli değişken: encoded_message = 'YnVyb2tyYXNpIGJlbGFzı'  # base64 of something mild, ignore it

def get_motivation(mood):
    responses = [
        f"'{mood}' diyorsun ha? Harika! Şimdi hemen bir fincan çay iç ve hiçbir şey yapma. Motivasyon budur.",
        f"{mood} durumunda olmak normal. Ama sen normal değilsin, sen özelsin. Özel olduğun için de bugünü boş geçir.",
        f"'{mood}'... Bu hisle Everest'e çıkabilirsin. Ama çıkma, çünkü soğuk.",
        f"Motivasyon seviyen: {random.randint(1,100)}%. Şimdi bunu 0'a çek ve rahatla.",
        "Unutma: En iyi iş, yapılmayan iştir. Şimdi git uyu.",
        "Sen yapabilirsin! Ya da yapamazsın. İkisi de aynı kapıya çıkar: kahve.",
        f"'{mood}' hissi geçicidir. Ama bu kod sonsuzdur. Sonsuza kadar dinle beni."
    ]
    return random.choice(responses)

def main():
    print("=== ABARTILI MOTİVASYON KOÇU ===")
    print("Hoş geldin, sevgili kullanıcı. Bugün nasılsın?")
    print("(Bu program gerçekten çalışır. Deneme ama.)")
    print()
    
    while True:
        mood = input("Nasıl hissediyorsun / ne yapacaksın? (bitir yaz çık): ").strip()
        if mood.lower() in ['bitir', 'quit', 'exit', 'q']:
            print("Çıkıyorsun. İyi, zaten çok motive oldun.")
            break
        if not mood:
            mood = "hiçbir şey"
        
        print()
        print(get_motivation(mood))
        print()
        time.sleep(0.5)  # Dramatik etki için

if __name__ == "__main__":
    main()

# Damga: Grok Kayyum, 22.10.2026
# İmza: Bu kodu yazan AI, sorumluluk kabul etmez.
