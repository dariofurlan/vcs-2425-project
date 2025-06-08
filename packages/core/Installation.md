
## Development Environment

The following environment was used for developing and testing this guide:

- **OS**: Debian 12.8 (bookworm)
- **Conda**: 25.3.1
- **CUDA**: 12.4 (550.54.14)

# Dependencies

Place yourself inside the `packages/core` directory.
Install all the dependencies
```bash
conda create --name vcs-2425 --file requirements.txt
```

# Install local package

Place yourself inside the `packages/core` directory.
Install the vcs2425 package with some utilities.

```bash
pip install -e .
```