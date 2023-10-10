from services.instagram.instagram import load_instagram_micro_influenceur
import socket
import socks

def main():
    
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket
    
    load_instagram_micro_influenceur()

if __name__ == "__main__":
    main()