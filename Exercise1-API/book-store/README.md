# Book Store REST API

## Requirements

Install with poetry:

```shell script
poetry shell
poetry install 
```

## How to run the API

```bash
python bookstore_api.py
```

Your API will start running at **`http://127.0.0.1:5000/`**.

## Run Tests

```bash
# Run all test
pytest . -s

# Run all test cases of single endpoint
pytest test_create.py -s

# Run individual test case
pytest test_update.py::test_update_all_200 -s
```
## Test strategy
### Objective and scope
This automation test suite is designed to ensure that CRUD operations of the bookstore app as expected. Additionally, it aims to:
- Improve test coverage 
- Reduce regression risks 
- Increase test efficiency

The test scope covers all functionalities related to CRUD operations. Non-functional tests are not included within this scope.
### Test approach
The test type to be carried out is unit testing. Test cases will be created employing methods such as equivalence partitioning, boundary value analysis, and error guessing. The test suite will be triggered automatically upon code changes being pushed to the repository.
### Tools and frameworks
pytest, pytest-cov, GitHub actions (CI)
### Test Data Management
The book data in tests/books.json will used as test data.<br>
The request payload data to be used for happy path tests will be randomly generated within the code.
### Reporting
The unit test result and the coverage report will be available via GitHub action everytime the code changes are pushed to the repository. 