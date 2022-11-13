import os
import shlex
import openai
import sys
import subprocess
import logging

openai.api_key = os.getenv("INPUT_OPENAIAPIKEY")
openai.organization = "org-5rQrsfeNRldhT14Nt33vg1ut"
MAX_CHARACTERS = 1000
BASE_PROMPT = "Summarize the following code commits in two, three, or four sentences with no more than ten words in any sentence"


def list_commits():
    output = subprocess.run(
        'git log --no-merges --pretty=format:"%s"'.split(" "),
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")[:MAX_CHARACTERS]
    return output


def get_prompt(commits: str):
    return f"{BASE_PROMPT}:\n\n{commits}"


def main(prompt: str):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.9,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    if "choices" in response:
        if len(response["choices"]) > 0:
            if response["choices"][0]["text"]:
                print(shlex.quote(response["choices"][0]["text"]))
            else:
                print("The text reponse contained nothing.")
        else:
            print(
                "Opps sorry, something went wrong with the request to the AI this time."
            )


# if __name__ == "__main__":
logging.debug(f"Starting the commit translation process. {os.getcwd()}")
commits: str = list_commits()
logging.debug(f"The commits: {commits}")
prompt: str = get_prompt(commits)
logging.info(f"The prompt: {prompt}")
main(prompt)
logging.debug("main(prompt) has been successfully run. Goodbye.")
