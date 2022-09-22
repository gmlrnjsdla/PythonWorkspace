import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels
from statsmodels.graphics.mosaicplot import mosaic

titanic = sns.load_dataset('titanic')
# print(titanic.info())

titanic = titanic[['survived', 'pclass', 'sex']]

titanic["SURVIVE"] = titanic.survived.map({0 : "DEAD", 1: "ALIVE"})
titanic["CLASS"] = titanic.pclass.map({1: "1ST", 2: "2ND", 3: "3RD"})
titanic["GENDER"] = titanic.sex.map({'male': 'MAN', 'female': 'WOMAN'})
# print(titanic)

# mosaic(titanic.sort_values('CLASS'),['SURVIVE','CLASS'], title='Titanic Survivor Chart')
# mosaic(titanic, ['SURVIVE','GENDER'],title='Titanic Survivor Chart')
mosaic(titanic.sort_values('CLASS'),['CLASS', 'SURVIVE', 'GENDER'])
plt.show()