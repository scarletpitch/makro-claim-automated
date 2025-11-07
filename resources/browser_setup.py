from webdriver_manager.chrome import ChromeDriverManager

def get_chromedriver_path():
    """Return universal path for ChromeDriver."""
    path = ChromeDriverManager().install()
    return path
