
VERBOSE = True
num_pass = 0
num_fail = 0


def assert_equals(msg, expected, actual):
    """
    Check whether code being tested produces
    the correct result for a specific test
    case. Prints a message indicating whether
    it does.
    :param: msg is a message to print at the beginning.
    :param: expected is the correct result
    :param: actual is the result of the
    code under test.
    """
    if VERBOSE:
        print(msg)

    global num_pass, num_fail

    if expected == actual:
        if VERBOSE:
            print("PASS")
        num_pass += 1
    else:
        if not VERBOSE:
            print(msg)
        print("**** FAIL")
        print("expected: " + str(expected))
        print("actual: " + str(actual))
        if not VERBOSE:
            print("")
        num_fail += 1

    if VERBOSE:
        print("")


def fail_on_error(msg, err):
    """
    if run-time error occurs, call this to insta-fail

    :param msg: message saying what is being tested
    :param err: type of run-time error that occurred
    """
    global num_fail
    print(msg)
    print("**** FAIL")
    print(err)
    print("")
    num_fail += 1
    

def start_tests(header):
    """
    Initializes summary statistics so we are ready to run tests using
    assert_equals. 
    :param header: A header to print at the beginning
    of the tests.
    """
    global num_pass, num_fail
    print(header)
    for i in range(0, len(header)):
        print("=", end="")
    print("")
    num_pass = 0
    num_fail = 0


def finish_tests():
    """
    Prints summary statistics after the tests are complete.
    """
    print("Passed %d/%d" % (num_pass, num_pass+num_fail))
    print("Failed %d/%d" % (num_fail, num_pass+num_fail))
    print()
