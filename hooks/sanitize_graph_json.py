import json
from pathlib import Path


def on_post_build(config, **kwargs):
    graph_path = Path(config["site_dir"]) / "graph" / "graph.json"
    if not graph_path.exists():
        return

    data = json.loads(graph_path.read_text(encoding="utf-8"))
    for node in data.get("nodes", []):
        node.pop("path", None)

    graph_path.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
