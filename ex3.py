class Article():
    TVA = 0.20
    def __init__(self, nom:str, code:int, prixHT:float):
        self.__nom = nom
        self.__code = code
        if prixHT <= 0:
            raise ValueError
        self.__prixHT = prixHT
    def __str__(self):
        return f"Je suis un {self.nom}, de code {self.code} et je coûte {self.prixHT}€ en HT"
    @property
    def nom(self):
        return self.__nom
    @property
    def code(self):
        return self.__code
    @property
    def prixHT(self):
        return self.__prixHT
    @nom.setter
    def nom(self, val:str):
        if isinstance(val, str):
            self.__nom = val
        else:
            raise TypeError("la valeur n'est pas un str")
    @code.setter
    def code(self, val:int):
        if isinstance(val, int):
            self.__code = val
        else:
            raise TypeError("la valeur n'est pas une série de chiffres")
    @prixHT.setter
    def prixHT(self, val:float):
        if isinstance(val, float):
            self.__prixHT = val
        else:
            raise TypeError("la valeur n'est pas un chiffre")
    def prixTTC(self):
        prix = self.prixHT * (1 + self.TVA)
        return prix

class Stock():
    def __init__(self, **articles: Article):
        self.__articles = articles
    def __str__(self):
        stock_str = "Le stock contient : \n"
        for article in self.articles['articles']:
            stock_str += str(self.articles['articles'][article]) + "\n"
        return stock_str
    @property
    def articles(self):
        return self.__articles
    def taille(self):
        i = 0
        for dict in self.articles.values():
            for article in dict:
                i += 1
        return i
    def ajout(self, article:Article):
        try:
            if article.code in self.articles['articles']:
                raise ValueError("un article avec ce code barre existe déjà")
        except AttributeError as err:
            return f"ERREUR {err} : la paramètre n'est pas un article"
        else:
            self.articles['articles'][article.code] = article
    def recherche():
        0
    def recherche():
        0
    def supprime():
        0
    def supprime():
        0

def main():
    try:
        art1 = Article("art1", 42549630, 15.3)
        art2 = Article("art2", 13548927, 9.8)
    except ValueError:
        print("ERREUR : le prix HT est égal ou inférieur à 0")
    else:
        TTC = art1.prixTTC()
        print(TTC)
    
    try:
        articles = {art1.code:art1, art2.code:art2}
    except AttributeError as err:
        print(f"ERREUR, {err} : une des options n'est pas un article")
    else:
        stock = Stock(articles=articles)
        print(stock)
        taille = stock.taille()
        print(taille)
        art3 = 0
        stock.ajout(art3)
        print(stock)

if __name__ == '__main__':
    main()