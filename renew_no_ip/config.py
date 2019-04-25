import configparser
import os
import typing

if typing.TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver

class RenewConfig(typing.NamedTuple):
    driver: typing.Optional['WebDriver']

    noip_username: str
    noip_password: str

    @staticmethod
    def from_file(filename: str, *, driver=None) -> "RenewConfig":
        config = configparser.ConfigParser()
        config.read(filename)

        return RenewConfig(
            driver=driver,
            noip_username=config["noip"]["username"],
            noip_password=config["noip"]["password"],
        )

    @staticmethod
    def from_env(*, driver=None) -> "RenewConfig":
        return RenewConfig(
            driver=driver,
            noip_username=os.environ["NOIP_USERNAME"],
            noip_password=os.environ["NOIP_PASSWORD"],
        )
