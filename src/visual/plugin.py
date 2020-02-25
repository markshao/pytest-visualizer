def pytest_addoption(parser):
    group = parser.getgroup("visual")
    group.addoption(
        "--vport",
        action="store",
        dest="vport",
        default="8080",
        help="Bind visual process port on"
    )
