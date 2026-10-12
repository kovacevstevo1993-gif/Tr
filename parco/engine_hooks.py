"""Le funzioni effetto vivono in engine; questo modulo evita l'import circolare con le scene."""
import sys, importlib
def __getattr__(name):
    return getattr(sys.modules["__main__"] if hasattr(sys.modules.get("__main__"), "frame") else importlib.import_module("engine"), name)
