# commit-meaning

Extract meaning from your verbose git commits into a succinct paragraph within your pull requests.

Simply add this as a step in your CI/CD process and your PRs will be annotated with a single
paragraph describing the git commits involved.

## Inputs

### `OPENAI_API_KEY`

**Required** An environment variable containing your OpenAI api key.

### `GITHUB_TOKEN`

**Required** Your Github token with read/write permissions.

## Example usage

```yaml
uses: actions/commit-meaning
with:
  openai-api-key: '$OPENAI_API_KEY'
  github-token: '$GITHUB_TOKEN'
```
