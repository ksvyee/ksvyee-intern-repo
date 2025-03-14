# Writing & Running E2E Tests

## Integrating WinAppDriver Tests into CI/CD

### Reflections

**How does running tests in CI/CD help maintain application stability?**

Running tests in CI/CD helps maintain application stability by automatically catching bugs before deployment. Every time new code is pushed, the tests run to check if anything is broken.

**What are the challenges of running GUI-based tests in CI/CD pipelines?**

The biggest challenge with GUI-based tests in CI/CD is that they rely on a visible interface, which may not always be available in a headless CI environment.

**How can flaky tests be handled in a CI/CD environment?**

Flaky tests can be handled by adding retries, improving element locators, and making sure waits are properly used.

**What would be the next steps to fully integrate Focus Bear’s automated tests into its deployment pipeline**

To ensure tests run reliably in CI/CD, add reporting for test results, and make sure failures block bad code from being deployed.
