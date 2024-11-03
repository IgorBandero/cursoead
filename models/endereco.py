class Endereco:
    
    def __init__(self, rua: str, num_residencia: int, bairro: str, cidade: str, cep: str):
        if isinstance(rua, str):
            self.__rua = rua
        else:
            raise TypeError("Rua deve ser uma string.")
        if isinstance(num_residencia, int):
            self.__num_residencia = num_residencia
        else:
            raise TypeError("Número da residência deve ser um inteiro.")
        if isinstance(bairro, str):
            self.__bairro = bairro
        else:
            raise TypeError("Bairro deve ser uma string.")
        if isinstance(cidade, str):
            self.__cidade = cidade
        else:
            raise TypeError("Cidade deve ser uma string.")
        if isinstance(cep, str):
            self.__cep = cep
        else:
            raise TypeError("CEP deve ser uma string.")

    @property
    def rua(self) -> (str):
        return self.__rua
    
    @rua.setter
    def rua(self, rua: str):
        if not isinstance(rua, str):
            raise TypeError("Rua deve ser uma string.")
        self.__rua = rua

    @property
    def num_residencia(self) -> (int):
        return self.__num_residencia
    
    @num_residencia.setter
    def num_residencia(self, num_residencia: int):
        if not isinstance(num_residencia, int):
            raise TypeError("Número da residência deve ser um inteiro.")
        self.__num_residencia = num_residencia

    @property
    def bairro(self) -> (str):
        return self.__bairro
    
    @bairro.setter
    def bairro(self, bairro: str):
        if not isinstance(bairro, str):
            raise TypeError("Bairro deve ser uma string.")
        self.__bairro = bairro
    
    @property
    def cidade(self) -> (str):
        return self.__cidade
    
    @cidade.setter
    def cidade(self, cidade: str):
        if not isinstance(cidade, str):
            raise TypeError("Cidade deve ser uma string.")
        self.__cidade = cidade

    @property
    def cep(self) -> (str):
        return self.__cep
    
    @cep.setter
    def cep(self, cep: str):
        if not isinstance(cep, str):
            raise TypeError("CEP deve ser uma string.")
        self.__cep = cep
