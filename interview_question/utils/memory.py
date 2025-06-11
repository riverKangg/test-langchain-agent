def append_to_history(history, role, message):
    history.append({"role":role, "message":message})
    return history