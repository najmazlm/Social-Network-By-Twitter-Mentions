
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


df = pd.read_excel('mention theeras clean2.xlsx')

G = nx.from_pandas_edgelist(df, source="username", target="mention", create_using=nx.DiGraph())

# Menghitung jumlah kemunculan pasangan 'username' dan 'mention'
edge_weights = df.groupby(['username', 'mention']).size().reset_index(name='weight')

# Menambahkan atribut berat ke grafik
for i, row in edge_weights.iterrows():
    u = row['username']
    v = row['mention']
    if G.has_edge(u, v):
        G[u][v].setdefault('weight', 0)
        G[u][v]['weight'] = row['weight']

# Menetapkan ukuran nodes berdasarkan jumlah hubungan
node_sizes = [G.in_degree(node, weight='weight') * 100 for node in G.nodes]

# Menetapkan ukuran edges berdasarkan berat edges
edge_widths = [G[u][v].get('weight', 0) for u, v in G.edges()]

# Menggambar grafik jaringan
fig = plt.subplots(figsize=(50,50))
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_size=node_sizes, node_color='red')

# Menampilkan grafik
plt.show()

"""
pada setiap running, hasil penempatan nodes akan berbeda
"""

# Dapatkan jumlah nodes
num_nodes = G.number_of_nodes()

# Dapatkan jumlah edges
num_edges = G.number_of_edges()

print("Jumlah nodes:", num_nodes)
print("Jumlah edges:", num_edges)

DC = nx.degree_centrality(G)

# Convert the 'DC' dictionary into a Pandas Series
centrality_series = pd.Series(DC)

# Use the 'nlargest' function to get the top 10 greatest centrality values
top_10_centrality = centrality_series.nlargest(10)

# Convert the resulting Series back into a Pandas DataFrame
top_10_df = top_10_centrality.to_frame()
