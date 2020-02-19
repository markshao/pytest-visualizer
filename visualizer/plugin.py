def pytest_addoption(parser, pluginmanager):
    parser.addoption("--visualizer",
                     action="store_true",
                     dest="visualizer",
                     default=False,
                     help="start the visualizer progress")
