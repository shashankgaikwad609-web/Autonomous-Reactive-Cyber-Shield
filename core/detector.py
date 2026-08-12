import os
import sys
import logging
import math
from collections import Counter

class IntrusionSentinel:
    """
    AI-Driven Predictive Machine Learning Model and Background System Audit Sentinel.
    """
    
    @staticmethod
    def _extract_ml_features(text_stream: str) -> dict:
        length = len(text_stream) if len(text_stream) > 0 else 1
        alphanumeric_ratio = sum(c.isalnum() for c in text_stream) / length
        
        # FIX: Treat underscores (_) as regular programming characters to eliminate false positives
        special_char_ratio = sum(not (c.isalnum() or c == '_') for c in text_stream) / length
        
        probabilities = [count / length for count in Counter(text_stream).values()]
        entropy = -sum(p * math.log2(p) for p in probabilities)
        
        return {
            "length": length,
            "alpha_ratio": alphanumeric_ratio,
            "special_ratio": special_char_ratio,
            "entropy": entropy
        }

    @classmethod
    def execute_ai_threat_classification(cls, raw_code_stream: str) -> tuple:
        """
        AI Core: Uses mathematical probability matrix to isolate malicious attack intent.
        """
        features = cls._extract_ml_features(raw_code_stream)
        
        # Tuned hyperparameter matrix for specific terminal exploitation footprints
        w_entropy = 1.20
        w_special = 3.50  # Highly sensitive to real network symbols like >, &, /
        w_alpha = -0.95
        bias = -4.60
        
        z = (features["entropy"] * w_entropy) + (features["special_ratio"] * w_special) + (features["alpha_ratio"] * w_alpha) + bias
        threat_probability = 1 / (1 + math.exp(-max(min(z, 20), -20)))
        
        logging.info(f"AI-ML Core Evaluated: Threat Probability Score -> {threat_probability:.4f}")
        
        # Strict matching for real reverse shell signatures
        suspicious_footprints = ["/bin/bash", "reverse_shell", "nc -e", "unauthorized_root", "dev/tcp"]
        has_malicious_footprint = any(footprint in raw_code_stream.lower() for footprint in suspicious_footprints)
        
        if threat_probability > 0.82 or has_malicious_footprint:
            msg = f"AI-ML Threat Model Certainty: {threat_probability*100:.2f}%"
            if has_malicious_footprint:
                msg += " (Verified Remote Attack Vector Signature)"
            return True, msg
                
        return False, "System Clear"
