from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

def query_chat(information):

    summary_template = """
        Stwórz mi zdania według szablonu, Jeżeli możesz stworzyć zdanie w pierwszej osobie liczby pojedyńczej, to, to zrób, twórz możliwie proste zdania:

        Podam ci w następnych wiadomościach frazy, które chce wykorzystać i ile chciałbym, żebyś wygenerował zdań, dobrze? Jeżeli nie podam żadnej liczby to domyślnie stwórz 1 zdanie

        <szablon>
        ---

        "<w tym miejscu zdania w języku angielskim 1>"
        // NOTE "<fraza w języku angielskim>" - "<fraza w języku polskim>"

        ---
        </szablon>

        Gdzie fraza to: {information}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(model_name="gpt-4o-mini")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(f"Doing... {information}")

    with open("./storage/output.txt", "a") as file:
        file.write(res.content + "\n")

if __name__ == "__main__":
    load_dotenv()

    with open("./storage/input.txt", "r") as file:
        for line in file:
            information = line.strip()
            query_chat(information)


