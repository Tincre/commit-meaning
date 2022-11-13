import os
import openai
import subprocess
import logging
from typing import Union

openai.api_key = os.getenv("INPUT_OPENAIAPIKEY")
openai.organization = "org-5rQrsfeNRldhT14Nt33vg1ut"
MAX_CHARACTERS = os.getenv("INPUT_MAXCHARACTERS") or 1000
TEMPERATURE = os.getenv("INPUT_TEMPERATURE") or 0.7
TOKENS = os.getenv("INPUT_TOKENS") or 256
PRESENCE = os.getenv("INPUT_PRESENCEPENALTY") or 0
FREQUENCY = os.getenv("INPUT_FREQUENCYPENALTY") or 0

ADDITIONAL_INSTRUCTION = (
    os.getenv("INPUT_PROMPT_INSTRUCTIONS")
    or "Ignore words between colons, i.e. :"
)
BASE_PROMPT = f"Summarize the following code commits into a single paragraph. Do not use bullet points. Do not use a list. {ADDITIONAL_INSTRUCTION}"


def list_commits():
    output = subprocess.run(
        'git log --no-merges --pretty=format:"%s"'.split(" "),
        stdout=subprocess.PIPE,
        universal_newlines=True,
    ).stdout[:MAX_CHARACTERS]
    return output


def get_prompt(commits: str):
    return f"{BASE_PROMPT}:\n\n{commits}"


def coerce_output(text: str):
    splits = text.strip().split("\n\n")
    if len(splits) > 1:
        return splits[-1]
    return splits[0]


def main(
    prompt: str,
    temperature: float = 0.7,
    tokens: int = 256,
    frequency: Union[float, int] = 0,
    presence: Union[float, int] = 0,
):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=temperature,
        max_tokens=tokens,
        top_p=1,
        frequency_penalty=frequency,
        presence_penalty=presence,
    )
    if "choices" in response:
        if len(response["choices"]) > 0:  # type: ignore
            if response["choices"][0]["text"]:  # type: ignore
                print(
                    r"{}".format(coerce_output(response["choices"][0]["text"]))
                )
            else:
                print("The text reponse contained nothing.")
        else:
            print(
                "Opps sorry, something went wrong with the request to the AI this time."
            )


# if __name__ == "__main__":
# logging.basicConfig(level=logging.DEBUG)
logging.debug(f"Starting the commit translation process. {os.getcwd()}")
commits: str = list_commits()
logging.debug(f"The commits: {commits}")
prompt: str = get_prompt(commits)
logging.info(f"The prompt: {prompt}")
main(
    prompt,
    float(TEMPERATURE),
    int(TOKENS),
    float(FREQUENCY),
    float(PRESENCE),
)
logging.debug("main(prompt) has been successfully run. Goodbye.")
