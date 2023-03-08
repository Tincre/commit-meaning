# commit-meaning

Extract meaning from your verbose git commits into a succinct paragraph within your pull requests.

Simply add this as a step in your CI/CD process and your PRs will be annotated with a single
paragraph describing the git commits involved.

## Inputs

### `OPENAI_API_KEY`

**Required** An environment variable containing your OpenAI api key.

### `GITHUB_TOKEN`

**Required** Your Github token with read/write permissions.

### `OPENAI_ORG`

**Required** Your OpenAI organization id.

## Example usage

```yaml
uses: actions/commit-meaning
with:
  openai-api-key: "$OPENAI_API_KEY"
  openai-org: "$OPENAI_ORG"
  github-token: "$GITHUB_TOKEN"
```

## Options

You can fully customize the behavior of this action.

- `temperature`: The OpenAI temperature parameter
- `tokens`: The OpenAI tokens paremter (number of tokens)
- `frequency-penalty`: The OpenAI frequency_penalty parameter
- `presence-penalty`: The OpenAI presence_penalty parameter
- `prompt-instructions`: Additional input instructions for the prompt

### Default `prompt-instructions`

We employ the use of [`gitmoji`](https://gitmoji.dev) at [Tincre](https://tincre.com) to annotate our commit messages with rich categorization.

This action by default uses the following prompt by default:

- 🐞 and 🐛 "refers to a bug fix"
- ♻️ "means to refactor code or content"
- ✨ "means something is new in the code"
- 🔧 "refers to code that is configuration or low-level in nature"
- 🔥 "means to remove code or remove content"
- 🚧 "references a commit considered to be work in-progress", and
- 📓 "references changes to documentation."

## Contributions

We :heart: contributions! File an issue, PR, or suggestion to improve this
action.

## License

This action is liberally licensed under the [MIT license](/LICENSE).

And we at [Tincre](https://tincre.com) would love attribution, if you feel so inclined.
