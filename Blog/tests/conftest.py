def pytest_report_teststatus(report, config):
    if report.when == 'call':  # 'call' phase is the test execution phase
        if report.passed:
            return "passed", '\033[92m✓', 'PASSED'
        elif report.failed:
            return "failed", '\033[91m✖', 'FAILED'
        elif report.skipped:
            return "skipped", '\033[93m⚠', 'SKIPPED'

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    passed = terminalreporter.stats.get('passed', [])
    if passed:
        terminalreporter.write_sep("=", "PASSED TESTS", bold=True)
        for rep in passed:
            terminalreporter.write_line(f"\033[92m{rep.nodeid}: PASSED ✓\033[0m")

    failed = terminalreporter.stats.get('failed', [])
    if failed:
        terminalreporter.write_sep("=", "FAILED TESTS", bold=True)
        for rep in failed:
            terminalreporter.write_line(f"\033[91m{rep.nodeid}: FAILED ✖\033[0m")

    skipped = terminalreporter.stats.get('skipped', [])
    if skipped:
        terminalreporter.write_sep("=", "SKIPPED TESTS", bold=True)
        for rep in skipped:
            terminalreporter.write_line(f"\033[93m{rep.nodeid}: SKIPPED ⚠\033[0m")
