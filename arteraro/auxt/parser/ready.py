from arteraro.auxt.ready.main import ready

def ready_command(args):
    ready()

def set_ready(main_sub_parsers):
    parser = main_sub_parsers.add_parser('ready')
    parser.set_defaults(handler = ready_command)

