project_slug = "{{ cookiecutter.project_slug }}"


def run():
    print("Running pre-generation hook...")
    if hasattr(project_slug, "isidentifier"):
        assert project_slug.isidentifier(), f"'{project_slug}' project slug is not a valid identifier."
    assert project_slug == project_slug.lower(), f"'{project_slug}' project slug should be all lowercase"


if __name__ == "__main__":
    run()


if __name__ == "__main__":
    run()
