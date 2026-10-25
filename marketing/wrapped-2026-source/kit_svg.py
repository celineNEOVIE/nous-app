import sys,os
OUT=sys.argv[1]
INK='#4A2A21'
S=f'stroke="{INK}" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"'
star='M50 4l10 34 34 12-34 12-10 34-10-34L6 50l34-12z'
E={
'lotus':f'''<g {S}><path d="M50 78C38 66 36 44 50 22c14 22 12 44 0 56z" fill="#F2D9C7"/><path d="M50 78C34 74 22 58 22 38c16 6 26 22 28 40z" fill="#E8C3A8"/><path d="M50 78C66 74 78 58 78 38c-16 6-26 22-28 40z" fill="#E8C3A8"/><path d="M50 80C34 82 16 74 8 60c16-4 32 4 42 20z" fill="#CFDAC2"/><path d="M50 80c16 2 34-6 42-20-16-4-32 4-42 20z" fill="#CFDAC2"/></g>''',
'eucalyptus':f'''<g {S}><path d="M30 92C40 60 52 36 74 10" fill="none"/><g fill="#B6C6A5"><ellipse cx="34" cy="68" rx="9" ry="15" transform="rotate(-55 34 68)"/><ellipse cx="50" cy="72" rx="8" ry="14" transform="rotate(35 50 72)"/><ellipse cx="44" cy="46" rx="9" ry="15" transform="rotate(-50 44 46)"/><ellipse cx="62" cy="48" rx="8" ry="14" transform="rotate(40 62 48)"/><ellipse cx="60" cy="24" rx="8" ry="13" transform="rotate(-40 60 24)"/><ellipse cx="76" cy="26" rx="7" ry="12" transform="rotate(50 76 26)"/></g></g>''',
'galets':f'''<g {S}><ellipse cx="50" cy="82" rx="38" ry="12" fill="#A9785A"/><ellipse cx="50" cy="62" rx="29" ry="10" fill="#D7B596"/><ellipse cx="50" cy="44" rx="21" ry="8.5" fill="#B6C6A5"/><ellipse cx="50" cy="28" rx="13" ry="7" fill="#EFE3D1"/></g>''',
'tasse-the':f'''<g {S}><path d="M38 30c-6-8 6-12 0-20M52 30c-6-8 6-12 0-20" fill="none"/><path d="M70 52h6a10 10 0 0 1 0 20h-8" fill="none" stroke-width="5"/><path d="M18 40h56v18c0 18-12 28-28 28S18 76 18 58z" fill="#CFDAC2"/><path d="M10 88h72" fill="none"/><circle cx="46" cy="60" r="7" fill="#D7B596"/></g>''',
'bougie':f'''<g {S}><path d="M50 8c10 12 10 22 0 26-10-4-10-14 0-26z" fill="#E9B98A"/><path d="M50 22c4 5 4 9 0 11-4-2-4-6 0-11z" fill="#FFF3D6"/><rect x="34" y="38" width="32" height="52" rx="6" fill="#F7F0E5"/><path d="M34 50c8 4 24 4 32 0" fill="none"/></g>''',
'lune':f'''<g {S}><path d="M58 12a38 38 0 1 0 30 52A30 30 0 1 1 58 12z" fill="#EBD3B5"/><path d="M78 18l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#B6C6A5"/></g>''',
'coeur':f'''<g {S}><path d="M50 86C20 64 10 48 14 32c4-14 24-20 36-4 12-16 32-10 36 4 4 16-6 32-36 54z" fill="#E8C3A8"/></g>''',
'etoile-sauge':f'''<g {S}><path d="{star}" fill="#93A784"/></g>''',
'etoile-beige':f'''<g {S}><path d="{star}" fill="#D7B596"/></g>''',
'etoile-sauge-claire':f'''<g {S}><path d="{star}" fill="#B6C6A5"/></g>''',
'fleche':f'''<g><path d="M22 30h56L50 72z" fill="{INK}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/></g>''',
'scotch-washi':'''<g><path d="M4 32l92-6 0 44-92 6z" fill="#CFDAC2" fill-opacity=".9"/><path d="M4 32l3 4-3 4 3 4-3 4 3 4-3 4 3 4-3 4M96 26l-3 4 3 4-3 4 3 4-3 4 3 4-3 4 3 4" fill="none" stroke="#B6C6A5" stroke-width="1.2"/></g>''',
'confetti-rectangle':f'''<g><rect x="20" y="38" width="60" height="26" rx="4" fill="#93A784" transform="rotate(-18 50 50)"/></g>''',
'confetti-rond':'''<g><circle cx="50" cy="50" r="30" fill="#A9785A"/></g>''',
}
for k,body in E.items():
    with open(os.path.join(OUT,k+'.svg'),'w') as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="1024" height="1024">\n{body}\n</svg>\n')
print(' '.join(E))
