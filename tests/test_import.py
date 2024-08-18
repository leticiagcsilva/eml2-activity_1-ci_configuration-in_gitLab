try:
    from ..model import predict, load_model
    print("Importação bem-sucedida!")
except ImportError as e:
    print(f"Erro de Importação: {e}")
