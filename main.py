import os
import openai
import sys
import subprocess
import logging

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-5rQrsfeNRldhT14Nt33vg1ut"

# prompt = "Summarize the following commits from the developer, in at least one sentence but up to four sentences, that comprise a paragraph. :sparkles: means 'new':\n\n:sparkles: add initial Dockerfile\n:sparkles: add yaml specification for commit-meaning action\n:sparkles: :notebook: add initial documentation overview for commit-meaning\n:sparkles: add initial entrypoint barebones"
# prompt = "Generate a blog on the topic: digital marketing in music using b00st.com."


def list_commits():
    return subprocess.run(
        'git log --no-merges --pretty=format:"%s"'.split(" "),
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")


def get_prompt(commits: str):
    return f"Summarize the following commits from the developer, in at least one sentence but up to four sentences, that comprise a paragraph:\n\n{commits}"


def main(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    if "choices" in response:
        if len(response["choices"]) > 0:
            if response["choices"][0]["text"]:
                print(response["choices"][0]["text"])
            else:
                print("The text reponse contained nothing.")
        else:
            print(
                "Opps sorry, something went wrong with the request to the AI this time."
            )


if __name__ == "__main__":
    logging.debug("Starting the commit translation process.")
    commits: str = list_commits()
    logging.debug(f"The commits: {commits}")
    prompt: str = get_prompt(commits)
    logging.info(f"The prompt: {prompt}")
    main(prompt)
    logging.debug("main(prompt) has been successfully run. Goodbye.")
