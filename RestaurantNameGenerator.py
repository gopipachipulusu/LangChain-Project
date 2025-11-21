# Langchain crash course
# from secret_key import openapi_key
# import os
# os.environ['OPENAI_API_KEY'] = openapi_key

import os
os.environ['OPENAI_API_KEY'] = "add your key here"
## LLMs
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
name = llm.predict("I want to open a restaurant for Indian food. Suggest a fency name for this.")
print(name)
llm("I want to open a restaurant for Indian food. Suggest a fency name for this.")
## Prompt Templates
from langchain.prompts import PromptTemplate

prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
)
p = prompt_template_name.format(cuisine="Italian")
print(p)

# print(llm.predict(p))
## Chains
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt_template_name)
chain.run("Mexican")
chain = LLMChain(llm=llm, prompt=prompt_template_name, verbose=True)
chain.run("Mexican")
llm = OpenAI(temperature=0.6)

prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
)

name_chain =LLMChain(llm=llm, prompt=prompt_template_name)

prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template="""Suggest some menu items for {restaurant_name}"""
)

food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items)
#### Simple Sequential Chain
from langchain.chains import SimpleSequentialChain
chain = SimpleSequentialChain(chains = [name_chain, food_items_chain])

content = chain.run("Indian")
print(content)
#### Sequential Chain
llm = OpenAI(temperature=0.7)

prompt_template_name = PromptTemplate(
    input_variables =['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fency name for this."
)

name_chain =LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")
llm = OpenAI(temperature=0.7)

prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template="Suggest some menu items for {restaurant_name}."
)

food_items_chain =LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
from langchain.chains import SequentialChain

chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', "menu_items"]
)
chain({"cuisine": "Indian"})
## Agents
# make sure yoy have installed this package: pip install google-search-results
# from secret_key import serpapi_key
# os.environ['SERPAPI_API_KEY'] = serpapi_key

os.environ['SERPAPI_API_KEY'] = "add your serpapi key here"
#### serpapi and llm-math tool
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)

# The tools we'll give the Agent access to. Note that the 'llm-math' tool uses an LLM, so we need to pass that in.
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Let's test it out!
agent.run("What was the GDP of US in 2022 plus 5?")
#### Wikipedia and llm-math tool
# install this package: pip install wikipedia

# The tools we'll give the Agent access to. Note that the 'llm-math' tool uses an LLM, so we need to pass that in.
tools = load_tools(["wikipedia", "llm-math"], llm=llm)

# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

# Let's test it out!
agent.run("When was Elon musk born? What is his age right now in 2023?")
## Memory
chain = LLMChain(llm=llm,prompt=prompt_template_name)
name = chain.run("Mexican")
print(name)
name = chain.run("Indian")
print(name)
chain.memory
type(chain.memory)
#### ConversationBufferMemory
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

chain = LLMChain(llm=llm, prompt=prompt_template_name, memory=memory)
name = chain.run("Mexican")
print(name)
name = chain.run("Arabic")
print(name)
print(chain.memory.buffer)
#### ConversationChain
from langchain.chains import ConversationChain

convo = ConversationChain(llm=OpenAI(temperature=0.7))
print(convo.prompt.template)
convo.run("Who won the first cricket world cup?")
convo.run("How much is 5+5?")
convo.run("Who was the captain ofthe winning team?")
print(convo.memory.buffer)
#### ConversationBufferWindowMemory
from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=1)

convo = ConversationChain(
    llm=OpenAI(temperature=0.7),
    memory=memory
)
convo.run("Who won the first cricket world cup?")
convo.run("How much is 5+5?")
convo.run("Who was the captain of the winning team?")