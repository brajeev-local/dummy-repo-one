# Using this repository as a template

This repo **is** the Python template. It is created and managed by Terraform under `module-github/platform/template-repos`; the template content lives here.

## For people creating a new project

1. On GitHub, open this repo and click **Use this template** → **Create a new repository**.
2. Clone your new repo, then:
   - Rename `src/my_python_app` to your package name.
   - Update `pyproject.toml` (name, description, authors) and `README.md`.
   - Add your code and dependencies.

## For maintainers of this template

- To change the template: edit files in this repo, commit, and push. New repos created via **Use this template** will get the latest content.
- Template repository setting: **Settings → General → Template repository** (should be enabled; Terraform sets the repo as a template when creating it).

## CI

GitHub Actions runs `pytest` on every push and pull request to `main`/`master`. See [.github/workflows/test.yml](.github/workflows/test.yml).
