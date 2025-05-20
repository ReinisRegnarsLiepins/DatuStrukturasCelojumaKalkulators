# Erasmus ceļojumu budžeta uzskaites programma

Šī ir vienkārša Python konsoles programma, kas ļauj uzskaitīt Erasmus ceļojumu izdevumus un budžetu. Programma ļauj veidot vairākus ceļojumus, pievienot izdevumus, pārskatīt atlikumu un saglabāt datus nākamajai palaišanas reizei.

## Funkcijas

- Vairāku ceļojumu izveide un pārvaldība
- Izdevumu pievienošana ar iespēju norādīt, vai tie ir atmaksājami
- Ceļojuma kopsavilkums ar atlikumu un pārtēriņu
- Saglabāšana un ielāde ar pickle bibliotēku (failā data.pkl)
- Vienkārša komandu ievade no konsoles

## Prasības

- Python 3.6 vai jaunāks
- Nav nepieciešamas papildu bibliotēkas

## Palaišana

1. Lejupielādē vai nokopē failus uz datoru.
2. Palaiž `main.py` failu:

## Komandas

Visas komandas raksta formātā:
komanda -args1 -args2 -args3 ...

Piemērs:
new -Itālija -300

Pieejamās komandas:

- `help` — Parāda visu komandu sarakstu
- `new -nosaukums -summa` — Izveido jaunu ceļojumu
- `select -indekss` — Izvēlas ceļojumu rediģēšanai
- `deselect` — Noņem izvēli no aktīvā ceļojuma
- `show trip` — Parāda atlasītā ceļojuma kopsavilkumu
- `show expenses` — Parāda visus izdevumus
- `show all` — Parāda visus ceļojumus
- `edit trip -nosaukums/summa -vērtība` — Rediģē ceļojumu
- `add expense -summa -transports [-vai_atmaksājams] [-piezīmes]` — Pievieno izdevumu
- `remove expense -indekss` — Dzēš izdevumu pēc kārtas numura
- `save` — Saglabā visus datus failā
- `exit` — Iziet no programmas

## Failsistēma

- `main.py` — Galvenais programmas fails ar komandu loģiku
- `trip.py` — Ceļojuma un izdevumu klases
- `linkedList.py` — Vienkārša saistītā saraksta struktūra
- `textPrompts.py` — Palaišanas un palīdzības teksts
- `data.pkl` — Failā tiek automātiski saglabāti dati

## Autors

Reinis Liepiņš (241RDB307)
