import os
from apps.graph import build_graph

if os.getenv("OPENAI_API_KEY") is None:
    import getpass
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

app = build_graph()

request = input(
    "What email do you need?\n> "
)

result = app.invoke({
    "request": request
})

print("\n===== FINAL EMAIL =====\n")
print(result["final_email"])
