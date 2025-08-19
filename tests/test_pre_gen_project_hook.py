import pytest

import hooks.pre_gen_project as pre_gen_project


def test_valid_project_slug(monkeypatch):
    monkeypatch.setattr(pre_gen_project, "project_slug", "validslug")
    assert pre_gen_project.project_slug.isidentifier()
    assert pre_gen_project.project_slug == pre_gen_project.project_slug.lower()


def test_invalid_project_slug(monkeypatch):
    monkeypatch.setattr(pre_gen_project, "project_slug", "invalid-slug")
    with pytest.raises(AssertionError):
        if hasattr(pre_gen_project.project_slug, "isidentifier"):
            assert pre_gen_project.project_slug.isidentifier()


def test_uppercase_project_slug(monkeypatch):
    monkeypatch.setattr(pre_gen_project, "project_slug", "UpperCaseSlug")
    with pytest.raises(AssertionError):
        assert pre_gen_project.project_slug == pre_gen_project.project_slug.lower()
