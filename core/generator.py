import ast
import astor
import logging

class CodeGenerator:
    """
    De-compiles abstract syntax tree maps back into compliant functional source code.
    """
    @staticmethod
    def generate_source(ast_tree: ast.AST) -> str:
        logging.info("GeneratorEngine: Re-synthesizing compilation tree back to source stream...")
        try:
            transformed_code = astor.to_source(ast_tree)
            logging.info("GeneratorEngine: Source text code re-synthesis executed successfully.")
            return transformed_code
        except Exception as e:
            logging.error(f"GeneratorEngine: Code re-generation lifecycle failed: {str(e)}")
            raise
