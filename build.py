from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')


name = 'vtool3'
default_task = ['clean', 'publish']


@init
def initialize(project):
    project.version = '0.1'
    project.depends_on('docopt')
    project.set_property('coverage_threshold_warn', 80)
    project.set_property('coverage_break_build', False)
