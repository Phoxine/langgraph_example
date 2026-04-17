from langgraph.graph import StateGraph, END
from apps.state import EmailState
from apps.agents import (
    writer_agent,
    human_review,
    rewrite_agent,
    send_agent
)

def route_review(state):
    if state["approved"]:
        return "send"
    return "rewrite"


def build_graph():
    graph = StateGraph(EmailState)

    graph.add_node("writer", writer_agent)
    graph.add_node("review", human_review)
    graph.add_node("rewrite", rewrite_agent)
    graph.add_node("send", send_agent)

    graph.set_entry_point("writer")

    graph.add_edge("writer", "review")

    graph.add_conditional_edges(
        "review",
        route_review,
        {
            "send": "send",
            "rewrite": "rewrite"
        }
    )

    graph.add_edge("rewrite", "review")
    graph.add_edge("send", END)

    return graph.compile()
