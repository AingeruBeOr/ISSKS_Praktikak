# 1.

- `md5sum <fitx_direk>`
- `sudo apt install stegosuite`
- `stegosuite`

# 2. 

- `sudo apt install gpg`
- `gpg --help`

## 2.1 

- `gpg --generate-key`
- `gpg --full-generate-key`
- `gpg --list-keys`
- `gpg --generate-revocation <user_id>`
- `gpg --export -a <user_id>`
- `gpg --export -a <user_id> > <fitxategi_izena>.key` edo `gpg --export -a <user_id> --output <fitxategi_izena>.key`
- `gpg --export-private-key -a <user_id> > <fitxategi_izena>.key`
- `gpg --import <fitxategi_izena>.key`
- `gpg --delete-keys <gako_ID>`

## 2.2

- `gpg -e <fitxategi_izena>`
- `gpg -e -r <user_ID_public_key> -a <fitxategia>`
- `gpg -c <fitxategia>`
- `gpg -d <fitxategi_izena>`
- `gpg -d <fitxategi_zifratua> > <fitxategi_dezifratua>`

## 2.3

- `gpg --sign-key <correo_electronico>`
- `gpg --edit-key` , trust , quit (edo q)
- `gpg --output Artxiboa.sig --sign Artxiboa.pdf`
- `gpg --output Artxiboa.sig --sign Artxiboa.pdf`
- `gpg --verify <fitxategia>`

## 2.4 

- `git config --global user.signingKey <GPG_gakoa>`
- `git commit -S -m "<commit testua>"`

## 2.5 

- `gpg --gen-revoke <user_id>`
