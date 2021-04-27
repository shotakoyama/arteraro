from arteraro.auxt.train.main import train

def train_command(args):
    train()

def set_train(main_sub_parsers):
    parser = main_sub_parsers.add_parser('train')
    parser.set_defaults(handler = train_command)

