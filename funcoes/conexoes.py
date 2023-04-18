from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import sqlalchemy as sa

def conexao_spotify():
    load_dotenv('.env')

    auth_manager = SpotifyClientCredentials(
        client_id=os.getenv('CLIENT_ID'), 
        client_secret=os.getenv('CLIENT_SECRET'))
    spotify = spotipy.Spotify(client_credentials_manager=auth_manager)
    return spotify

def conexao_banco_dados():
    """Conecta com o banco de dados e retorne o objeto engine"""
    load_dotenv('.env')
    conn_str = f"mysql+pymysql://{os.getenv('user')}:{os.getenv('senha')}@{os.getenv('url_banco')}/{os.getenv('nome_db')}"
    engine = sa.create_engine(conn_str)
    return engine