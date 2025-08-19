# Hooks

Cookiecutter supports pre- and post-generation hooks for custom logic during project creation.

- `hooks/pre_gen_project.py`: Runs before project generation. Use for validation or setup.
- `hooks/post_gen_project.py`: Runs after project generation. Use for cleanup or additional configuration.

You can customize these Python scripts to automate tasks specific to your workflow.
