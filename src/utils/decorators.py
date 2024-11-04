from functools import wraps


#  Decorator para tratar as exceções da aplicação
#  É necessário criar a função mostrar_erro na classe que deseja utilizar
def tratar_excecoes(metodo):
    @wraps(metodo)
    def wrapper(self, *args, **kwargs):
        try:
            return metodo(self, *args, **kwargs)
        except Exception as e:
            self.mostrar_erro(str(e))
    return wrapper
