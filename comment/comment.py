from colorama import Fore, Style, Back, init

init(autoreset=True)


def Logo():
    print(LightRed("""
        ██████╗ ██╗  ██╗ █████╗ ███████╗███╗  ██╗██╗██╗  ██╗
        ██╔══██╗██║  ██║██╔══██╗██╔════╝████╗ ██║██║╚██╗██╔╝
        ██████╔╝███████║██║  ██║█████╗  ██╔██╗██║██║ ╚███╔╝
        ██╔═══╝ ██╔══██║██║  ██║██╔══╝  ██║╚████║██║ ██╔██╗
        ██║     ██║  ██║╚█████╔╝███████╗██║ ╚███║██║██╔╝╚██╗
        ╚═╝     ╚═╝  ╚═╝ ╚════╝ ╚══════╝╚═╝  ╚══╝╚═╝╚═╝  ╚═╝
    """))


def Success(message):
    return Fore.GREEN + message + Style.RESET_ALL


def Error(message):
    return Fore.RED + message + Style.RESET_ALL


def Warning(message):
    return Fore.YELLOW + message + Style.RESET_ALL


def LightRed(message):
    return Fore.LIGHTRED_EX + message + Style.RESET_ALL


def Info(message):
    return Fore.CYAN + message + Style.RESET_ALL


def LightGreen(message):
    return Fore.LIGHTGREEN_EX + message + Style.RESET_ALL
