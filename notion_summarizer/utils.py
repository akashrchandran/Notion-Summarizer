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