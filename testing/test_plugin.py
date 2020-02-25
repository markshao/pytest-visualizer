def test_vport_cmd_option(testdir):
    config = testdir.parseconfig("--vport=9090")
    assert config.option.vport == "9090"
