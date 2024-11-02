from crewai import Task
from tools import yt_tool
from agents import blog_researcher,content_writer

# research task

research_task = Task(
    description = (
        "Identify the video {topic}."
        "Get deatialed information about the video from the channel"
    ),
    expected_output='A comprehensive 3 Paragraphs long report based on {topic} the video content',
    tools=[yt_tool],
    agent=blog_researcher
)

write_task = Task(
    description = (
        "Get the info from youtube channel on the topic {topic}"
    ),
    expected_output='Suumarize the info from the Yt channel video on the topic {topic} and create the content for the blog',
    tools=[yt_tool],
    agent=content_writer,
    async_execution=False,
    output_file='new-blog-post.md'
)