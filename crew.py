from crewai import Crew,Process
from agents import blog_researcher,content_writer
from tasks import research_task,write_task


crew = Crew(
    agents=[blog_researcher,content_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# start the task execution with enhanced feedback
results = crew.kickoff(inputs={'topic':'Create a Large Language Model from Scratch with Python - Tutorial'})
print(results)