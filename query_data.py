import argparse
# from dataclasses import dataclass
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

openai_api = os.getenv("OPENAI_API_KEY")


CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You will assist a crew member in identifying the root cause of an alarm and recommending appropriate actions:

Specific Requirements:
Associated sensor(s)
Sensor measuring point(s)
Sensor description
Sensor measuring range
Related system(s)
Dependent system(s)
Related sensors
Potential Triggers: Identify possible causes of the alarm, including:
Temperature, pressure, or power exceeding threshold setpoints
Engine shutdown
Sensor failure
Crew Member Guidance: Provide recommended actions for the crew member to take in response to the alarm, considering.
Based on this context:
{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB.
    embedding_function = OpenAIEmbeddings(openai_api_key=openai_api)
    db = Chroma(persist_directory=CHROMA_PATH,
                embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=6)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join(
        [doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = ChatOpenAI(openai_api_key=openai_api, model_name="gpt-4o", temperature=0)

    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)


if __name__ == "__main__":
    main()
