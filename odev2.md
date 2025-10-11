### Python örnek çözümler (hafta 2)

Aşağıda her bir soru için kısa açıklama ve çalıştırılabilir Python kodu bulunur. Her örnek bağımsızdır; çalıştırmak için birer dosya veya interaktif kabukta kullanabilirsiniz.

#### Kullanıcıdan Alınan Metni Ekranda Gösterme
```python
s = input("Metin girin: ")
print(s)
```

#### Kullanıcının Girdiği İki Sayıyı Toplama
```python
a = float(input("1. sayı: "))
b = float(input("2. sayı: "))
print("Toplam:", a + b)
```

#### Girilen Sayının Tek veya Çift Sayı Olduğunu Belirleme
```python
n = int(input("Sayı girin: "))
print("Çift" if n % 2 == 0 else "Tek")
```

#### İki Sayı ile İşlem Yapan Basit Hesap Makinesi
```python
a = float(input("1. sayı: "))
b = float(input("2. sayı: "))
op = input("İşlem (+,-,*,/): ")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print("Sonuç:", a / b if b != 0 else "Sıfıra bölünemez")
else:
    print("Bilinmeyen işlem")
```

#### Hesap Makinesinde Kullanıcı Hatalarını Önleme
```python
def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Geçersiz sayı, tekrar deneyin.")
a = read_float("1. sayı: ")
b = read_float("2. sayı: ")
op = input("İşlem (+,-,*,/): ")
try:
    if op == '+': print(a + b)
    elif op == '-': print(a - b)
    elif op == '*': print(a * b)
    elif op == '/': print(a / b)
    else: print("Geçersiz işlem")
except ZeroDivisionError:
    print("Sıfıra bölünemez")
```

#### +/- İşaretine Her Basıldığında Sayıyı Arttırma/Azaltma
(Basit terminal örneği; q ile çıkış)
```python
val = 0
print("Değer:", val)
while True:
    cmd = input("Komut (+/-/q): ")
    if cmd == '+':
        val += 1
    elif cmd == '-':
        val -= 1
    elif cmd == 'q':
        break
    else:
        print("Geçersiz komut")
    print("Değer:", val)
```

#### +10 ile -10 Arasındaki Sayıları Ekrana Yazma
```python
for i in range(-10, 11):
    print(i, end=" ")
print()
```

#### Metindeki Her Harfin Arasına Virgül Koyma
```python
s = input("Metin: ")
print(','.join(list(s)))
```

#### 1 ile 100 Arasında Rastgele 10 Tam Sayı Üretip Dizi İçine Ekleme
```python
import random
arr = [random.randint(1, 100) for _ in range(10)]
print(arr)
```

#### -100 ile +100 Arasındaki 5’e Tam Bölünen Sayıları Yan Yana Gösterme
```python
nums = [i for i in range(-100, 101) if i % 5 == 0]
print(nums)
```

#### Üç Adet Sayıyı Karşılaştırıp Sıralama
```python
a = float(input("1. sayı: "))
b = float(input("2. sayı: "))
c = float(input("3. sayı: "))
sorted_list = sorted([a, b, c])
print("Küçükten büyüğe:", sorted_list)
```

#### Faktöriyel Hesaplama ve Açılımını Yazdırma
```python
n = int(input("Sayı (>=0): "))
if n < 0:
    print("Tanımsız")
else:
    fact = 1
    parts = []
    for i in range(1, n+1):
        fact *= i
        parts.append(str(i))
    print("x".join(parts), "=", fact)
```

#### Metindeki İlk Kelime ile Son Kelimeyi Bulma
```python
s = input("Cümle: ").strip()
words = s.split()
if words:
    print("İlk:", words[0], "Son:", words[-1])
else:
    print("Kelime yok")
```

#### Girilen Sayıların Toplamını ve Ortalamasını Bulma
(Kullanıcı istediği kadar sayı girebilir; boş girişle bitirir)
```python
nums = []
while True:
    s = input("Sayı gir (boş = bitir): ")
    if s == "":
        break
    try:
        nums.append(float(s))
    except ValueError:
        print("Geçersiz, atlandı.")
if nums:
    print("Toplam:", sum(nums), "Ortalama:", sum(nums)/len(nums))
else:
    print("Sayı girilmedi")
```

#### Büyük Harfleri Küçük Harflere, Küçük Harfleri Büyük Harflere Dönüştürme
```python
s = input("Metin: ")
print(s.swapcase())
```

#### Personel Maaşından Yüzdesel Zam Hesaplama
```python
maas = float(input("Mevcut maaş: "))
zam_yuzde = float(input("Zam yüzdesi (%): "))
yeni = maas * (1 + zam_yuzde/100)
print("Yeni maaş:", yeni)
```

#### Sayı Değerlerinin Toplamını Hesaplama
(Liste içindeki değerlerin toplamı)
```python
nums = list(map(float, input("Sayıları boşlukla girin: ").split()))
print("Toplam:", sum(nums))
```

#### Kullanıcının Sonsuz Sayıda Girdiği Değerlerin Yanına Tek/Çift Yazma
(Boş girişle bitir)
```python
while True:
    s = input("Sayı (boş=bitir): ")
    if s == "":
        break
    try:
        n = int(s)
        print(n, "Çift" if n % 2 == 0 else "Tek")
    except ValueError:
        print("Geçersiz giriş")
```

#### 1 ile 300 Arasındaki Sayılardan 11 Sayısına Bölünenleri Bulma
```python
print([i for i in range(1, 301) if i % 11 == 0])
```

#### Mutlak Sistemde Sınıfı Geçmek İçin Gereken Final Notunu Hesaplama
(Örnek: vize %40, final %60; geçme notu 50)
```python
vize = float(input("Vize notu: "))
gecme = 50
vize_katsayi = 0.4
final_katsayi = 0.6
# final_needed * final_katsayi + vize * vize_katsayi >= gecme
needed_final = max(0, (gecme - vize * vize_katsayi) / final_katsayi)
print("Gereken final notu:", needed_final)
```

#### Üç Kenarı Girilen Üçgenin Alanını Hesaplama
(Heron's formula)
```python
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
s = (a + b + c) / 2
import math
if a + b > c and a + c > b and b + c > a:
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print("Alan:", area)
else:
    print("Geçerli üçgen değil")
```

#### Metindeki Sesli Harf Sayısını Hesaplama
(Türkçe sesliler: a,e,ı,i,o,ö,u,ü)
```python
s = input("Metin: ").lower()
vowels = set("aeıioöuü")
count = sum(1 for ch in s if ch in vowels)
print("Sesli harf sayısı:", count)
```

#### Her Sayıyı Kendisi Kadar Yan Yana Yazdırma
(Örnek: 3 -> 333)
```python
n = int(input("Sayı: "))
print(str(n) * n)
```

#### Tekrarsız Rastgele Sayı Üretme
(1 ile 100 arası 10 benzersiz sayı)
```python
import random
nums = random.sample(range(1, 101), 10)
print(nums)
```

#### Asal Çarpanlarını Bulma
```python
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1 if i == 2 else 2
    if n > 1: factors.append(n)
    return factors

n = int(input("Sayı: "))
print("Asal çarpanlar:", prime_factors(abs(n)))
```

#### Metindeki En Uzun Kelimeyi Bulma
```python
s = input("Metin: ").strip()
words = [w.strip(".,!?;:") for w in s.split()]
if words:
    longest = max(words, key=len)
    print("En uzun kelime:", longest)
else:
    print("Kelime yok")
```

#### Girilen Bir Notun Harf Karşılığını Bulma
(Örnek harf skalası: >=90 A, >=80 B, >=70 C, >=60 D, else F)
```python
n = float(input("Not: "))
if n >= 90: grade = "A"
elif n >= 80: grade = "B"
elif n >= 70: grade = "C"
elif n >= 60: grade = "D"
else: grade = "F"
print("Harf notu:", grade)
```

#### Cümledeki Her Kelimeyi Tersten Yazdırma
```python
s = input("Cümle: ")
print(" ".join(word[::-1] for word in s.split()))
```

#### Metni Mors Alfabesine Çevirme
(Basit harf->mors sözlüğü; desteklenmeyen karakterler atlanır)
```python
MORSE = {
 'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.',
 'g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..',
 'm':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.',
 's':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
 'y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--',
 '4':'....-','5':'.....','6':'-....','7':'--...','8':'---..',
 '9':'----.','0':'-----',' ':'/'}
s = input("Metin: ").lower()
print(" ".join(MORSE.get(ch, '') for ch in s if ch in MORSE or ch.isalnum()))
```

#### Kümülatif Toplam Hesaplama
(Liste için kümülatif toplamın listesi)
```python
nums = list(map(float, input("Sayıları boşlukla gir: ").split()))
cum = []
total = 0
for x in nums:
    total += x
    cum.append(total)
print("Kümülatif toplamlar:", cum)
```

---


