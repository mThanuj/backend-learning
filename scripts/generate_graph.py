import re
from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx

ROOT = Path(__file__).resolve().parents[1]

IGNORE = {
    ".git",
    ".github",
    ".obsidian",
    "assets",
    "scripts",
    "__pycache__",
    "00_System",
}

graph = nx.Graph()

wiki_pattern = re.compile(r"\[\[([^\]|#]+)")

markdown_files = []

for file in ROOT.rglob("*.md"):
    if any(part in IGNORE for part in file.parts):
        continue
    markdown_files.append(file)

name_to_path = {}

for file in markdown_files:
    name = file.stem
    name_to_path[name] = file
    graph.add_node(name)

for file in markdown_files:

    source = file.stem

    text = file.read_text(encoding="utf-8", errors="ignore")

    links = wiki_pattern.findall(text)

    for target in links:
        target = target.strip()

        if target in name_to_path:
            graph.add_edge(source, target)

print(f"Nodes : {graph.number_of_nodes()}")
print(f"Edges : {graph.number_of_edges()}")

if graph.number_of_nodes() == 0:
    raise RuntimeError("No markdown files found.")

degree = dict(graph.degree())

sizes = []

for node in graph.nodes():
    sizes.append(300 + degree[node] * 120)

plt.figure(figsize=(18, 18))

pos = nx.spring_layout(graph, k=0.55, iterations=100, seed=42)

nx.draw_networkx_edges(graph, pos, alpha=0.28, width=0.6)

nx.draw_networkx_nodes(
    graph,
    pos,
    node_size=sizes,
)

nx.draw_networkx_labels(
    graph,
    pos,
    font_size=8,
)

plt.axis("off")

output = ROOT / "assets" / "knowledge_graph.png"

plt.savefig(
    output,
    dpi=300,
    bbox_inches="tight",
)

print(f"Saved to {output}")
