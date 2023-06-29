import pandas as pd
import numpy as np

print('Lendo arquivo...')

df = pd.read_excel(r'D:\faculdade\mtg_data\cards.xlsx')

print('Filtrando Colunas...')

df_filtered = pd.DataFrame(df,
                      columns=['colorIdentity','colors','edhrecRank','edhrecSaltiness', 'manaCost','manaValue','name','originalReleaseDate','originalText','originalType','printings','rarity','setCode','subtypes', 'supertypes', 'text','power', 'toughness', 'type', 'types','targetType','colorName'])

print('Filtrando texto de efeito...')

df_dmg = df_filtered[df_filtered['originalText'].str.contains(r"deals [xX0-9] damage", na=False)]

print('Criando coluna de cores...')

list_color = []

for c in df_dmg['colorIdentity'].tolist():
    if c == 'W': list_color.append('White')
    elif c == 'B': list_color.append('Black')
    elif c == 'G': list_color.append('Green')
    elif c == 'U': list_color.append('Blue')
    elif c == 'R': list_color.append('Red')
    elif c == 'U, W': list_color.append('Azorius')
    elif c == 'R, W': list_color.append('Boros')
    elif c == 'G, W': list_color.append('Selesnya')
    elif c == 'B, W': list_color.append('Orzhov')
    elif c == 'B, U': list_color.append('Dimir')
    elif c == 'B, G': list_color.append('Golgari')
    elif c == 'R, U': list_color.append('Izzet')
    elif c == 'G, U': list_color.append('Simic')
    elif c == 'B, R': list_color.append('Rakdos')
    elif c == 'G, R': list_color.append('Gruul')
    elif c == 'B, U, W': list_color.appen('Esper')
    elif c == 'B, G, R': list_color.append('Jund')
    elif c == 'G, R, W': list_color.append('Naya')
    elif c == 'G, U, W': list_color.append('Bant')
    elif c == 'B, G, W': list_color.append('Abzan')
    elif c == 'R, U, W': list_color.append('Jeskai')
    elif c == 'B, G, U': list_color.append('Sultai')
    elif c == 'B, R, W': list_color.append('Mardu')
    elif c == 'B, R, U, W': list_color.append('Yore-Tiller')
    elif c == 'B, G, R, U': list_color.append('Glint-Eye')
    elif c == 'B, G, R, W': list_color.append('Dune-Brood')
    elif c == 'G, R, U, W': list_color.append('Ink-Treader')
    elif c == 'B, G, U, W': list_color.append('Witch-Maw')
    elif c == 'B, G, R, U, W': list_color.append('5 Color')
    else: list_color.append('Colorless')


df_dmg['colorName'] = list_color

print('Criando coluna de targets...')

list_target = []

for t in df_dmg['text'].tolist():
    if "to target" in t or "any target" in t:
        list_target.append('target')
    elif "to each" in t:
        list_target.append('each')
    elif "to you" in t:
        list_target.append('you')
    else:
        list_target.append('other')


df_dmg['targetType'] = list_target

print('Criando Arquivo...')

df_dmg.to_excel(r'D:\faculdade\mtg_data\df_dmg.xlsx', index=None, header=True)

print('Arquivo Criado.')