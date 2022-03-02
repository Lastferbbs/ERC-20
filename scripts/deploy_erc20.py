from brownie import OurToken, network, config
from scripts.helpful_scripts import get_account


def deploy_lottery():
    account = get_account()
    Token = OurToken.deploy(10000000000000000000000000, {"from": account})
    print(Token.balanceOf(account))


def main():
    deploy_lottery()
