def main():
    import sys
    import os
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = os.path.split(curPath)[0]
    sys.path.append(os.path.dirname(os.path.dirname(rootPath)))
    from alpaca_server.alpaca_serving import AlpacaServer
    from alpaca_server.alpaca_serving.helper import get_run_args
    with AlpacaServer(get_run_args()) as server:
        server.join()

if __name__ == '__main__':
    main()
def terminate():
    from alpaca_server.alpaca_serving import AlpacaServer
    from alpaca_server.alpaca_serving.helper import get_run_args, get_shutdown_parser
    args = get_run_args(get_shutdown_parser)
    AlpacaServer.shutdown(args)