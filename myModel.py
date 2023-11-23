from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

from myKey import api_key
import os
os.environ["OPENAI_API_KEY"] = api_key
llm = openai.OpenAI(temperature=0.7)

def resturant(cusine):
    #chain1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=["cusine"],
        template="""I want to open a restaurant for {cusine} food. Suggest a fancy name for this."""
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
    
    #chain2: Restaurant Menu
    prompt_template_menu = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""I want to open a {restaurant_name} restaurant. Suggest a menu for this restaurant. Return it as comma separated string"""
    )
    menu_chain = LLMChain(llm=llm, prompt=prompt_template_menu, output_key="menu")
    
    chain = SequentialChain(
        chains=[name_chain, menu_chain],
        input_variables=["cusine"],
        output_variables=['restaurant_name', 'menu']
        )
    response = chain({"cusine": cusine})
    
    return response

if __name__ == "__main__":
    print(resturant("Chinese"))