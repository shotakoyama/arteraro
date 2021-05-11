from arteraro.auxt.conv.eval_config import convert_eval_config

def convert_eval_config_command(args):
    convert_eval_config()

def set_conv(main_sub_parsers):
    parser = main_sub_parsers.add_parser('conv')
    sub_parsers = parser.add_subparsers()

    eval_config = sub_parsers.add_parser('eval-config')
    eval_config.set_defaults(handler = convert_eval_config_command)

