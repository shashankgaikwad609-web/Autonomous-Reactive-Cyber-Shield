import tkinter as tk
import logging
import math
import os
from collections import Counter
from core.parser import CodeParser
from core.detector import IntrusionSentinel
from core.mutators import AdvancedResilienceEngine
from core.generator import CodeGenerator
from app.gui import FrameworkGUI

class ApplicationController:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("MasterOrchestrator: Mounting AI-driven active self-healing modules...")
        
        # 🛡️ HIDDEN PATH CONFIGURATION
        self.hidden_dir = ".hidden_source"
        self.target_file_path = os.path.join(self.hidden_dir, "core_service.py")
        self._initialize_hidden_target_file()

        self.root = tk.Tk()
        self.interface = FrameworkGUI(self.root, self.execute_pipeline_bridge)
        
        # Monitor the hidden path every 2 seconds
        self.root.after(2000, self._autonomous_system_audit_loop)
        self.was_compromised = False
        self.last_seen_content = ""

    def _initialize_hidden_target_file(self):
        """Safely generates a hidden directory and source file if non-existent."""
        os.makedirs(self.hidden_dir, exist_ok=True)
        if not os.path.exists(self.target_file_path):
            with open(self.target_file_path, "w", encoding="utf-8") as f:
                f.write("def hidden_system_node():\n    access_key = 'root_secure'\n    print('Stealth core operational.')\n")
            logging.info(f"MasterOrchestrator: Mounted hidden tracking asset at '{self.target_file_path}'")

    def _calculate_entropy_score(self, data_stream: str) -> float:
        if not data_stream:
            return 0.0
        frequencies = [count / len(data_stream) for count in Counter(data_stream).values()]
        return -sum(p * math.log2(p) for p in frequencies)

    def _autonomous_system_audit_loop(self):
        """Watches the stealth hidden path for any unauthorized terminal modifications."""
        try:
            if os.path.exists(self.target_file_path):
                with open(self.target_file_path, "r", encoding="utf-8") as f:
                    current_file_data = f.read().strip()
                
                if current_file_data and current_file_data != self.last_seen_content:
                    self.last_seen_content = current_file_data
                    sanitized_data = current_file_data.replace('\t', '    ')
                    
                    self.interface.editor_source.delete("1.0", tk.END)
                    self.interface.editor_source.insert(tk.END, current_file_data)
                    
                    compromised, threat_message = IntrusionSentinel.execute_ai_threat_classification(sanitized_data)
                    if compromised or self.was_compromised != compromised:
                        self.interface.run_transformation()
        except Exception as e:
            logging.error(f"HiddenPathLoop Error: {str(e)}")
        
        self.root.after(2000, self._autonomous_system_audit_loop)

    def execute_pipeline_bridge(self, raw_code: str, enable_obfuscation: bool) -> tuple:
        try:
            raw_code = raw_code.replace('\t', '    ')
            compromised, threat_message = IntrusionSentinel.execute_ai_threat_classification(raw_code)
            self.was_compromised = compromised
            base_entropy = self._calculate_entropy_score(raw_code)
            
            tree = CodeParser.parse_source(raw_code)
            engine = AdvancedResilienceEngine(enable_scrambling=enable_obfuscation)
            mutated_tree = engine.visit(tree)
            
            final_code = CodeGenerator.generate_source(mutated_tree)
            poly_entropy = self._calculate_entropy_score(final_code)
            
            # If compromised, immediately overwrite the hidden asset with mutated text code!
            if compromised:
                with open(self.target_file_path, "w", encoding="utf-8") as file_out:
                    file_out.write(final_code)
                logging.warning(f"BackgroundDaemon: CRITICAL HIJACK ISOLATED! Hidden asset at '{self.target_file_path}' has been dynamically mutated and locked.")

            metrics = {
                "base_entropy": base_entropy,
                "poly_entropy": poly_entropy
            }
            return True, compromised, threat_message, metrics, final_code
            
        except SyntaxError as syntax_err:
            return False, False, "", {}, f"Invalid Syntax: {str(syntax_err)}"
        except Exception as e:
            return False, False, "", {}, str(e)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ApplicationController()
    app.run()
