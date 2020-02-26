from visual.vsession import VSession, PLUGIN_NAME


def pytest_addoption(parser):
    group = parser.getgroup("visual")
    group.addoption(
        "--vport",
        action="store",
        dest="vport",
        default="8080",
        help="Bind visual process port on"
    )


def pytest_configure(config):
    # register the vsession here
    pm = config.pluginmanager
    plugin = pm.getplugin(PLUGIN_NAME)
    if plugin is None:
        plugin = VSession()
        pm.register(plugin, PLUGIN_NAME)


def pytest_unconfigure(config):
    # clean the environment
    pass
