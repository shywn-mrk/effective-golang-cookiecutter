from unittest import mock

import hooks.post_gen_project as post_gen_project


@mock.patch("hooks.post_gen_project.Path.unlink")
def test_remove_mysql_client(mock_unlink):
    with mock.patch("hooks.post_gen_project.Path.exists", return_value=True):
        post_gen_project.remove_mysql_client()
        mock_unlink.assert_called_once()


@mock.patch("hooks.post_gen_project.Path.unlink")
def test_remove_postgresql_client(mock_unlink):
    with mock.patch("hooks.post_gen_project.Path.exists", return_value=True):
        post_gen_project.remove_postgresql_client()
        mock_unlink.assert_called_once()


@mock.patch("hooks.post_gen_project.Path.unlink")
def test_remove_redis_client(mock_unlink):
    with mock.patch("hooks.post_gen_project.Path.exists", return_value=True):
        post_gen_project.remove_redis_client()
        mock_unlink.assert_called_once()


@mock.patch("hooks.post_gen_project.subprocess.run")
def test_go_tidy(mock_run):
    post_gen_project.go_tidy()
    mock_run.assert_called_with(["go", "mod", "tidy"], check=True)


@mock.patch("hooks.post_gen_project.subprocess.run")
def test_build_compose(mock_run):
    post_gen_project.build_compose()
    mock_run.assert_called_with(["docker", "compose", "build"], check=True)


@mock.patch("hooks.post_gen_project.subprocess.run")
def test_git_init(mock_run):
    post_gen_project.git_init()
    mock_run.assert_called_with(["git", "init"], check=True)


@mock.patch("hooks.post_gen_project.subprocess.run")
def test_install_pre_commit_git_no(mock_run):
    with mock.patch("builtins.print") as mock_print:
        with mock.patch("hooks.post_gen_project.cookiecutter", {"use_git": "no"}):
            post_gen_project.install_pre_commit()
            mock_print.assert_any_call("Skipping pre-commit installation because Git is not used.")


@mock.patch("hooks.post_gen_project.shutil.rmtree")
def test_remove_grpc_server(mock_rmtree):
    post_gen_project.remove_grpc_server()
    mock_rmtree.assert_called_once()


@mock.patch("hooks.post_gen_project.shutil.rmtree")
@mock.patch("hooks.post_gen_project.Path.unlink")
def test_remove_docker(mock_unlink, mock_rmtree):
    post_gen_project.remove_docker()
    mock_rmtree.assert_called_once()
    mock_unlink.assert_called()


@mock.patch("hooks.post_gen_project.Path.unlink")
def test_remove_licence(mock_unlink):
    with mock.patch("hooks.post_gen_project.Path.exists", return_value=True):
        post_gen_project.remove_licence()
        mock_unlink.assert_called_once()
