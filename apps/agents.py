from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")


def writer_agent(state):
    prompt = f"""
    Write a professional business email.

    Request:
    {state["request"]}
    """

    result = llm.invoke(prompt)

    return {
        "draft": result.content
    }


def human_review(state):
    print("\n===== AI GENERATED EMAIL =====\n")
    print(state["draft"])

    decision = input(
        "\nApprove this email? (y/n): "
    ).strip().lower()

    if decision == "y":
        return {"approved": True}
    else:
        return {"approved": False}


def rewrite_agent(state):
    prompt = f"""
    Rewrite this email to improve clarity and tone.

    {state["draft"]}
    """

    result = llm.invoke(prompt)

    return {
        "draft": result.content
    }


def send_agent(state):
    return {
        "final_email": state["draft"]
    }
