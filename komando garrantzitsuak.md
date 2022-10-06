# 1. Komando garrantzitsuak

- GnuPG (GPG) instalatu: `sudo apt install gpg`
- GPG-ren laguntza erabili: `gpg --help`

## 1.1 Gakoak sortu

- GPG-n gako pare bat, pribatua eta publikoa, sortu: `gpg --generate-key`
- Gakoak bere sorkuntzan personalizatzeko: `gpg --full-generate-key`
- Gure GPG sisteman sortuta dauden gakoak ikusteko: `gpg --list-keys`
- Errebokazio ziurtagiria sortzeko: `gpg --generate-revocation <user_id>`
- Klabe publikoa pantailatik ikusteko: `gpg --export -a <user_id>`
- Klabe publikoa fitxategi batean lortzeko: `gpg --export -a <user_id> > <fitxategi_izena>.key` edo `gpg --export -a <user_id> --output <fitxategi_izena>.key`
- Klabe pribatua esportatzeko: `gpg --export-private-key -a <user_id> > <fitxategi_izena>.key`
- Klabe publiko bat sisteman importatzeko: `gpg --import <fitxategi_izena>.key`

## 1.2 Zifraketa

- Fitxategi bat zifratzeko: `gpg -e <fitxategi_izena>`
- Fitxategi bat desenkriptatzeko: `gpg -d <fitxategi_izena>`
- Fitxategi bat desnekriptatzeko, eta beste fitxategi batean gordetzeko: `gpg -d <fitxategi_zifratua> > <fitxategi_dezifratua>`

## 1.3 Sinadurak

- Klabe publiko bat sinatzeko: `gpg --sign-key <correo_electronico>`
- Norbaiteko konfiantza maila aldatzeko: `gpg --edit-key` , trust , quit (edo q)
- Artxibo bat sinatzeko: `gpg --output Artxiboa.sig --sign Artxiboa.pdf`
- Fitxategi bat egiaztatzeko GPG sisteman kargatuta dugun identitate batena dela benetan: `gpg --output Artxiboa.sig --sign Artxiboa.pdf`
- Klabe bat GPG sistematik ezabatzeko: `gpg --delete-keys <gako_ID>`

## 1.4 Git-en commit-etan sinadura aplikatu

- Gure makinan gure GPG gakoa sartzeko: `git config --global user.signingKey <GPG_gakoa>`
- Commit bat sinatzeko (gure GitHub kontuan jadanik egon behar da gako publikoa igota): `git commit -S -m "<commit testua>"`

## 1.5 Beste batzuk

- Klabe bat errebokatzeko: `gpg --gen-revoke <user_id>`

GPG gakoa = ID user = fingerprint 