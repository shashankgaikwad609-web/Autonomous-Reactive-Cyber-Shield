import ast
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CodeParser:
    """
    Ingests source code streams and compiles them into an Abstract Syntax Tree (AST).
    """
    @staticmethod
    def parse_source(source_text: str) -> ast.AST:
        logging.info("ParserEngine: Initiating syntax tokenization process...")
        try:
            parsed_tree = ast.parse(source_text)
            logging.info("ParserEngine: Abstract Syntax Tree compilation successful.")
            return parsed_tree
        except SyntaxError as se:
            logging.error(f"ParserEngine: Tokenization failed due to syntax error: {str(se)}")
            raise
        except Exception as e:
            logging.error(f"ParserEngine: Unexpected exception during parsing phase: {str(e)}")
            raise
