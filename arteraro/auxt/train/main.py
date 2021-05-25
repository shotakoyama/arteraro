from pathlib import Path
from arteraro.auxt.util.load import load_config, load_sub_config, check_sub_config
from arteraro.auxt.util.num_iter import get_num_train_iter
from .worker import WorkerJobScript
from .job import TrainJobScript
from .run import TrainRunScript
from .sub import TrainSubScript

def train():
    config = load_config()
    if check_sub_config():
        sub_config = load_sub_config()
        num_node = sub_config['train']['num_node']
        gpu_per_node = sub_config['train'].get('gpu_per_node', None)
        port = sub_config['train'].get('port', None)
    else:
        sub_config = None
        num_node = 1

    num_iter = get_num_train_iter()

    if num_node > 1:
        worker_script_list = [
                WorkerJobScript(index, num_node, gpu_per_node, port)
                for index in range(num_iter)]
    else:
        worker_script_list = [WorkerJobScript(index, num_node) for index in range(num_iter)]

    train_script_list = [TrainJobScript(index, num_node) for index in range(num_iter)]

    if sub_config is not None:
        sub_script = TrainSubScript(train_script_list)
    else:
        run_script = TrainRunScript(train_script_list)

