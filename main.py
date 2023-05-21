import decimal
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv


def main():
    load_dotenv()
    llm = OpenAI()
    llm.openai_api_key = os.environ.get("OPENAI_API_KEY")
    llm.temperature = 0.9
    # print(llm.temperature)

    prompt = PromptTemplate(
        input_variables=["product"],
        template="Suggest three names for a company that makes {product}?",
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    query = input("\nEnter your query: ")
    print(chain.run(query))


if __name__ == "__main__":
    main()
