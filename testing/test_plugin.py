def test_visualizer_option(testdir):
    from visualizer import plugin
    testdir.plugins.append(plugin)
    config = testdir.parseconfigure("--visualizer")
    assert config.option.visualizer == True
