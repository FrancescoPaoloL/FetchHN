def load_config(config_file):
    import yaml

    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    
    return config