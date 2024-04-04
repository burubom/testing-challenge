## Test strategy

### Objective and scope
This test suite is to validate the functionalities of Speed test site https://www.debugbear.com/test/website-speed.
The functionalities specific to the page are covered. General functionalities such as 'Log in' are not included.
The test will be carried out using Chrome.

### Test approach
The test type to be carried out is behavior testing. Test cases will be created employing methods such as equivalence partitioning and exploratory testing.

### Tools and frameworks
pytest, selenium

### Reporting
Test report will be available in html format.

## How to run the test suite
```bash
# With publishing html report
pytest . --html=report.html --capture=tee-sys
```

### Test parameters
Following parameters can be adjustable in the constants.py.
```python
TIMEOUT = 120
RETRIES = 3
TARGET_URL = 'https://es.idoven.ai/'
```
TIMEOUT<br>
The duration, in seconds, before timing out while waiting for a test result page to render.

RETRIES<br>
The retry count specifies the number of attempts made to locate the error message element. This is necessary because the element may be removed upon selection, potentially resulting in it not being found during the initial attempt.

TARGET_URL<br>
The website URL to evaluate the speed can be modified here.
