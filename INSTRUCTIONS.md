# Setting up from this placeholder repository

## Checklist

### Relace placeholder names

- [ ] Replace `<package_name>` or `package_name` with your package name.
- [ ] Replace `<owner_name>` or `<owner>` with the owner of the git repository - this could be an organisation or a 
user.
- [ ] Replace `<repo_name>` with the name of the repository.


### Environment Variables

Ensure the github actions have access to the following environment variables:

- [ ] In order to deploy documentation and the package to pypi:
  - [ ] `PYPI_TOKEN`
  - [ ] `READTHEDOCS_TOKEN`
- [ ] Ensure the `CODECOV_TOKEN` is accessible for code coverage using codecov.

These token can be access through the providers and can be sent at a repository owner level or at a repository level.

### Project setup on third-party providers:

- [ ] Create a new project on readthedocs with the same name as your `package_name`.
- [ ] Configure project on codecov
- [ ] Create project on pypi

## Useful information

- Releases should be triggered by manually creating a release on github. The associated workflow will be triggered.
- There is a makefile with handy commands
