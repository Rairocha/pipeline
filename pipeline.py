from funcoes.extracao import read_from_gsheets
from funcoes.conexoes import conexao_spotify
from funcoes.conexoes import conexao_banco_dados
from funcoes.transformacao import artista_uri
from funcoes.carregamento import carregar

tb_festivals = read_from_gsheets(
    "https://docs.google.com/spreadsheets/d/1aUiwstZKEENiw3KAT1CCCXcji1iLWdCL_HwngvLxzJc/edit?usp=sharing"
)

spotify = conexao_spotify()
engine = conexao_banco_dados()

tb_festivals['uri_artista'] =  tb_festivals['headliners'].apply(artista_uri,spotify=spotify)

carregar(tb_festivals,'headliner', engine)