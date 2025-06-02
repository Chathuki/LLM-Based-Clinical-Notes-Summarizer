from langchain.prompts import PromptTemplate
from langchain_community.llms import GPT4All

def load_llm(model_path):
    return GPT4All(model=model_path, backend='gpt4all', verbose=False)

def summarize_text(text, llm):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following clinical notes clearly:\n\n{text}\n\nSummary:"
    )
    chain = prompt | llm
    return chain.invoke({"text": text})
