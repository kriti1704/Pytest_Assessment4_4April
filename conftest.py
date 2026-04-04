import pytest
from selenium import webdriver
# import config
from config.env import ConfigReader

# create fixture
@pytest.fixture
def setup_and_teardown():
    #Read config
    config = ConfigReader.read_config()
    env = config['qa'] # since our yaml has only qa 
    base_url = env['base_url'] # fetching url from yaml
    
    # setup before test
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.maximize_window()
    yield driver #test runs here
    # teardown
    driver.close()