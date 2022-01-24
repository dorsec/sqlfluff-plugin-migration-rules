from setuptools import find_packages, setup

PLUGIN_LOGICAL_NAME = "migration-rules"
PLUGIN_ROOT_MODULE = "migration_rules"

setup(
    name="sqlfluff-plugin-{}".format(PLUGIN_LOGICAL_NAME),
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires="sqlfluff>=0.9.0",
    entry_points={
        "sqlfluff": [
            "{logical_name} = {root_module}.rules".format(logical_name=PLUGIN_LOGICAL_NAME, root_module=PLUGIN_ROOT_MODULE)
        ]
    },
)
