"""
This module implements an SQLFluff rule that requires `CREATE X` clauses to specify `IF NOT EXISTS`.
"""

from sqlfluff.core.plugin import hookimpl
from sqlfluff.core.rules.base import (BaseRule, LintResult, RuleContext)
from sqlfluff.core.rules.doc_decorators import (document_fix_compatible, document_configuration)
from typing import List
import os.path
from sqlfluff.core.config import ConfigLoader


@hookimpl
def get_rules() -> List[BaseRule]:
    """Get plugin rules."""
    return [RequireIfNotExists_MigrationRules_L001]


@hookimpl
def load_default_config() -> dict:
    """Loads the default configuration for the plugin."""
    return ConfigLoader.get_global().load_default_config_file(
        file_dir=os.path.dirname(__file__),
        file_name="plugin_default_config.cfg",
    )


# @hookimpl
# def get_configs_info() -> dict:
#     """Get rule config validations and descriptions."""
#     return {
#         "forbidden_columns": {"definition": "A list of column to forbid"},
#     }

# These two decorators allow plugins to be displayed in the sqlfluff docs
@document_fix_compatible
@document_configuration
# sqlfluff expects class names of the form RuleName_PkgName_RuleId
class RequireIfNotExists_MigrationRules_L001(BaseRule):
    def _eval(self, context: RuleContext):
        """We should not use CREATE XXX without IF NOT EXISTS."""
        return LintResult(
            anchor=context.segment,
            description=f"IF NOT EXISTS not allowed in CREATE TABLE.",
        )
        if context.segment.is_type("create_table_clause"):
            children = context.segment.segments
            return LintResult(
                anchor=context.segment,
                description=f"IF NOT EXISTS not allowed in CREATE TABLE. {children}",
            )
            # for seg in context.segment.segments:
            #     col_name = seg.raw.lower()
            #     if (
            #         seg.is_type("column_reference")
            #         and col_name in self.forbidden_columns
            #     ):
            #         return LintResult(
            #             anchor=seg,
            #             description=f"Column `{col_name}` not allowed in ORDER BY.",
            #         )
