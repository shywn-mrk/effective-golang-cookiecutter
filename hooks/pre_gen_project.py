# Pre-generation hook for Cookiecutter
# You can add logic here to clean up or validate before project generation

def run():
    print("Running pre-generation hook...")

    project_slug = "{{ cookiecutter.project_slug }}"
    if hasattr(project_slug, "isidentifier"):
        assert project_slug.isidentifier(), "'{}' project slug is not a valid identifier.".format(project_slug)

    assert project_slug == project_slug.lower(), "'{}' project slug should be all lowercase".format(project_slug)

if __name__ == "__main__":
    run()
