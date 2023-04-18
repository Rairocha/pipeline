import pandas as pd
import numpy as np

def artista_uri(nome_artista,spotify):
    """Procura o nome do artista no spotify e retorna o número identificador(URI) desse artista"""
    try:
        result_artista = spotify.search(q=nome_artista,type='artist')
        df_artistas = pd.json_normalize(result_artista['artists']['items'])
        mask_artistas = df_artistas['name'].str.title() == nome_artista.title()
        uri = df_artistas[mask_artistas].iloc[0,7]
        return uri
    except:
        return np.nan