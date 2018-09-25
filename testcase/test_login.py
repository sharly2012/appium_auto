from pages.homepage import HomePage


class TestHomePage:
    homepage = HomePage()
    homepage.click(homepage.login_text)