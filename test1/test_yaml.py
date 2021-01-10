import yaml


def test_yaml():
    env = {
        "default": "dev",
        "req_url": {
            "dev": "192.168.61.130",
            "test": "127.0.0.1"
        }
    }
    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)
