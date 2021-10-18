import importlib.util

def pytest_addoption(parser):
    parser.addoption(
        "--path",
        action="append",
        default=[],
        help="list of paths to pass to test functions",
    )

def pytest_generate_tests(metafunc):
    if "number_of_coins" in metafunc.fixturenames:
        file_paths = metafunc.config.getoption("path")
        
        functions = []
        for file_path in file_paths:
            spec = importlib.util.spec_from_file_location("module.name", file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            functions.append(module.number_of_coins)
            
        metafunc.parametrize("number_of_coins", functions)