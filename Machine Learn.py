import pandas as pd
arquivo = pd.read_csv('C:/Users/Z033976/Desktop/Python/archive/wine_dataset.csv')
arquivo.head()

arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

y = arquivo['style']
x = arquivo.drop('style', axis = 1)

from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size = 0.3)

from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

resultado = modelo.score(x_teste, y_teste)
print("Acurária", resultado)