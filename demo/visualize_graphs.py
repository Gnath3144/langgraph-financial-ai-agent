# visualize_graphs.py
import sys, types
m = types.ModuleType('uuid_utils'); m.compat = types.ModuleType('uuid_utils.compat'); m.compat.uuid7 = lambda: __import__('uuid').uuid4(); sys.modules['uuid_utils'] = m; sys.modules['uuid_utils.compat'] = m.compat

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import build_utils

def draw_demo1():
    nodes = {
        "start": (1.0, 3.0, "START", 1.2, 0.8, "accent"),
        "process": (3.5, 3.0, "process\n(upper case)", 1.8, 1.0, "subtle"),
        "end": (6.0, 3.0, "END", 1.2, 0.8, "accent")
    }
    connections = [
        ("start", "process", ""),
        ("process", "end", "")
    ]
    os.makedirs("assets", exist_ok=True)
    build_utils.generate_diagram(nodes, connections, "Demo 01: Basic LangGraph flow", "assets/demo1_graph.png")
    print("Demo 1 graph generated successfully at assets/demo1_graph.png")

def draw_demo7():
    nodes = {
        "start": (1.0, 3.0, "START", 1.2, 0.8, "accent"),
        "classifier": (3.2, 3.0, "classifier\n(Classifier Node)", 2.0, 1.0, "subtle"),
        "even": (6.0, 4.5, "even\n(Even Node)", 1.8, 1.0, "subtle"),
        "odd": (6.0, 1.5, "odd\n(Odd Node)", 1.8, 1.0, "subtle"),
        "end": (8.5, 3.0, "END", 1.2, 0.8, "accent")
    }
    connections = [
        ("start", "classifier", ""),
        ("classifier", "even", "even"),
        ("classifier", "odd", "odd"),
        ("even", "end", ""),
        ("odd", "end", "")
    ]
    os.makedirs("assets", exist_ok=True)
    build_utils.generate_diagram(nodes, connections, "Demo 07: Conditional LangGraph flow", "assets/demo7_graph.png")
    print("Demo 7 graph generated successfully at assets/demo7_graph.png")

if __name__ == "__main__":
    draw_demo1()
    draw_demo7()
