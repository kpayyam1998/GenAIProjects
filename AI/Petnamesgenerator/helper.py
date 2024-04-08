import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
load_dotenv()

# Issue i have openly somewhere my openai api key is stored
key="you key"


def generate_pet_name(pet_name,pet_color):
    prompt_template=PromptTemplate(
        input_variables=["animal_name","animal_color"],
        template="I have {animal_name} i want to set cool name for it,it is color {animal_color} suggest me five cool name for  my pet",
    )
    llm=OpenAI(openai_api_key=key,model="gpt-3.5-turbo-instruct",temperature=0.7)
    
    name_chain=LLMChain(llm=llm,prompt=prompt_template,output_key="petname")

    response=name_chain({"animal_name":pet_name,"animal_color":pet_color})
    return response


# if __name__=="__main__":

#     print(generate_pet_name("dog","brown"))

