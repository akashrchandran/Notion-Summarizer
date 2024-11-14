import requests


def process_vtt_fillers(text):
    filtered_lines = [line for line in text.split('\n')[1:] if '-->' not in line and line.strip()]
    return '\n'.join(filtered_lines)


def get_file_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def get_vtt_file_from_url(url):
    response = get_file_content(url)
    return process_vtt_fillers(response)


PROMPT = """"Summarize concepts, knowledge, advices and ideas from the Video Transcript text with a Summary text of at least {} words and Takeaways bullet points. Use heading as keys. Add codes and other examples if need make summary more elaborate and easy to understand. use markdown format. Do verify the markdown format.
Transcript:
{}
"""
def prompt_formater(transcript):
    word_count = max(len(transcript.split()) * 0.5, 300)
    return PROMPT.format(word_count, transcript)