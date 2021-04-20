from pathlib import Path

def add_environmental_script(lst, source):
    source = Path(source).resolve()
    lst.append('if [[ -n $IS_SGE ]] ; then')
    lst.append('    . /etc/profile.d/modules.sh')
    lst.append('    . {}'.format(source))
    lst.append('fi')
    lst.append('')
    return lst

def add_workdir_script(lst):
    lst.append('if [[ -z $WORKDIR ]] ; then')
    lst.append('    WORKDIR=$(dirname $0)')
    lst.append('fi')
    lst.append('cd $WORKDIR')
    lst.append('')
    return lst

def add_localdir_script(lst):
    lst.append('if [[ -z $SGE_LOCALDIR ]] ; then')
    lst.append('    mkdir tmp')
    lst.append('    SGE_LOCALDIR=tmp')
    lst.append('fi')
    lst.append('')
    return lst

def add_await_script(lst, job):
    lst.append('await () {')
    lst.append('    while [[ "$(jobs | wc -l)" -ge {} ]]; do'.format(job))
    lst.append('        sleep 1')
    lst.append('    done')
    lst.append('}')
    lst.append('')
    return lst

