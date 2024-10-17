from langchain_core.prompts import PromptTemplate
from langchain_core.callbacks import StreamingStdOutCallbackHandler
from langchain_huggingface import HuggingFaceEndpoint
from langchain.chains.llm import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()

endpoint_url = "https://vl5mckr989noncb7.us-east-1.aws.endpoints.huggingface.cloud"

llm = HuggingFaceEndpoint(
    endpoint_url=endpoint_url,
    max_new_tokens=1024,
    top_k=10,
    top_p=0.95,
    typical_p=0.95,
    temperature=0.01,
    repetition_penalty=1.03,
    streaming=True,
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

def create_prompt_template(input):
    system = """Write a cover letter for the Job title at the company mentioned, 
            incorporating the candidate’s relevant experiences, qualifications, and skills from their resume, 
            and aligning them with the responsibilities and requirements listed in the job description. 
            Show the candidate’s enthusiasm for working for the company mentioned by including specific reasons why the 
            candidate is interested in this company and how their background makes them a great fit."""
    
    # Correctly format the template
    template = """<|begin_of_text|><|start_header_id|>system<|end_header_id|>{system}<|eot_id|><|start_header_id|>user<|end_header_id|>{input}<|eom_id|>"""
    
    # Create PromptTemplate instance
    prompt = PromptTemplate.from_template(template=template)
    
    # Format the prompt with the given system and input
    return prompt.format(system=system, input=input)

def create_output_chain(prompt):
    chain = LLMChain(llm=llm,
                     prompt=prompt,
                     callbacks=[StreamingStdOutCallbackHandler()])
    return chain
    
    