from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

from netzob.all import *
import binascii



# Входной список строк
messages = PCAPImporter.readFile("/home/vboxuser/TestENvironment/ProtoReverser/input/TCPProtocol.pcap").values()
hex_messages = []
for m in messages:
    hex_messages.append(binascii.hexlify(m.data).decode("ASCII"))
    print(hex_messages)
# Создание числового представления строк с помощью TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(hex_messages)

print(X)
# Задаем диапазон количества кластеров, кластеры начинаются не с нуля
min_clusters = 2
max_clusters = 60

# Списки для сохранения значений суммы квадратов расстояний и индекса силуэта
ssd = []
silhouette_scores = []

i=2
# Перебираем количество кластеров от min_clusters до max_clusters
for k in range(min_clusters, max_clusters+1):
    # Применение алгоритма k-средних
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)

    # Сохраняем значения суммы квадратов расстояний
    ssd.insert(i, kmeans.inertia_)

    # Вычисляем индекс силуэта
    silhouette_scores.insert(i, silhouette_score(X, kmeans.labels_))

    i = i+1

# Визуализация результатов метода локтя
plt.plot(range(min_clusters, max_clusters + 1), ssd, 'bx-')
plt.xlabel('Количество кластеров')
plt.ylabel('Сумма квадратов расстояний')
plt.title('Метод локтя')
plt.show()

# Визуализация результатов индекса силуэта
plt.plot(range(min_clusters, max_clusters + 1), silhouette_scores, 'bx-')
plt.xlabel('Количество кластеров')
plt.ylabel('Индекс силуэта')
plt.title('Индекс силуэта')
plt.show()

# Вычисление оптимального числа кластеров

silmax = max(silhouette_scores)
silmaxind = silhouette_scores.index(silmax)

print(silmax)
print(silmaxind)
