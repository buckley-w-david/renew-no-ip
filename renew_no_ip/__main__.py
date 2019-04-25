from renew_no_ip.config import RenewConfig
from renew_no_ip.renew import renew

if __name__ == "__main__":
    config = RenewConfig.from_env()
    renew(config.noip_username, config.noip_password)
