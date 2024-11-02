from crewai import Agent
from tools import yt_tool

import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.environ.get("GROQ_API_KEY")
from crewai import LLM

llm = LLM(
    model="groq/llama3-8b-8192", 
    base_url="https://api.groq.com/openai/v1", 
    api_key=api_key
)
 

#create a senior blog content researcher
blog_researcher = Agent(
    role = 'Blog Researcher from Youtube Videos',
    goal = 'get the relevant video content for the topic {topic} from the YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI , Data Science , Machine Learning and Gen AI and providing suggestions"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True
)

## Creating a content writer agent with YT tools
content_writer = Agent( role = 'Writer',
    goal = 'Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    llm=llm,
    backstory=(
        "With a Flair for simplyfying complex topics, you craft"
        "engage narratives that captivate and educate, bringing new"
        "discoveries to light in accessible manner"
    ),
    tools=[yt_tool],
    allow_delegation=False
)

