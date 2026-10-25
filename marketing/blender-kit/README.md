# Kit Blender – Noûs Bilan 2026

Tous les éléments de la vidéo `marketing/nous-wrapped-2026.mp4` (format 1080×1920, 50,5 s), prêts pour une mise en scène 3D dans Blender.

## Contenu

| Dossier | Contenu |
|---|---|
| `assets/svg/` | Éléments vectoriels d'origine : lotus, eucalyptus, galets, tasse-the, bougie, lune, coeur, étoiles (sauge, beige, sauge-claire), flèche, scotch-washi, confettis (rectangle, rond). |
| `assets/png/autocollant/` | Les mêmes éléments en PNG transparent **avec le contour blanc d'autocollant** (comme dans la vidéo), ≥ 1200 px sur le petit côté, sans ombre portée. |
| `assets/png/sans-contour/` | Les mêmes éléments, sans contour blanc. |
| `assets/png/pastilles/` | Les pastilles de texte de la vidéo (BILAN 2026, RECORD, 22 JUIN · CRÉATION DE L'APPLI, etc.) et les numéros 1 à 4 du classement, en PNG transparent. |
| `assets/png/mascottes/` | Les 7 nuages Noûs détourés en autocollants. |
| `assets/photos/` | Photos carrées des 8 praticien·nes (500 px). |
| `palette/` | `palette-nous.json` (hex, sRGB et valeurs linéaires pour Blender), `.css`, `.gpl` (GIMP/Krita/Inkscape), nuancier `.png`. |
| `fonts/` | Caveat (titres manuscrits) et Nunito (textes, chiffres) en TTF + licences OFL. |

## Utilisation dans Blender

- **PNG** : *Ajouter › Image › Image en tant que plans* (Images as Planes). Le contour blanc est dans le PNG. Les ombres viennent de l'éclairage de la scène.
- **SVG** : *Fichier › Importer › Scalable Vector Graphics*. Les SVG deviennent des courbes, qu'on peut extruder pour donner de l'épaisseur. Blender importe les remplissages mais pas les traits : les contours marron (`#4A2A21`, épaisseur 2,6 sur 100) se recréent avec *Solidify* ou un matériau de contour.
- **Couleurs** : dans un matériau, saisir le **hex** dans la pipette (Blender convertit tout seul) ou utiliser les valeurs `blender_lineaire_0_1` du JSON.
- **Polices** : objet Texte › *Propriétés des données de l'objet › Police* › charger le `.ttf`. Titres : `Caveat-Bold`. Chiffres : `Nunito-Black`. Textes : `Nunito-ExtraBold`.

## Styles

- Fond crème `#F7F0E5` avec un quadrillage papier : traits `rgba(150,120,95,0.13)`, 2 px tous les 54 px.
- Autocollants : contour blanc `#FFFDF8`, légère rotation (−8° à +8°), ombre douce `rgba(74,42,33,0.22)`.
- Pastilles : bord marron `#4A2A21` de 4 px, ombre dure décalée de 10 px vers le bas.

## Déroulé de la vidéo (textes exacts)

1. **0–4,5 s · Intro** (fond crème quadrillé) : nuage lunettes-collier, « Noûs », pastille BILAN 2026, « Notre année bien-être, en chiffres ».
2. **4,5–9,5 s · Total** (sauge clair) : « Cette année, vous avez réservé » **25 788 €** « de séances bien-être avec nos praticien·nes », pastille CRÉDIT D'IMPÔT -50 %, nuage chèque-billet.
3. **9,5–17 s · Mois après mois** (crème) : « Chiffre d'affaires 2026 », barres janv. 500 · févr. 500 · mars 500 · avril 4 335 · mai 2 462 · juin 4 018 · juil. 3 138 · août 835 · sept. 3 500 · **oct. 6 000 €** (barre sauge + RECORD). Pastille « 22 JUIN · CRÉATION DE L'APPLI » avec flèche sur juin. Nuage chapeau d'été.
4. **17–22 s · Meilleur mois** (marron clair) : « Notre meilleur mois » **Octobre**, **6 000 €**, +71 % VS SEPTEMBRE, confettis.
5. **22–28 s · Vos plus grosses demandes** (sauge clair) : 1 Gestion du stress · 2 Relations & couple · 3 Émotions · 4 Santé de la femme, nuage tableau France + EN CABINET OU EN VISIO.
6. **28–35 s · Nos praticien·nes** (crème quadrillé) : pastille N°1 DES VENTES EN 2026. 8 fiches façon Polaroïd par ordre alphabétique : Émilie Béchard (Kinésiologue, ★ 5,0 · 57 avis), Camille Chopinot (Naturopathe, ★ 5,0 · 26), Sophie Clouet (Coach santé, ★ 5,0 · 26), Océane Danjon (Psycho-corporel, ★ 5,0 · 32), Valérie Elineau (Sophrologue, ★ 5,0 · 100), Nathalie Garnier (Méditation), Laurence Giudicelli (Psychothérapeute, ★ 4,8 · 60), Clara Regnier (Thérapeute holistique).
7. **35–41,5 s · app-nous.fr** (crème foncé) : « a la cote depuis son lancement », DU 22 JUIN À FIN OCTOBRE 2026, 2,6k sessions · 2,2k visiteurs · 4,4k pages vues · 12k interactions, courbe qui finit au plus haut + OCTOBRE AU TOP, nuage téléphone.
8. **41,5–46 s · Crédit d'impôt** (marron clair) : nuage déclaration d'impôt, **50 %** « de crédit d'impôt sur chaque séance, imposable ou non », « soit jusqu'à 12 894 € remboursés à nos client·es ».
9. **46–50,5 s · Merci !** (crème quadrillé) : nuage zen, « Pour cette belle année à prendre soin de vous », APP-NOUS.FR, @nous.zen.

Sources HTML de la vidéo actuelle : `marketing/wrapped-2026-source/`.
