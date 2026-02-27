# Contributing to Green Bharat

Thank you for your interest in contributing to **Green Bharat: Live AI Market Intelligence**!

## How to Contribute

1.  **Fork the Repository**: Create your own copy of the project to work on.
2.  **Create a Feature Branch**:
    ```bash
    git checkout -b feature/your-awesome-feature
    ```
3.  **Implement Changes**: Ensure your code follows the established [modular patterns](docs/backend.md).
4.  **Add Tests**: If you add new functionality, please include corresponding unit tests in the `tests/` directory.
5.  **Run Verification**:
    ```bash
    pytest tests/
    ```
6.  **Submit a Pull Request**: Provide a clear description of your changes and why they are beneficial.

## Code Style
- Follow PEP 8 guidelines for Python code.
- Ensure all new components use the centralized `Config` class for settings.
- Document new features in the `docs/` directory.

## License
By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
