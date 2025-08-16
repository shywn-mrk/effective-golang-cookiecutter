# Makefile for cookiecutter template development

# Variables
PROJECT_NAME ?= golang

# Render the template
bake:
	cookiecutter . project_slug=$(PROJECT_NAME)

# Remove previous generated project
clean:
	rm -rf $(PROJECT_NAME)

# Run tests in generated project (if any)
test-generated:
	cd $(PROJECT_NAME) && make test || echo 'No Makefile or tests found in generated project.'
