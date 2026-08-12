import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class FrameworkGUI:
    def __init__(self, root, trigger_pipeline_callback):
        self.root = root
        self.root.title("Autonomous Reactive Cyber Shield v3.0")
        self.root.geometry("1200x780")
        self.root.configure(bg="#0F172A")

        self.trigger_pipeline_callback = trigger_pipeline_callback
        self.obfuscate_var = tk.BooleanVar(value=True)

        # 1. Unified Control Command Panel Toolbar
        top_banner = tk.Frame(root, bg="#1E293B", height=65, bd=0)
        top_banner.pack(fill=tk.X, side=tk.TOP)
        top_banner.pack_propagate(False)

        title_lbl = tk.Label(top_banner, text="REACTIVE POLYSYSTEM SECURITY CONSOLE",
                             font=("Segoe UI", 11, "bold"), fg="#38BDF8", bg="#1E293B")
        title_lbl.pack(side=tk.LEFT, padx=20)

        self.btn_run = tk.Button(top_banner, text="Ingest & Monitor Stream", font=("Segoe UI", 9, "bold"),
                                  fg="#0F172A", bg="#38BDF8", activebackground="#7DD3FC", relief=tk.FLAT, 
                                  padx=15, pady=6, command=self.run_transformation)
        self.btn_run.pack(side=tk.RIGHT, padx=20)

        # 2. Threat Vector Alert System Display Strip
        self.threat_panel = tk.Frame(root, bg="#0284C7", height=45)
        self.threat_panel.pack(fill=tk.X, side=tk.TOP)
        self.threat_panel.pack_propagate(False)

        self.lbl_threat_status = tk.Label(self.threat_panel, text="MONITOR STATUS: PERIMETER SECURE | LISTENING...", 
                                          font=("Segoe UI", 9, "bold"), fg="#FFFFFF", bg="#0284C7")
        self.lbl_threat_status.pack(side=tk.LEFT, padx=20)

        # 3. Main Operational Workstation Windows Split
        workspace = tk.Frame(root, bg="#0F172A", padx=15, pady=10)
        workspace.pack(fill=tk.BOTH, expand=True)
        
        workspace.columnconfigure(0, weight=1, uniform="split")
        workspace.columnconfigure(1, weight=1, uniform="split")
        workspace.rowconfigure(0, weight=1)

        # Input Workspace Box
        left_container = tk.Frame(workspace, bg="#0F172A")
        left_container.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        tk.Label(left_container, text="TARGET APPLICATION STREAM TARGET", font=("Segoe UI", 8, "bold"), fg="#64748B", bg="#0F172A").pack(anchor=tk.W, pady=(0, 5))
        self.editor_source = scrolledtext.ScrolledText(left_container, font=("Consolas", 10), bg="#1E293B", fg="#F8FAFC", relief=tk.FLAT, bd=0)
        self.editor_source.pack(fill=tk.BOTH, expand=True)

        # Output Resilient View Box
        right_container = tk.Frame(workspace, bg="#0F172A")
        right_container.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        tk.Label(right_container, text="REACTIVE POLYSIGNATURE CAMOUFLAGE GENERATION", font=("Segoe UI", 8, "bold"), fg="#64748B", bg="#0F172A").pack(anchor=tk.W, pady=(0, 5))
        self.editor_output = scrolledtext.ScrolledText(right_container, font=("Consolas", 10), bg="#1E293B", fg="#10B981", relief=tk.FLAT, bd=0)
        self.editor_output.pack(fill=tk.BOTH, expand=True)

        # 4. Telemetry Metrics Matrix Foot Panel
        metrics_panel = tk.Frame(root, bg="#1E293B", height=45)
        metrics_panel.pack(fill=tk.X, side=tk.BOTTOM)
        metrics_panel.pack_propagate(False)

        self.lbl_base_entropy = tk.Label(metrics_panel, text="Initial Entropy: 0.00", font=("Consolas", 9, "bold"), fg="#94A3B8", bg="#1E293B")
        self.lbl_base_entropy.pack(side=tk.LEFT, padx=20)

        self.lbl_poly_entropy = tk.Label(metrics_panel, text="Mutated Entropy: 0.00", font=("Consolas", 9, "bold"), fg="#10B981", bg="#1E293B")
        self.lbl_poly_entropy.pack(side=tk.LEFT, padx=30)

        self.lbl_status = tk.Label(metrics_panel, text="Operational Node: Idle", font=("Segoe UI", 9), fg="#94A3B8", bg="#1E293B")
        self.lbl_status.pack(side=tk.RIGHT, padx=20)

    def run_transformation(self):
        raw_input = self.editor_source.get("1.0", tk.END).strip()
        if not raw_input:
            return

        success, compromised, message, metrics, output_data = self.trigger_pipeline_callback(
            raw_input, self.obfuscate_var.get()
        )
        
        if success:
            if compromised:
                self.threat_panel.config(bg="#DC2626")
                self.lbl_threat_status.config(text=f"ALERT: INTRUSION ISOLATED -> {message.upper()}", bg="#DC2626", fg="#FFFFFF")
                self.editor_output.config(fg="#EF4444") 
                self.lbl_status.config(text="Status: Autonomous Camouflage Active", fg="#EF4444")
            else:
                self.threat_panel.config(bg="#16A34A")
                self.lbl_threat_status.config(text="MONITOR STATUS: CLEAR | CODE EXECUTION AUTHORIZED SECURELY", bg="#16A34A", fg="#FFFFFF")
                self.editor_output.config(fg="#10B981")
                self.lbl_status.config(text="Status: Processing Pipeline Complete", fg="#10B981")

            self.editor_output.delete("1.0", tk.END)
            self.editor_output.insert(tk.END, output_data)
            self.lbl_base_entropy.config(text=f"Initial Entropy: {metrics['base_entropy']:.2f}")
            self.lbl_poly_entropy.config(text=f"Mutated Entropy: {metrics['poly_entropy']:.2f}")
        else:
            # Handles mid-typing syntax errors silently without raising blocking popups
            if "invalid syntax" in output_data.lower():
                self.lbl_status.config(text="Status: Awaiting Valid Python Syntax...", fg="#F59E0B")
            else:
                messagebox.showerror("Pipeline Exception Failure", output_data)
                self.lbl_status.config(text="Status: Transaction Interruption", fg="#EF4444")
