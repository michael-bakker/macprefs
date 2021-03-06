from os.path import exists
from config import get_ssh_backup_dir, get_ssh_user_dir, get_user, ensure_exists
from utils import copy_dir, ensure_dir_owned_by_user


def backup():
    source = get_ssh_user_dir()
    if not exists(source):
        print 'No .ssh dir found... skipping.'
        return
    print 'Backing up .ssh dir...'
    dest = get_ssh_backup_dir()
    ensure_exists(dest)
    copy_dir(source, dest)


def restore():
    source = get_ssh_backup_dir()
    if not exists(source):
        print 'No .ssh dir found... skipping.'
        return
    print 'Restoring .ssh dir...'
    dest = get_ssh_user_dir()
    copy_dir(
        source, dest, with_sudo=True
    )
    ensure_dir_owned_by_user(dest, get_user())